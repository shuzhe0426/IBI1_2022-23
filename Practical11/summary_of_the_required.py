# Read in the sequences to be compared (Seq1 and Seq2) from their respective files
# (e.g. ACE2_human.fa and ACE2_cat.fa).
with open("ACE2_mouse.fa") as f:
    seq1_name = f.readline().strip()
    seq1 = f.readline().strip()

with open("ACE2_human.fa") as f:
    seq2_name = f.readline().strip()
    seq2 = f.readline().strip()

# Read in the BLOSUM62 matrix from its file (e.g. BLOSUM62.txt)
# And store it in a dictionary for easy access.
blosum62 = {}
with open("BLOSUM62.txt") as f:
    headers = f.readline().split()
    for line in f:
        row = line.split()
        aa1 = row[0]
        for i in range(1, len(row)):
            aa2 = headers[i-1]
            blosum62[(aa1, aa2)] = int(row[i])

# Iterate through each pair of amino acids in the two sequences and calculate their BLOSUM62 score.
# Store each score in a list.
scores = []
for i in range(len(seq1)):
    aa1 = seq1[i]
    aa2 = seq2[i]
    score = blosum62.get((aa1, aa2), blosum62.get(("X", "X")))
    # Note: We use "X" as a fallback score for any unknown amino acid pairs.
    scores.append(score)

# Calculate the total score by summing up all the individual scores.
total_score = sum(scores)

# Calculate the percentage identity by counting the number of identical amino acids.
identical_count = sum(1 for aa1, aa2 in zip(seq1, seq2) if aa1 == aa2)
# And dividing by the total length of the sequences.
percent_identity = 100.0 * identical_count / len(seq1)

# Print out the result
print(seq1_name)
print(seq1)
print(seq2_name)
print(seq2)
print("BLOSUM62 score:", total_score)
print("Percentage identity:", percent_identity)