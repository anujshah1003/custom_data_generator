# Custom Data Generator
 
 This repository elucidates the blog where I discussed how we can create our won custom data generator for different kind of inputs like single image input, a sequence of input or multiple input to be fed to multiple model (ensemble of model).

The links of the blog are given below:

[Chapter -1 : What is a generator function in python and the difference between yield and return].(https://medium.com/@anuj_shah/creating-custom-data-generator-for-training-deep-learning-models-part-1-5c62b20cff26)
Chapter-2: Writing a generator function to read your data that can be fed for training an image classifier in Keras.

This project is a template for Python projects, supplying the general layout and skeletons for mandatory files as defined in [the AIR CV style guide](http://github.conti.de/air-computer-vision/AirCvStyleGuide/blob/master/airCvPythonGuide.md).

This README file contains general content and should be seen as a starting point for the specific project only!
    
# Usage

Either clone this repository to start your own project or simply add all the files (also ```.gitignore```!) to the new project.
__Please delete all lines in this README file above the next section in order to get a proper README file.__
Edit all remaining lines in a meaningful way.

# _insert project name_

## COPYRIGHT

Copyright 2017 Corp S&T CDS&T AIR CV & Contributors

Licensed under the ContiSource License, Version 1.0.
You may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://github.conti.de/pages/ContiSource/ContiForge/documents/CSLicense

Software distributed under the License is distributed on AS IS BASIS and WITHOUT WARRANTY, either expressed or implied.
        
## INSTALLATION

### PYTHON DEPENDENCIES

Required python packages are collected in ```requirements.txt```, and can be installed (using pip) system-wide using
```bash
cd <project main folder>
sudo pip install -r requirements.txt
```
or locally using
```bash
cd <project main folder>
pip install --user -r requirements.txt 
```
### PACKAGE INSTALLATION

The package can be installed system-wide using
```bash
sudo python setup.py  install
```
or locally using
```bash
python setup.py  install --user
```
If you want to edit the source files while using the library, it may be useful to replace ```install``` with ```develop```.

## DEINSTALLATION

Use
```bash
(sudo) pip uninstall <package name>
```
to uninstall the package.

## Unit tests

To run all implemented unit tests, run

```bash
cd <project main folder>
python -m unittest discover
```
