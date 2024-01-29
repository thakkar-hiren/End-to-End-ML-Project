from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requires(filepath:str)->List[str]:
    requirements = []
    with open(filepath) as file:
        requirements = file.readlines()
        requirements = [require.replace("\n","") for require in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements

setup(
    name='ML-Project',
    version='0.0.1',
    author='Hiren Thakkar',
    author_email='thakkarhirenm@gmail.com',
    packages=find_packages(),
    install_requires = get_requires('requirements.txt')
)