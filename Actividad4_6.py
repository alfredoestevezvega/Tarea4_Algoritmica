from Class_Monticulos import MonticuloBinario

lista = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

monticulo = MonticuloBinario()
monticulo.construirMonticulo(lista)
print("Montículo antes del ordenamiento:", monticulo)

monticulo.heap_sort()
print("Montículo después del ordenamiento:", monticulo)

