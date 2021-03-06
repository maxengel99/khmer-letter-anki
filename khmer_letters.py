'''Handles khmer letters'''


class KhmerLetters:
    """Handles khmer letters"""

    def __init__(self):
        self.consonant_arr = ['ក', 'គ', 'ខ', 'ឃ', 'ង', 'ង៉', 'ច', 'ជ',
                              'ឆ', 'ឈ', 'ញ', 'ញ៉', 'ដ', 'ឌ', 'ឋ', 'ឍ', 'ថ',
                              'ធ', 'ណ', 'ន', 'ត', 'ទ', 'ប', 'ប៊', 'ប៉', 'ព',
                              'ផ', 'ភ', 'ម៉', 'ម', 'យ៉', 'យ', 'រ៉', 'រ', 'ឡ',
                              'ល', 'វ៉', 'វ', 'ស', 'ស៊', 'ហ', 'ស៊', 'ហ', 'ហ៊',
                              'អ', 'អ៊']
        self.vowel_arr = ['', 'ា', 'ិ', 'ី', 'ឹ', 'ឺ', 'ុ', 'ូ', 'ួ', 'ើ', 'ឿ',
                            'ៀ', 'េ', 'ែ', 'ៃ', 'ោ', 'ៅ', 'ុំ', 'ំ',
                            'ាំ', 'ះ', 'ុះ', 'េះ', 'ោះ', 'ិះ', 'ឹះ']
        self.new_vowels_arr = ['ោះ', 'ិះ', 'ឹះ']

    def create_combinations(self):
        '''Creates all combinations of consonants and vowels'''
        combined_arr = []
        for consonant in self.consonant_arr:
            for vowel in self.vowel_arr:
                combined_arr.append(consonant + vowel)

        return combined_arr
