class Colibri:
    def __init__(self, especie, color, velocitat_vol, tamany, edat):
        """Constructor de la classe Colibrí."""
        self.__especie = especie
        self.__color = color
        self.__velocitat_vol = velocitat_vol
        self.__tamany = tamany
        self.__edat = edat

    # Getters
    def get_especie(self):
        return self.__especie

    def get_color(self):
        return self.__color

    def get_velocitat_vol(self):
        return self.__velocitat_vol

    def get_tamany(self):
        return self.__tamany

    def get_edat(self):
        return self.__edat

    # Setters
    def set_especie(self, especie):
        self.__especie = especie

    def set_color(self, color):
        self.__color = color

    def set_velocitat_vol(self, velocitat_vol):
        self.__velocitat_vol = velocitat_vol

    def set_tamany(self, tamany):
        self.__tamany = tamany

    def set_edat(self, edat):
        self.__edat = edat
