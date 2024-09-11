import time
import os
import domino

isValid = True

while (isValid):

    print("\n============== ¿Cuantos jugadores van a jugar? [2-4] ==================== \n")

    try:

        amountPlayer = int(input("Cantidad de jugadores: "))

        # OPCION 0 para cerrar el juego

        if (amountPlayer == 0):
            isValid = False
            print("Juego cancelado")
            break

        if (amountPlayer > 4 or amountPlayer < 2):
            
            print("La cantidad de jugadores no es valida  \n")

            time.sleep(2)

            os.system("cls")

            continue

        juego = domino.Domino(amountPlayer)
        
        while True:
            
            juego.imprimirFichas()
            
            print(f"\nTurno del jugador {juego.jugadorActual + 1}")
            
            indiceFicha =  int(input('Selecciona la ficha que vas a jugar (selecciona por número): ')) - 1;
            
            print()
            
            lado = int(input('Para jugar el lado izquierdo de la ficha, selecciona 0 y 1 para la derecha: '))
            
            if juego.jugarFicha(indiceFicha, lado):
                
                juego.siguienteTurno()
                
            else:
                print("Esta jugada no es válida, utiliza otro lado o intenta con otra ficha")
            time.sleep(1)
            
    except ValueError as error:
        print("El número que ha introdicido no es válido\n")
        time.sleep(1)
        os.system("cls")





