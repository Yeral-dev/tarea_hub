def metros_a_kilometros(metros):
    return metros / 1000

metros = float(input("Introduce la cantidad en metros: "))

kilometros = metros_a_kilometros(metros)

print(f"{metros} metros son {kilometros} kilómetros.")