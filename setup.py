# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# This call to setup() does all the work

from setuptools import setup, find_packages


setup(
    name="PromptTrack",
    version="1.0.2",
    description="Demo library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://PaquetLab_PromptTrack.readthedocs.io/",
    author="sophie NGO BIBINBE",
    author_email="anne.ngobibinbe@gmail.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent"
    ],
    packages=find_packages(include=["PromptTrack", "PromptTrack.*"]), #["PromptTrack"],
    include_package_data=True,
    install_requires=["numpy","timm","transformers", "matplotlib", "lap", "scikit-image", "opencv-python", "nms","torch", "torchvision", "torchaudio"]
)