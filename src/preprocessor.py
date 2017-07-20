
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from gensim.parsing import PorterStemmer
import re
import string

class Preprocessor(object):
    
    def __init__(self):
        self.stop_words = stopwords.words('english')        
            
    def process_file(self, file):
        with open(file) as input_file: 
            text = input_file.read()
            sentences = self._split_sentences(text)
            phrases = self._generate_candidate_keywords(sentences)
        return phrases     
        
    def _split_sentences(self, text):        
        sentence_delimiters = re.compile(u'[.!?,;:\t\\\\"\\(\\)\\\'\u2019\u2013]|\\s\\-\\s')
        sentences = sentence_delimiters.split(text)
        return sentences  
    
    def _generate_candidate_keywords(self, sentences):
        phrases = []
        for sentence in sentences:                     
            words = map(lambda x: "|" if x in self.stop_words or x in string.punctuation else x, word_tokenize(sentence.lower()))            
            phrase = []
            for word in words:                           
                if word == "|":
                    if len(phrase) > 0:                        
                        phrases.append(phrase)
                        phrase = []
                else:
                    phrase.append(word)  
            if len(phrase) > 0:                
                phrases.append(phrase)                         
        return phrases
    
    def parse_input(self, filename):
        """Import the file and parse its contents"""
        global_stemmer = PorterStemmer()
        with open(filename) as input_file:
            stop_words = stopwords.words('english')
            sentences = []
            alpha_pattern = re.compile(r'[^a-zA-Z]')
    
            for line in input_file:
                word_list = []
                words = word_tokenize(line)
                for word in words:
                    clean_word = alpha_pattern.sub('', word)
                    if clean_word:
                        lower_word = clean_word.lower()
                        if len(lower_word) > 1 and lower_word not in stop_words:
                            stemmed = global_stemmer.stem(lower_word)
                            word_list.append(stemmed)
    
                if len(word_list) > 0:
                    sentences.append(word_list)
    
        return sentences
    