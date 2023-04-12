
import re

seq = 'ATGCAATCGACTACGATCTGAGAGGGCCTAA'

start_codon = 'ATG'
stop_codon = ['TAA', 'TAG', 'TGA']

possible_sequences = 0

match = re.search(start_codon, seq) # search for start codon

if match: # if start codon is found
    sub_seq = seq[match.end():] # take a sub-sequence after the start codon
    for codon in stop_codon:
        matches = re.findall(codon, sub_seq) # count number of stop codons in the sub-sequence
        possible_sequences += len(matches) # add the count to possible sequences

print('Total possible coding sequences:', possible_sequences)