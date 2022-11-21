import keras
import tensorflow as tf
import numpy as np
from tensorflow.keras import layers



def build_NN_Architecture(batch_size):
    inputs = keras.Input((batch_size))

    x = layers.Dense(units=64, activation='relu')(inputs)
    x = layers.Dense(units=64, activation='relu')(x)
    x = layers.Dense(units=64, activation='relu')(x)
    x = layers.Dense(units=64, activation='relu')(x)
    x = layers.Dense(units=64, activation='relu')(x)

    output = layers.Dense(units=6, activation='sigmoid')(x)

    model = keras.Model(inputs, output, name="Example_Model")
    return model

    return model



def DNN_train(model, DNN_input_array, DNN_output_array, batch_size, learning_rate):
    # Creates the Tensorflow Training Array
    print('Dataset Input size = ', DNN_input_array.shape)
    print('Dataset Output Size = ', DNN_output_array.shape)
    print(DNN_output_array)
    train_dataset = tf.data.Dataset.from_tensor_slices((DNN_input_array, DNN_output_array))
    train_dataset = train_dataset.shuffle(1).batch(batch_size)

    model.summary()

    optimizer = keras.optimizers.Adam(learning_rate=learning_rate)

    model.compile(loss="categorical_crossentropy",
                  optimizer=optimizer,
                  metrics=['acc'])

    model.fit(
        train_dataset,
        #validation_data=train_dataset,
        epochs=30,
        verbose=1
    )