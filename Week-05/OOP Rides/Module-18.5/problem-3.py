def DNA_to_RAN_transfer(dna):
    rna = ""
    
    for necleotide in dna:
        if necleotide == "T":
            rna += "U"
        else:
            rna += necleotide
    return rna

dna = "GATGGAACTTGACTACGTAAATT"
rna = DNA_to_RAN_transfer(dna)
print(rna)