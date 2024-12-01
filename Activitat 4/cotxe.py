class Cotxe:
    def __init__(self, marca, model, any_fabricacio, color, motor):
        self.__marca = marca
        self.__model = model
        self.__any_fabricacio = any_fabricacio
        self.__color = color
        self.__motor = motor


    def get_marca(self):
        return self.__marca

    def get_model(self):
        return self.__model

    def get_any_fabricacio(self):
        return self.__any_fabricacio

    def get_color(self):
        return self.__color

    def get_motor(self):
        return self.__motor

    

    def set_marca(self, marca):
        self.__marca = marca

    def set_model(self, model):
        self.__model = model

    def set_any_fabricacio(self, any_fabricacio):
        self.__any_fabricacio = any_fabricacio

    def set_color(self, color):
        self.__color = color

    def set_motor(self, motor):
        self.__motor = motor
