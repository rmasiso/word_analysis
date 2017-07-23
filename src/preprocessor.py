"""Preprocesses the input by splitting into lists and removing extraneous words and characters"""
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from gensim.parsing import PorterStemmer
import re
import string

class Preprocessor(object):
    """Preprocessor class"""
    def __init__(self):
        self._stop_words = stopwords.words('english')
        self._global_stemmer = PorterStemmer()
        self._text = ""
        self._separate_lines = False
        self._whole_sentences = True
        self._stemming = False

    def process_file(self, file, separate_lines, whole_sentences, stemming):
        """Takes input file and parses the text
        returning a list of list of either phrases or sentences"""
        with open(file) as input_file:
            self._text = input_file.read()
            self._separate_lines = separate_lines
            self._whole_sentences = whole_sentences
            self._stemming = stemming
            phrases = self._parse_text()
        return phrases

    def process_text(self, text, separate_lines, whole_sentences, stemming):
        """Takes input text and parses it returning a list of list of either phrases or sentences"""
        self._text = text
        self._separate_lines = separate_lines
        self._whole_sentences = whole_sentences
        self._stemming = stemming
        phrases = self._parse_text()
        return phrases

    def _parse_text(self):
        """Parses input text and returns phrases from text"""
        phrases = []
        #alpha_pattern = re.compile(r'[^a-zA-Z]')
        extra_chars = re.compile(u'[-\"\'\u201C\u201D\u2018\u2019\u2013/]|(\.\.\.)|[0-9]')
        text = re.sub(extra_chars, ' ', self._text)

        if self._separate_lines:
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
                if word not in self._stop_words and word not in string.punctuation:
                    #clean_word = alpha_pattern.sub('', word)
                    #if clean_word:
                    if self._stemming:
                        word = self._global_stemmer.stem(word)
                    phrase.append(word)
                else:
                    if not self._whole_sentences:
                        if len(phrase) > 0:
                            phrases.append(phrase)
                            phrase = []
            if len(phrase) > 0:
                phrases.append(phrase)

        return phrases
