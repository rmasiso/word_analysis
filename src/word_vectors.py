"""This script will read an input file of statements and create a plot of the word associations"""

import re
import warnings

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
import numpy as np
from sklearn.manifold import TSNE
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
import gensim
from gensim.parsing import PorterStemmer


def main():
    """Main driver function"""
    threshold = 2
    sentences = parse_input("../Default Report.txt")
    model = gensim.models.Word2Vec(sentences, min_count=threshold)
    vectors = reduce_dims(model)
    plot_with_labels(vectors, model, filename='tsne.png')


def parse_input(filename):
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


def plot_with_labels(embeddings, model, filename='default.png'):
    """Create a plot with the words as labels"""
    plt.figure(figsize=(18, 18))  # in inches
    for i, label in enumerate(model.wv.vocab):
        x_pos, y_pos = embeddings[i, :]
        marker_size = model.wv.vocab[label].count * 2
        plt.scatter(x_pos, y_pos, marker_size)
        plt.annotate(label,
                     xy=(x_pos, y_pos),
                     xytext=(5, 2),
                     textcoords='offset points',
                     ha='right',
                     va='bottom')

    plt.savefig(filename)


def reduce_dims(model):
    """Reduce the dimensions of the word2vec vectors"""
    vectors = []
    for word in model.wv.vocab:
        vectors.append(model[word])

    vectors = np.asarray(vectors)
    tsne = TSNE(n_components=2, init='pca', random_state=0)
    vectors = tsne.fit_transform(vectors)

    return vectors


if __name__ == "__main__":
    main()
