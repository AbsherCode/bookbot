from stats import get_num_words, get_char_counts, sort_char_counts

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


def main():
   
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    if text:
        
        num_words = get_num_words(text)
        char_counts_dict = get_char_counts(text)
        sorted_chars_list = sort_char_counts(char_counts_dict)
        
        # --- Print Report ---
        
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")

        # Word Count Section
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")

        # Character Count Section
        print("--------- Character Count -------")
        for item in sorted_chars_list:
            char = item["char"]
            count = item["num"]
            
            # Filter: only print alphabetical characters
            if char.isalpha():
                # Print in the required format: 'char: count'
                print(f"{char}: {count}")

        # End of Report
        print("============= END ===============")
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
