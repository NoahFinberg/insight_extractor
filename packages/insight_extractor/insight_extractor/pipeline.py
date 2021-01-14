import config
import preprocessors
import get_input_data
import predict

###################################
### Insight Prediction Pipeline ###
###################################


### LOAD ###
docs = get_input_data.load_data(config.INPUT_DATA_PATH)
print(docs)

### PREPROCESS ##
cleaned_docs = preprocessors.clean_docs(docs) # clean docs
tokenized_docs = preprocessors.tokenize(cleaned_docs, config.TOKENIZER_PATH) # tokenize docs 

## PREDICT ##
model = predict.load_model(config.MODEL_PATH) # load model
predictions = predict.predict(tokenized_docs, model) # make predictions [prob_no_insight, prob_yes_insight]
print(predictions)