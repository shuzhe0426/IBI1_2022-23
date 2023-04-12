

import re

#Ask user to input stop codon
stop_codon = input("Please enter a stop codon (TAA/TAG/TGA): ").upper()

#Create output file name
output_file = f"{stop_codon}_stop_genes.fa"

# Open input and output files


# Define regular expression pattern to match gene name
# This assumes that the name is contained in the string after the first whitespace character
gene_name_pattern = re.compile(r'^>\s*(\S+)')

# Initialize variables
gene_seq = ''
gene_name = ''
gene_count = 0
total_count = 0
# Open input and output files
input_file = open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r")
output_file = open(output_file, "w")

# Iterate over input file
for line in input_file:
    # For the line starting with ">", get the matching gebe name
    if line.startswith(">"):
        gene_name = gene_name_pattern.search(line).group()
        gene_seq = ''
    # Update the sequence, or it will gather wrong sequences
    else:
        gene_seq += line.strip() # Remove line breaks and add to gene sequence
        # Count number of instances of stop codon in current line
        if re.compile(r'{}$'.format(stop_codon)).search(gene_seq):
            gene_count=len(re.findall(r'{}'.format(stop_codon),gene_seq))
            # Put gene name, possible sequence number, gene sequence into output file
            output_file.write('{}\n{}\n{}\n'.format(gene_name,gene_count,gene_seq))
    total_count += gene_count  # The total number is the sum of each sequence number.

# Print total count of coding sequences with given stop codon
print(f"Total coding sequences with {stop_codon}: {total_count}")

# Close input and output files
input_file.close()
output_file.close()