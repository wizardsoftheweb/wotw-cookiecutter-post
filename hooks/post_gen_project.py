"""This file provides hooks to be run after basic generation"""

# from os import getcwd()
from cookiecutter.main import cookiecutter

cookiecutter(
    'https://github.com/wizardsoftheweb/wotw-cookiecutter-base.git',
    no_input=True,
    extra_context={
        'directory_name': '{{ cookiecutter.directory_name }}'
    }
)
