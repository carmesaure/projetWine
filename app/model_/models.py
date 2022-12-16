from keras import models
from keras import layers
from keras import metrics
from sklearn.linear_model import LinearRegression
import pickle

"""
    Create a model with:
        - Dense layers of 11 units with the LeakyReLU activation
        - Dense layers of 64 units with the LeakyReLU activation
        - Dense layers of 64 units with the LeakyReLU activation
        - Dense layers of 1 units with the linear activation
    loss : mean squared error
    optimizer : adam
    metrics : MeanAbsolutePercentage
"""
def _base_model():
    base_model = models.Sequential()
    base_model.add(layers.Dense(units = 11, input_shape=(11,),activation='LeakyReLU'))
    base_model.add(layers.Dense(units = 64,activation='LeakyReLU'))
    base_model.add(layers.Dense(units = 64,activation='LeakyReLU'))
    base_model.add(layers.Dense(units = 1,activation='linear'))
    base_model.compile(loss='mean_squared_error',optimizer='adam', metrics=[metrics.MeanAbsolutePercentageError()])
    return base_model

"""
    Linear Regression
"""
def _regression_model():
    regression_model = LinearRegression()
    return regression_model


"""
    Load the model from the file
"""
def _load_model(model_type : str):
    if model_type=='regression':
        model = pickle.load(open('regression_model_wine.h5', 'rb'))
    elif model_type=='base':
        model = models.load_model('base_model_wine.h5')
    else:
        model=None
    return model

