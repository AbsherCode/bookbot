

def get_book_text(filepath):
    """
    Reads a file from the given filepath and returns its entire content as a string.

    Args:
        filepath (str): The relative or absolute path to the text file.

    Returns:
        str: The complete content of the file.
    """
    try:
        # Use 'r' mode for reading and 'utf-8' encoding for general text files
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: The file was not found at path: {filepath}")
        return ""
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")
        return ""

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

def main():
    """
    The main function to demonstrate reading and printing the book content.
    """
    # Use the relative path to the Frankenstein book file
    book_path = "books/frankenstein.txt"
    
    # print(f"--- Attempting to read book from: {book_path} ---")
    
    # Get the contents of the book
    text = get_book_text(book_path)

    if text:
        # Get the number of words
        num_words = get_num_words(text)

        # Print the required output with the word count
        print(f"Found {num_words} total words")
    else:
        print("Book text could not be retrieved.")

    # if text:
    #     # Print the entire contents of the book to the console
    #     # Note: This will be very long!
    #     print("\n--- START OF BOOK CONTENT ---")
    #     print(text)
    #     print("--- END OF BOOK CONTENT ---")
    # else:
    #     print("Book text could not be retrieved.")

# Execute the main function when the script is run
if __name__ == "__main__":
    main()
