#!/usr/bin/python

from setuptools import setup
import setuptools

setup(
    name = "dokusyometer",
    author = 'dynamonda',
    version = '0.0.1',
    description = "読書メーターから情報を取得するAPI",
    packages = setuptools.find_packages(),
    test_suite = 'test'
)