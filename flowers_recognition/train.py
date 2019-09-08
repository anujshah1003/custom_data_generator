# import the necessary modules from the library
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten, Activation, MaxPooling2D, Dropout

from config import Config
from custom_dataloader import FlowerRecognition


def load_model(pretrained_weights=None):
    
    input_shape = (Config.resize,Config.resize,3)
#    print (input_shape)
    model = Sequential()
    
    #filters,kernel_size,strides=(1, 1),padding='valid',data_format=None,dilation_rate=(1, 1),activation=None,use_bias=True,
    #kernel_initializer='glorot_uniform',bias_initializer='zeros',kernel_regularizer=None,bias_regularizer=None,
    #activity_regularizer=None,kernel_constraint=None,bias_constraint=None,
    
    #pool_size=(2, 2), strides=None, padding='valid',data_format=None
    
    model.add(Conv2D(32, (3,3),padding='same',input_shape=input_shape,name='conv2d_1'))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2),name='maxpool2d_1'))
    
    model.add(Conv2D(32, (3, 3),name='conv2d_2'))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2),name='maxpool2d_2'))
    
    model.add(Dropout(0.5))
    
    #model.add(Convolution2D(64, 3, 3))
    #model.add(Activation('relu'))
    #model.add(Convolution2D(64, 3, 3))
    #model.add(Activation('relu'))
    #model.add(MaxPooling2D(pool_size=(2, 2)))
    #model.add(Dropout(0.5))
    
    model.add(Flatten())
    model.add(Dense(64))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(Config.num_classes))
    model.add(Activation('softmax'))
    
    if pretrained_weights:
        model.load_weights(pretrained_weights)

    return model

if __name__=='__main__':
    
    #call the dataloader and create traina nd test dataloader object
    
    dataloader = FlowerRecognition(root_dir=r'D:\Trainings-2019\custom_data_generator\flowers_recognition')
       
    train_data_path = 'flowers_recognition_train.csv'
    test_data_path = 'flowers_recognition_test.csv'
    
    train_samples = dataloader.load_samples(train_data_path)
    test_samples = dataloader.load_samples(test_data_path)
    
    num_train_samples = len(train_samples)
    num_test_samples = len(test_samples)
    
    print ('number of train samples: ', num_train_samples)
    print ('number of test samples: ', num_test_samples) 
       
    # Create generator
    batch_size = Config.batch_size
    train_generator = dataloader.data_generator(train_samples, batch_size=batch_size)
    validation_generator = dataloader.data_generator(test_samples, batch_size=batch_size)
       
    
    model = load_model()
    model.summary()
    
    model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])
    
    model.fit_generator(
        train_generator,
        steps_per_epoch=num_train_samples // batch_size,
        epochs=Config.num_epochs,
        validation_data=validation_generator,
        validation_steps=num_test_samples // batch_size)
    model.save_weights('first_try.h5')
    