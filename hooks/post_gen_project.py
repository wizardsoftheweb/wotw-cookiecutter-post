"""This file provides hooks to be run after basic generation"""

from os import getcwd, listdir, makedirs, remove
from os.path import join
from shutil import move, rmtree
from subprocess import check_call

from cookiecutter.main import cookiecutter

from wotw_blogger.generator.macro import ShellSession

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

NESTED_DIR = join(ROOT_DIR, '{{ cookiecutter.directory_name }}')
remove(join(NESTED_DIR, '{{ cookiecutter.directory_name }}.sublime-project'))

CURRENT_FILES = listdir(NESTED_DIR)
NEW_FILES = listdir(ROOT_DIR)

for item in NEW_FILES:
    new_file_path = join(ROOT_DIR, item)
    if item in CURRENT_FILES:
        with open(new_file_path, 'r') as new_file:
            with open(join(NESTED_DIR, item), 'a') as current_file:
                current_file.write(new_file.read())
        remove(new_file_path)
    else:
        move(new_file_path, NESTED_DIR)

CURRENT_FILES = listdir(NESTED_DIR)
for item in CURRENT_FILES:
    move(join(NESTED_DIR, item), ROOT_DIR)

rmtree(NESTED_DIR)

check_call(['git', 'add', '.gitignore'])
check_call(
    [
        'git',
        'commit',
        '-m',
        'Extend .gitignore with Python.gitignore'
    ]
)
check_call(['git', 'add', 'README.md'])
check_call(['git', 'commit', '-m', 'Expand docs'])
check_call(['git', 'add', 'compiler.py'])
check_call(['git', 'commit', '-m', 'Draft basic post compiler'])
check_call(['git', 'add', join('{{ cookiecutter.posts_dir }}', '.gitignore')])
check_call(['git', 'commit', '-m', 'Define posts directory'])

if 'yes' == '{{ cookiecutter.install_shell_session }}':
    ShellSession().install('{{ cookiecutter.templates_dir }}')
    check_call(
        [
            'git',
            'add',
            join('{{ cookiecutter.templates_dir }}', 'shell_session.j2')
        ]
    )
    check_call(
        [
            'git',
            'commit',
            '-m',
            'Include shell_session macro']
    )

check_call(['git', 'add', '{{ cookiecutter.directory_name }}.sublime-project'])
check_call(['git', 'commit', '-m', 'Add common build systems'])
