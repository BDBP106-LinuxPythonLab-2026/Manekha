def cell_metabolism(glucose_count, oxygen_count):
    def energy_output():
        return min(glucose_count, oxygen_count // 6) * 38
    total_atp = energy_output()
    return total_atp


glucose = int(input("Enter the number of glucose molecules: "))
oxygen = int(input("Enter the number of oxygen molecules: "))
atp = cell_metabolism(glucose, oxygen)

print("Total ATP produced:", atp)