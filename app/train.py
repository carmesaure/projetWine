import keras
import sys
import unittest

sys.path.append("./")

from dataset import Dataset_Loader
import model_.models as models

class TrainClass:
    model_type : str

    batch_size : int
    epochs : int

    model = None
    

    def __init__(self,model_type="regression", batch_size=128, epochs = 200):
        self.model_type=model_type
        self.batch_size=batch_size
        self.epochs=epochs
        if model_type == "regression":
                self.model = models._regression_model()
        elif model_type =="classification":
                self.model = models._classification_model()   ##pb
        else:
            raise ValueError

    def _train(self):
        loader = Dataset_Loader('data/Wines.csv')
        train_data, train_label=loader._get_train_data()
        val_data, val_label=loader._get_val_data()
        self.model.fit(train_data,train_label,batch_size=self.batch_size,epochs=self.epochs,verbose=1,validation_data=(val_data,val_label))

    def _save(self):
        filename=self.model_type+'_model_wine.h5'
        self.model.save(filename)


if __name__ == '__main__':
    t=TrainClass()
    t._train()
    t._save()

    loader = Dataset_Loader('data/Wines.csv')
    X_test, Y_test = loader._get_test_data()
    predictions=t.model.predict(X_test)
    for i in range(0,len(predictions)):
        print("predict : ",predictions[i], "resultat attendu : ", Y_test[i])

    print(t.model.evaluate(X_test,Y_test))