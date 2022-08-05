## Challenge ##
# Write code to find the word in a list that would come first alphabetically

## Example: When given the list below
# word_list = ["Hamster", "Turtle", "Cat", "Bird"]
# The code should find "bird" as teh word that would come first


def find_first(list):
    return min(list)

if __name__ == "__main__":
    print(find_first(word_list))