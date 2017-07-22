

class Rake(object):

    def run(self, phrase_list, number_to_return):
        word_scores = self._calculate_word_scores(phrase_list)
        keyword_candidates = self._generate_candidate_keyword_scores(phrase_list, word_scores)
        sorted_keywords = sorted(keyword_candidates, key=keyword_candidates.get, reverse=True)
        return sorted_keywords[:number_to_return]

    def _calculate_word_scores(self, phrase_list):
        word_frequency = {}
        word_degree = {}
        for phrase in phrase_list:
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

    def _generate_candidate_keyword_scores(self, phrase_list, word_score):
        keyword_candidates = {}
        for phrase in phrase_list:
            phrase_string = " ".join(phrase)
            keyword_candidates.setdefault(phrase_string, 0)
            candidate_score = 0
            for word in phrase:
                candidate_score += word_score[word]
            keyword_candidates[phrase_string] = candidate_score
        return keyword_candidates

