# from keras.preprocessing.image import ImageDataGenerator
# from keras.models import Sequential
# from keras.layers import Conv2D, MaxPooling2D
# from keras.layers import Activation, Dropout, Flatten, Dense
# from keras import backend as K
# from keras.callbacks import TensorBoard
# from keras.applications.vgg16 import VGG16
# import numpy as np
#
# model = VGG16(weights='imagenet', include_top=False)
# print(model.summary())
#
# datagen = ImageDataGenerator(
#         rotation_range=40,
#         width_shift_range=0.2,
#         height_shift_range=0.2,
#         rescale=1./255,
#         shear_range=0.2,
#         zoom_range=0.2,
#         horizontal_flip=True,
#         fill_mode='nearest')
#
# generator = datagen.flow_from_directory(
#         'data/train',
#         target_size=(150, 150),
#         batch_size=32,
#         class_mode=None,  # this means our generator will only yield batches of data, no labels
#         shuffle=False)  # our data will be in order, so all first 1000 images will be cats, then 1000 dogs
# # the predict_generator method returns the output of a model, given
# # a generator that yields batches of numpy data
#
#
#
# bottleneck_features_train = model.predict_generator(generator, 2000)
# # save the output as a Numpy array
# print(type(bottleneck_features_train))
# print(bottleneck_features_train.shape)
# # print(bottleneck_features_train)
# np.save(open('bottleneck_features_train.npy', 'wb'), bottleneck_features_train)
#
# # generator = datagen.flow_from_directory(
# #         'data/validation',
# #         target_size=(150, 150),
# #         batch_size=32,
# #         class_mode=None,
# #         shuffle=False)
# # bottleneck_features_validation = model.predict_generator(generator, 400)
# # np.save(open('bottleneck_features_validation.npy', 'w'), bottleneck_features_validation)
#
#


mygenerator = (x*x for x in range(3))

for i in mygenerator :
        print(i)
for i in mygenerator :
        print(i)
