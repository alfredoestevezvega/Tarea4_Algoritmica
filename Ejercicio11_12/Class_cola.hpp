#include <iostream>
#include <vector>

template<typename TIPOELEM>
class Cola {
private:
    std::vector<TIPOELEM> items;

public:
    Cola() {}

    std::string toString() {
        std::string cadena;
        for (auto elemento : items) {
            cadena += std::to_string(elemento) + " ";
        }
        return cadena;
    }

    bool estaVacia() {
        return items.empty();
    }

    void agregar(TIPOELEM item) {
        items.insert(items.begin(), item);
    }

    TIPOELEM avanzar() {
        TIPOELEM valor = items.back();
        items.pop_back();
        return valor;
    }

    int tamano() {
        return items.size();
    }

    TIPOELEM frente() {
        return items.back();
    }

    TIPOELEM ultimo() {
        if (!items.empty()) {
            return items.front();
        }
    }
};
