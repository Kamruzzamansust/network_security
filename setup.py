'''
The setup.py file is an essential part of packaging and 
distributing Python projects. It is used by setuptools 
(or distutils in older Python versions) to define the configuration 
of your project, such as its metadata, dependencies, and more
'''

from setuptools import find_packages , setup
from typing import List
def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """

    requirements_lst = []
    try: 
        with open('requirements.txt','r') as file:
            # read lines from the file 
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != 'e .':
                    requirements_lst.append(requirement)
            print(requirements_lst)
    except FileNotFoundError:
        print("requirements.txt file not found")
    
    return requirements_lst

setup(
    name="MyNetworkSecurity",
    version="0.0.1",
    author="",
    author_email="kamruzzaman.sust15@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)


# if __name__ == "__main__":
#     get_requirements()
