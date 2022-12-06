import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os


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


def combine_book_and_entity(booknlp: pd.DataFrame) -> pd.DataFrame:
    pass


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
