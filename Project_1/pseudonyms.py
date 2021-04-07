from __future__ import print_function
"""Generate a Benedict Cumberbatch name"""
import sys
import random

print("Welcome to the Benedict-Cumberbatch-esque Name Generator.\n")

first = (
    'Benadryl', 'Bumblebee', 'Benefit', 'Bendystraw', 'Beanie-baby',
    'Bonkyhort', 'Barbeque', 'Butterhick', 'Belvidere', 'Bulbasaur',
    'Beezlebub', 'Binkytrick', 'Blundersnort', 'Basketball', 'Buttercup',
    'Buffalo', 'Brittany', 'Boogerflick', 'Brendadirk'
)

last = (
    'Cabbagepatch', 'Crustysnack', 'Custardbath', 'Cucumberback',
    'Clusterfudge', 'Crumpetbutt', 'Crinklebench', 'Crimpysnitch',
    'Cutiebrunch', 'Cabbagewank', 'Camelneck', 'Cottonswab', 'Cuddlefish',
    'Corgi-sniff', 'Curdlesnoot', 'Crispycrunch', 'Cramplescrunch',
    'Crabapple'
)

while True:
    firstName = random.choice(first)
    lastName = random.choice(last)

    
    print("{} {}".format(firstName, lastName), file=sys.stderr)

    try_again = input("\n\nTry again? (Press enter. Otherwise, type n to quit.")
    if try_again.lower() == "n":
        break

input("\nPress Enter to exit.")
