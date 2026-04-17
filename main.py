#1-misol
class Kitob:
    def __init__(self, nomi, muallifi, sahifa_soni):
        self.nomi = nomi
        self.muallifi = muallifi
        self.sahifa_soni = sahifa_soni

        def info(self):
            print(self.nomi, self.muallifi, self.sahifa)

        Kitob("O‘tkan kunlar", "Abdulla Qodiriy", 300)
        Kitob("Alkimyogar", "Paulo Coelho", 200)

  # 2
class Mashina:
    def __init__(self, nomi, rang, yil):
        self.nomi = nomi
        self.rang = rang
        self.yil = yil

    def info(self):
        print(self.nomi, self.rang, self.yil)

m1 = Mashina("Cobalt", "oq", 2022)
m1.info()

# 3
class Telefon:
    def __init__(self, model, narx, xotira):
        self.model = model
        self.narx = narx
        self.xotira = xotira

    def info(self):
        print(self.model, self.narx, self.xotira)

t = Telefon("iPhone", 1000, "128GB")
t.info()


# 4
class Oqituvchi:
    def __init__(self, ism, fan, tajriba):
        self.ism = ism
        self.fan = fan
        self.tajriba = tajriba

    def info(self):
        print(self.ism, self.fan, self.tajriba)

o = Oqituvchi("Dilshod", "Matematika", 10)
o.info()

# 5
class Hayvon:
    def __init__(self, nomi, turi, yoshi):
        self.nomi = nomi
        self.turi = turi
        self.yoshi = yoshi

    def info(self):
        print(self.nomi, self.turi, self.yoshi)

h = Hayvon("Rex", "it", 5)
h.info()


# 6
class Kompyuter:
    def __init__(self, model, protsessor, ram):
        self.model = model
        self.protsessor = protsessor
        self.ram = ram

    def info(self):
        print(self.model, self.protsessor, self.ram)

k = Kompyuter("HP", "i5", "8GB")
k.info()


# 7
class Film:
    def __init__(self, nomi, janr, yil):
        self.nomi = nomi
        self.janr = janr
        self.yil = yil

    def info(self):
        print(self.nomi, self.janr, self.yil)

f = Film("Avatar", "fantastika", 2009)
f.info()


# 8
class Sportchi:
    def __init__(self, ism, sport, yosh):
        self.ism = ism
        self.sport = sport
        self.yosh = yosh

    def info(self):
        print(self.ism, self.sport, self.yosh)

s = Sportchi("Jasur", "futbol", 25)
s.info()


# 9
class Shahar:
    def __init__(self, nomi, aholi, davlat):
        self.nomi = nomi
        self.aholi = aholi
        self.davlat = davlat

    def info(self):
        print(self.nomi, self.aholi, self.davlat)

sh = Shahar("Toshkent", 3000000, "Uzbekistan")
sh.info()


# 10
class Dars:
    def __init__(self, nomi, vaqt, xona):
        self.nomi = nomi
        self.vaqt = vaqt
        self.xona = xona

    def info(self):
        print(self.nomi, self.vaqt, self.xona)

d = Dars("Python", "10:00", "101-xona")
d.info()
