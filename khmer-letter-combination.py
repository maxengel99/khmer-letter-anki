import requests

class KhmerLetters:

    def __init__(self):
        self.consonant_arr = ['ក','គ','ខ','ឃ']
        self.vowel_arr = ['','ា', 'ិ']
    
    def create_combinations(self):
        combined_arr = []
        for consonant in self.consonant_arr:
            for vowel in self.vowel_arr:
                combined_arr.append(consonant + vowel)
        
        return combined_arr

    def get_audio(self, combined_arr):
        for combination in combined_arr:
            url="https://translate.google.com/translate_tts?ie=UTF-8&tl=km&client=tw-ob&q=" + combination
            doc = requests.get(url)
            filename = 'files/' + combination + ".mp3"
            with open(filename, "wb") as f:
                f.write(doc.content)