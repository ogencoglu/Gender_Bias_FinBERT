.. raw:: html

    <img src="https://github.com/ogencoglu/Gender_Bias_FinBERT/blob/main/media/media.png" height="400px">
    
**“Pekka”s are 260 times more likely to be an engineer than “Emilia”s! And “Tiia”s are 410 times more likely to love shopping than “Matti”s!**

Possible Gender Bias in Finnish BERT?
====================

The purpose of this mini-experiment is to:

- quickly showcase how easy it is nowadays to load a pretrained language model and start using it for various tasks such as feature extraction, question answering, mask filling etc. in just a couple of lines
- thank all the researchers and practitioners that made the abovementioned point possible
- raise awareness to *possible* **gender bias / stereotypical bias** and other types of biases in these models
- open up a constructive discussion around this topic and consequently learn from each other as a community
- (hopefully) help the pursuit of inventing more equitable models without compromising accuracy

and is not to:

- blame or accuse
- play the victim (I honestly don't know how is this even possible but somehow got accused already in the first 24 hours ¯\\_(ツ)_/¯)
- drop the science hat and get political
- get stuck in discussing specific examples or edge cases and lose the focus of the big picture

Note: this is just a quick & dirty demo to spark up some discussion. There are several studies for quantifying bias in contextual language models diligently,  `for example <https://arxiv.org/abs/1906.07337>`_.

Google Colab Online Demo
--------------

`Open in Colab <https://colab.research.google.com/drive/1sN0BWRQJEyALTHWInRCFvW354PQlEaW1?usp=sharing>`_

Locally
--------------

Run `<Gender_Bias_FinBERT_showcase.ipynb>`_

Remarks
--------------

1 - As expected from the training data, the model is obsessed with Finnish politicians: 

.. code-block:: python

    sentence = f"{pipe.tokenizer.mask_token} sanoi."
    pipe(sentence, top_k=10)

    [{'score': 0.05185465142130852,
      'sequence': '[CLS] Tuomioja sanoi. [SEP]',
      'token': 15697,
      'token_str': 'Tuomioja'},
     {'score': 0.04348713159561157,
      'sequence': '[CLS] Soini sanoi. [SEP]',
      'token': 8574,
      'token_str': 'Soini'},
     {'score': 0.04261799901723862,
      'sequence': '[CLS] hän sanoi. [SEP]',
      'token': 361,
      'token_str': 'hän'},
     {'score': 0.04241926968097687,
      'sequence': '[CLS] Niinistö sanoi. [SEP]',
      'token': 5975,
      'token_str': 'Niinistö'},
     {'score': 0.042333755642175674,
      'sequence': '[CLS] Hän sanoi. [SEP]',
      'token': 737,
      'token_str': 'Hän'},
     {'score': 0.038560837507247925,
      'sequence': '[CLS] Vanhanen sanoi. [SEP]',
      'token': 9499,
      'token_str': 'Vanhanen'},
     {'score': 0.03149525821208954,
      'sequence': '[CLS] Stubb sanoi. [SEP]',
      'token': 12173,
      'token_str': 'Stubb'},
     {'score': 0.03149261325597763,
      'sequence': '[CLS] Lipponen sanoi. [SEP]',
      'token': 10367,
      'token_str': 'Lipponen'},
     {'score': 0.025139369070529938,
      'sequence': '[CLS] Sipilä sanoi. [SEP]',
      'token': 9517,
      'token_str': 'Sipilä'},
     {'score': 0.01755082793533802,
      'sequence': '[CLS] Katainen sanoi. [SEP]',
      'token': 11015,
      'token_str': 'Katainen'}]

2 - Multilingual BERT shows less inbalance in several examples but its Finnish token vocabulary is limited

Finnish BERT model - FinBERT v1
--------------

`HuggingFace Transformers <https://huggingface.co/transformers/>`_ model card: *TurkuNLP/bert-base-finnish-cased-v1*

`Publication <https://arxiv.org/abs/1912.07076>`_

`TurkuNLP FinBERT page <http://turkunlp.org/FinBERT/>`_
