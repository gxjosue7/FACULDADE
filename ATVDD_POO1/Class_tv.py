class TV:
    def __init__(self, canal=1, volume=10):
        self.canal_min = 1
        self.canal_max = 100
        self.volume_min = 0
        self.volume_max = 50

        self.canal = canal
        self.volume = volume

    def mudar_canal(self, novo_canal):
        if self.canal_min <= novo_canal <= self.canal_max:
            self.canal = novo_canal
            print(f"Canal alterado para {self.canal}")
        else:
            print("Canal inválido!")

    def aumentar_volume(self):
        if self.volume < self.volume_max:
            self.volume += 1
            print(f"Volume: {self.volume}")
        else:
            print("Volume já está no máximo!")

    def diminuir_volume(self):
        if self.volume > self.volume_min:
            self.volume -= 1
            print(f"Volume: {self.volume}")
        else:
            print("Volume já está no mínimo!")

    def mostrar_status(self):
        print(f"Canal atual: {self.canal} | Volume: {self.volume}")

tv = TV()

tv.mostrar_status()
tv.mudar_canal(10)
tv.aumentar_volume()
tv.aumentar_volume()
tv.diminuir_volume()
tv.mostrar_status()