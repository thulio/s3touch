# -*- coding: utf-8 -*-
import codecs
import os.path
from setuptools import setup

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(PROJECT_DIR, 'README.rst'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

setup(
    name='s3touch',
    version='0.1.3',
    py_modules=['s3touch'],
    install_requires=[
        'awscli==1.11.82',
        'click==6.7',
    ],
    entry_points={"console_scripts": ["s3touch = s3touch:main"]},
    test_suite='tests',
    tests_require=[
    ],
    url='https://github.com/thulio/s3touch',
    license='MIT',
    author='Thúlio Costa',
    author_email='contact@thul.io',
    description="Touch files on S3.",
    long_description=long_description,
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
