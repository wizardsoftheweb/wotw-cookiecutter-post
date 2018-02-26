"""This file provides hooks to be run after basic generation"""

from os import getcwd, makedirs
from cookiecutter.main import cookiecutter

ROOT_DIR = getcwd()

if '{{ cookiecutter.posts_dir }}' != '{{ cookiecutter.templates_dir }}':
    makedirs('{{ cookiecutter.templates_dir }}')

cookiecutter(
    'https://github.com/wizardsoftheweb/wotw-cookiecutter-base.git',
    no_input=True,
    extra_context={
        'directory_name': '{{ cookiecutter.directory_name }}'
    }
)
