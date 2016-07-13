from random import choice
import sys


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file_string = open(file_path).read()
    # file_string = sys.argv[1]

    return file_string

    # return "This should be a variable that contains your file text as one long string"


def make_chains(file_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    list1 = file_string.split()
    chains = {}

    for items in range(len(list1) - 2):
        key = (list1[items], list1[items + 1])
        value = [list1[items + 2]]
        
        if chains.get(key):
            chains.get(key).extend(value)

        else:
            chains[key] = value

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    random_key = choice(chains.keys())
    text = "{} {} ".format(random_key[0], random_key[1])

    while random_key in chains:
        random_value = choice(chains[random_key])
        random_key = (random_key[1], random_value)
        text = text + "{} " .format(random_value)

    return text

input_path = "hakuna-matata.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text



# Would you - could, like
# you could - you, you
# could you - in, with, in, with
# you in - a, a
# in a - house, box
# a house? - Would
# house? Would - you
# you with - a, a
# with a - mouse?, fox?
# a mouse? - Would
# mouse? Would - you
# a box? - Would
# box? Would - you
# a fox? - Would
# fox? Would - you
# you like - green, them,
# like green - eggs
# green eggs - and
# eggs and - ham?
# and ham? - Would
# ham? Would - you
# like them, - Sam
# them, Sam - I
# Sam I - am?
# I am? - 