class MonticuloMaximo:
    def __init__(self):
        self.listaMonticulo = [0]
        self.tamanoActual = 0

    def __str__(self):
        return "".join(str(self.listaMonticulo))

    def infiltArriba(self, i):
        while i // 2 > 0:   
            if self.listaMonticulo[i] > self.listaMonticulo[i//2]:
                # Intercambiar los elementos
                self.listaMonticulo[i//2], self.listaMonticulo[i] = self.listaMonticulo[i], self.listaMonticulo[i//2]
            i = i // 2

    def insertar(self, k):
        self.listaMonticulo.append(k)
        self.tamanoActual = self.tamanoActual + 1
        self.infiltArriba(self.tamanoActual)

    def infiltAbajo(self, i):
        while (i * 2) <= self.tamanoActual:
            hm = self.hijoMax(i)
            if self.listaMonticulo[i] < self.listaMonticulo[hm]:
                # Intercambiar los elementos
                self.listaMonticulo[i], self.listaMonticulo[hm] = self.listaMonticulo[hm], self.listaMonticulo[i]
            i = hm

    def hijoMax(self, i):
        if i * 2 + 1 > self.tamanoActual:
            return i * 2
        else:
            if self.listaMonticulo[i*2] > self.listaMonticulo[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1
          
    def hijoIzq(self, i):
        return self.listaMonticulo[2*i]
    
    def hijoDerecho(self, i):
        return self.listaMonticulo[2*i+1]

    def eliminarMax(self):
        valorSacado = self.listaMonticulo[1]
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual]
        self.tamanoActual = self.tamanoActual - 1
        self.listaMonticulo.pop()
        self.infiltAbajo(1)
        return valorSacado

    def construirMonticulo(self, unaLista):
        i = len(unaLista) // 2
        self.tamanoActual = len(unaLista)
        self.listaMonticulo = [0] + unaLista[:]
        while (i > 0):
            self.infiltAbajo(i)
            i = i - 1
