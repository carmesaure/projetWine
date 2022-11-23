import csv
import random

class Dataset_Loader:
    path : str
    data = []
    labels = []
    test_data = []
    test_labels = []
    train_data = []
    train_labels =[]
    caption = []

    def __init__(self, path,ratio=0.75):
        self.path = path
        self._load_data()
        self._init_train_test_dataset(ratio)

    def _load_data(self):
        with open(self.path, 'r') as file:
            reader = csv.reader(file)
            i=0
            for row in reader:
                if i==0 : 
                    i=i+1
                    self.caption = row
                else: 
                    tmp = row[:-2]
                    data_line={}
                    for j in range(len(tmp)):
                        data_line[self.caption[j]] = float(tmp[j])

                    self.data.append(data_line)
                    self.labels.append(float(row[-2]))
                    
    def _init_train_test_dataset(self, ratio):
        data_tmp = self.data
        labels_tmp = self.labels
        i=0
        while i<ratio*len(data_tmp):
            random_int=random.randrange(len(data_tmp))
            self.train_data.append(data_tmp.pop(random_int))
            self.train_labels.append(labels_tmp.pop(random_int))
            i=i+1
        self.test_data=data_tmp
        self.test_labels=labels_tmp


    def _info(self):
        print("Datasets Information :")
        print("Dataset train : ")
        print("Taille : ",len(self.train_data))
        print("\nDataset test : ")
        print("Taille : ",len(self.test_data))
        print("\nDataset total : ")
        print("Taille : ",len(self.data))


    def _get_train_data(self):
        return(self.train_data,self.train_labels)

    def _get_test_data(self):
        return(self.test_data,self.test_labels)

    def _get_data(self):
        return(self.data,self.labels)

    def _get_caption(self):
        return self.caption
        
    

    
    

#if __name__ == '__main__':
#    loader = Dataset_Loader('data/Wines.csv')
#    loader._info()
    
