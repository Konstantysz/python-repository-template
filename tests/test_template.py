import os
import subprocess
from pathlib import Path


def test_copier_copy_defaults(tmp_path):
    result = subprocess.run(
        [
            "copier",
            "copy",
            Path(__file__).parent.parent,
            str(tmp_path / "output"),
            "--defaults",
        ],
        env={**os.environ, "SKIP_POST_HOOK": "1"},
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr
    assert (tmp_path / "output" / "pyproject.toml").exists()
    assert (tmp_path / "output" / "src").is_dir()
