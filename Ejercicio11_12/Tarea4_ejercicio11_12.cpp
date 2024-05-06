#include <iostream>
#include <map>
#include <vector>
using namespace std;

#include "Class_cola.hpp"
#include "Class_grafos.hpp"
void recorrido_anchura (Graph x,int nodo);
int main()
{
    Graph g;

    for (int i = 0; i < 6; i++)
    {
        g.addVertex(i);
    }
//Ejercicio11
cout<<"Ejercicio11:"<<endl;
    g.addEdge(1, 2, 10);
    g.addEdge(1, 3, 15);
    g.addEdge(1, 6, 5);
    g.addEdge(2, 3, 7);
    g.addEdge(3, 4, 7);
    g.addEdge(3, 6, 10);
    g.addEdge(4, 5, 7);
    g.addEdge(6, 4, 5);
    g.addEdge(5, 6, 13);

    cout << g << endl;


//Ejercicio12
cout<<"Ejercicio12:"<<endl;
    recorrido_anchura(g,3);
    cout<<endl;
    return 0;
}

void recorrido_anchura(Graph x,int nodo) {
    // Crear una cola de tipo Vertex
    Cola<Vertex> q;

    // Marcar el nodo raíz
    int raiz = 1;
    map<int, bool> mark;
    mark[raiz] = true;

    // Agregar el nodo raíz a la cola
    q.agregar(*x.getVertex(raiz));

    // Mientras la cola no esté vacía
    while (!q.estaVacia()) {
        // Obtener el primer elemento de la cola
        Vertex st = q.frente();
        q.avanzar();

        // Si el nodo actual es igual al nodo buscado
        if (st.id == nodo) {
            printf("'%d'n", nodo);
            return;
        } else {
            // Imprimir el nodo actual
            printf("%d ", st.id);

            // Obtener el tamaño de los nodos vecinos
            int T = (int)st.getConnections().size();
            for (int i = 0; i < T; ++i) {
                // Si el nodo vecino no está marcado
                if (!mark[st.getConnections()[i]]) {
                    // Marcar el nodo vecino y agregarlo a la cola
                    mark[st.getConnections()[i]] = true;
                    q.agregar(*x.getVertex(st.getConnections()[i]));
                }
            }
        }
    }
}
