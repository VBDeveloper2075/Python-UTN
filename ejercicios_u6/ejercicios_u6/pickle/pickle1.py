import pickle

diccionario = {'id':1, 'nombre':'Anna'}
archivo = open("archivo.pkl", "wb")
pickle.dump(diccionario, archivo)
archivo.close()