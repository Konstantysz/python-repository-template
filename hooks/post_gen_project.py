import os
import subprocess
import sys
from pathlib import Path


def main():
    if os.environ.get("SKIP_POST_HOOK") == "1":
        print("Skipping post-generation hook as requested.")
        sys.exit(0)

    # Access answers via globals
    package_manager = globals().get("package_manager", "uv")
    use_pre_commit = globals().get("use_pre_commit", True)
    use_ai_agents = globals().get("use_ai_agents", True)

    project_dir = Path.cwd()

    # Initialize git only if not already inside a repo
    if not (project_dir / ".git").exists():
        subprocess.run(["git", "init"], cwd=project_dir, check=True)

    # Create AGENTS.md as a copy of CLAUDE.md if use_ai_agents is true
    claude_md = project_dir / "CLAUDE.md"
    agents_md = project_dir / "AGENTS.md"
    if use_ai_agents and claude_md.exists():
        # Copy instead of symlink for cross-platform reliability
        agents_md.write_text(claude_md.read_text(), encoding="utf-8")

    # Make scripts executable
    scripts_dir = project_dir / "scripts"
    if scripts_dir.exists():
        for script in scripts_dir.glob("*.sh"):
            script.chmod(0o755)

    # Install dependencies
    if package_manager == "uv":
        # First run: create lockfile and sync
        subprocess.run(["uv", "sync"], cwd=project_dir, check=True)
    elif package_manager == "python-env":
        # Create venv using current Python
        subprocess.run([sys.executable, "-m", "venv", ".venv"], cwd=project_dir, check=True)
        # Determine venv bin path
        if os.name == "nt":
            venv_python = project_dir / ".venv" / "Scripts" / "python.exe"
        else:
            venv_python = project_dir / ".venv" / "bin" / "python"
        subprocess.run(
            [str(venv_python), "-m", "pip", "install", "-r", "requirements-dev.txt"],
            cwd=project_dir,
            check=True,
        )
    elif package_manager == "pixi":
        subprocess.run(["pixi", "install"], cwd=project_dir, check=True)

    # Install pre-commit hooks if requested
    if use_pre_commit:
        subprocess.run(["pre-commit", "install"], cwd=project_dir, check=True)

    print("\nProject generated. Next steps:")
    print("  - Review the generated files.")
    print("  - Add your code to src/.")
    print("  - Run tests with the configured package manager.")


if __name__ == "__main__":
    main()
