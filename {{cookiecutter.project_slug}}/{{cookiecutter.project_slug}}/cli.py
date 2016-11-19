import click


@click.group()
def {{ cookiecutter.command_name }}():
    pass


@{{ cookiecutter.command_name }}.command()
def test():
    print("Hello, World!")
