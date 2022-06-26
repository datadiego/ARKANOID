def csv_a_dict(archivo):
    import csv
    raw_data = {}
    csv_file = open(archivo, "r")
    csv_reader = csv.DictReader(csv_file)
    
    for elemento in csv_reader:
        raw_data[elemento["Jugador"]] = elemento["Puntos"]
    return raw_data

'''
a = convierte_a_dict("puntuaciones.csv")
boo = max(a)
print(boo)
Podemos usar la funcion max para sacar el valor maximo de un diccionario
Si conforme accedemos al mayor lo borramos o sobreescribimos su valor a 0, podemos recorrer el diccionario
'''

def csv_a_lista(archivo):
    import csv
    raw_data = []
    csv_file = open(archivo, "r")
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for elemento in csv_reader:
        raw_data.append(elemento)
    return raw_data

def extrae_valores_records(archivo):
    import csv
    raw_data = []
    csv_file = open(archivo, "r")
    csv_reader = csv.reader(csv_file)
    for elemento in csv_reader:
        raw_data.append(int(elemento[1]))
    return raw_data

def extrae_nombres_records(archivo):
    import csv
    raw_data = []
    csv_file = open(archivo, "r")
    csv_reader = csv.reader(csv_file)
    for elemento in csv_reader:
        raw_data.append(elemento[0])
    return raw_data
def bubble_sort(valores, nombres):
    loop = True
    while loop:
        loop = False
        for i in range(len(valores)-1):
            if valores[i] < valores[i+1]:
                save_valor = valores[i]
                save_nombre = nombres[i]
                valores[i] = valores[i+1]
                nombres[i] = nombres[i+1]
                valores[i+1] = save_valor
                nombres[i+1] = save_nombre
                loop = True
def limit_array(valores, val):
    if len(valores) > val:
        valores.pop()

if __name__ == "__main__":
    valores = extrae_valores_records("puntuaciones.csv")
    nombres = extrae_nombres_records("puntuaciones.csv")
    bubble_sort(valores, nombres)
    limit_array(valores,4)
    limit_array(nombres,4)
    #Sobreescribo el archivo
    print(valores)
    print(nombres)