'''
this file is essential for packaging and distrubuting the python projects.
'''

from setuptools import find_packages,setup
from typing import List


def get_requirements()->List[str]:
    '''
    this will return the list of requirements
    '''
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            # Read lines from the file
            lines = file.readlines()
            # process each line
            for line in lines:
                # whitespace removal
                requirement = line.strip()
                # ignoring empty lines and -e.
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print('requirements.txt file not found')

    return requirement_lst

setup(
    name = 'Network Security',
    version = '0.0.1',
    author='Somesh',
    author_email='biradarsomesh52@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)
    