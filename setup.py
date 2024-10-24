from setuptools import find_packages,setup
from typing import List
def get_requirements(file_path:str)->List[str]:
    '''
     This function will return the list of requirements
     '''
    HYPEN_E_DOT="-e ."
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readline()
        [req.replace("\n","") for req in requirements]
        
        if(HYPEN_E_DOT in requirements):
            requirements.remove(HYPEN_E_DOT)
        
    return requirements
setup(
    name="House Rent Price Prediction",
    version="0.0.1",
    author="Ranjit",
    author_email="vhanmaneranjit80@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    
)