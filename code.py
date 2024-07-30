def metros_a_centimetros(metros):
    return metros * 100

metros = float(input("Introduce la cantidad en metros: "))

centimetros = metros_a_centimetros(metros)

print(f"{metros} metros son {centimetros} centímetros.")