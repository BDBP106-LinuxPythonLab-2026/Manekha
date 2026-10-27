def protein_energy_temp():
    def calculate_free_energy(delta_h, delta_s, temp):
        delta_g = delta_h - temp * delta_s
        return delta_g
    enthalpy = float(input("Enter enthalpy change (ΔH): "))
    entropy = float(input("Enter entropy change (ΔS): "))
    temperature = float(input("Enter temperature in Kelvin: "))
    result = calculate_free_energy(enthalpy, entropy, temperature)

    print("Change in free energy (ΔG):", round(result, 2))

    if result < 0:
        print("The process is thermodynamically favourable.")
    elif result > 0:
        print("The process is thermodynamically unfavourable.")
    else:
        print("The system is at equilibrium.")

protein_energy_temp()