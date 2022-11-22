import keras
import tensorflow as tf
import numpy as np
from tensorflow.keras import layers
import random



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



def DNN_train_Predict(model, DNN_input_array, DNN_output_array, batch_size, learning_rate):

    #this function is the post-processing to change the DNN values back into powerball numbers to pick
    def Interprate_Predictions(predictions): #todo this section is very hard coded for the power ball... this needs modularity for additional games
        output_predictions = []
        for i in range(5): #hardwired for the first 5 numbers that range from 1-69
            temp = predictions[0, i] * 69
            temp = np.round(temp)
            output_predictions.append(temp)

        #manually compute last digit... #todo thiis is not modular at all.
        temp = predictions[0, -1] * 26 #manually adjust the value for the 1-26 number
        temp = np.round(temp)
        output_predictions.append(temp)

        print('THE WINNING NUMBERS ARE!.')
        print(output_predictions)



    # Creates the Tensorflow Training Array
    print('Dataset Input size = ', DNN_input_array.shape)
    print('Dataset Output Size = ', DNN_output_array.shape)
    train_dataset = tf.data.Dataset.from_tensor_slices((DNN_input_array, DNN_output_array))
    train_dataset = train_dataset.shuffle(1).batch(batch_size)

    model.summary()

    optimizer = keras.optimizers.Adam(learning_rate=learning_rate)

    model.compile(loss="mean_squared_error",
                  optimizer=optimizer,
                  metrics=['acc'])

    model.fit(
        train_dataset,
        epochs=30,
        verbose=1
    )

    seed = (np.zeros(1) + random.uniform(0,1))
    print('\n')
    print('SEED = ', seed)
    predictions = model.predict(seed)

    Interprate_Predictions(predictions) #post-processing for human readability, and termination ofo program





