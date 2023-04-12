

import re

#Ask user to input stop codon
stop_codon = input("Please enter a stop codon (TAA/TAG/TGA): ").upper()

#Create output file name
output_file = f"{stop_codon}_stop_genes.fa"

# Open input and output files
input_file = open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r")
output_file = open(output_file, "w")

# Define regular expression pattern to match gene name
# This assumes that the name is contained in the string after the first whitespace character
gene_name_pattern = re.compile(r'^>\s*(\S+)')

# Initialize variables
gene_seq = ""
gene_name = ""
gene_count = 0
total_count = 0

# Iterate over input file
for line in input_file:
    if line.startswith(">"):
        # Check if previous gene sequence had the given stop codon
        if gene_seq.endswith(stop_codon):
            # Write gene information to output file
            output_file.write(f">{gene_name} ({gene_count})\n{gene_seq}\n")
            total_count += gene_count

        # Initialize variables for new gene
        gene_seq = ""
        gene_count = 0
        gene_name = gene_name_pattern.search(line).group(1)
    else:
        # Count number of instances of stop codon in current line
        gene_count += line.count(stop_codon)
        # Remove line breaks and add to gene sequence
        gene_seq += line.strip()

# Check if last gene sequence had the given stop codon
if gene_seq.endswith(stop_codon):
    # Write gene information to output file
    output_file.write(f">{gene_name} ({gene_count})\n{gene_seq}\n")
    total_count += gene_count

# Print total count of coding sequences with given stop codon
print(f"Total coding sequences with {stop_codon}: {total_count}")

#Close input and output files
input_file.close()
output_file.close()