def analyse_dna(sequence):
    def gc_content():
        g_count = sequence.count('G')
        c_count = sequence.count('C')
        total = len(sequence)

        percentage = ((g_count + c_count) / total) * 100
        return percentage

    percentage = gc_content()

    if percentage > 50:
        print("GC-rich sequence")
    else:
        print("AT-rich sequence")

    print("GC content:", round(percentage, 2), "%")

analyse_dna("ATGCGCGT")
analyse_dna("ATATATGC")