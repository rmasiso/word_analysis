"""Word2Vec analysis. Takes in text and create a plot of the word associations"""

import warnings
import matplotlib.pyplot as plt
import numpy as np
from sklearn.manifold import TSNE
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
import gensim


class WordVectors(object):
    """Word2Vec class"""
    def __init__(self):
        self._model = None

    def run(self, sentences, threshold=2, output_file_name='default.png'):
        """Main driver function"""
        self._model = gensim.models.Word2Vec(sentences, min_count=threshold)
        vectors = self._reduce_dims()
        self._plot_with_labels(vectors, filename=output_file_name)


    def _plot_with_labels(self, embeddings, filename):
        """Create a plot with the words as labels"""
        plt.figure(figsize=(18, 18))  # in inches
        for i, label in enumerate(self._model.wv.vocab):
            x_pos, y_pos = embeddings[i, :]
            marker_size = self._model.wv.vocab[label].count * 2
            plt.scatter(x_pos, y_pos, marker_size)
            plt.annotate(label,
                         xy=(x_pos, y_pos),
                         xytext=(5, 2),
                         textcoords='offset points',
                         ha='right',
                         va='bottom')

        plt.savefig(filename)


    def _reduce_dims(self):
        """Reduce the dimensions of the word2vec vectors"""
        vectors = []
        for word in self._model.wv.vocab:
            vectors.append(self._model[word])

        vectors = np.asarray(vectors)
        tsne = TSNE(n_components=2, init='pca', random_state=0)
        vectors = tsne.fit_transform(vectors)

        return vectors
