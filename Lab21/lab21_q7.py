def analyse_dna(sequence):
    def gc_content():
        gc_count = 0
        for base in sequence:
            if base == 'G' or base == 'C':
                gc_count += 1
        gc_percentage = (gc_count / len(sequence)) * 100
        return gc_percentage
    result = gc_content()

    print("GC Content:", round(result, 2), "%")

    if result > 50:
        print("The DNA sequence is GC-rich.")
    else:
        print("The DNA sequence is AT-rich.")

dna = input("Enter a DNA sequence: ").upper()
analyse_dna(dna)