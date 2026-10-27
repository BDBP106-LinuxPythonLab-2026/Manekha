def extract_codons(sequence, position):
    codons = []

    start = position - 1

    for i in range(start, len(sequence) - 2, 3):
        codon = sequence[i:i+3]
        codons.append(codon)

    return codons

sequence = "GTTTCGATTATAACG"

print(extract_codons(sequence, 1))
print(extract_codons(sequence, 3))