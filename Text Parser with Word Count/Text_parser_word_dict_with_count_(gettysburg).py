"""This program opens a particular file (gettysburg.txt) and then parses the text. The process_line function removes
the trailing white-spaces, converts the words to lowercase to avoid creating separate entries for the same words with
different capitalizations, removes the punctuation, and then splits the resulting string on the ' ' character.
Afterwards, list entries of empty strings were removed (this occurs in the gettysburg.txt file due to
double-white-spaces occurring prior to the string.split() after the removal of the '--' character). The add_word
function is then used to populate a dictionary with the unique words and their number of occurrences in the text. The
main function processes this dictionary into a list which is then sorted in descending order based on number of
occurrences and that list is then converted back into a dictionary to be fed into the pretty_print function which
converts the dictionary into an easily readable format."""

import string


def add_word(word, dictionary):
    # Populates a dictionary with unique words paired with their frequency of occurrence
    if word not in dictionary:
        dictionary[word] = 1
    else:
        dictionary[word] += 1


def process_line(line, dictionary):
    # Processes text to remove whitespaces and punctuation and creates a list of words from the string input.
    # Removes any empty-string list entries before populating a dictionary with unique word occurrences and their
    # frequencies.
    line = line.strip()
    line = line.lower()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.split(' ')
    for word in line:
        if word == '':
            line.remove(word)
    for word in line:
        add_word(word, dictionary)


def pretty_print(dictionary):
    # Receives a final dictionary and formats it into a pleasing and easy-to-read string
    print(f"Length of dictionary is: {len(dictionary)}")
    print('Word', ' '*10, 'Count')
    print(' ')
    print('-'*21)
    for key, value in dictionary.items():
        print(f"{key.ljust(17)}{str(value)}")


def main():
    # Main function that allows program to be run from within the module itself. Uses the process_line function to
    # ultimately populate a dictionary with unique words and their frequencies of occurrence (avoids processing blank
    # lines). It then converts the dictionary to a list for sorting, and converts that list back to a final dictionary.
    # Then calls pretty_print function to present the final dictionary in a pleasing and easy-to-read format.

    # If you wish to try this with your own text, replace the text_path destination with your own text file path.
    text_path = r"gettysburg.txt"
    gba_dict = {}
    gba_file = open(text_path, 'r')
    for line in gba_file:
        if not line.isspace():
            process_line(line, gba_dict)
        else:
            continue
    gba_dict_list = []
    for key, value in gba_dict.items():
        gba_dict_list.append((value, key))
    gba_dict_list.sort(reverse=True)
    gba_dict_reversed = {}
    for (key, value) in gba_dict_list:
        gba_dict_reversed[value] = key
    pretty_print(gba_dict_reversed)


if __name__ == "__main__":
    main()
