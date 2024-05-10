/*#include <iostream>
#include <fstream>

void mostrar_grafo(const std::vector<std::vector<int>>& grafo, const std::string& titulo) {
    std::ofstream archivo("grafo.dot");
    archivo << "digraph G {\n";

    // Agregar aristas al archivo DOT
    for (int vertice = 0; vertice < grafo.size(); ++vertice) {
        for (int vecino : grafo[vertice]) {
            archivo << vertice << " -> " << vecino << ";\n";
        }
    }

    archivo << "}\n";
    archivo.close();

    // Generar el archivo de imagen utilizando Graphviz
    std::string comando = "dot -Tpng grafo.dot -o grafo.png";
    system(comando.c_str());

    // Abrir la imagen generada
    comando = "xdg-open grafo.png";
    system(comando.c_str());
}*/