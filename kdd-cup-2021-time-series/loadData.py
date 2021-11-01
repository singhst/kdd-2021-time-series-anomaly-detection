import os
# from tqdm import tqdm
import pandas as pd
import numpy as np


class DataLoader():
    '''
    Example
    ---

    path = '../data-sets/KDD-Cup/data/'

    loader = DataLoader(path)

    data_df_list = loader.getDataInDfList()

    print(data_df_list[0][0])
    '''

    def __init__(self,
                 path: str):
        self.path = path

        self.df_datasets = []
        self.datasets = []
        self.train_datasets = []
        self.test_datasets = []

        self.loadData()

    def loadData(self):
        ''' Just load all the .txt into memory in `pandas.DataFrame` and `numpy.array` format.
        '''
        filenames = os.listdir(self.path+'.')   # . is cwd
        # Keep filename started by integer, filter out others
        filenames = [p for p in filenames if p[0].isdigit()]
        filenames = sorted(filenames)

        # filenames = [filenames[203]]

        # # For progress bar
        # progress = tqdm(total=len(filenames))

        # Read and split the data into train & test self.datasets
        for filename in filenames:
            # progress.update(1) #Progress bar
            #     print(filename)

            # (1) Get the split-number in file name
            start = filename.find('y_') + 2
            end = filename.find('.txt')
            split_number = int(filename[start:end])
        #     print(f'id:{filename[:3]};split:{split_number};len():{len(_dataset)}', end=',\t')

            # (2) Load the .txt as string and format it
            with open(self.path+filename, "r") as myfile:
                data = myfile.read()
                data = data.replace('\n', '')  # `001.txt` use
                data = data.replace('   ', ',')
                data = data.replace('  ', ',')
                data = data.split(',')
                data = list(filter(lambda x: len(x) > 0, data))

            # (2.1) Save the formated data in Pandas dataframe
            # self.df_datasets format: `set(filename, dataframedf)`
            _df = pd.DataFrame(data, columns=['values'], dtype=float)
            _df.loc[:split_number, 'label'] = 'train'
            _df.loc[split_number::, 'label'] = 'test'
            self.df_datasets.append((filename, _df))

            # (2.2) Save the formated data in numpy array
            _dataset = np.array(data)
            _dataset = _dataset.astype(float)
            self.datasets.append(_dataset)
            self.train_datasets.append(_dataset[:split_number])
            self.test_datasets.append(_dataset[split_number::])

            print('.', end='')

        #     if filename[:3] == '005':
        #         break

    def getDataInDfList(self) -> pd.DataFrame:
        ''' Retrun loaded data in df list format.
        '''
        return self.df_datasets


if __name__ == "__main__":
    path = '../data-sets/KDD-Cup/data/'
    loader = DataLoader(path)
    data_df_list = loader.getDataInDfList()
    print(data_df_list[0][0])
