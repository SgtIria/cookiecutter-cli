from click.testing import CliRunner

from {{ cookiecutter.project_slug }} import cli


def test_command_line_interface():
    runner = CliRunner()
    result = runner.invoke(cli.{{ cookiecutter.project_slug }}, ["test"])
    assert result.exit_code == 0
    assert result.output == "Hello, World!\n"
