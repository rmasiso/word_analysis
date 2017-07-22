
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from gensim.parsing import PorterStemmer
import re
import string

class Preprocessor(object):
    
    def __init__(self):
        self.stop_words = stopwords.words('english')
        self.global_stemmer = PorterStemmer()        
            
    def process_file(self, file, separate_lines=False, whole_sentences=True, stemming=False):
        """Takes input file and parses the text returning a list of list of either phrases or sentences"""
        with open(file) as input_file:
            text = input_file.read()
            phrases = self._parse_text(text, separate_lines, whole_sentences, stemming)                           
        return phrases
    
    def process_text(self, text, separate_lines=False, whole_sentences=True, stemming=False):  
        """Takes input text and parses it returning a list of list of either phrases or sentences"""      
        phrases = self._parse_text(text, separate_lines, whole_sentences, stemming)                           
        return phrases
    
    def _parse_text(self, text, separate_lines, whole_sentences, stemming):
        """Parses input text and returns phrases from text"""
        phrases = []
        #alpha_pattern = re.compile(r'[^a-zA-Z]')
        extra_chars = re.compile(u'[-\"\'\u201C\u201D\u2018\u2019\u2013/]|(\.\.\.)|[0-9]')
        text = re.sub(extra_chars, ' ', text)

        if separate_lines:
            lines = text.splitlines()
            sentences = []
            for line in lines:
                sentences += sent_tokenize(line) 
        else:
            sentences = sent_tokenize(text)
         
        for sentence in sentences:                                      
            phrase = []
            words = word_tokenize(sentence.lower())
            for word in words:                    
                if word not in self.stop_words and word not in string.punctuation:
                    #clean_word = alpha_pattern.sub('', word)
                    #if clean_word:
                    if stemming:
                        word = self.global_stemmer.stem(word)
                    phrase.append(word) 
                else:
                    if not whole_sentences: 
                        if len(phrase) > 0:                        
                            phrases.append(phrase)                            
                            phrase = []     
            if len(phrase) > 0:                
                phrases.append(phrase)  
                                       
        return phrases
    