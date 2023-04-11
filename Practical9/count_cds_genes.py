
import re

# Read file
with open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r") as f:
    file_content = f.read().splitlines()

# Request a stop codon
stop_codon = input("Please enter one of the three stop codons (TAA, TAG or TGA): ")

# Create output file name
output_filename = f"{stop_codon}_stop_genes.fa"

# Stores a list of gene names and sequences that meet the requirements
genes = []
sequence_lines = []
gene_name = ""
gene_count = 0
for line in file_content:
    if line.startswith(">"):
        if gene_name:
            # Complete the recording of the previous gene
            genes.append(gene_name)
            sequence_lines.append("".join(sequence))
        # Start recording new genes
        gene_name = re.match("^>(\S+)", line).group(1)
        sequence = []
        gene_count = 1
    else:
        # Processing gene sequence
        sequence.append(line)
        if line.endswith(stop_codon):
            gene_count += 1
if gene_name:
    # The record of the last gene
    genes.append(gene_name)
    sequence_lines.append("".join(sequence))

# Write output file
with open(output_filename, "w") as f:
    for i in range(len(genes)):
        gene = genes[i]
        gene_sequence = sequence_lines[i]
        f.write(f">{gene} {gene_count}\n{gene_sequence}\n")
