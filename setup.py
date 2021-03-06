"""Mailmerge build and install configuration."""
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme_file:
    README = readme_file.read()

setup(
    name="mailmerge",
    description="A simple, command line mail merge tool",
    long_description=README,
    version="1.9",
    author="Andrew DeOrio",
    author_email="awdeorio@umich.edu",
    url="https://github.com/awdeorio/mailmerge/",
    license="MIT",
    packages=["mailmerge"],
    keywords=["mail merge", "mailmerge", "email"],
    install_requires=[
        "backports.csv;python_version<='2.7'",
        "chardet",
        "click",
        "configparser",
        "jinja2",

        # The attachments feature relies on a bug fix in the future library
        # https://github.com/awdeorio/mailmerge/pull/56
        "future>0.18.0",

        "backports.csv;python_version<='2.7'",
        "markdown",
        "mock;python_version<='2.7'",
        "sh",
    ],
    extras_require={
        'dev': [
            'check-manifest',
            'codecov>=1.4.0',
            'pdbpp',
            'pycodestyle',
            'pydocstyle',
            'pylint',
            'pytest',
            'pytest-cov',
            'tox',
        ]
    },

    # Python command line utilities will be installed in a PATH-accessible bin/
    entry_points={
        'console_scripts': [
            'mailmerge = mailmerge.__main__:cli',
        ]
    },
)
