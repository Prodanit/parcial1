def solicitar_datos():
    departamento = input("Ingrese el nombre del departamento: ")
    
    while True: #captacion de errores
        try:
            limite = int(input("Ingrese el número de registros a consultar: "))
            if limite > 0:
                return departamento, limite
            else:
                print("Error: El número de registros debe ser mayor a 0.")
        except ValueError:
            print("Error: Ingrese un número entero.")

def mostrar_datos(df):
    if df is None or df.empty:
        print("No hay datos para mostrar.")
    else:
        print(df)
