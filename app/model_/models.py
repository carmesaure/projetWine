from keras import models
from keras import layers
from keras import metrics


def _regression_model():
    regression_model = models.Sequential()
    regression_model.add(layers.Dense(units = 11, input_shape=(11,),activation='LeakyReLU'))
    regression_model.add(layers.Dense(units = 1,activation='linear'))
    regression_model.compile(loss='mean_squared_error',optimizer='adam', metrics=[metrics.MeanAbsolutePercentageError()])
    return regression_model


def _classification_model():
    classification_model=models.Sequential()
    classification_model.add(layers.Dense(units=64, input_shape=(11,),activation='LeakyReLU'))
    classification_model.add(layers.Dense(units=128,activation='LeakyReLU'))
    classification_model.add(layers.Dense(units=11,activation='softmax'))

    classification_model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return classification_model

def _load_model(model_type : str):
    if model_type=='regression':
        model = models.load_model('regression_model_wine.h5')
    elif model_type=='classification':
        model = models.load_model('classification_model_wine.h5')
    else:
        model=None
    return model

