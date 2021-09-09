import random

def generar_matriz():
  print("La matriz es:")
  matriz=[[0,0,0],[0,0,0],[0,0,0]]
  for i in range(0,3):
     for j in range(0,3):
       numero=random.randrange(0,2)
       matriz[i][j]=numero
       print(matriz[i][j],end=' ')
     print(" ")
  return matriz
  
def validar_numero_entero(mensaje):
  numero=input(mensaje)
  correcto=True
  while correcto:
    try:
      numero=int(numero)
      correcto=False
    except ValueError:
      correcto=True
      print("Valor ingresado incorrecto, vuelva a digitar el valor")
      numero=input(mensaje)
  return numero

def jugador_matriz():
  contador_aciertos=0
  contador_errores=0

  while(contador_aciertos!=3 and contador_errores!=3):
    matriz=generar_matriz()
    indice1=validar_numero_entero("Ingrese indice 1 de la matiz:")
    indice2=validar_numero_entero("Ingrese el indice 2 de la matriz:")
    valida=True
    while(valida):

      try:
        matriz[indice1][indice2]
        valida=False
      except IndexError:
        print("***********************************************")
        print("EL valor ingresado no es valido")
        print('''Recuerde que la matriz en 3 por 3 y en python se empieza a contar los
        indices desde el 0. Valores permitidos solo entre 0-2
        ''')
        print("**************************************************")
        indice1=validar_numero_entero("Ingrese indice 1 de la matiz:")
        indice2=validar_numero_entero("Ingrese el indice 2 de la matriz:")
        valida=True
    if contador_aciertos!=3 and matriz[indice1][indice2]==1:
      contador_aciertos+=1
      print(f"({indice1},{indice2}) en la fila {indice1}, columna {indice2} observamos un 1")
      print("Por tanto: acertó")
      print(f'''Marcador: 
      Aciertos:{contador_aciertos}
      Error:{contador_errores}
      ''')
    
    elif contador_errores!=3 and matriz[indice1][indice2]==0:
      contador_errores+=1
      print(f"({indice1},{indice2}) en la fila {indice1}, columna {indice2} observamos un 0")
      print("Por tanto: Error")
      print(f'''Marcador: 
      Aciertos:{contador_aciertos}
      Error:{contador_errores}
      ''')
  if contador_aciertos==3:
    print("¡Felicitaciones, ha ganado!")
  elif contador_errores==3:
    print("Fin del juego, mejor suerte la proxima")

def menu():
  print('''
  1) Para empezar a jugar
  2) salir
  ''')
#Programa principal
def programa_principal():
  print('''
   ______________________________________________________________
  |                           RETO SEMANA 6                      |
  |                        JUEGO DE LA MATRIZ                    |
  |______________________________________________________________|
  ''')
  print('''
   ________________________________________________________________
  |   dada una matriz 3 por 3 encontrar los elementos que no son   |
  |   ceros                                                        |
  |________________________________________________________________|
  ''')
       
  iniciador="1"
  while(iniciador=="1"):
    menu() 
    opc=validar_numero_entero("Ingrese una opción:")
    if opc==1:
      
      jugador_matriz()
      
    elif opc==2:
      print("Hasta luego, vuelva pronto.")
      iniciador="2"

def init ():  
    programa_principal()

if __name__ == "__name__":
    init()