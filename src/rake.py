
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
import string

test = True

class Rake(object):
    
    def __init__(self):
        self.stop_words = stopwords.words('english')        

    def run(self, text):
        sentence_list = self.split_sentences(text)        
        phrase_list = self.generate_candidate_keywords(sentence_list)        
        word_scores = self.calculate_word_scores(phrase_list)
        keyword_candidates = self.generate_candidate_keyword_scores(phrase_list, word_scores)        
        sorted_keywords = sorted(keyword_candidates, key=keyword_candidates.get, reverse=True)
        return sorted_keywords
    
    def split_sentences(self, text):        
        sentence_delimiters = re.compile(u'[.!?,;:\t\\\\"\\(\\)\\\'\u2019\u2013]|\\s\\-\\s')
        sentences = sentence_delimiters.split(text)
        return sentences

    def generate_candidate_keywords(self, sentences):
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
    
    def calculate_word_scores(self, phraseList):
        word_frequency = {}
        word_degree = {}
        for phrase in phraseList:        
            word_list_length = len(phrase)
            word_list_degree = word_list_length - 1
            
            for word in phrase:
                word_frequency.setdefault(word, 0)
                word_frequency[word] += 1
                word_degree.setdefault(word, 0)
                word_degree[word] += word_list_degree
                
        for item in word_frequency:
            word_degree[item] = word_degree[item] + word_frequency[item]    
       
        word_score = {}
        for item in word_frequency:
            word_score.setdefault(item, 0)
            word_score[item] = word_degree[item] / (word_frequency[item] * 1.0)        
        return word_score
    
    def generate_candidate_keyword_scores(self, phrase_list, word_score):
        keyword_candidates = {}
        for phrase in phrase_list:
            phrase_string = " ".join(phrase)
            keyword_candidates.setdefault(phrase_string, 0)        
            candidate_score = 0
            for word in phrase:
                candidate_score += word_score[word]
            keyword_candidates[phrase_string] = candidate_score
        return keyword_candidates

if test:
    text = "Compatibility of systems of linear constraints over the set of natural numbers. Criteria of compatibility of a system of linear Diophantine equations, strict inequations, and nonstrict inequations are considered. Upper bounds for components of a minimal set of solutions and algorithms of construction of minimal generating sets of solutions for all types of systems are given. These criteria and the corresponding algorithms for constructing a minimal supporting set of solutions can be used in solving all the considered types of systems and systems of mixed types."

    

    rake = Rake()
    keywords = rake.run(text)
    print(keywords)