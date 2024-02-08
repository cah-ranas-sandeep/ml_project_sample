from setuptools import find_packages, setup
from typing import List

HYPHEN_DOT = '-e .'
def get_requirements(
    file_path: str        
) -> List[str]:
    
    '''
    Function will return list of requriements.
    '''

    requriement = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_DOT in requirements:
            requirements.remove(HYPHEN_DOT)

    return requirements

    
setup(
    name = 'ml_project',
    version = '0.0.1',
    author = 'Rana Sandeep S.',
    author_email = 'sandeep.rana@cardinalhealth.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
    
)