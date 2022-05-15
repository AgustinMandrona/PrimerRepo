class Cetaceo():
    def __init__(self, notas, viveEn, peso):
        self.notas=notas
        self.viveEn=viveEn
        self.peso=peso
    def nacer(self):
        pass
    def nadar(self):
        pass
    def describir(self):
        print(f"{self.notas}, vivo en el {self.viveEn} y peso {self.peso} kg")
class AnimalMarino(Cetaceo):
    def nadar(self):
        print("Si se nadar")
    def __init__(self, notas, viveEn, peso, tieneBranqueas, especie):
        Cetaceo.__init__(self, notas, viveEn, peso)
        self.tieneBranqueas=tieneBranqueas
        self.especie=especie
    def tipo(self):
        print(f"Soy un/a {self.especie} y {self.tieneBranqueas} tengo branqueas")
class Mamifero(Cetaceo):
    def nacer(self):
        print("Nazco en el mar")
    def __init__(self, notas, viveEn, peso, cantMamas, espezanzaDeVida):
        Cetaceo.__init__(self, notas, viveEn, peso)
        self.cantMamas=cantMamas
        self.esperanzaDeVida=espezanzaDeVida
    def mamar(self):
        return self.mamar
    def describir2(self):
        print(f"Tengo {self.cantMamas} mamas y una esperanza de vida de {self.esperanzaDeVida} años")
animal= AnimalMarino("Soy peligroso", "mar", 5000, "no", "ballena")
animal.tipo()
animal.describir()
animal.nadar()
animal=Mamifero("Soy peligroso", "mar", 5000, 10, 150)
animal.describir2()
animal.nacer()