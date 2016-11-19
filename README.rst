================
Cookiecutter-cli
================

.. image:: https://travis-ci.org/Kalwyn/cookiecutter-cli.svg?branch=master
    :target: https://travis-ci.org/Kalwyn/cookiecutter-cli

.. image:: https://ci.appveyor.com/api/projects/status/n3dheupcd9lcffkg?svg=true
    :target: https://ci.appveyor.com/project/Kalwyn/cookiecutter-cli

|

A Cookiecutter_ template to generate a command line interface project
with click for python version >= 3.3.
Template inspired by Pypackage_ of Audrey Roy Greenfeld.

Features
========

* Generate .env files from autoenv_ to activate python virtualenv and export
  custom environment variables
* Testing with ``py.test`` or ``python setup.py pytest``
* Continuous Integration with Travis_ and Appveyor_
* Launch tests with several environments thanks to Tox_
* Documentation generation with Sphinx_
* Manage version with Bumpversion_


Prerequisite
============
Install cookiecutter_ and virtualenv_ [#]_ packages from pip::

    pip install -U cookiecutter virtualenv

Define a VENV env variable in your bash or zsh rc file that store the
absolute path to the folder containing your virtual environments::

    # File: $HOME/.zshenv
    export VENV=$HOME/".virtualenvs"

Create a virtualenv with project_slug as name::

    # With virtualenv
    virtualenv $VENV/project_slug

.. [#] If you already have virtual env solution like pew_, just be sure to add
   the VENV variable and create your virtual env with the project_slug as env
   name. If you're using pyenv-virtualenv_ you will need to make some
   ajustments to the .env file concerning the way of activation.


Usage
=====

Generate the python project::

    cookiecutter https://github.com/Kalwyn/cookiecutter-cli

Answer the questions to personalize the project

Get into the newly generated project. Thanks to .env file, your virtualenv
get automatically activated::

    cd project_slug

Install the requirements::

    pip install -r requirements/local.txt

**You are ready!**


.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _virtualenv: https://pypi.python.org/pypi/virtualenv
.. _pew: https://github.com/berdario/pew
.. _pyenv-virtualenv: https://github.com/yyuu/pyenv-virtualenv
.. _autoenv: https://github.com/kennethreitz/autoenv
.. _Pypackage: https://github.com/audreyr/cookiecutter-pypackage
.. _Travis: http://travis-ci.org/
.. _Appveyor: https://ci.appveyor.com/
.. _Tox: http://testrun.org/tox/
.. _Sphinx: http://sphinx-doc.org/
.. _Bumpversion: https://github.com/peritus/bumpversion
