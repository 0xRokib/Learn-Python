# Importing choice function from random module
from random import choice

# Defining some constants related to Kansas
capital = "Topeka"
bird = "Western Meadowlark"
flower = "Sunflower"
song = "Home on the Range"

# Function to print a random fun fact about Kansas
def randomfunfact():
    funfacts = [
        "Kansas is considered flat, but it does have a mountain.",
        "Wichita is the largest city in the state, but many would guess that it is Kansas City.",
        "A considerable portion of Kansas City is actually in Missouri.",
        "Most Kansans are annoyed by Wizard of Oz references from people outside of Kansas."
    ]

    # Choosing a random index from the string "0123" and converting it to an integer
    index = choice("0123")
    print(f"Fun Fact: {funfacts[int(index)]}")

# This block runs only when kansas.py is executed directly, not when imported
if __name__ == "__main__":
    print("Executing kansas.py directly:")
    randomfunfact()
