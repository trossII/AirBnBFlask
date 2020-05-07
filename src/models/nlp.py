import pickle

def encode_neighbor(data):
    loaded_model = load_model()
    test_value = data['name']
    nlp = loaded_model.predict([[test_value]])
    return nlp
    

def load_model():
    """ Load the model from the .pickle file """
    model_file = open("src/models/nlp.sav", "rb")
    loaded_model = pickle.load(model_file)
    model_file.close()
    return loaded_model