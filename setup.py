from setuptools import setup, find_packages
from src.constants import __package_name__, __version__

with open('README.md', 'r', encoding = 'utf-8') as f:
    readme = f.read()

with open('requirements.txt', 'r', encoding = 'utf-8') as f:
    requires = f.read().splitlines()

with open('test_requirements.txt', 'r', encoding = 'utf-8') as f:
    test_requires = f.read().splitlines()

setup(
    name = __package_name__,
    version = __version__,
    author = 'wanny',
    author_email = 'wanny@gmail.com',
    long_desciption = readme,
    packages = find_packages(exclude = ['src', 'docs', 'tests']),
    package_data = {'': ['*.yaml', '*.yml']},
    install_requires = requires,
    setup_requires = ['pytest-runner'],
    tests_require = test_requires,
    python_requires = '>3.10',
    entry_points = {
        'console_scripts': ['woorin-stock-sts = src.main:main']
    },
    classifiers = [
        'Environment :: Console',
        'Operating System :: WINDOWS 10 x64',
        'Programming Language :: Python :: 3.10'
    ]
)

