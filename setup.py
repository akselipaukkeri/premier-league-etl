# setup.py
from setuptools import setup, find_packages

setup(
    name="PL_ETL",  # Replace with a name for your project
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)