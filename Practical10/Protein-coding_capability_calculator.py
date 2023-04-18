def dna_coding(sequence):
    """Determine whether a given DNA sequence is protein-coding or not.

    Args:
        sequence (str): A DNA sequence.

    Returns:
        tuple: A tuple containing the percentage of the sequence which is coding and
        whether the sequence should be labelled as ‘protein-coding’, ‘non-coding’, or
        ‘unclear’.
    """

    # Convert the sequence to upper case
    sequence = sequence.upper()

    # Find the indices of the start and stop codons
    start_index = sequence.find("ATG")
    stop_index = sequence.find("TGA")

    # If either the start or stop codon is not found, return unclear
    if start_index == -1 or stop_index == -1:
        return 0, "unclear"

    # Calculate the length of the coding sequence
    coding_length = stop_index - start_index - 3

    # Calculate the percentage of the sequence which is coding
    coding_percentage = coding_length / len(sequence) * 100

    # Determine whether the sequence is protein-coding, non-coding, or unclear
    if coding_percentage > 50:
        return coding_percentage, "protein-coding"
    elif coding_percentage < 10:
        return coding_percentage, "non-coding"
    else:
        return coding_percentage, "unclear"
# Example
sequence = "ATGACGTAGCTAGCTAGCTGCTAGCTAGCTAGCTAGCTGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTGTGA"
coding_percentage, coding_label = dna_coding(sequence)
print(f"The sequence is {coding_percentage:.2f}% coding and is {coding_label}.")
