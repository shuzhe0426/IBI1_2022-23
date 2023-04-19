# hexagons.py

# Define a function to calculate the nth hexagonal number using the formula h = n(2n-1)
def hexagonal_number(n):
    return n*(2*n-1)

# Create a list to store the first five hexagonal numbers
hexagon_sequence = []

# Loop through the first five values of n and add the corresponding hexagonal number to the list
for n in range(1, 6):
    hexagon_sequence.append(hexagonal_number(n))

# Print the hexagon sequence
print(hexagon_sequence)
# It turns out to be [1, 6, 15, 28, 45]

