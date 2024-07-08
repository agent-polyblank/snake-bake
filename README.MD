<h1 align="center">
  <a href="https://github.com/agent-polyblank/snake-bake">
    <img src="./assets/logo.jpeg" alt="Logo" width="300" height="300">
  </a>
</h1>

<div align="center">
  <h1>SnakeBake 🐍🥧</h1>
  <p>Lightweight Python project generator using CookieCutter and Hatch.</p>
  <br />
  <a href="https://github.com/agent-polyblank/snake-bake/issues/new?assignees=&labels=bug&template=1-bug-report.md&title=bug%3A+">Report a Bug</a>
  ·
  <a href="https://github.com/agent-polyblank/snake-bake/issues/new?assignees=&labels=enhancement&template=4-feature-request.md&title=feat%3A+">Request a Feature</a>
  .
  <a href="https://github.com/agent-polyblank/snake-bake/discussions">Ask a Question</a>
<br />
</div>

<div align="center">

<br />

[![Licence](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)](./LICENSE)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Ruff](https://img.shields.io/badge/ruff-3670A0?style=for-the-badge&logo=ruff&logoColor=d7ff64)
![Pre-commit](https://img.shields.io/badge/pre--commit-3670A0?style=for-the-badge&logo=pre-commit&logoColor=fab040)
![PyTest](https://img.shields.io/badge/pytest-3670A0?style=for-the-badge&logo=pytest&logoColor=0a9edc)
![Cookiecutter](https://img.shields.io/badge/cookiecutter-3670A0?style=for-the-badge&logo=cookiecutter&logoColor=d4aa00)

</div>

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Features](#features)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Step-by-step](#step-by-step)
- [Usage](#usage)
  - [Activating the Environment](#activating-the-environment)
  - [Running the Application](#running-the-application)
- [Project Structure](#project-structure)
- [Development](#development)
  - [Installing Dependencies](#installing-dependencies)
  - [Linting and Formatting](#linting-and-formatting)
- [Testing](#testing)
  - [Pre-Commit](#pre-commit)
- [Deployment](#deployment)
  - [Building the Package](#building-the-package)
  - [Publishing the Package](#publishing-the-package)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Features

- **Hatch**: Modern project management for Python, including environment management, testing, and packaging.
- **Pre-configured linting:**: With ruff
- **Pre-configured test suite**: Pytest for robust testing.
- **Pre-commit**: Hooks for automated code checks.

## Installation

### Prerequisites

- Python 3.8+
- Cookiecutter
- Hatch

### Step-by-step

1. Install Cookiecutter and Hatch:

```bash
pip install cookiecutter hatch
```

2. Create a new project using the template:

```bash
cookiecutter gh:agent-polyblank/snake-bake
```

Follow the prompts to customize your project.

3. Navigate to the project directory:

```bash
cd your-project-name
```

4. Initialize the Hatch environment:

```bash
hatch env create
```

## Usage

### Activating the Environment

To activate the Hatch environment, run:

```bash
hatch shell
```


### Running the Application

After activating the environment, you can run your application using:

```bash
python -m your_project_name
```

## Project Structure

The project structure follows a standard layout:

```
your_project_name
 ┣ .github
 ┃ ┣ ISSUE_TEMPLATE
 ┃ ┃ ┣ 1-bug-report.md
 ┃ ┃ ┣ 2-failing-test.md
 ┃ ┃ ┣ 3-docs-bug.md
 ┃ ┃ ┣ 4-feature-request.md
 ┃ ┃ ┣ 5-enhancement-request.md
 ┃ ┃ ┣ 6-security-report.md
 ┃ ┃ ┣ 7-question-support.md
 ┃ ┃ ┗ config.yml
 ┃ ┣ CODEOWNERS
 ┃ ┣ CODE_OF_CONDUCT.md
 ┃ ┣ CONTRIBUTING.md
 ┃ ┣ FUNDING.yml
 ┃ ┣ ISSUE_TEMPLATE.md
 ┃ ┣ SECURITY.md
 ┃ ┣ SUPPORT.md
 ┃ ┣ config.yml
 ┃ ┣ issue_label_bot.yaml
 ┃ ┣ pull_request_template.md
 ┃ ┗ settings.yml
 ┣ src
 ┃ ┗ your_project_name
 ┃ ┃ ┣ __about__.py
 ┃ ┃ ┣ __init__.py
 ┃ ┃ ┣ __main__.py
 ┃ ┃ ┗ example.py
 ┣ tests
 ┃ ┣ __init__.py
 ┃ ┗ test.py
 ┣ .gitignore
 ┣ .pre-commit-config.yaml
 ┣ LICENSE.txt
 ┣ README.md
 ┗ pyproject.toml
```

## Development

### Installing Dependencies

To install the project dependencies, activate the Hatch environment and run:

```bash
hatch env install
```

### Linting and Formatting

Run the following command to lint and format code with Ruff:

```bash
hatch fmt
```
## Testing

To run tests using Pytest, execute:

```bash
hatch test
```

### Pre-Commit

To install pre-commit hooks:

```bash
pip install pre-commit && pre-commit install
```

## Deployment

### Building the Package

To build the package, run:

```bash
hatch build
```

### Publishing the Package

To publish the package to PyPI, configure your credentials in `~/.pypirc` and run:

```bash
hatch publish
```

## Contributing

Contribution to SnakeBake are welcomed! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Install pre-commit hooks
4. Make your changes.
5. Ensure your changes pass pre-commit
6. Submit a pull request with a detailed description of your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---


## Acknowledgments

Special thanks to:

* [DecodeOs: Amazing Github Template](https://github.com/dec0dOS/amazing-github-template): for their excellent README.
* [Josee9988](project-template): For their Excellent issue templates.
