from cotxe import Cotxe
from colibri import Colibri

cotxe1 = Cotxe("Toyota", "Corolla", 2020, "Blau", "Híbrid")
cotxe2 = Cotxe("Ford", "Focus", 2018, "Negre", "Diesel")
cotxe3 = Cotxe("Tesla", "Model S", 2022, "Vermell", "Elèctric")


colibri1 = Colibri("Rubí", "Verd", 25, "Petit", 3)
colibri2 = Colibri("Anna", "Blau", 30, "Medià", 2)
colibri3 = Colibri("Jacobí", "Groc", 20, "Petit", 5)


print("Informació del cotxe 1:")
print("Marca:", cotxe1.get_marca())
print("Model:", cotxe1.get_model())
print("Any de fabricació:", cotxe1.get_any_fabricacio())


print("\nInformació del colibrí 1:")
print("Espècie:", colibri1.get_especie())
print("Color:", colibri1.get_color())
print("Velocitat de vol:", colibri1.get_velocitat_vol())
print("Tamany:", colibri1.get_tamany())


cotxe1.set_color("Blanc")
cotxe1.set_motor("Elèctric")


print("\nAtributs modificats del cotxe 1:")
print("Color:", cotxe1.get_color())
print("Motor:", cotxe1.get_motor())


colibri1.set_color("Vermell")
colibri1.set_velocitat_vol(28)


print("\nAtributs modificats del colibrí 1:")
print("Color:", colibri1.get_color())
print("Velocitat de vol:", colibri1.get_velocitat_vol())
