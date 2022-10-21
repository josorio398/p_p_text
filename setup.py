#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 11:31:37 2022

@author: oscar
"""

from setuptools import setup

setup(name="p_p_text",
    version="0.1.7",
    description='''
                Esta libreria es para preprocesar texto
                ''',
    author="Curso NLP U America",
    author_email='',
    license="MIT",
    url="https://gitlab.com/oscarriojas/p_p_text_ti.git",
    install_requires=[i.strip() for i in open("requirements.txt").readlines()],
    )
