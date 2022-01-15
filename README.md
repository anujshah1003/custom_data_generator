[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/anujshah645)

# Custom Data Generator
 
 This repository elucidates the video and the blog where I discussed how we can create our own custom data generator for different kind of inputs like single image input, a sequence of input or multiple input to be fed to multiple model (ensemble of model).

The links of the videos are given below:

Part-1: Introduction - https://youtu.be/oy5EeamF_M8

Part-2: What is a generator function - https://youtu.be/2tRR45vcn3o

Part-3: For single image input - https://www.youtube.com/watch?v=EkzB6PJIcCA&list=PLd9i_xMMzZF6mxod8D1CfqhMy85dyLMq2&index=8

Part-4: For temporal input / video - https://www.youtube.com/watch?v=TyM1F0fvwoI&list=PLd9i_xMMzZF6mxod8D1CfqhMy85dyLMq2&index=9

The links of the blog are given below:

[Chapter -1 : What is a generator function in python and the difference between yield and return](https://medium.com/@anuj_shah/creating-custom-data-generator-for-training-deep-learning-models-part-1-5c62b20cff26)

[Chapter-2: Writing a generator function to read your data that can be fed for training an image classifier in Keras.](https://medium.com/@anuj_shah/creating-custom-data-generator-for-training-deep-learning-models-part-2-be9ad08f3f0e)

[Chapter-3: Writing generator function for different kind of inputs — multiple input or sequence of input.](https://medium.com/@anuj_shah/creating-custom-data-generator-for-training-deep-learning-models-part-3-c239297cd5d6)
    
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

