import os
import sys
import importlib

from click.testing import CliRunner


def test_bake_project(cookies):
    result = cookies.bake()

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == "python_project"
    assert result.project.isdir()


def test_bake_project_with_wrong_project_name(cookies):
    result = cookies.bake(extra_context={"project_slug": "project$name"})
    assert result.exit_code == -1


def test_bake_project_with_wrong_email(cookies):
    result = cookies.bake(extra_context={"email": "my.false.email"})
    assert result.exit_code == -1


def test_bake_project_with_wrong_command_name(cookies):
    result = cookies.bake(extra_context={"command_name": "my command"})
    assert result.exit_code == -1


def test_bake_project_without_license(cookies):
    result = cookies.bake(extra_context={"license": "Not open source"})
    assert result.exception is None
    assert not result.project.join("LICENSE").check()


def test_bake_project_without_travis(cookies):
    result = cookies.bake(extra_context={"use_travis": "No"})
    assert result.exit_code == 0
    assert result.exception is None
    assert not result.project.join(".travis.yml").check()


def test_bake_project_without_appveyor(cookies):
    result = cookies.bake(extra_context={"use_appveyor": "Nope"})
    assert result.exit_code == 0
    assert result.exception is None
    assert not result.project.join("appveyor.yml").check()


def test_console_script_cli(cookies):
    result = cookies.bake()
    project_path = str(result.project)
    project_slug = os.path.split(project_path)[-1]
    project_dir = os.path.join(project_path, project_slug)
    module_path = os.path.join(project_dir, "cli.py")
    module_name = ".".join([project_slug, "cli"])

    if sys.version_info >= (3, 5):
        spec = importlib.util.spec_from_file_location(module_name, module_path)
        cli = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cli)
    elif sys.version_info >= (3, 3):
        file_loader = importlib.machinery.SourceFileLoader
        cli = file_loader(module_name, module_path).load_module()
    else:
        raise Exception(
            "Error: Wrong python version: {} need 3.3+".format(
                sys.version[:5])
        )

    runner = CliRunner()
    cli_result = runner.invoke(cli.python_project, ["test"])
    assert cli_result.output == "Hello, World!\n"
