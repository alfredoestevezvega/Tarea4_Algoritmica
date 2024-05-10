class MonticuloBinario:
    def __init__(self):
        self.listaMonticulo = [0]
        self.tamanoActual = 0

    def infiltAbajo(self, i, tamaño):
        while (i * 2) <= tamaño:
            hijo_izquierdo = i * 2
            hijo_derecho = i * 2 + 1
            if hijo_derecho <= tamaño and self.listaMonticulo[hijo_derecho] < self.listaMonticulo[hijo_izquierdo]:
                hijo_min = hijo_derecho
            else:
                hijo_min = hijo_izquierdo
            if self.listaMonticulo[i] > self.listaMonticulo[hijo_min]:
                self.listaMonticulo[i], self.listaMonticulo[hijo_min] = self.listaMonticulo[hijo_min], self.listaMonticulo[i]
            else:
                break
            i = hijo_min

    def heapify(self):
        tamaño = len(self.listaMonticulo) - 1
        i = tamaño // 2
        while i > 0:
            self.infiltAbajo(i, tamaño)
            i -= 1

    def heap_sort(self):
        tamaño = len(self.listaMonticulo) - 1
        self.heapify()
        while tamaño > 0:
            self.listaMonticulo[1], self.listaMonticulo[tamaño] = self.listaMonticulo[tamaño], self.listaMonticulo[1]
            tamaño -= 1
            self.infiltAbajo(1, tamaño)

    def insertar(self, k):
        self.listaMonticulo.append(k)
        self.tamanoActual += 1

    def construirMonticulo(self, unaLista):
        self.listaMonticulo = [0] + unaLista[:]
        self.tamanoActual = len(unaLista)
        self.heapify()

    def __str__(self):
        return ', '.join(map(str, self.listaMonticulo[1:]))


