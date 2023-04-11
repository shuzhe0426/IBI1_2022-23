import re

input_file = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
output_file = 'TGA_genes.fa'

# Define regular expression pattern to match gene name
# This assumes that the name is contained in the string after the first whitespace character
gene_name_pattern = re.compile(r'^>\s*(\S+)')

# Define regular expression pattern to match TGA stop codon at end of sequence
# This assumes that there are no whitespace characters in the sequence lines
TGA_pattern = re.compile(r'TGA$')

# Open input and output files
with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
    current_gene_name = ''
    current_sequence = ''
    for line in f_in:
        if line.startswith('>'):
            # If we encounter a new gene name, check if the previous sequence matched the TGA pattern
            if current_gene_name and TGA_pattern.search(current_sequence):
                # If it did, write the gene name and sequence to the output file
                f_out.write('>{}\n{}\n'.format(current_gene_name, current_sequence))
            # Update the current gene name and sequence
            current_gene_name = gene_name_pattern.search(line).group(1)
            current_sequence = ''
        else:
            # Concatenate all sequence lines into a single string
            current_sequence += line.strip()
    # Check the final sequence after the end of the file
    if current_gene_name and TGA_pattern.search(current_sequence):
        f_out.write('>{}\n{}\n'.format(current_gene_name, current_sequence))

print(gene_name_pattern)