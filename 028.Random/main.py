# random numbers

import random

 low = 1
 high = 100

 random_number = random.randint(low,high) # randint = random whole integer & (a,b) = start and the end of our range
 # random.random() = random floating number

 print(random_number) # it is always between range's start through range's end


# rock, paper, scissors for "choice"
options = ('rock', 'paper', 'scissors')
option = random.choice(options) # random choice from the elements of the tuple
print(option)

# cards for "shuffle"
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K", "A"]
random.shuffle(cards) # shuffling
print(cards)

