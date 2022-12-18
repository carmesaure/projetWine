import csv
import random
from sklearn import preprocessing

"""
    This class is used to load the dataset and to split it into training and test sets.
    Class variables:
        path : str
        data : list
        labels : list
        test_data : list
        test_labels : list
        train_data : list
        train_labels : list
        scaler : object
"""
class Dataset_Loader:

    path : str
    data : list
    labels : list
    test_data : list
    test_labels : list
    train_data : list
    train_labels : list
    val_data : list
    val_labels : list
    scaler : object


    """
        This function initialize our class
    """
    def __init__(self, path,ratio=0.75):
        self.path = path
        self.data = []
        self.labels = []
        self.test_data = []
        self.test_labels = []
        self.train_data = []
        self.train_labels = []
        self.val_data = []
        self.val_labels = []
        self.scaler=None
        self._load_data()
        self._normalize()
        self._init_train_test_dataset(ratio)
        self._init_val_dataset(0.05)
        

    """
        Load the data from the csv file self.path : parameters are stored in self.data and results (quality column) in self.labels
        Id column is not stored
        The data in the file have to be write like this :
        fixed acidity,volatile acidity,citric acid,residual sugar,chlorides,free sulfur dioxide,total sulfur dioxide,density,pH,sulphates,alcohol,quality,Id
    """
    def _load_data(self):
        try : 
            with open(self.path, 'r') as file:
                reader = csv.reader(file)
                i=0
                for row in reader:
                    if i==0 : 
                        i=i+1
                        caption = row
                    else: 
                        tmp = row[:-2]
                        for j in range(len(tmp)):
                            tmp[j] = float(tmp[j])

                        self.data.append(tmp)
                        self.labels.append(float(row[-2]))
        except FileNotFoundError:
            print("File not found")
                    
    
    """
        Split the dataset into training and test sets
        ratio : percentage of the dataset used for training. By default, 75% of the dataset is used for training
    """
    def _init_train_test_dataset(self, ratio):
        data_tmp = self.data.copy()
        labels_tmp = self.labels.copy()
        
        i=0
        while (i<ratio*len(self.data)):
            random_int=random.randrange(len(data_tmp))
            self.train_data.append(data_tmp.pop(random_int))
            self.train_labels.append(labels_tmp.pop(random_int))
            i=i+1
        self.test_data=data_tmp
        self.test_labels=labels_tmp

    """
        Split the dataset train into training and validation sets
        ratio : percentage of the dataset used for validation. By default, 5% of the dataset is used for validation
    """
    def _init_val_dataset(self, ratio):
        data_tmp = self.train_data.copy()
        labels_tmp = self.train_labels.copy()
        
        i=0
        while (i<ratio*len(self.train_data)):
            random_int=random.randrange(len(data_tmp))
            self.val_data.append(data_tmp.pop(random_int))
            self.val_labels.append(labels_tmp.pop(random_int))
            i=i+1
        self.train_data=data_tmp
        self.train_labels=labels_tmp


    """
        Normalize data between -1 and 1
    """
    def _normalize(self):
        self.scaler = preprocessing.StandardScaler().fit(self.data)
        self.data = (self.scaler.transform(self.data)).tolist()


    """
        Print size of dataset
    """
    def _info(self):
        print("Datasets Information :")
        print("Dataset train : ")
        print("Taille : ",len(self.train_data))
        print("Dataset validation : ")
        print("Taille : ",len(self.val_data))
        print("\nDataset test : ")
        print("Taille : ",len(self.test_data))
        print("\nDataset total : ")
        print("Taille : ",len(self.data))


#----------------GETTERS----------------

    """
        Return the train dataset
    """
    def _get_train_data(self):
        return(self.train_data,self.train_labels)

    """
        Return the validation dataset
    """
    def _get_val_data(self):
        return(self.val_data,self.val_labels)

    """
        Return the test dataset
    """
    def _get_test_data(self):
        return(self.test_data,self.test_labels)

    """
        Return the data dataset
    """
    def _get_data(self):
        return(self.data,self.labels)

    """
        Return the scaler
    """
    def _get_scaler(self):
        return(self.scaler)


    

