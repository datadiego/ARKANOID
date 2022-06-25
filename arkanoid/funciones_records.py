def csv_a_dict(archivo):
    import csv
    raw_data = {}
    csv_file = open(archivo, "r")
    csv_reader = csv.DictReader(csv_file)
    for elemento in csv_reader:
        raw_data[elemento["Jugador"]] = int(elemento["Puntos"])
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