# basic-sentiment
This repository implements sentiment analysis based on movie review data from the Rotten Tomatoes dataset. The data description can be found from [Kaggle](https://www.kaggle.com/c/sentiment-analysis-on-movie-reviews). A pre-trained neural network (NN) model from [my work](https://www.kaggle.com/issactai/sentiment-analysis-on-movie-review) is used.

The NN model is implemented by [Tensorflow 2.2.0](https://www.tensorflow.org/). A very simple server is hosted using Python's [Flask](https://flask.palletsprojects.com/en/1.1.x/). 

## Demonstration
This application is hosted at https://basic-sentiment.herokuapp.com/.
A pre-trained tokenizer and model are first instantiated.
User can input a short sentence and hit the submit button. A few steps will be carried to obtain the corresponding result on sentiment.
- pre-processing (lemmatized, turned to lower case and with punctuation removed).
- tokenization (using the loaded tokenizer).
- pre-padding (or truncation) to get a vector of length 48.
- prediction (using the loaded model).
The result (sentiment with probability) will then be displayed.

Furthermore, an end-point `\run` under a simple REST Architecture is available.

## NN Model
```sh
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
embedding_1 (Embedding)      (None, 48, 50)            842600    
_________________________________________________________________
lstm_1 (LSTM)                (None, 48, 128)           91648     
_________________________________________________________________
lstm_2 (LSTM)                (None, 48, 64)            49408     
_________________________________________________________________
global_max_pooling1d_1 (Glob (None, 64)                0         
_________________________________________________________________
dense_1 (Dense)              (None, 50)                3250      
_________________________________________________________________
dropout_1 (Dropout)          (None, 50)                0         
_________________________________________________________________
dense_2 (Dense)              (None, 5)                 255       
=================================================================
Total params: 987,161
Trainable params: 987,161
Non-trainable params: 0
```

## Getting Started
###Requirements
Python 3.8

### Install Dependencies
```sh
pip install -r requirements.txt
```
the cpu only of tensorflow 2.2.0 is used because the full package is too big to be deployed to Heroku.

### Run Application
```sh
export FLASK_APP=app.py
flask run
```

## Deployment to Heroku
To [deploy the application to Heroku](https://devcenter.heroku.com/articles/git), run the following:
```sh
heroku apps:create <NAME>
git push heroku master
```

## License
GPL-3.0