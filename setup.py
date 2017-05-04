# -*- coding: utf-8 -*-
import os.path
from setuptools import setup, find_packages

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

setup(
    name='s3touch',
    version='0.1.0',
    packages=find_packages(exclude=('tests', 'tests.*')),
    install_requires=[
        'awscli==1.11.82',
        'click==6.7',
    ],
    entry_points={"console_scripts": ["s3touch = cli:main"]},
    test_suite='tests',
    tests_require=[
    ],
    url='https://github.com/thulio/s3touch',
    license='MIT',
    author='Thúlio Costa',
    author_email='contact@thul.io',
    description="Touch files on S3.",
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy'
    ]
)
