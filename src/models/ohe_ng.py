import pickle

def encode_neighbor(data):
    loaded_model = load_model()
    test_value = data['neighbourhood_group_cleansed']
    data_ng = loaded_model.transform([[test_value]])
    return data_ng
    

def load_model():
    """ Load the model from the .pickle file """
    model_file = open("src/models/ohe_ng.sav", "rb")
    loaded_model = pickle.load(model_file)
    model_file.close()
    return loaded_model