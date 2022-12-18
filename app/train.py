import keras
import sys
import unittest

sys.path.append("./")

from app.dataset import Dataset_Loader
import app.model_.models as models
import pickle


"""
    This class is used to train the model and or save it .
    Class variables:
        model_type : str    by default 'regression'
        batch_size : int    by default 128
        epochs : int    by default 200
        model
"""
class TrainClass:
    model_type : str

    batch_size : int
    epochs : int

    model = None
    
    """
        This function initialize our class
    """
    def __init__(self,model_type="regression", batch_size=128, epochs = 300):
        self.model_type=model_type
        self.batch_size=batch_size
        self.epochs=epochs
        if model_type == "regression":
                self.model = models._load_model('regression')
        elif model_type =="base":
                self.model = models._load_model('base')
        else:
            raise ValueError

    """
        Train our model with the chosen parameter and on the trainning dataset with the validation dataset
    """
    def _train(self):
        loader = Dataset_Loader('app/data/Wines.csv')
        train_data, train_label=loader._get_train_data()
        val_data, val_label=loader._get_val_data()
        if self.model_type == 'base':
            self.model.fit(train_data,train_label,batch_size=self.batch_size,epochs=self.epochs,verbose=1,validation_data=(val_data,val_label))
        elif self.model_type=='regression':
            self.model.fit(train_data,train_label)
        else :
            raise ValueError
    """
        Save the model
    """
    def _save(self):
        filename=self.model_type+'_model_wine.h5'
        if self.model_type == 'base':
            self.model.save(filename)
        else :
            pickle.dump(self.model, open(filename, 'wb'))
        

    """
        Fonction qui retourne la description du modèle
    """
    def _description(self):
        res=''
        if self.model_type=='base':
            res=self.model.summary()
        elif self.model_type=='regression':
            res=self.model.coef_
        else:
            res="Model not found"
        return res

#Test du code
# if __name__ == '__main__':
#     t=TrainClass('regression')
#     t._train()
#     t._save()
#     print(t._description())

#     bestwine=[10.5,0.3,0.5,2.78,0.071,9.0,16.0,0.994,3.15,0.75,14]


#    loader = Dataset_Loader('data/Wines.csv')

#    X_test, Y_test = loader._get_test_data()   

#    predictions=t.model.predict(X_test)
#    for i in range(0,len(predictions)):
#        print("predict : ",predictions[i], "resultat attendu : ", Y_test[i])

