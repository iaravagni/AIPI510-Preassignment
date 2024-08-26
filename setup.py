from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = [line.strip() for line in f if line.strip()]

setup(
    name="preassignment",
    version="0.0.1",
    description="Reads a CSV file and calculates de average age for men and women having a stroke",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "preassignment=preassignment.main:main",
        ],
    },
    author="Iara Ravagni",
    author_email="iara.ravagni@duke.edu",
    packages=find_packages(),
)