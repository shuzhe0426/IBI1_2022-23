# What does this piece of code do?
# Answer:Progress is the loop variable for the entire body of the loop, which is 0 to 9 for 10 times. n is a random number. A number between 1 and 100 is selected at random and reserved for comparison. In the ten random results, the largest number will be compared and output.
# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0
stored_random_number=0
while progress<10:
	progress+=1
	n = randint(1,100)
	if n > stored_random_number:
		stored_random_number = n

print(stored_random_number)
