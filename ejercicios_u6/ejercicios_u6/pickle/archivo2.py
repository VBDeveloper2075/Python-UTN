import pickle

archivo = open("archivo.pkl", "rb")
recuperar = pickle.load(archivo)
print(recuperar)