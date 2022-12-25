from calendar import c


class Hayvan():

    def __init__(self, isim, cins, yas, agirlik, beslenme_sekli):
        self.isim = isim
        self.cins = cins
        self.yas = yas
        self.agirlik = agirlik
        self.beslenme_sekli = beslenme_sekli

class Dinazor(Hayvan):
    def __init__(self, isim, cins, yas, agirlik, beslenme_sekli, alt_tur):
        super().__init__(isim, cins, yas, agirlik, beslenme_sekli)
        self.alt_tur = alt_tur
    
    def abc(self):

        print("Hayvan İsmi: {}".format(self.isim))
        print("Hayvan Cismi: {}".format(self.cins))
        print("Hayvan Yaşı: {}".format(self.yas))
        print("Hayvan Ağırlığı: {}".format(self.agirlik))
        print("Beslenme Şekli: {}".format(self.beslenme_sekli))
        print("Alt türü: {}".format(self.alt_tur))
        print("\n-------------------------\n")

class Orkinos(Hayvan):
    def __init__(self, isim, cins, yas, agirlik, beslenme_sekli, alt_tur):
        super().__init__(isim, cins, yas, agirlik, beslenme_sekli)
        self.alt_tur = alt_tur
    
    def abc(self):

        print("Hayvan İsmi: {}".format(self.isim))
        print("Hayvan Cismi: {}".format(self.cins))
        print("Hayvan Yaşı: {}".format(self.yas))
        print("Hayvan Ağırlığı: {}".format(self.agirlik))
        print("Beslenme Şekli: {}".format(self.beslenme_sekli))
        print("Alt türü: {}".format(self.alt_tur))
        print("\n-------------------------\n")

class Kartal(Hayvan):
    def __init__(self, isim, cins, yas, agirlik, beslenme_sekli, alt_tur):
        super().__init__(isim, cins, yas, agirlik, beslenme_sekli)
        self.alt_tur = alt_tur
    
    def abc(self):

        print("Hayvan İsmi: {}".format(self.isim))
        print("Hayvan Cismi: {}".format(self.cins))
        print("Hayvan Yaşı: {}".format(self.yas))
        print("Hayvan Ağırlığı: {}".format(self.agirlik))
        print("Beslenme Şekli: {}".format(self.beslenme_sekli))
        print("Alt türü: {}".format(self.alt_tur))
        print("\n-------------------------\n")
        
class Ceylan(Hayvan):
    def __init__(self, isim, cins, yas, agirlik, beslenme_sekli, alt_tur):
        super().__init__(isim, cins, yas, agirlik, beslenme_sekli)
        self.alt_tur = alt_tur
    
    def abc(self):

        print("Hayvan İsmi: {}".format(self.isim))
        print("Hayvan Cismi: {}".format(self.cins))
        print("Hayvan Yaşı: {}".format(self.yas))
        print("Hayvan Ağırlığı: {}".format(self.agirlik))
        print("Beslenme Şekli: {}".format(self.beslenme_sekli))
        print("Alt türü: {}".format(self.alt_tur))
        print("\n-------------------------\n")



Dinazor("Reis-ül Mumin", "Dinazor", "182", 1200, "Etçil","T-Rex").abc()
Dinazor("Mahmut-u Kel","Dinazor","99",12000,"Otçul","Supersaurus").abc()
Orkinos("Denizlerin Reisi","Orkinos","0,12",90,"Bilinmiyor","Atlantic Bluefin Tuna").abc()
Orkinos("Deniz Korsanı","Orkinos","0,18",120,"Bilinmiyor","Albacore").abc()
Kartal("Hava Limanı","Kartal","4",9,"Etçil","Altın Kafalı Kartal").abc()
Ceylan("Mazlum","Ceylan","8",110,"Otçul","Dağ Ceylanı").abc()