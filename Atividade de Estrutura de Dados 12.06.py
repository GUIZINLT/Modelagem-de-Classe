# Atividade de Estrutura de Dados 

class Vertice:
    def __init__(self, valor):
        self.valor = valor
        self.vizinhos = set()

class Grafo:
    def __init__(self):
        self.vertices = {}

    def adicionar_vertice(self, valor):
        if valor not in self.vertices:
            self.vertices[valor] = Vertice(valor)
            print(f"Vértice {valor} adicionado.")
        else:
            print(f"Vértice {valor} já existe.")

    def adicionar_aresta(self, valor_origem, valor_destino):
        if valor_origem in self.vertices and valor_destino in self.vertices:
            vertice_origem = self.vertices[valor_origem]
            vertice_destino = self.vertices[valor_destino]
            
            vertice_origem.vizinhos.add(vertice_destino)
            vertice_destino.vizinhos.add(vertice_origem)
            print(f"Aresta conectando {valor_origem} e {valor_destino} adicionada.")
        else:
            print("Um ou ambos os vértices não foram encontrados.")

    def remover_vertice(self, valor):
        if valor in self.vertices:
            vertice_removido = self.vertices.pop(valor)
            for vizinho in vertice_removido.vizinhos:
                vizinho.vizinhos.remove(vertice_removido)
            print(f"Vértice {valor} e suas arestas foram removidos.")
        else:
            print(f"Vértice {valor} não encontrado para remoção.")

    def buscar(self, valor):
        return valor in self.vertices

    def exibir_grafo(self):
        if not self.vertices:
            print("O grafo está vazio.")
            return
            
        print("\n--- Estrutura do Grafo ---")
        for valor, vertice in self.vertices.items():
            vizinhos_str = ', '.join(str(v.valor) for v in vertice.vizinhos) or "Nenhum"
            print(f"Vértice {valor} -> [ {vizinhos_str} ]")
        print("--------------------------")

def menu():
    grafo = Grafo()
    while True:
        print("\n--- Menu de Opções ---")
        print("1. Adicionar Vértice")
        print("2. Adicionar Aresta (Conexão)")
        print("3. Remover Vértice")
        print("4. Buscar Vértice")
        print("5. Exibir Grafo")
        print("6. Sair")
        
        opcao = input("Escolha uma Opção: ")

        if opcao == '1':
            valor = int(input("Digite o valor do vértice a ser inserido: "))
            grafo.adicionar_vertice(valor)
        
        elif opcao == '2':
            origem = int(input("Digite o vértice de origem: "))
            destino = int(input("Digite o vértice de destino: "))
            grafo.adicionar_aresta(origem, destino)

        elif opcao == '3':
            valor = int(input("Digite o valor do vértice a remover: "))
            grafo.remover_vertice(valor)

        elif opcao == '4':
            valor = int(input("Digite o valor do vértice a buscar: "))
            encontrado = grafo.buscar(valor)
            print("Encontrado!" if encontrado else " Não encontrado.")
        
        elif opcao == '5':
            grafo.exibir_grafo()
        
        elif opcao == '6':
            print("Saindo...")
            break
            
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()