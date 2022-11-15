import keras
import tensorflow as tf
import numpy as np

def main():

    def load_csv(fileName):
        arr = np.loadtxt(fileName, delimiter=",", dtype=str)

        #remove / symbol from date
        arr = np.char.replace(arr, '/', '')

        #remove random ï»¿ trash...
        arr = np.char.replace(arr, 'ï»¿', '')

        arr = arr.astype('uint')
        return arr

    def build_NN_Architecture(batch_size):
        model = keras.Sequential()
        model.add(tf.keras.layers.Dense(1, activation='relu', name='Input'))
        model.add(tf.keras.layers.Dense(16, activation='relu', name='Hidden_01'))
        model.add(tf.keras.layers.Dense(32, activation='relu', name='Hidden_02'))
        model.add(tf.keras.layers.Dense(64, activation='relu', name='Hidden_03'))
        model.add(tf.keras.layers.Dense(7, activation='relu', name='Output'))

        model.build(input_shape=(batch_size,1))

        return model

    def def_train_and_TestSet(dataset):
        #converts

    dataset = load_csv("dataset.csv")

    model = build_NN_Architecture(5)

    print(dataset)
    print(model.summary())

if __name__ == "__main__":
    main()
