class Paciente:
    def __init__(self, id_paciente, nome, dor):
        self.id = id_paciente
        self.nome = nome
        self.dor = dor  

    def __repr__(self):
        return f"{self.nome} (Dor: {self.dor})"


class TriagemProntoSocorro:
    def __init__(self):
        self.heap = [] 
        self.posicao_paciente = {}  

    def _subir(self, i):
        while i > 0:
            pai = (i - 1) // 2
            if self.heap[i].dor > self.heap[pai].dor:
                # Atualiza as posições no dicionário
                self.posicao_paciente[self.heap[i].id] = pai
                self.posicao_paciente[self.heap[pai].id] = i
                self.heap[i], self.heap[pai] = self.heap[pai], self.heap[i]
                i = pai
            else:
                break

    def _descer(self, i):
        n = len(self.heap)
        while 2 * i + 1 < n:
            filho_esquerdo = 2 * i + 1
            filho_direito = 2 * i + 2
            maior = filho_esquerdo

            if filho_direito < n and self.heap[filho_direito].dor > self.heap[filho_esquerdo].dor:
                maior = filho_direito

            if self.heap[maior].dor > self.heap[i].dor:
                self.posicao_paciente[self.heap[i].id] = maior
                self.posicao_paciente[self.heap[maior].id] = i
                # Troca os elementos de lugar
                self.heap[i], self.heap[maior] = self.heap[maior], self.heap[i]
                i = maior
            else:
                break

    def adicionar_paciente(self, id_paciente, nome, dor):
        """Insere um novo paciente no Max-Heap."""
        novo_paciente = Paciente(id_paciente, nome, dor)
        self.heap.append(novo_paciente)
        idx = len(self.heap) - 1
        self.posicao_paciente[id_paciente] = idx
        self._subir(idx)
        print(f"⁺ {nome} deu entrada com nível de dor {dor}.")

    def atender_proximo(self):
        if not self.heap:
            print("Nenhum paciente na fila.")
            return None
        
        raiz = self.heap[0]
        ultimo = self.heap.pop()
        
        del self.posicao_paciente[raiz.id]
        
        if self.heap:
            self.heap[0] = ultimo
            self.posicao_paciente[ultimo.id] = 0
            self._descer(0)
            
        print(f"🩺 Atendendo agora: {raiz.nome} (Nível de dor: {raiz.dor})")
        return raiz

    def alterar_prioridade(self, id_paciente, nova_dor):
        """Ajusta a prioridade (dor) de um paciente já na fila."""
        if id_paciente not in self.posicao_paciente:
            print("Paciente não encontrado na fila.")
            return

        idx = self.posicao_paciente[id_paciente]
        dor_antiga = self.heap[idx].dor
        self.heap[idx].dor = nova_dor

        print(f"⚡ Atualizando dor de {self.heap[idx].nome}: {dor_antiga} -> {nova_dor}")

        if nova_dor > dor_antiga:
            self._subir(idx)
        elif nova_dor < dor_antiga:
            self._descer(idx)

    def exibir_fila(self):
        print(f"Fila atual (Visualização do Heap): {self.heap}")


if __name__ == "__main__":
    pronto_socorro = TriagemProntoSocorro()

    print("--- 1. Entrada de Pacientes ---")
    pronto_socorro.adicionar_paciente(101, "Alice", 4)
    pronto_socorro.adicionar_paciente(102, "Bob", 8)
    pronto_socorro.adicionar_paciente(103, "Carlos", 5)
    pronto_socorro.adicionar_paciente(104, "Diana", 9)
    
    pronto_socorro.exibir_fila()
    print("\n--- 2. Alteração de Prioridade (Meta do Exercício) ---")
    
    pronto_socorro.alterar_prioridade(103, 10)
    
    pronto_socorro.alterar_prioridade(102, 3)

    pronto_socorro.exibir_fila()
    print("\n--- 3. Processando os Atendimentos por Prioridade ---")
    pronto_socorro.atender_proximo()
    pronto_socorro.atender_proximo()
    pronto_socorro.atender_proximo()
    pronto_socorro.atender_proximo()