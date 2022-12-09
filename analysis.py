import numpy as np
import pandas as pd


# skeleton code before meeting will most likely change significantly

def read_booknlp(booknlp: str) -> pd.DataFrame:
    """function to read in bookNLP data and return a dataframe of gender and related words
    :param booknlp
    :return
    """

    pass


def read_books(books: str):
    """function to read in book metadata
    :param books
    """
    pass


def combine_book_and_entity(entities_df: pd.DataFrame, book_df: pd.DataFrame) -> pd.DataFrame:
    """
    Given the two dataframes of interest, combine characters with book info to match gender inferences to characters.
    :param entities_df: DataFrame of entities (characters)
    :param book_df: DataFrame of book information
    :return:
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
    :return:
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


def count_words(gender: pd.DataFrame):
    """function to count most frequent words identified per gender
        :param gender

    """
    pass


def make_gender_graphs(chars: pd.DataFrame):
    """
    function to take a processed character dataframe and make a bar graph of gender inferences
    :param chars:
    """
    pass


if __name__ == '__main__':
    pass
