"""Filesystem behavior matters here: installation writes outside the repository."""

import importlib.util
from pathlib import Path
import tempfile
import unittest


spec = importlib.util.spec_from_file_location(
    "planner_install", Path(__file__).resolve().parents[1] / "scripts" / "install.py"
)
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class InstallationTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.home = Path(temporary.name)

    def test_both_copies_preserve_resources_and_only_claude_gets_extension(self):
        source = installer.SOURCE
        installer.preflight(source, self.home, ["codex", "claude"])
        original = (source / "SKILL.md").read_bytes()
        for agent in ("codex", "claude"):
            target = installer.destination(self.home, agent)
            installer.install(source, target, agent)
            for resource in source.rglob("*"):
                if resource.is_file() and resource.name != "SKILL.md":
                    self.assertEqual(resource.read_bytes(),
                                     (target / resource.relative_to(source)).read_bytes())
            installed = (target / "SKILL.md").read_text()
            if agent == "codex":
                self.assertEqual(installed.encode(), original)
            else:
                self.assertEqual(installed.replace("disable-model-invocation: true\n", "", 1)
                                 .encode(), original)
        self.assertEqual((source / "SKILL.md").read_bytes(), original)

    def test_existing_installation_is_preserved(self):
        target = installer.destination(self.home, "claude")
        target.mkdir(parents=True)
        marker = target / "keep.txt"
        marker.write_text("user content")
        with self.assertRaises(FileExistsError):
            installer.install(installer.SOURCE, target, "claude")
        self.assertEqual(marker.read_text(), "user content")
        self.assertEqual(list(target.iterdir()), [marker])

    def test_preflight_checks_both_before_any_install(self):
        target = installer.destination(self.home, "claude")
        target.mkdir(parents=True)
        with self.assertRaises(FileExistsError):
            installer.preflight(installer.SOURCE, self.home, ["codex", "claude"])
        self.assertFalse(installer.destination(self.home, "codex").exists())

    def test_broken_symlink_is_preserved(self):
        target = installer.destination(self.home, "codex")
        target.parent.mkdir(parents=True)
        target.symlink_to(self.home / "missing")
        with self.assertRaises(FileExistsError):
            installer.preflight(installer.SOURCE, self.home, ["codex"])
        self.assertTrue(target.is_symlink())

    def test_legacy_codex_installation_blocks_duplicate(self):
        legacy = self.home / ".codex" / "skills" / "planner"
        legacy.mkdir(parents=True)
        with self.assertRaises(FileExistsError):
            installer.preflight(installer.SOURCE, self.home, ["codex"])
        self.assertFalse(installer.destination(self.home, "codex").exists())

    def test_missing_source_is_rejected_without_writing(self):
        with self.assertRaises(ValueError):
            installer.preflight(self.home / "missing", self.home, ["codex"])
        self.assertFalse((self.home / ".agents").exists())


if __name__ == "__main__":
    unittest.main()
