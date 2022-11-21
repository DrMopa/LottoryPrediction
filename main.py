import NeauralNetwork
import getnumbers
import Data_Cleaning
import numpy as np

def main():
    CSV_URL = 'https://data.ny.gov/resource/d6yy-54nr.csv'
    CSV_File_Name = 'dataset.csv'

    getnumbers.Pull_Data(CSV_URL, CSV_File_Name)
    dataset = Data_Cleaning.load_Clean_Data(CSV_File_Name)
    dataset_labels = Data_Cleaning.Data_Labeling(dataset)


    DNN_output_array, DNN_input_array = Data_Cleaning.NN_Preperation(dataset, dataset_labels)
    batch_size = 1
    learning_rate = 0.01
    model = NeauralNetwork.build_NN_Architecture(batch_size)
    NeauralNetwork.DNN_train(model, DNN_input_array, DNN_output_array, batch_size, learning_rate)



if __name__ == "__main__":
    main()
