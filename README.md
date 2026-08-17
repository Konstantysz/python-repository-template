# python-repository-template

A Copier template for Python projects. It sets up a repository with the tools and structure I use for new packages.

## Features

- Questions about package name, Python version, and optional components.
- Choice of package manager: uv, python-env, or pixi.
- Source layout, tests, CI, documentation, and pre-commit hooks.
- Instruction files for AI coding assistants.

## Usage

1. Install Copier:

   ```
   uv tool install copier
   ```

2. Generate a project:

   ```
   copier copy gh:your-user/python-repository-template path/to/new-project
   ```

3. Answer the questions.

4. The post-generation hook installs dependencies and initializes git.

## Development

Install dev dependencies:

```
uv sync --dev
```

Run tests:

```
uv run pytest
```

Generate a test project:

```
copier copy . /tmp/test-project --defaults
```

## Updating projects

Projects generated from this template keep a `.copier-answers.yml` file. To update them later, run:

```
copier update
```

## License

MIT