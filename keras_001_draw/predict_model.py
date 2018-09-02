from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

datagen = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')

datagen1 = ImageDataGenerator()

img = load_img('datu-1.jpg')  # this is a PIL image
x = img_to_array(img)  # this is a Numpy array with shape (3, 150, 150)
x = x.reshape((1,) + x.shape)  # this is a Numpy array with shape (1, 3, 150, 150)

print(type(x))
print(x.shape)


# the .flow() command below generates batches of randomly transformed images
# and saves the results to the `preview/` directory
i = 0


for batch in datagen1.flow_from_directory('log_dir',target_size=(300,300),color_mode='grayscale'):
    print(type(batch))
    print(type(batch[1]))
    print(type(batch[0]))
    i += 1
    if i > 20:
        break  # otherwise the generator would loop indefinitely

# for batch in datagen1.flow(x, batch_size=1,
#                           save_to_dir='log_dir', save_prefix='cat', save_format='jpeg'):
#     i += 1
#     if i > 20:
#         break  # otherwise the generator would loop indefinitely
