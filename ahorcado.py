from itertools import count
from re import I
import funciones

def ahorcado(palabra,num_strikes):
    num_letras = len(palabra)
    ya_gano    = False
    abcdario  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    usadas = ""
    #letras = { c:False for c in palabra}
    intentos = 0
    respuesta = ""
    lista   = [ [x,False] for x in palabra]
    usadas = []
    #diccionario = { 'V':[[0],False], "I":[[1],False], "E":[[2,5],False], "R":[[3],False], "N":[[4],False], "S":[[6],False]}
    while intentos<=num_strikes and ya_gano==False:
        contador = 0
        fallo = True
        mostrar_pisos(lista)
        print("Strikes: ",intentos)
        if(intentos < 6):
            respuesta = input("Ingresa una letra o la palabra: ")
        else:
            print("Lo siento pero se te acabaron los intentos, gracias por jugar!")
        respuesta = respuesta.upper()


        #Si la respuesta viene vacia
        if(len(respuesta) == 0):
            print("\n===========================")
            print("Tienes que ingresar al menos una letra!")

        #Si la respuesta ya ha sido utilizada
        if(respuesta not in usadas):
            if(respuesta != ""):
                usadas.append(respuesta)
                #print(usadas)
        else:
            respuesta = ""
            print("\n===========================")
            print("La letra escrita ya ha sido utilizada!")
            #Si la respuesta es solo una letra
        if(len(respuesta) == 1):
            #print(len(respuesta))
            for elemento in lista:
                if respuesta not in elemento:
                    None
                else:
                    if respuesta in elemento:
                        fallo = False
                        elemento = [respuesta,True]
                        lista[contador] = elemento
                contador = contador + 1
            if(fallo == False):
                print("")
            else:
                intentos = intentos + 1
                print("La letra")
            print("===========================")
            ya_gano = verificar_ganar(lista,ya_gano)
        else:
            if(len(respuesta) > 1):
                ya_gano = verificar_palabra(palabra,lista,ya_gano,respuesta)
                if(ya_gano == False):
                    print("===========================")
                    print("\nLa Respuesta no coincide con la palabra secreta")
                    intentos = intentos + 2

        
        print("")

def verificar_palabra(palabra,lista,ya_gano,respuesta):
    #Verifica si la respuesta introducida coincide con la palabra
    #si es así devuelve la variable ya_gano en True
    contador = 0
    if(palabra == respuesta):
        for elemento in lista:
            elemento = [elemento[0],True]
            lista[contador] = elemento
            contador = contador + 1
        ya_gano = True
        print("\n===========================\n")
        print("La palabra secreta es: ")
        mostrar_pisos(lista)
        print("Felicidades haz ganado!")
    return ya_gano

def verificar_ganar(lista,ya_gano):
    #Verifica si todos los elementos de la lista están en True, 
    # si es así regresa ya_gano = True y el juego se acaba.
    #print(lista,len(lista))
    contador = 0
    for elemento in lista:
        if True in elemento:
            contador = contador + 1
    #print(contador)
    if(contador == len(lista)):
        ya_gano = True
        print("\n===========================\n")
        print("La palabra secreta es: ")
        mostrar_pisos(lista)
        print("Felicidades haz ganado!")
    return ya_gano

def mostrar_pisos(lista):
    #Nos muestra la letra de elementos que tienen valor de True, los que están en False muestra un "_"
    for elemento in lista:
        if elemento[1] == True:
            print(elemento[0],end=" ")
        else:
            print("_", end=" ")
    print("")

palabra = "INGENIERIA"

#print(lista)

def main():
    print("Bienvenido al juego del Ahorcado\nPuedes fallar 6 veces(6 strikes) \nFallar con una letra es 1 Strike\nFallar al intento de Adivinar la palabra son 2 Strikes")
    ahorcado(palabra,6)        
    print("")

if __name__ == "__main__":
    main()


#lista[1] = ['I',True]
#['V', 'I', 'E', 'R', 'N', 'E', 'S']
#[['V',False], ['I',False], ['E',False], ]
#mostrar_pisos(lista)

