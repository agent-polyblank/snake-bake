"""Entry point for module {{cookiecutter.cli_name}}."""

from argparse import ArgumentParser

from src.example import greeting


def main() -> None:
    """{{cookiecutter.project_name}} entry."""
    parser = ArgumentParser("{{cookiecutter.project_name}}")
    # Usage example
    parser.add_argument(
        "--some_arg",
        help="desc",
        dest="arg_dest",
        required=True,
    )
    args = parser.parse_args()
    greeting(args.greeting)
