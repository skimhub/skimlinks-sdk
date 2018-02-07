from setuptools import find_packages, setup

setup(
    name='skimlinks-sdk',
    version='0.0.1',
    author='Skimlinks',
    author_email='dev@skimlinks.com',
    description='Wrapper for Skimlinks APIs',
    url='https://github.com/skimhub/skimlinks-sdk',
    packages=find_packages(exclude=['tests']),
    namespace_packages=[],
    install_requires=[],
)
