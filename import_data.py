import os
import pickle

import pandas as pd
import pandas as pickle

"""
This file imports our bookNLP data and outputs it as a pickle. If available, it also connects metadata to our 
HathiTrust IDs (HTIDs) 
"""

def read_booknlp(booknlp: str) -> pd.DataFrame:
    """function to read in bookNLP data and return a dataframe of gender and related words
    :param booknlp
    :return
    """

    pass

def read_metadata(metadata:str) -> pd.DataFrame:
    """
    function to read in metadata and return it as a dataframe
    :param metadata:
    :return:
    """
    pass

def mutate_data(booknlp:pd.DataFrame, metadata:pd.DataFrame) -> pickle:
    """
    function to combine booknlp and metadata and output pickle
    :param booknlp:
    :param metadata:
    :return:
    """

if __name__ == '__main__':
    pass
