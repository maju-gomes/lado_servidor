class EntradaCinema:
    def __init__(self, dia, horario):
        self.__dia = dia
        self.__horario = horario

    def entradaNormal(self, dia, horario):
        entrada = 0

        if dia == "segunda" or dia == "terça" or dia == "quarta":
            entrada += 16

        elif dia == "sexta" or dia == "sábado" or dia == "domingo":
            entrada += 20

        else:
            entrada = 8

        if horario >= 17 and horario <= 24:
            entrada = entrada + entrada * 1/2

        entrada = entrada + entrada * 1/2
    def meiaEntrada(self, dia, horario):
        entrada = 0

        if dia == "segunda" or dia == "terça" or dia == "quarta":
            entrada += 16

        elif dia == "sexta" or dia == "sábado" or dia == "domingo":
            entrada += 20

        else:
            entrada = 8

        if horario >= 17 and horario <= 24:
            entrada = entrada + entrada * 1/2

        entrada = entrada/2
        





   

