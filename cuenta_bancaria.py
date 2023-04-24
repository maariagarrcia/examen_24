
from multiprocessing import Process,Lock,Pool
from colorama import Fore
import time


def arrancar_hilos(hilos) -> None:
    print("* Arrancando hilos...")
    for h in hilos:
        h.start()
        print(Fore.LIGHTYELLOW_EX + "." + Fore.WHITE, end='')

    print()


def crear_hilos_100(cantidad: int, contador: int, lock: Lock,c) -> list():
    hilos = []
    print("* Creando hilos...")
    for i in range(0, cantidad):
        hilo = Process(target=incrementar, args=[contador, lock,c])
        hilos.append(hilo)

        hilo = Process(target=decrementar, args=[contador, lock,c])
        hilos.append(hilo)
     


    
    return hilos


def crear_hilos_50(cantidad: int, contador: int, lock: Lock,c) -> list():
    hilos = []
    print("* Creando hilos...")
    for i in range(0, cantidad):
        hilo = Process(target=incrementar, args=[contador, lock,c])
        hilos.append(hilo)

        hilo = Process(target=decrementar, args=[contador, lock,c])
        hilos.append(hilo)
     
    
    return hilos

def crear_hilos_20(cantidad: int, contador: int, lock: Lock,c) -> list():
    hilos = []
    print("* Creando hilos...")
    for i in range(0, cantidad):
        hilo = Process(target=incrementar, args=[contador, lock,c])
        hilos.append(hilo)

        hilo = Process(target=decrementar, args=[contador, lock,c])
        hilos.append(hilo)
     
    
    return hilos

def esperar_finalizacion_hilos(hilos):
    print("* Esperando finalización hilos...")
    for h in hilos:
        h.join()


def incrementar(contador: list, lock: Lock,c) -> None:
    # lo q hace el bucle es q cada hilo incremente 5 veces el contador
    # Si usamos with no es necesario usar adquire ni release
    # Se usa el modo blocking=True en adquire() ya que es el metodo por defecto
    for i in range(0,c):
        with lock:
            # Región critica: Donde usamos el recurso compartido
            copia_contador = contador[0]
            time.sleep(0.01)
            contador[0] = copia_contador + 1
            #print(Fore.RED + "+" + Fore.WHITE, end="")

    

def decrementar(contador: list, lock: Lock,c) -> None:
    # Si usamos with no es necesario usar adquire ni release
    # Se usa el modo blocking=True en adquire() ya que es el metodo por defecto
    for x in range(0,c):
        with lock:
            # Región critica: Donde usamos el recurso compartido
            copia_contador = contador[0]
            time.sleep(0.0001)
            contador[0] = copia_contador - 1
            #print(Fore.YELLOW + "-" + Fore.WHITE, end="")



def main() -> None:
    print()
    print("MUCHOS HILOS ACCEDIENDO A UNA REGIÓN CRÍTICA")
    print("-"*40)
    print("· Al final el contador deberia ser 100")
    print()

    # Esta es la lista que actualizaran todos los hilos
    contador = [100]

    # Crear un objeto Lock para proteger región cr´tica
    lock = Lock()
    
    # creamos la caantidad
    # Crear hilos
    hilos = []
    hilos = crear_hilos_100(40, contador, lock,100)
    hilos=crear_hilos_50(20,contador,lock,50)
    hilos=crear_hilos_20(60,contador,lock,20)
    




    # Ejecutar hilos
    arrancar_hilos(hilos)
    esperar_finalizacion_hilos(hilos)
    print()
    print("Contador"+Fore.RED, contador, Fore.WHITE)


if __name__ == '__main__':
    main()

