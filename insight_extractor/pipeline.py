
from pkg_resources import resource_filename

from .preprocessors import clean_docs, tokenize
from .predict import load_model, predict


### CONFIG ###
MAX_SEQ_LENGTH    = 500
MAX_NUM_WORDS     = 15000


# get current working directory
MODEL_PATH = resource_filename(__name__, "models/model-combined-1.h5")
TOKENIZER_PATH = resource_filename(__name__, "models/combined-tokenizer.json")

###################################
### Insight Prediction Pipeline ###
###################################

# takes a list of sentences and returns insight predictions.
def extract_insights(sentences):
    ### PREPROCESS ##
    cleaned_docs = clean_docs(sentences) # clean docs
    tokenized_docs = tokenize(cleaned_docs, TOKENIZER_PATH) # tokenize docs 

    ## PREDICT ##
    model = load_model(MODEL_PATH) # load model
    predictions = predict(tokenized_docs, model) # make predictions [prob_no_insight, prob_yes_insight]

    # return prob of insight
    probs_insight = [p[1] for p in predictions]
    return probs_insight