import numpy as np
import pandas as pd


def combine_book_and_entity(entities_df: pd.DataFrame, book_df: pd.DataFrame) -> pd.DataFrame:
    """
    Given the two dataframes of interest, combine characters with book info to match gender inferences to characters.
    :param entities_df: DataFrame of entities (characters)
    :param book_df: DataFrame of book information
    :return: DataFrame of entities associated with book data of the related text and gender inferences
    >>> book_test = pd.DataFrame({'id_y': [1, 2, 1],'title': ['one', 'two', 'one'], 'g.argmax': ['she/her', 'he/him', 'she/her'], 'g.max': [0.9, 0.8, 1.0], 'count': [10, 1, 9]})
    >>> entities_test = pd.DataFrame({'COREF': [1, 2, 1], 'prop': ['PR', 'PR', 'PR'], 'text': ['she', 'John', 'Mary']})
    >>> test_df = combine_book_and_entity(entities_test, book_test)
    >>> test_df.columns
    Index(['text', 'g.argmax', 'g.max'], dtype='object')
    >>> test_df.loc[1]['text']
    array(['she', 'Mary'], dtype=object)
    """
    chars_tmp = entities_df.merge(book_df, left_on='COREF', right_on='id_y', how='inner')
    chars_combined = chars_tmp.groupby('COREF')[[
                                                 'text', 'g.argmax', 'g.max'
                                                ]].agg({
                                                        'text': 'unique',
                                                        'g.argmax': 'first',
                                                        'g.max': 'first'
                                                        })
    return chars_combined


def get_character_refs(chars: list, entities_df: pd.DataFrame) -> pd.DataFrame:
    """
    Given a list of characters of interest and a dataframe of entities, return a dataframe containing only references
    to the characters of interest.
    :param chars: list of strings, each string is a character name
    :param entities_df: full DataFrame of entities from one book
    :return: DataFrame containing only references to the characters of interest
    >>> entities_test = pd.DataFrame({'COREF': [1, 2, 1], 'prop': ['PR', 'PR', 'PR'], 'text': ['she', 'John', 'Mary']})
    >>> char_list = ['Mary']
    >>> test_df = get_character_refs(char_list, entities_test)
    >>> len(test_df)
    2
    >>> test_df['COREF'].values
    array([1, 1])
    """
    char_refs_df = pd.DataFrame(columns=['character_name'])

    for character in chars:
        # get explicit references to the character and store the 'coref' value
        ref_token = entities_df[entities_df['text'] == character]
        ref_token_list = np.unique(ref_token['COREF'].values.tolist())
        for ref in ref_token_list:
            char_refs_df = pd.concat([char_refs_df, pd.DataFrame({'character_name': character}, index=[ref])])

    chars_of_interest = list(char_refs_df.index)
    # return a dataframe with only the COREF values we stored earlier
    return entities_df[entities_df['COREF'].isin(chars_of_interest)]



if __name__ == '__main__':
    pass
