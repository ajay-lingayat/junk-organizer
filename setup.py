from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name = 'junk-organizer',
    version = '0.0.1',
    author="Ajay Lingayat",
    author_email="lingayatajay2810@gmail.com",
    description = "This module helps to organize the files that are randomly placed inside a specified folder.",
    url="https://github.com/Ajay2810-hub/file-organizer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules = ['JunkOrganizer'],
    package_dir = {'': 'src'},
    install_requires=[], 
    extras_require = {
       "dev":[
       "pytest>=3.7",
       ]
    },
    classifiers=[
       "Programming Language :: Python :: 3",
       "License :: OSI Approved :: MIT License",
       "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)
