import numpy as np
import tensorflow as tf

def load_Clean_Data(fileName):
        arr = np.loadtxt(fileName, delimiter=",", dtype=str, skiprows=1)

        # remove / symbol from date
        arr = np.char.replace(arr, '/', '')

        # remove [ symbol...
        arr = np.char.replace(arr, '[', '')
        arr = np.char.replace(arr, ']', '')

        #remove random spaces
        arr = np.char.replace(arr, ' ', '')

        arr = arr.astype('uint')
        return arr

def NN_Preperation(dataset, labels):
    #this function will accept either the N dimensional dataset, or the 1-dimensional label set, and normalize both.
    def dataset_normalization(dataset): #todo to help support more games, record the maximum value of each array before normalization, so it can be used in post-processing
        dataset = np.array(dataset).astype('float32')
        for i in range(dataset.shape[1]):
            dataset[:, i] = dataset[:, i] / np.max(dataset[i]) #normalizes each colum to their own maximum
        return dataset

    # this function will accept either the N dimensional dataset, or the 1-dimensional label set, and split both the same amount.
    def dataset_splitSets(dataset): #todo actually split arrays, instead of just returning None as the test set.
        #train_dataset, test_dataset = np.split(dataset[:-20, :])
        return dataset, None



    #normalize both dataset and labels
    dataset = dataset_normalization(dataset)
    labels = labels / np.max(labels)

    return dataset, labels


def Data_Labeling(dataset): #adds an additional colum to the data, numbering them in order. This will be used as the NN input.
    label_array = list(range(0, dataset.shape[0])) #creats an array from 0 to the number of elements in the dataset.. numbering each
    label_array = np.array(label_array) #converts to numpy array

    return label_array
