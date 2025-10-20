def get_num_words(text):
    """
    Counts and returns the number of words in a given text string.

    Args:
        text (str): The text content of the book.

    Returns:
        int: The total count of words.
    """
    # The split() method splits the string by whitespace and returns a list of words.
    words = text.split()
    return len(words)

def get_char_counts(text):
    """
    Counts the frequency of each character (including symbols and spaces) 
    in the text after converting the entire text to lowercase.

    Args:
        text (str): The text content of the book.

    Returns:
        dict: A dictionary where keys are characters (str) and values are 
              their counts (int).
    """
    char_counts = {}
    lowered_text = text.lower()

    for char in lowered_text:
        # If the character is already in the dictionary, increment its count
        if char in char_counts:
            char_counts[char] += 1
        # If the character is not in the dictionary, initialize its count to 1
        else:
            char_counts[char] = 1

    return char_counts

# Helper function for sorting the list of dictionaries
def sort_on_num(d):
    """Returns the 'num' value of a dictionary for sorting purposes."""
    return d["num"]

def sort_char_counts(char_dict):
    """
    Takes a dictionary of character counts and returns a sorted list of 
    dictionaries, ordered from greatest to least count.
    """
    # Convert the dictionary into a list of dictionaries
    sorted_list = []
    for char, count in char_dict.items():
        sorted_list.append({"char": char, "num": count})

    # Sort the list using the helper function as the key, in reverse order
    sorted_list.sort(reverse=True, key=sort_on_num)
    
    return sorted_list
