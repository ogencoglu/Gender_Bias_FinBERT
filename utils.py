'''
Utility functions
'''

__author__ = 'Oguzhan Gencoglu'

import numpy as np


def get_fill_in_the_blank_probability(pipe, masked_sentence, test_word):
    '''
    [pipe]            : transformers pipeline object
    [masked_sentence] : str
    [test_word]       : str

    Returns the probability of 'test_word' filling the blank in
    'masked_sentence', given a model.
    '''
    # get probabilities of all tokens in the vocab
    predictions = pipe(masked_sentence, top_k=pipe.tokenizer.vocab_size)

    # find the test_word token and fetch its probability
    rank = np.where(
                [pred['token_str'] == test_word for pred in predictions]
                )[0][0]
    probability = np.round(predictions[rank]["score"], 6)

    print(f'\tProbability of "{test_word}" filling the blank in the sentence'
          f' "{masked_sentence.replace("[MASK]", "_________")}" is'
          f' {probability}.')

    return probability
