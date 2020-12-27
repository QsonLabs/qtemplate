import os

from invoke import task, Collection, run


@task
def info(c):
    """Prints info about the templating engine"""
    print("Welcome to qtemplate - https://github.com/QsonLabs/qtemplate")
