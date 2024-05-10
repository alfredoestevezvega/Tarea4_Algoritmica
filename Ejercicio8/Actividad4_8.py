from Class_mont_cola import *

cola_prioridad = ColaPrioridad()
cola_prioridad.agregar(5)
cola_prioridad.agregar(3)
cola_prioridad.agregar(7)

print("Elementos de la cola de prioridad:")
print(cola_prioridad.avanzar())  # Imprime el elemento mínimo: 3
print(cola_prioridad.avanzar())  # Imprime el siguiente elemento mínimo: 5