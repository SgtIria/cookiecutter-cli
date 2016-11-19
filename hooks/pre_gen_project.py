import re
import sys


# Validate project name
name_regex = re.compile(r'^[_a-zA-Z][_a-zA-Z0-9]+$')
project_name = "{{ cookiecutter.project_slug }}"
if not name_regex.match(project_name):
    print('ERROR: {} is not a valid Python module name!'.format(project_name))
    sys.exit(1)

# Validate email
email_regex = re.compile(
    r"(^[-!#$%&'*+/=?^_`{}|~0-9A-Z]+(\.[-!#$%&'*+/=?^_`{}|~0-9A-Z]+)*"
    r'|^"([\001-\010\013\014\016-\037!#-\[\]-\177]|\\[\001-011\013\014\016-\177])*"'
    r')@(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?$',
    re.IGNORECASE
)
email = "{{ cookiecutter.email }}"
if not email_regex.search(email):
    print("Error: {} is not a valid email!".format(email))
    sys.exit(1)

# Validate command name
cmd_regex = re.compile("[^a-zA-Z0-9-_]")
cmd = "{{ cookiecutter.command_name }}"
if cmd_regex.search(cmd):
    print("Error: {} is not a command name!".format(cmd))
    sys.exit(1)
