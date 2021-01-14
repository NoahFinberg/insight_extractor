### GET INPUT DATA ###

## Input data here. For now hard coded, but want a list of sentences to check
def load_data(file):

    with open(file) as f:
        data = f.readlines()
        # you may also want to remove whitespace characters like `\n` at the end of each line
        data = [x.strip() for x in data] 
    return data
