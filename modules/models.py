import pandas as pd
import itertools

from utils.utils import *

class Categ:

    def __init__(self, nameoffile):
        self.nameoffile = nameoffile
        self.path_data = 'data_sets/'
        self.path_models = 'models/'
        self.data = read_csv_data(self.path_data, self.nameoffile)

    def model_compl(self):
        data = self.data
        compl = 1
        for col in data.columns:
            tempdata = data[col]
            cat = len(tempdata.values.categories)
            compl = compl * cat

        return compl

    def modelinfo(self):

        data = self.data
        compl = self.model_compl(data)

        print("Table shape: ", data.shape)
        print("Model Complexity: ", compl)
        print("Table head: ")
        print(data.head())

    def selection(self):

        data = self.data
        compl = self.model_compl()

        # Prepare modeltable 
        values_cat = []
        for col in data.columns:
            values_cat.append(data[col].values.categories)
        values_cat.append([0])
        possible_vectors = list(itertools.product(*values_cat))

        columns = list(data.columns)
        columns.append('p')
        modeltable = pd.DataFrame(columns=columns)

        for i in range(0, compl):
            modeltable.loc[i] = possible_vectors[i]

        # Calculate parameters
        numb_columns = len(data.columns)
        numb_data = len(data)
        for i in range(0, compl):
            row = modeltable.iloc[i, 0:numb_columns]
            temp_table = data.isin(list(row)).T
            numb = ((temp_table == True).sum() == numb_columns).sum()
            modeltable.iloc[i, numb_columns] = numb / numb_data

        return modeltable

'''
    def marg(model):

    def cond(model):

    def aggr(model):

    def samp(model):

    def dens(model):
'''