class SistemaStreaming:
    def __init__(self):
        self.catalogo_filmes = ["Filme 1", "Filme 2", "Filme 3"]
        self.catalogo_series = ["Série 1", "Série 2", "Série 3"]

    def exibir_menu(self):
        print("\nBem-vindo ao Sistema de Streaming de Vídeo!")
        print("1. Filmes Disponíveis")
        print("2. Séries Disponíveis")
        print("3. Sair")

    def exibir_catalogo(self, tipo):
        if tipo == "filmes":
            print("\nFilmes Disponíveis:")
            for filme in self.catalogo_filmes:
                print("-", filme)
        elif tipo == "series":
            print("\nSéries Disponíveis:")
            for serie in self.catalogo_series:
                print("-", serie)

    def iniciar_streaming(self):
        while True:
            self.exibir_menu()
            escolha = input("Escolha uma opção (1-3): ")

            if escolha == "1":
                self.exibir_catalogo("filmes")
            elif escolha == "2":
                self.exibir_catalogo("series")
            elif escolha == "3":
                print("Obrigado por usar nosso Sistema de Streaming. Até mais!")
                break
            else:
                print("Opção inválida. Por favor, escolha novamente.")

if __name__ == "__main__":
    sistema = SistemaStreaming()
    sistema.iniciar_streaming()
