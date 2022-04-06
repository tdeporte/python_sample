#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('CHANGELOG.rst') as history_file:
    history = history_file.read()

requirements = []

setup_requirements = ['pytest-runner', 'wheel', ]

test_requirements = ['pytest>=3',]

setup(
    author="Tom Déporte",
    author_email='tom.deporte@etu.u-bordeaux.fr',
    python_requires='>=3.5',
    classifiers=[
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Basic python project to learn GitLab.",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='tom_project',
    name='tom_project',
    packages=find_packages(include=['tom_project', 'tom_project.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://gitlab.com/tdeporte/tom_project.git',
    version='0.1.0',
    zip_safe=False,
)
