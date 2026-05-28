class Grafo:
    def __init__(self, vertices):
        self.V = vertices
        self.arestas = []

    def adicionar_aresta(self, u, v, w):
        self.arestas.append((u, v, w))

    def bellman_ford(self, origem, iteracoes_desejadas=3):
        distancia = [float('inf')] * self.V
        predecessor = [None] * self.V
        distancia[origem] = 0

        print("--- TABELA DE ITERAÇÕES (Distância / Predecessor) ---")
        
        self._imprimir_linha_tabela("Inicial", distancia, predecessor)

        for i in range(1, iteracoes_desejadas + 1):
            for u, v, w in self.arestas:
                if distancia[u] != float('inf') and distancia[u] + w < distancia[v]:
                    distancia[v] = distancia[u] + w
                    predecessor[v] = u
            
            self._imprimir_linha_tabela(f"Iteração {i}", distancia, predecessor)

        print("-" * 60)

        tem_ciclo_negativo = False
        for u, v, w in self.arestas:
            if distancia[u] != float('inf') and distancia[u] + w < distancia[v]:
                tem_ciclo_negativo = True
                break

        if tem_ciclo_negativo:
            print("⚠️ Resultado: Existe pelo menos um CICLO NEGATIVO no grafo!")
        else:
            print("✅ Resultado: NÃO existe ciclo negativo no grafo.")

    def _imprimir_linha_tabela(self, nome_passo, distancias, predecessores):
        linha = f"{nome_passo:<12} | "
        for v in range(self.V):
            dist = "∞" if distancias[v] == float('inf') else str(distancias[v])
            pred = "-" if predecessores[v] is None else str(predecessores[v])
            linha += f"V{v}: {dist}/{pred}   "
        print(linha)


if __name__ == "__main__":
    g = Grafo(5)

    g.adicionar_aresta(0, 1, 5)
    g.adicionar_aresta(1, 2, 1)
    g.adicionar_aresta(1, 3, 2)
    g.adicionar_aresta(2, 4, 1)
    g.adicionar_aresta(4, 3, -1)

    g.bellman_ford(origem=0, iteracoes_desejadas=3)