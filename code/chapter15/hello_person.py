import argparse

# Function to print a greeting based on the provided language
def hello(name, lang):
    """
    Prints a personalized greeting based on the provided language.
    :param name: Name of the person to greet.
    :param lang: Language in which to greet (English, Spanish, German).
    """
    greetings = {
        "English": "Hello",
        "Spanish": "Hola",
        "German": "Hallo"  # Corrected German greeting
    }
    
    print(f"{greetings[lang]} {name}!")

# Function to handle command-line argument parsing and call the hello function
def main():
    """
    Parses command-line arguments and calls the hello function.
    """
    parser = argparse.ArgumentParser(description="Provide a personal greeting.")
    
    # Adding command-line argument for name
    parser.add_argument("-n", "--name", metavar="name", required=True, help="The name of the person to greet.")
    
    # Adding command-line argument for language selection with predefined choices
    parser.add_argument("-l", "--lang", metavar="language", required=True, choices=["English", "Spanish", "German"], help="The language of the greeting.")
    
    args = parser.parse_args()
    
    # Call the hello function with the parsed arguments
    hello(args.name, args.lang)

# Ensuring the script runs only when executed directly
if __name__ == "__main__":
    main()
