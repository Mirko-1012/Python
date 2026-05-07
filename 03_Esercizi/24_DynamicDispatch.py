class Avviamento:
    def start(self):
        print("Il motore si avvia")

class AvviamentoElettrico:
    def start(self):
        print("Il motore si avvia elettricamente")

class AvviamentoStrappo:
    def start(self):
        print("Il motore si avvia a strappo")

def partenza(entita):
    entita.start()


a1 = Avviamento()
a2 = AvviamentoElettrico()
a3 = AvviamentoStrappo()

partenza(a1)
partenza(a2)
partenza(a3)