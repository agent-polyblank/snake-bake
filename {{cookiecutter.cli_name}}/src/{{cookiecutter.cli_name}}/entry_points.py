"""Entry point for module {{cookiecutter.cli_name}}."""

from argparse import ArgumentParser

from src.{{cookiecutter.cli_name}}.example import greeting


def main() -> None:
    """{{cookiecutter.project_name}} entry."""
    parser = ArgumentParser("{{cookiecutter.project_name}}")
    # Usage example
    parser.add_argument(
        "--some_arg",
        help="desc",
        dest="greeting",
        required=True,
    )
    args = parser.parse_args()
    greeting(args.greeting)
