response = input("Size1: ")
width1, height1 = response.split("x")
width1 = int(width1)
height1 = int(height1)

response = input("Size2: ")
width2, height2 = response.split("x")
width2 = int(width2)
height2 = int(height2)

def calculate(original, valor, nuevo):
    return nuevo * valor / original

while True:
    operation = input("Tipo de operacion: ")

    if operation == "salir":
        break
    val = int(input("Valor: "))
    if operation == "w":
        value = calculate(width1, val, width2)
    elif operation == "h":
        value = calculate(height1, val, height2)
    print("Resultado: ", value)
