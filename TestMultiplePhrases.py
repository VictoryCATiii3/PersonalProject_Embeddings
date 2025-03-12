from EmbeddingClasses import Phrase
import shutil

def print_all_cosines(phrases, new_phrase):
    if not phrases:
        print("There must be at least be one phrase to compare to")
    for phrase in phrases:
        similarity = new_phrase.cosine_similarity(phrase)
        print("-"*shutil.get_terminal_size().columns)
        print(f"-{new_phrase.sentence}")
        print(f"-{phrase.sentence}")
        print(f"Cosine similarity: {similarity}")
    print("|"*shutil.get_terminal_size().columns)
    phrases.append(new_phrase)

if __name__=="__main__":
    phrases = []
    print("Enter phrases to see them compared to eachother, or enter 'EXIT' to exit the program. \n\n")
    while True:
        user_input = input("New Phrase: ")
        if user_input.strip().upper() == "EXIT":
            break
        new_phrase = Phrase(user_input)
        print_all_cosines(phrases, new_phrase)
    print("\n\n----------Ending program----------\n\n")
