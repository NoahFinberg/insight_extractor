import tensorflow as tf

def load_model(file):
    ### Load ML Model ###
    cnn_ = tf.keras.models.load_model(file)
    return cnn_

### Run Predictions ##
## Model does ok here, but some insights are given 10-30% chance of being an insight. Correctly classifies non-insights so could possible set the threshold lower than 50% to predict.
def predict(tokenized_sentences, model):
    predictions = model.predict(tokenized_sentences, batch_size=10, verbose=0)
    return predictions