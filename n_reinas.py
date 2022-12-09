class Tablero:
    def __init__(self, tamanio):
        # Establecemos un tablero de amplitud "tamanio x tamanio".
        self.tamanio = tamanio
        self.columnas = []

    def agregar_siguiente_fila (self, columna):
        self.columnas.append(columna)
        

    def eliminar_fila_actual(self):
        return self.columnas.pop()

    
    def siguiente_fila (self, columna):

        fila = len(self.columnas)

        # Nos fijamos en la columna.
        for reina in self.columnas:
            if columna == reina:
                return False

        # Nos fijamos en la diagonal. 
        for r_fila, r_columna in enumerate(self.columnas):
            if r_columna - r_fila == columna - fila:
                return False

        # Miramos la otra diagonal
        for r_fila, r_columna in enumerate(self.columnas):
            if ((self.tamanio - r_columna) - r_fila) == ((self.tamanio - columna) - fila):
                return False

        return True


    def formato(self):
        for fila in range(self.tamanio):
            for columna in range(self.tamanio):
                if columna == self.columnas[fila]:
                    print("R", end=" ")
                else:
                    print("·", end=" ")

            print()

def resolucion(tamanio):

    tablero = Tablero(tamanio)

    soluciones = 0

    fila = 0

    columna = 0

    while True:

        while columna < tamanio:
            if tablero.siguiente_fila(columna):
                tablero.agregar_siguiente_fila(columna)
                fila +=1
                columna = 0
                break
            
            else:
                columna += 1

        
        if (columna == tamanio or fila == tamanio):

            if fila == tamanio:
                tablero.formato()
                print()
                soluciones +=1
                tablero.eliminar_fila_actual()
                fila -= 1

            try:
                columna_anterior = tablero.eliminar_fila_actual()

            except IndexError:

                # Se han eliminado todas las reinas.
                break

            fila -= 1
            columna = 1 + columna_anterior

    print("Numero de soluciones:", soluciones)


if __name__ == "__main__":
    a = 4
    resolucion(10)

