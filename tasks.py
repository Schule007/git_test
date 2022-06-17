from invoke import task
import os

@task
def invls(c):

    # get current directory
    path = os.getcwd()
    print("Current Directory", path)

    # prints parent directory
    parent_direc = (os.path.abspath(os.path.join(path, os.pardir)))

    print(os.listdir(parent_direc))


