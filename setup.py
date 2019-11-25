import setuptools
import CrudeBHT

def requirements():
    with open('requirements.txt') as f:
        install_requires = [line.strip() for line in f]
    return install_requires

with open("readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "CrudeBHT",
    version = "1.0.7",
    author = "Naimish Mani B",
    author_email = "naimish240@gmail.com",
    description = "A simple implementation of the Barnes-Hut algorithm for N-body simulations in python 3.7 ",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    entry_points = {'console_scripts' : ['crudebht = CrudeBHT.__main__:main']},
    packages=setuptools.find_packages(),
    install_require = requirements(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)