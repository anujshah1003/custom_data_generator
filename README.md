# Custom Data Generator
 
 This repository elucidates the blog where I discussed how we can create our own custom data generator for different kind of inputs like single image input, a sequence of input or multiple input to be fed to multiple model (ensemble of model).

The links of the blog are given below:

[Chapter -1 : What is a generator function in python and the difference between yield and return](https://medium.com/@anuj_shah/creating-custom-data-generator-for-training-deep-learning-models-part-1-5c62b20cff26)

[Chapter-2: Writing a generator function to read your data that can be fed for training an image classifier in Keras.](https://medium.com/@anuj_shah/creating-custom-data-generator-for-training-deep-learning-models-part-2-be9ad08f3f0e)
    
I have used the code and concept of this blog as reference - http://www.jessicayung.com/using-generators-in-python-to-train-machine-learning-models/

# Usage

To create a data genrator you can follow the note book [flowers_recognition\data_generator.ipynb]()

        
## INSTALLATION

### PYTHON DEPENDENCIES
I used conda environment and I have installed few libraries explicitly like keras, opencv,scikit-laern, pandas.

All the libraries may not be present in the requirements.txt file

if you are getting error in installing some libraries from requirements.txt the you can just use pip install library name without any specific version.


      pip install -r requirements.txt
      pip install library_name



## Unit tests

To run all implemented unit tests, run

```bash
cd <project main folder>
python -m unittest discover
```
