import subprocess
from pathlib import Path

from so101_leisaac_course import environment


def test_versions_equivalent_accepts_official_suffixes_and_trailing_zero():
    assert environment.versions_equivalent("5.1.0.0", "5.1.0")
    assert environment.versions_equivalent("2.7.0+cu128", "2.7.0")
    assert not environment.versions_equivalent("5.1.1", "5.1.0")
    assert not environment.versions_equivalent("5.1.0rc1", "5.1.0")


def test_isaaclab_uses_exact_source_tag(monkeypatch, tmp_path: Path):
    source_root = tmp_path / "dependencies" / "IsaacLab"
    source_root.mkdir(parents=True)
    monkeypatch.setattr(environment, "package_version", lambda distribution: "0.47.2")
    monkeypatch.setattr(environment.shutil, "which", lambda executable: "/usr/bin/git")

    def fake_run(command, **kwargs):
        assert command == [
            "/usr/bin/git",
            "-C",
            str(source_root),
            "describe",
            "--tags",
            "--exact-match",
            "HEAD",
        ]
        return subprocess.CompletedProcess(command, 0, "v2.3.0\n", "")

    monkeypatch.setattr(environment.subprocess, "run", fake_run)
    result = environment.check_isaaclab_version(tmp_path)
    assert result.ok
    assert "v2.3.0" in result.detail
    assert "0.47.2" in result.detail


def test_isaaclab_rejects_source_head_without_exact_tag(monkeypatch, tmp_path: Path):
    (tmp_path / "dependencies" / "IsaacLab").mkdir(parents=True)
    monkeypatch.setattr(environment, "package_version", lambda distribution: "0.47.2")
    monkeypatch.setattr(environment.shutil, "which", lambda executable: "/usr/bin/git")
    monkeypatch.setattr(
        environment.subprocess,
        "run",
        lambda command, **kwargs: subprocess.CompletedProcess(command, 128, "", "no tag"),
    )

    result = environment.check_isaaclab_version(tmp_path)
    assert not result.ok
    assert "未精确匹配" in result.detail
