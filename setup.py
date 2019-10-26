from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='cli_utility',
    version='1.0.0',
    description='A simple CLI menu and output utility for python.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/bluewingtan/cli_utility',
    author='BlueWingTan',
    author_email='bluewingtan@yeah.net',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    keywords='menu output CLI',
    packages=find_packages(),
    python_requires='>=3.5',
    install_requires=['colorama>=0.4.1'],
    project_urls={
        'Bug Reports': 'https://github.com/bluewingtan/cli_utility/issues',
        'Source': 'https://github.com/bluewingtan/cli_utility/'
    }
)
