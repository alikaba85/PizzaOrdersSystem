import csv
import datetime
import locale
locale.getpreferredencoding()


# Pizza İçin Base Sınıf Oluşturuyoruz

class Pizza:
    def __init__(self,price,comment):
        self.price = price #fiyat
        self.comment = comment # açıklama
    def get_cost(self):
        return self.price
    def get_description(self):
        return self.comment

#Pizza Seçimi İçin Alt Sınıflar Oluşturuyoruz

class Klasik(Pizza):
    def __init__(self):
        self.price = 90
        self.comment = "Klasik Pizza : Klasik Pizza: Domates, Mozzarella ve tabii ki Fesleğen"


class Margherita(Pizza):
    def __init__(self):
        self.price = 100
        self.comment = "Margherita : Domates, Mozarella, Fesleğen, Zeytinyağı ve Tuz"

class Sade(Pizza):
    def __init__(self):
        self.price = 85
        self.comment = "Sade Pizza  : Kaşar Peyniri, Mozzarella Peyniri, Kırmızı Biber, Domates, Mantar, Siyah Zeytin, Sosis, Sucuk, Tane Mısır ve Kekik"


class Turk(Pizza):
    def __init__(self):
        self.pricet = 79
        self.comment = "Türk Pizza: Domates, Mozzarella, Sucuk,Salam,Sosis,Zeytin"


class Dominos(Pizza):
    def __init__(self):
        self.price = 145
        self.comment = "Dominos Pizza: Domates, Kaşar Peyniri, Mozzarella Peyniri, Kırmızı Biber, Domates, Mantar, Siyah Zeytin, Sosis, Sucuk, Tane Mısır ve Kekik Fesleğen "

class Perfecto(Pizza):
    def __init__(self):
        self.price = 89
        self.comment = "Perfecto Pizza: Domates, Keçi Peyniri,Salam,Sosis,Brokoli"


#Sos ve Diğer Malzemeler İçin Base Sınıf Oluşturuyoruz


class Decorator(Pizza):
    def __init__(self, price, comment):
        Pizza.__init__(price, comment)

    def get_cost(self):
        return Pizza.get_cost(self)

    def get_description(self):
        return Pizza.get_description(self)

#Sos ve Diğer Malzemeler İçin Alt Sınıfları Oluşturuyoruz

class Zeytin(Decorator):
    def __init__(self):
        self.price = 8.25
        self.comment = " Zeytin "

class Mantar(Decorator):
    def __init__(self):
        self.price = 4.35
        self.comment = " Mantar "

class Keci_Peyniri(Decorator):
    def __init__(self):
        self.price = 6.50
        self.comment = " Keçi Peyniri "


class Et(Decorator):
    def __init__(self):
        self.price = 7.50
        self.comment = " Et "


class Onion(Decorator):
    def __init__(self):
        self.price = 3.75
        self.comment = " Soğan "

class Corn(Decorator):
    def __init__(self):
        self.price = 3.95
        self.comment = " Mısır "


class Pastirma(Decorator):
    def __init__(self):
        self.price = 12.75
        self.comment = " Pastırma "


class Sucuk(Decorator):
    def __init__(self):
        self.price = 9.75
        self.comment = " Sucuk "


class Mozzarella(Decorator):
    def __init__(self):
        self.price = 12.25
        self.comment = " Mozzarella"


class Brokoli(Decorator):
    def __init__(self):
        self.price = 8.50
        self.comment = " Brokoli "


class Kekik(Decorator):
    def __init__(self):
        self.price = 1.50
        self.comment = " Kekik "


class Tuz(Decorator):
    def __init__(self):
        self.price = 0.75
        self.comment = " Tuz "

# Main Fonksiyonu İle Programımızı İşleyişini Yazıyoruz
def Main():
    f = open('menu.txt', "r") #menümüzü listeliyoruz
    print(f.read())
    #pizza seçiyoruz
    p_sec = input("Lütfen Pizza Seçiniz: ")
    if p_sec == "1":
        my_p = Klasik()

    elif p_sec == "2":
        my_p = Margherita()

    elif p_sec == "3":
        my_p = Sade()

    elif p_sec == "4":
        my_p = Turk()

    elif p_sec == "5":
        my_p = Dominos()

    elif p_sec == "6":
        my_p = Pastirma()

    else:
        print("Hatalı İşlem....")
    #sos seçiyoruz
    s_sec = input("Sos Seçininiz: (Onay İçin 0 Basınız :) ")
    if s_sec == "11":
        sosum = Zeytin()

    elif s_sec == "12":
        sosum = Mantar()

    elif s_sec == "13":
        sosum = Keci_Peyniri()

    elif s_sec == "14":
        sosum = Et()

    elif s_sec == "15":
        sosum = Onion()

    elif s_sec == "16":
        sosum = Corn()

    elif s_sec == "17":
        sosum = Pastirma()

    elif s_sec == "18":
        sosum = Sucuk()

    elif s_sec == "19":
        sosum = Mozzarella()

    elif s_sec == "20":
        sosum = Brokoli()

    elif s_sec == "21":
        sosum = Kekik()

    elif s_sec == "22":
        sosum = Tuz()

    else:
        print("Sos Yok")


    #fiyat ve açıklamaları bir  birine bağlıyoruz
    my_pirce = my_p.get_cost() + sosum.get_cost()
    price_comment = my_p.get_description() + sosum.get_description()
    print(f"Açıklama : {price_comment} " + f"Tutar : {my_pirce}" + "TL")
    print("\n")

    #müşteri bilgilerini giriyoruz
    print("---------Müşteri ve Sipariş Bilgileeri--------")

    name = input("İsminiz: ")
    TcNO = input("Tc Kimlik Numaranız: ")
    credit_cards = input("Kredi Kartı Numaranız: ")
    card_paswd = input("Kart Şifresniz: ")
    tarih = datetime.datetime.now()

    print("Siparişiniz Onaylandı....\n")


    #verilerimizi orders dosyamıza aktarıyoruz
    with open('data_orders.csv', mode="a") as data:
        data = csv.writer(data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        data.writerow([name, TcNO, credit_cards, card_paswd, price_comment, my_pirce, tarih])




#main menümüzü çağırıyoruz
if __name__ == "__main__":
    Main()
