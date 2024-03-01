def get_hamming_distance(dna1, dna2):
    hamming_distance = 0
    i = 0

    while (i < len(dna1)):
        if dna1[i] != dna2[i]:
            hamming_distance += 1

        i += 1
    
    return hamming_distance

def get_dna_complement(dna):
    complement = ""

    for char in dna:
        if char == "A":
            complement = "T" + complement
        elif char == "C":
            complement = "G" + complement
        elif char == "T":
            complement = "A" + complement
        elif char == "G":
            complement = "C" + complement
        else:
            complement = char + complement

    return complement        