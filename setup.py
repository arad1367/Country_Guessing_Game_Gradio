from setuptools import find_packages, setup
from typing import List

# Constant
HYPHEN_E_DOT="-e ."

# Define setup function
def get_requirements(file_path:str) -> List[str]:
    '''
    This function will return a list of requirements 
    '''
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name='country guessing game',
    version='0.0.1',
    author='Pejman Ebrahimi',
    author_email='pejman.ebrahimi77@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
