class estado_de_juego():
    def __init__(self):
        self.tablero =[
            ["Nt","Nc","Na","Nq","Nr","Na","Nc","Nt"],              #Definir el tablero junto con las piezas
            ["Np","Np","Np","Np","Np","Np","Np","Np"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["Bp","Bp","Bp","Bp","Bp","Bp","Bp","Bp"],
            ["Bt","Bc","Ba","Bq","Br","Ba","Bc","Bt"]]
        self.movimientos_de_piezas = {"p": self.peones, "t": self.torres, "c": self.caballos, #definir nombres para crear funciones de movimiento.
                                      "a": self.alfiles, "q": self.reinas, "r": self.reyes}
        self.movimiento_blanco = True
        self.registro = []
        self.rey_blanco = (7, 4) # Posicion del rey blanco
        self.rey_negro = (0, 4) # Posicion del rey negro
        self.jaque_mate = False



    def moverse(self, cambiar):
        self.tablero[cambiar.fila][cambiar.columna] = "--"
        self.tablero[cambiar.finfila][cambiar.fincolumna] = cambiar.movida
        self.registro.append(cambiar)
        self.movimiento_blanco = not self.movimiento_blanco # Cambiar jugadores
        if cambiar.movida == "Br":
            self.rey_blanco = (cambiar.finfila, cambiar.fincolumna)
        elif cambiar.movida == "Nr":
            self.rey_negro = (cambiar.finfila), (cambiar.fincolumna)







    def quitar_movimiento(self):
        if self.registro != 0:
          cambiar = self.registro.pop()
          self.tablero[cambiar.fila][cambiar.columna] = cambiar.movida
          self.tablero[cambiar.finfila][cambiar.fincolumna] = cambiar.comida
          self.movimiento_blanco = not self.movimiento_blanco
          if cambiar.movida == "Br":
              self.rey_blanco = (cambiar.fila, cambiar.columna)
          elif cambiar.movida == "Nr":
              self.rey_negro = (cambiar.fila), (cambiar.columna)

 #Movimientos contando los mates.
    def movimientos_validos(self):
        turno = self.movimientos_posibles() # generar movimientos posibles
        for m in range(len(turno)-1, -1, -1):
            self.moverse(turno[m])
            self.movimiento_blanco = not self.movimiento_blanco
            if self.jaque():
                turno.remove(turno[m])
            self.movimiento_blanco = not self.movimiento_blanco
            self.quitar_movimiento()
        if len(turno) == 0: # Jaque mate
            if self.jaque():
                self.jaque_mate = True

            else:
                self.sin_movimientos = True
        else:
            self.jaque_mate = False
            self.sin_movimientos = False


        return turno
#Determinar si el jugador se enceuntra en jaque
    def jaque(self):
        if self.movimiento_blanco:
            return self.cuadrado_del_rey(self.rey_blanco[0], self.rey_blanco[1])
        else:
            return self.cuadrado_del_rey(self.rey_negro[0], self.rey_negro[1])



# Ver si el enemigo puede atacar a rey en su posición
    def cuadrado_del_rey(self, i, j):
        self.movimiento_blanco = not self.movimiento_blanco
        rival = self.movimientos_posibles()
        self.movimiento_blanco = not self.movimiento_blanco
        for movimiento in rival:
            if movimiento.finfila == i and movimiento.fincolumna == j:
                return True
        return False

    #Movimientos sin contar los mates.
    def movimientos_posibles(self):
        movimientos = []
        for i in range(len(self.tablero)):
            for j in range(len(self.tablero[i])):
                turno = self.tablero[i][j][0]
                if (turno == "B" and self.movimiento_blanco) or (turno == "N" and not self.movimiento_blanco):
                    pieza = self.tablero[i][j][1]
                    self.movimientos_de_piezas[pieza](i, j, movimientos)
        return movimientos

    #Movimientos de los peones
    def peones(self, i, j, movimientos): #peones blancos
        if self.movimiento_blanco:
            if self.tablero[i-1][j] == "--":
                movimientos.append(movimiento((i, j), (i-1, j), self.tablero))
                if i == 6 and self.tablero[i-2][j] == "--":
                    movimientos.append(movimiento((i, j), (i-2, j), self.tablero))
            if j-1 >= 0: #diagonal izquierda.
                if self.tablero[i-1][j-1][0] == "N":
                    movimientos.append(movimiento((i,j), (i-1, j-1), self.tablero))
            if j+1 <= 7: #diagonal derecha.
                if self.tablero[i-1][j+1][0] == "N":
                    movimientos.append(movimiento((i,j), (i-1, j+1), self.tablero))
        else:
            if self.tablero[i+1][j] == "--":
                movimientos.append(movimiento((i, j), (i + 1, j), self.tablero))
                if i == 1 and self.tablero[i + 2][j] == "--":
                    movimientos.append(movimiento((i, j), (i + 2, j), self.tablero))

                if j - 1 >= 0:  # diagonal izquierda.
                    if self.tablero[i + 1][j - 1][0] == "B":
                        movimientos.append(movimiento((i, j), (i + 1, j - 1), self.tablero))
                if j + 1 <= 7:  # diagonal derecha.
                    if self.tablero[i + 1][j + 1][0] == "B":
                        movimientos.append(movimiento((i, j), (i + 1, j + 1), self.tablero))






    #Movimientos de las torres
    def torres(self, i, j, movimientos):
        direcciones = ((-1, 0), (0, -1), (1,0), (0,1))
        enemigos = "N" if self.movimiento_blanco else "B"
        for d in direcciones:
            for m in  range(1, 8):
                fin_de_fila = i + d[0] * m
                fin_de_columna = j + d[1] * m
                if 0 <= fin_de_fila < 8 and 0 <= fin_de_columna < 8:
                    fin_de_pieza = self.tablero[fin_de_fila][fin_de_columna]
                    if fin_de_pieza == "--":
                        movimientos.append(movimiento((i, j), (fin_de_fila, fin_de_columna), self.tablero))
                    elif fin_de_pieza[0] == enemigos:
                        movimientos.append(movimiento((i, j), (fin_de_fila, fin_de_columna), self.tablero))
                        break
                    else:
                        break
                else:
                    break


    def caballos(self, i, j, movimientos):
        caballos_caminantes = ((-2, -1), (-2,1), (-1,-2), (-1,2), (1,-2), (1, 2),(2, -1), (2, 1))
        aliados = "B" if self.movimiento_blanco else "N"
        for m in caballos_caminantes:
            finfila = i + m[0]
            fincolumna = j + m[1]
            if 0 <= finfila < 8 and 0 <= fincolumna < 8:
                fin_de_pieza2 = self.tablero[finfila][fincolumna]
                if fin_de_pieza2[0] != aliados:
                    movimientos.append(movimiento((i, j), (finfila, fincolumna), self.tablero))


    def alfiles(self, i, j, movimientos):
        direcciones = ((-1, -1), (-1,1), (1,-1), (1,1))
        enemigos = "N" if self.movimiento_blanco else "B"
        for d in direcciones:
            for m in  range(1, 8):
                fin_de_fila = i + d[0] * m
                fin_de_columna = j + d[1] * m
                if 0 <= fin_de_fila < 8 and 0 <= fin_de_columna < 8:
                    fin_de_pieza = self.tablero[fin_de_fila][fin_de_columna]
                    if fin_de_pieza == "--":
                        movimientos.append(movimiento((i, j), (fin_de_fila, fin_de_columna), self.tablero))
                    elif fin_de_pieza[0] == enemigos:
                        movimientos.append(movimiento((i, j), (fin_de_fila, fin_de_columna), self.tablero))
                        break
                    else:
                        break
                else:
                    break



    def reinas(self, i, j, movimientos):
        direcciones = ((-1, -1), (-1, 1), (1, -1), (1, 1),(-1, 0), (0, -1), (1,0), (0,1))
        enemigos = "N" if self.movimiento_blanco else "B"
        for d in direcciones:
            for m in range(1, 8):
                fin_de_fila = i + d[0] * m
                fin_de_columna = j + d[1] * m
                if 0 <= fin_de_fila < 8 and 0 <= fin_de_columna < 8:
                    fin_de_pieza = self.tablero[fin_de_fila][fin_de_columna]
                    if fin_de_pieza == "--":
                        movimientos.append(movimiento((i, j), (fin_de_fila, fin_de_columna), self.tablero))
                    elif fin_de_pieza[0] == enemigos:
                        movimientos.append(movimiento((i, j), (fin_de_fila, fin_de_columna), self.tablero))
                        break
                    else:
                        break
                else:
                    break




    def reyes(self, i, j, movimientos):
        direcciones = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
        subditos = "B" if self.movimiento_blanco else "N"
        for z in range(8):
            fin_fila = i + direcciones[z][0]
            fin_columna = j + direcciones[z][1]
            if 0 <= fin_fila < 8 and 0 <= fin_columna < 8:
                pieza_final = self.tablero[fin_fila][fin_columna]
                if pieza_final[0] != subditos:
                    movimientos.append(movimiento((i, j), (fin_fila, fin_columna), self.tablero))














class movimiento():
#En diccionario, asignamos las filas y columnas
    numero_de_filas = {"8": 7, "7": 6, "6": 5, "5": 4, "4": 3, "3": 2, "2": 1, "1":0}
    reversa = {v: k for k, v in numero_de_filas.items()}
    letra_de_columna = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h":7}
    reversa2 = {v: k for k, v in letra_de_columna.items()}


    def __init__(self, cuadradoI, cuadradoT, tabla):
        self.fila = cuadradoI[0]
        self.columna = cuadradoI[1]
        self.finfila = cuadradoT[0]
        self.fincolumna = cuadradoT[1]
        self.movida = tabla[self.fila][self.columna]
        self.comida = tabla[self.finfila][self.fincolumna]
        self.identificador = self.fila * 1000 + self.columna * 100 + self.finfila * 10 + self.fincolumna

    def __eq__ (self,otro):
        if isinstance(otro, movimiento):
            return self.identificador == otro.identificador
        return False




    def historial(self):
        print("Movimeinto anterior:")
        return self.posicion(self.fila, self.columna) + self.posicion(self.finfila, self.fincolumna)


    def posicion(self, i, j):
        return self.reversa2[j] + self.reversa[i]

