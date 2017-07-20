from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

#initialising cnn
classifier = Sequential()

#step-1 Convolution
classifier.add(Convolution2D(32,3,3,input_shape=(64,64,3),activation='relu'))

#step-2 Max Pooling
classifier.add(MaxPooling2D(pool_size = (2,2)))

#second Convolutional layer
classifier.add(Convolution2D(32,3,3,activation='relu'))

#second Max Pooling layer
classifier.add(MaxPooling2D(pool_size = (2,2)))

#step-3 Flattening
classifier.add(Flatten())

#step-4 Full Connection
classifier.add(Dense(output_dim = 128, activation = 'relu'))
classifier.add(Dense(output_dim = 1, activation = 'sigmoid'))

#compiling the cnn
classifier.compile(optimizer = 'adam',loss='biary_crossentropy',metrics=['accuracy'])

#Fitting cnn to the images
from keras.preprocessing.image import ImageDateGenerator
train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

train_set = train_datagen.flow_from_directory('dataset/training_set',
                                                target_size=(64, 64),
                                                batch_size=32,
                                                class_mode='binary')

test_set = test_datagen.flow_from_directory('dataset/test_set',
                                             target_size=(64, 64),
                                             batch_size=32,
                                             class_mode='binary')

classifier.fit_generator(
        train_set,
        steps_per_epoch=8000,
        epochs=25,
        validation_data=test_set,
        validation_steps=2000)

