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
            if ((self.tamanio - r_columna) - r_fila) == ((self.tamanio) - fila):
                return False

        return True


        