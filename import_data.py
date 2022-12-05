import os
import pathlib
import pickle

import pandas as pd
import pandas as pickle
import json

"""
This file imports our bookNLP data and outputs it as a pickle. If available, it also connects metadata to our 
HathiTrust IDs (HTIDs) 
"""

def read_booknlp(booknlp: str) -> pd.DataFrame:
    """function to read in bookNLP data and return a dataframe of gender and related words
    :param booknlp
    :return
    """
    ps = pathlib.Path(booknlp)

    allfiles = list(ps.glob('*/*/*.book'))

    files = [p for p in allfiles if p.is_file()]

    # print(allfiles)

    for f in allfiles:
        t = open(f.as_posix())
        temp_json = json.load(t)
        # print(temp_json)
        lhd_book = pd.concat([pd.DataFrame(temp_json),
                              pd.json_normalize(temp_json['characters'])],
                             axis=1)

        # drop characters column
        lhd_book = lhd_book.drop('characters', axis=1)
        # lhd_book.set_index('id' , inplace=True)

        #do we want to return as single dataframe or multiple?
        # return ldh_book
        print(lhd_book)


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
    read_booknlp('data/')
    pass
