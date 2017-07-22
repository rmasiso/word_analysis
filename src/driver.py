from rake import Rake
from preprocessor import Preprocessor
from word_vectors import WordVectors

def main():

    preprocessor = Preprocessor()

    input_file = "../Default Report.txt"
    separate_lines=True
    whole_sentences=False
    stemming=False
    number_to_return = 10

    phrases = preprocessor.process_file(input_file, separate_lines, whole_sentences, stemming)
    rake = Rake()
    keywords = rake.run(phrases, number_to_return)
    print(keywords)

    separate_lines=True
    whole_sentences=True
    stemming=True
    threshold = 2
    output_file_name = "tsne.png"

    phrases = preprocessor.process_file(input_file, separate_lines, whole_sentences, stemming)
    word_vectors = WordVectors()
    word_vectors.run(phrases, threshold, output_file_name)


if __name__ == "__main__":
    main()
