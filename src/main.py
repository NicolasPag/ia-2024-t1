"""Utilize este arquivo para depurar seus algoritmos."""

from graph import read_graph
from busca import a_star


if __name__ == "__main__":
    grafo = read_graph(r"C:\Users\nicol\OneDrive\Documentos\GitHub\.venv\ia-2024-t1\mapas\mini_map.txt")

    print(grafo)

    

    #vertices_avaliados, custo, caminho = a_star(grafo, 1, 100)
    #print(vertices_avaliados, custo, caminho)



