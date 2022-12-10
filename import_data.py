import pathlib
import pickle
import pandas as pd
import json

"""
This file imports our bookNLP data and outputs it as a pickle. If available, it also connects metadata to our 
HathiTrust IDs (HTIDs) 
"""


def read_booknlp(booknlp: str):
    """function to read in bookNLP data and create a dataframe of gender and related words. Nothing is returned
    because this function calls mutate_data(), which saves a pickled version of the data for future usage.
    :param booknlp: a string representing a filepath to a data directory containing BookNLP output
    """
    ps = pathlib.Path(booknlp)
    allbooks = list(ps.glob('*/*/*.book'))
    csv_temp = list(ps.glob('*.csv'))
    big_df = []

    # read in csv, since there is only one include it here
    for md in csv_temp:
        metadata = pd.read_csv(md.as_posix())

    for f in allbooks:
        t = open(f.as_posix())
        temp_json = json.load(t)
        lhd_book = pd.concat([pd.DataFrame(temp_json),
                              pd.json_normalize(temp_json['characters'])],
                             axis=1)

        # return filename as a new column
        lhd_book['filename'] = f.name[:-5]

        # drop characters column
        lhd_book = lhd_book.drop('characters', axis=1)
        big_df.append(lhd_book)

    # concat all into one large df
    df_book = pd.concat(big_df, ignore_index=True)

    # set index to id.
    # df_book.set_index('id', inplace=True)

    # only run if character is mentioned more than 50 times
    df_book = df_book[df_book['count'] >= 50]

    # save columns, we want as dataframe
    df_book = df_book[['id', 'g.inference.he/him/his', 'g.inference.she/her',
                       'g.inference.they/them/their', 'g.inference.xe/xem/xyr/xir',
                       'g.inference.ze/zem/zir/hir', 'g.argmax', 'g.max', 'mentions.proper', 'filename', 'count']]

    # finally mutate data
    mutate_data(df_book, metadata)


def read_char(booknlp: str) -> pd.DataFrame:
    """function to read in character entity data and return a dataframe of name related words.
    :param booknlp: a string representing a filepath to a data directory containing BookNLP output
    :return: DataFrame of entities for each book
    >>> path_str = 'data'
    >>> test_char = read_char(path_str)
    >>> test_char.columns
    Index(['COREF', 'prop', 'cat', 'text'], dtype='object')
    """
    ps = pathlib.Path(booknlp)
    allentities = list(ps.glob('*/*/*.entities'))
    entities = []
    for md in allentities:
        entities.append(pd.read_csv(md.as_posix(), sep='\t'))

    df_entities = pd.concat(entities, ignore_index=True)
    df_entities.drop(['start_token', 'end_token'], axis=1, inplace=True)

    return df_entities


def mutate_data(booknlp: pd.DataFrame, metadata: pd.DataFrame) -> pickle:
    """
    function to combine booknlp and metadata and output pickle
    :param booknlp:
    :param metadata:
    :return:
    """
    # merge name with id in
    combined = pd.merge(metadata, booknlp, left_on='id', right_on='filename', how='right')
    combined.drop(['id_x'], axis=1, inplace=True)
    # print(combined.iloc[0])

    combined.to_pickle("./booknlp.pkl")


if __name__ == '__main__':
    file = 'data/'
    read_booknlp(file)
    read_char(file)
