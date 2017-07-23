"""Driver for the analysis. User can choose which analysis to run and vary the parameters."""
from rake import Rake
from preprocessor import Preprocessor
from word_vectors import WordVectors

def main():
    """Main driver function"""

    analysis = ""
    while analysis != "exit":
        analysis = choose_analysis()

        if analysis == "exit":
            exit(0)

        preprocessor = Preprocessor()
        input_file = "../Default Report.txt"

        if analysis == "rake":
            rake_analysis(preprocessor, input_file)
        elif analysis == "word2vec":
            word2vec_analysis(preprocessor, input_file)


def choose_analysis():
    """Present analysis menu and returns analysis"""

    print("\nAvailable analyses\n")
    print("1. Rake")
    print("2. Word2Vec")
    print("3. Exit")

    valid_selection = False
    analysis = ""
    while not valid_selection:
        analysis_idx = input("Please enter the number of the analysis: ")
        print("")
        if analysis_idx.isdigit() and (0 < int(analysis_idx) <= 3):
            valid_selection = True
            if analysis_idx == "1":
                analysis = "rake"
            elif analysis_idx == "2":
                analysis = "word2vec"
            elif analysis_idx == "3":
                analysis = "exit"
        else:
            print("That is not a valid selection.")

    return analysis


def rake_analysis(preprocessor, input_file):
    """Run the Rake analysis"""
    separate_lines = True
    whole_sentences = False
    stemming = False
    number_to_return = 10

    phrases = preprocessor.process_file(input_file, separate_lines,
                                        whole_sentences, stemming)
    rake = Rake()
    keywords = rake.run(phrases, number_to_return)
    print(keywords)

def word2vec_analysis(preprocessor, input_file):
    """Run the Word2Vec analysis"""
    separate_lines = True
    whole_sentences = True
    stemming = True
    threshold = 2
    output_file_name = "tsne.png"

    phrases = preprocessor.process_file(input_file, separate_lines,
                                        whole_sentences, stemming)
    word_vectors = WordVectors()
    word_vectors.run(phrases, threshold, output_file_name)


if __name__ == "__main__":
    main()
