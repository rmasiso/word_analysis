from rake import Rake
from preprocessor import Preprocessor
from word_vectors import WordVectors

def main():
    
    preprocessor = Preprocessor()
    
    input_file = "../Default Report.txt"
    separate_lines=True
    whole_sentences=False
    stemming=False
    
    phrases = preprocessor.process_file(input_file, separate_lines, whole_sentences, stemming)
    rake = Rake()
    keywords = rake.run(phrases)
    print(keywords[:10])
    
    separate_lines=True
    whole_sentences=True
    stemming=True
    threshold = 2
    
    phrases = preprocessor.process_file(input_file, separate_lines, whole_sentences, stemming)
    word_vectors = WordVectors()
    word_vectors.run(phrases, threshold)


if __name__ == "__main__":
    main()