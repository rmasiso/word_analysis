"""Rake analysis class. Keyword extraction from text input."""

class Rake(object):
    """Rake class"""
    def __init__(self):
        self._phrase_list = []

    def run(self, phrase_list, number_to_return):
        """Run the Rake analysis"""
        self._phrase_list = phrase_list
        word_scores = self._calculate_word_scores()
        keywords = self._generate_keyword_scores(word_scores)
        sorted_keywords = sorted(keywords, key=keywords.get, reverse=True)
        return sorted_keywords[:number_to_return]

    def _calculate_word_scores(self):
        word_frequency = {}
        word_degree = {}
        for phrase in self._phrase_list:
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

    def _generate_keyword_scores(self, word_score):
        keywords = {}
        for phrase in self._phrase_list:
            phrase_string = " ".join(phrase)
            keywords.setdefault(phrase_string, 0)
            candidate_score = 0
            for word in phrase:
                candidate_score += word_score[word]
            keywords[phrase_string] = candidate_score
        return keywords
