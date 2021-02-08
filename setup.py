 

from setuptools import setup, find_packages

setup(
    name="dpersona",
    packages=["dpersona"],
    version="0.9",
    entry_points={
        'console_scripts': [
            "Dtest=dpersona.dpersona:main"]
    }
)
