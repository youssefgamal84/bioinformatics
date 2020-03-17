def amino_acids_num(dna):
    dna_length = len(dna)
    AA_count = int(dna_length/3)
    remainder = dna_length%3
    return AA_count, remainder