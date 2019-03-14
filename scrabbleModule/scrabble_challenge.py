"""
module containing main classes for scrabble
"""

import random


class TilePool(object):

    TILES_CSV_FILENAME = 'tiles.csv'

    def __init__(self):
        """
        Reads in the tiles csv and maps the letter counts and values
        """
        self.letter_count = {}
        self.letter_value = {}

        with open(TilePool.TILES_CSV_FILENAME) as f:
            data = f.readlines()
            for line in data:
                letter, value, count = line.split(',')
                if letter == 'letter':
                    continue
                self.letter_value[letter] = float(value)
                self.letter_count[letter] = int(count.strip())

    def __len__(self):
        return sum(self.letter_count.values())

    def pop(self, tile_count=None):
        """
        :param tile_count: int; how many tiles to return, optional, defaults to 7
                           valid values 1..7 (inclusive)
                           if tile pool contains less than requested qty of tiles,
                           then returns all remaining tiles

        :returns: list of characters (random, letter tiles), e.g. ['t','a','c']
        """

        if tile_count == None:
            tile_count = 7

        if not isinstance(tile_count, int):
            raise TypeError('tile_count must be an integer')

        if tile_count < 1 or tile_count > 7:
            raise ValueError('tile_count must be between 1 and 7 (inclusive)')

        tiles = []
        while(len(self) and tile_count):
            random_tile = random.choice(self.letter_count.keys())
            count = self.letter_count[random_tile]
            if count > 0:
                tiles.append(random_tile)
                self.letter_count[random_tile] = count - 1
                tile_count -= 1
            else:
                continue

        return tiles

    def get_word_score(self, word):
        """
        :param word: str 

        :returns: float, score for word
                         calc by adding up the tile values for all letters in word
        """
        if word is None:
            raise ValueError('word must not be None')

        if not isinstance(word, str):
            raise TypeError('word must be a string')

        return sum([self.letter_value[x] for x in word])


class WordFinder(object):

    WORD_DICTIONARY_FILENAME = 'word_dictionary.txt'
    tile_pool = TilePool()

    def __init__(self):
        """
        Reads in all words from the word dictionary and creates a list
        """
        self.all_words = []
        with open(WordFinder.WORD_DICTIONARY_FILENAME) as f:
            data = f.readlines()
            for line in data:
                self.all_words.append(line.strip())

    def list_words(self, letters, cross_letter):
        """
        :param letters: list of chars, basically letter tiles
        :param cross_letter: char, None is valid

        :returns: list of tuples, each tuple = (word, score)
                  where each word is one that can formed using the tiles (upto
                  7 from letters passed into method call and constrained by
                  the cross_letter);
                  the list is sorted by score in desc order (highest scorings words first)
        """
        if letters is None:
            raise ValueError('letters must not be None')

        result = []
        for word in self.all_words:
            if cross_letter and cross_letter not in word:  # disqualify word
                continue

            letters_copy = letters[:]

            word_work = word
            if cross_letter:
                # remove only 1 occurence
                word_work = word_work.replace(cross_letter, '', 1)

            end_idx = len(word_work) - 1

            for idx, char in enumerate(word_work):
                if char not in letters_copy:
                    if ' ' in letters_copy:
                        char = ' '  # let's use a blank since available
                    else:
                        break  # word cannot be made

                letters_copy.remove(char)  # consumed letter from player rack
                                           # note: removes only 1 occurence

                if idx == end_idx:  # word can be made
                    result.append((word, WordFinder.tile_pool.get_word_score(word)))
        return sorted(result, key=lambda tupl: tupl[1], reverse=True)


if __name__ == '__main__':
    tp = TilePool()
    wf = WordFinder()
    print wf.list_words(['i', 'u', 'c', 'b', 'o', 'g', 'q'], 'b')

