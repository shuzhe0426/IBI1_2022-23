import re

seq = 'ATGCAATCGACTACGATCTGAGAGGGCCTAA'

codon_count = 0

# Look for start codon 'ATG' followed by stop codon 'TAA'
if re.search('ATG.*TAA', seq):
    codon_count += 1

# Look for start codon 'ATG' followed by stop codon 'TAG'
if re.search('ATG.*TAG', seq):
    codon_count += 1

# Look for start codon 'ATG' followed by stop codon 'TGA'
if re.search('ATG.*TGA', seq):
    codon_count += 1

print(f"Possible coding sequences: {codon_count}")