import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(file_path):
    os.remove(os.path.join(PROJECT_DIRECTORY, file_path))


if __name__ == "__main__":
    if '{{ cookiecutter.use_travis }}' != 'y':
        remove_file('.travis.yml')

    if '{{ cookiecutter.use_appveyor }}' != 'y':
        remove_file('appveyor.yml')

    if 'Not open source' == '{{ cookiecutter.license }}':
        remove_file('LICENSE')

    # Add .env and .env_leave to gitignore
    with open(os.path.join(PROJECT_DIRECTORY, ".gitignore"), "a") as git_file:
        git_file.write((
            "\n# Env files\n"
            ".env\n"
            ".env_leave"
        ))
