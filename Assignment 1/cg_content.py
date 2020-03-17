def cg_content(dna):
    dna = dna.upper()
    c_count = dna.count("C")
    g_count = dna.count("G")
    dna_length = len(dna)
    return (c_count+g_count)/dna_length