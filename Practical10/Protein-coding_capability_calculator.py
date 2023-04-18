def coding_percentage(dna_sequence):
    """Determine whether a given DNA sequence is protein-coding or not.

        Args:
            sequence (str): A DNA sequence.

        Returns:
            tuple: A tuple containing the percentage of the sequence which is coding and
            whether the sequence should be labelled as ‘protein-coding’, ‘non-coding’, or
            ‘unclear’.
        """
    # Convert sequence to uppercase
    dna_sequence = dna_sequence.upper()
    # Find the indices of the start and stop codons
    start_codon = dna_sequence.find('ATG')
    stop_codon = dna_sequence.rfind('TGA')
    # Calculate the distance between the start and stop codons
    coding_length = stop_codon - start_codon - 3
    # Calculate the percentage of the sequence that is codin
    coding_percentage = coding_length / len(dna_sequence)
    # Determine the label based on the percentage
    if coding_percentage > 0.5:
        label = 'protein-coding'
    elif coding_percentage < 0.1:
        label = 'non-coding'
    else:
        label = 'unclear'
    # Return the percentage and label
    return (coding_percentage * 100, label)

# Example
dna_sequence = 'ATGAACTGTCGACTGCTGAGTCGACTGCTGATCGATCGTAGCTAGCTAGCTAGCTAGCTGATGCTGATGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGTCGATCGATCGATCGTGA'
percentage, label = coding_percentage(dna_sequence)
print(f'This DNA sequence is {percentage:.2f}% and it is labeled as {label}.')
