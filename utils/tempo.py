# Classe temporizador para medir tempo de execução
import time

class Temporizador:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def iniciar(self):
        self.inicio = time.time()

    def parar(self):
        self.fim = time.time()

    def tempo_decorrido(self) -> float:
        if self.inicio is not None and self.fim is not None:
            return self.fim - self.inicio
        return 0.0

    def imprimir_tempo(self):
        print(f"Tempo decorrido: {self.tempo_decorrido():.6f} segundos")
