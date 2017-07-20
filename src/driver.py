from rake import Rake
from preprocessor import Preprocessor
from word_vectors import WordVectors

def main():
    input_file = "../Default Report.txt"
    preprocessor = Preprocessor()
    phrases = preprocessor.process_file(input_file)
    rake = Rake()
    keywords = rake.run(phrases)
    print(keywords[:10])
    
    sentences = preprocessor.parse_input(input_file)    
    word_vectors = WordVectors()
    word_vectors.run(sentences, 2)


if __name__ == "__main__":
    main()