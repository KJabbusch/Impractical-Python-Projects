from __future__ import print_function
"""Load textfile as a list

Arguments: 
- text file name (and directory path, if needed)

Exceptions:
- IOError if filename not found

Returns:
- A list of all words in textfile in lower case
"""
import sys

def load(file):
    """Open textfile & return list of lowercase strings."""
    try:
        with open(file) as in_file:
            loaded_txt = in_file.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, file), file=sys.stderr)
        sys.exit(1)

