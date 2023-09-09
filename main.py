import os
from time import sleep
import shutil
import datetime

def take_time():
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = str(now.hour) + ":" + str(now.minute)
    date = str(day) + "/" + str(month) + "/" + str(year) + " - " + hour
    return date

def clear_console():  # I have used this too much so I have decided to write a function is better
    return os.system('cls' if os.name == 'nt' else 'clear')


def good_print(i, string, count): # I have also used this too much so I have decided to write a function again

    a = count - len(i[string])
    print(" " * a, end="")
    print("|", end="")


def critical_level(i):
    if i["patient_count"] != 0:
        if int(i["amount"]) < 100 or int(i["amount"])/int(i["patient_count"])*100 < 10:
            print("\033[31m" + "\n   KRİTİK SEVİYE EN KISA SÜREDE YENİ İLAÇ TEMİN EDİLMESİ GEREKİYOR"+ "\033[39m")
    else:
        print("\033[31m" + "\n {} ID'Lİ İLACI KULLANAN YOK ".format(i["id"]) + "\033[39m")


class HealthBase:
    def __init__(self, idd, password):
        self.idd = idd
        self.password = password
        self.data = []
        self.main_window()

    def main_window(self):
        self.data_adjusting()
        while True:
            clear_console()
            print("\n\n   HealthBase | İlaç Envanter Otomasyonu - Personel : {} -".format(self.idd))
            print("\n\n     1) Mevcut İlaçları görüntüle")
            print("\n     2) ID ile ilaç ara")
            print("\n     3) İlaç üreticisi ara")
            print("\n     4) İlaç ara")
            print("\n     5) İlaç temin et")
            print("\n     6) İlaç sat/at")
            print("\n     7) Yeni ilaç kaydı")
            print("\n     8) Hasta işlemleri")
            print("\n     9) Personel ayarları")
            print("\n     G) Giriş menüsüne geri dön")
            print("\n     Q) Çıkış")
            secim = input("\n\n      Seçim = ")

            if secim == "1":
                self.show_data()
            elif secim == "2":
                self.find_medicine_by_ID()
            elif secim == "3":
                self.find_company()
            elif secim == "4":
                self.find_medicine()
            elif secim == "5":
                self.buy_medicine()
            elif secim == "6":
                self.sell_remove_medicine()
            elif secim == "7":
                self.new_medicine()
            elif secim == "8":
                self.patient_system()
            elif secim == "9":
                self.personel_settings()
            elif secim == "G" or secim == "g":
                main()
            elif secim == "Q" or secim == "q":
                quit()

        
    def data_adjusting(self):
        try:
            self.data_file = open('2439230.txt', "r+", encoding="utf-16")

        except FileNotFoundError:
            clear_console()
            print("\033[31m"+"\n\n      Güvenlik açığı tespit edildi. uygulamadan "
                             "çıkışınız verilmiştir. "+"\033[39m"+"\n\n")
            quit()

        for self.i in self.data_file:
            self.i = self.i[:-1]
            self.gecici = self.i.split(",")
            self.data_ids = self.gecici[0]
            self.company = self.gecici[1]
            self.medicine = self.gecici[2]
            self.amount = self.gecici[3]
            self.patient_count = self.gecici[4]

            datum = {"id": self.data_ids,
                     "company": self.company,
                     "medicine": self.medicine,
                     "amount": self.amount,
                     "patient_count": self.patient_count}
            self.data.append(datum)

    def show_data(self):
        clear_console()
        print("\n\n    HealthBase  |  İlaç Envanter Otomasyonu - Mevcut İlaçları görüntüle")
        print("\n\n|    ID     |          İlaç Üretici           |                İlaç Ad             "
              "|    Sayı     |  Hasta Sayısı |")
        print("\n  ---------------------------------------------------------------------------"
              "-------------------------------------")

        for i in self.data:
            print("|"+" " * 2, i["id"], end="")
            good_print(i, "id", 8)
            print(" " * 2, i["company"], end="")
            good_print(i, "company", 30)
            print(" " * 2, i["medicine"], end="")
            good_print(i, "medicine", 33)
            if int(i["amount"]) > 10**11:
                a = int(i["amount"])//10**14
                print(str(a)+" * 10^14", end="")
                b = 5 - len(str(a))
                print(" " * b, end="")
                print("|", end="")
            else:
                print(" " * 2, i["amount"], end="")
                good_print(i, "amount", 10)
            print(" " * 2, i["patient_count"], end="")
            good_print(i, "patient_count", 12)

            print("\n")


        while True:
            a = input("\033[92m"+"\n\n    Geri dönmek için a'ya basınız. "+"\033[39m")
            if a == "a":
                clear_console()
                break
            else:
                continue

    def find_medicine_by_ID(self):
        while True:
            clear_console()
            print("\n\n    HealthBase  |  İlaç Envanter Otomasyonu - İlaç Ara(ID)")
            try:
                iddd = int(input("\nAranacak ID'yi girin: "))
            except ValueError:

                a = input("\033[31m" + "\n\n      ID olarak INT değerler giriniz. (Geri dönmek için herhangi bir tuşa,"
                                       "\n      tekrar denemek için T' harfine basınız) \n\n" + "\033[39m")
                if a == "t" or a == "T":
                    continue
                break
            index = -1
            control = False
            for i in self.data:
                index += 1
                if str(iddd) == i["id"]:
                    control = True
                    break
            if control:
                clear_console()
                a = self.data[index]
                print("\n\n    HealthBase  |  İlaç Envanter Otomasyonu - İlaç Ara(ID)")
                print("""


                    ID                            |  {}

                   ------------------------------------------------------------------

                    İlaç Üreticisi                |  {}

                   ------------------------------------------------------------------

                    İlaç Adı                      |  {}

                   ------------------------------------------------------------------

                    Stok                          |  {}

                   ------------------------------------------------------------------

                    Kullanan Hasta Sayısı         |  {}

                   ------------------------------------------------------------------

                                """.format(a["id"], a["company"], a["medicine"], a["amount"], a["patient_count"]))

                a = input(
                    "\033[92m" + "\n\n      Geri dönmek için herhangi bir tuşa, yeni arama için T' "
                                 "harfine basınız " + "\033[39m")
                if a == "T" or a == "t":
                    continue
                else:
                    break

            else:
                print("\033[31m"+"\n   ARAMA BAŞARISIZ GİRMİŞ OLDUĞUNUZ ID'E SAHİP BİR ÜRÜN BULUNMAMAKTADIR"+"\033[39m")
                a = input("\033[92m"+"\n\n      Geri dönmek için herhangi bir tuşa, yeni arama için T' harfine basınız "
                                     "var olan ürün listesini görmek için A'ya basın "+"\033[39m")
                if a == "T" or a == "t":
                    continue
                elif a == "A" or a == "a":
                    self.show_data()
                else:
                    break

    def find_company(self):
        while True:
            clear_console()
            print("\n\n    HealthBase  |  İlaç Envanter Otomasyonu - İlaç Üreticisi Ara")
            medicine_list = []
            a = input("Aranacak İlaç üreticisinin ismini girin: ")
            for i in self.data:
                if i["company"] == a:
                    medicine_list.append((i["medicine"], i["amount"], i["patient_count"]))
            if len(medicine_list) == 0:
                print("\033[31m"+"\n   ARAMA BAŞARISIZ GİRMİŞ OLDUĞUNUZ {} ÜRETİCİSİNE AİT BİR "
                                 "ÜRÜN BULUNMAMAKTADIR".format(a)+"\033[39m")
                a = input(
                    "\033[92m" + "\n\n      Geri dönmek için herhangi bir tuşa, yeni arama için T' "
                                 "harfine basınız var olan ürün listesini görmek için A'ya basın " + "\033[39m")
                if a == "T" or a == "t":
                    clear_console()
                    continue
                elif a == "A" or a == "a":
                    self.show_data()
                else:
                    break

            else:
                print(a)
                print("--------------------\n")
                num = 1
                for m, a, p in medicine_list:
                   print("{}) {} adlı ilaçtan {} kadar kaldı ve bu ilacı {} kişi kullanıyor.".format(str(num), m, a, p))
                   num += 1

                b = input(
                    "\033[92m" + "\n\n      Geri dönmek için herhangi bir tuşa, yeni arama için "
                                 "T' harfine basınız " + "\033[39m")
                if b == "T" or b == "t":
                    continue
                else:
                    break

    def find_medicine(self):
        while True:
            clear_console()
            print("\n\n    HealthBase  |  İlaç Envanter Otomasyonu - İlaç Ara")
            company_list = []
            a = input("Aranacak İlacın ismini girin: ")
            for i in self.data:
                if i["medicine"] == a:
                    company_list.append((i["company"]))
            if len(company_list) == 0:
                print(
                    "\033[31m" + "\n   ARAMA BAŞARISIZ GİRMİŞ OLDUĞUNUZ {} İLACA AİT BİR ÜRÜN BULUNMAMAKTADIR".format(
                        a) + "\033[39m")
                a = input(
                    "\033[92m" + "\n\n      Geri dönmek için herhangi bir tuşa, yeni arama için T "
                                 "harfine basınız var olan ürün listesini görmek için A'ya basın " + "\033[39m")
                if a == "T" or a == "t":
                    continue
                elif a == "A" or a == "a":
                    self.show_data()
                else:
                    break

            else:
                print(a)
                print("--------------------\n")
                num = 1
                for c in company_list:
                    print(
                        "{}) {} adlı ilacı {} şirketi üretiyor".format(str(num), a, c))
                    num += 1

                b = input(
                    "\033[92m" + "\n\n      Geri dönmek için herhangi bir tuşa, yeni "
                                 "arama için T' harfine basınız " + "\033[39m")
                if b == "T" or b == "t":
                    continue
                else:
                    break

    def update_medicine(self):
        shutil.copy2("2439230.txt", "log_dir/ilaç_veri_eski")
        try:
            filed = open("2439230.txt", "w", encoding="utf-16")
        except FileNotFoundError:
            clear_console()
            print("\033[31m"+"\n\n      Güvenlik açığı tespit edildi. "
                             "Uygulamadan çıkışınız verilmiştir. "+"\033[39m"+"\n\n")
            quit()

        for i in self.data:
            filed.write(i["id"])
            filed.write(",")
            filed.write(i["company"])
            filed.write(",")
            filed.write(i["medicine"])
            filed.write(",")
            filed.write(i["amount"])
            filed.write(",")
            filed.write(i["patient_count"])
            filed.write("\n")
        filed.close()
        self.data_adjusting()

    def buy_medicine(self):
        while True:
            clear_console()
            print("\n\n    HealthBase  |  İlaç Envanter Otomasyonu - İlaç Temin Et")
            try:
                iddd = int(input("\n\n     Temin etmek istediğiniz ilaç ID = "))
            except ValueError:
                a = input(
                    "\033[31m" + "\n\n      ID olarak INT değerler giriniz. (Geri dönmek için herhangi bir tuşa,"
                                 "\n      tekrar denemek için T' harfine basınız) " + "\033[39m")
                if a == "t" or a == "T":
                    continue
                break

            index = -1
            control = False
            for i in self.data:
                index += 1
                if str(iddd) == i["id"]:
                    control = True
                    break
            if control:
                clear_console()
                a = self.data[index]   # a ilgili ürünü bulunduran bir sözlüğümüz var ilaç
                # temini olduğundan amountu güncelleyip updatei çağırıcaz
                try:
                    how_many_to_buy = int(input("\n\n     KAÇ ADET İLAÇ TEMİN EDİLECEK "))
                except ValueError:
                    ah = input(
                        "\033[31m" + "\n\n      Değer olarak INT değerler giriniz. "
                                     "(Geri dönmek için herhangi bir tuşa,\n      tekrar denemek için "
                                     "T' harfine basınız) " + "\033[39m")
                    if ah == "t" or ah == "T":
                        continue
                    break
                if how_many_to_buy > 0:
                    amount = int(a["amount"])
                    amount += how_many_to_buy
                    a["amount"] = str(amount)
                    self.update_medicine()
                    clear_console()
                    print("\n\n    HealthBase  |  İlaç Envanter Otomasyonu - İlaç Temin Et")
                    print("\n\n    İstediğiniz ilaçtan {} adet temin edildi.".format(how_many_to_buy))
                    clear_console()
                    print("\n\n    HealthBase  |  İlaç Envanter Otomasyonu - İlaç Temin Et")
                    b = input(
                        "\033[92m" + "\n\n      Geri dönmek için herhangi bir tuşa, yeni arama için "
                                     "T harfine basınız " + "\033[39m")
                    if b == "T" or b == "t":
                        continue
                    else:
                        break

                else:
                    print("\033[31m" + "\n   GİRMİŞ OLDUĞUNUZ ADET NEGATİF SAYIDA EĞER DEVAM EDERSENİZ "
                                       "SATILMAK İSTENDİĞİ DÜŞÜNÜLÜP BUNA HAREKET HAREKET EDİLECEKTİR (STOKTA AZALMA)" +
                          "\033[39m")
                    ff = input("\033[31m" + "\n   EĞER - (EKSİ)'YE YANLIŞLIKLA BASTIYSANIZ P'YE, "
                                            "GERİ DÖNMEK İÇİN G'YE, İŞLEMİZ DOĞRUYSA"
                                       "C'YE BASIN " + "\033[39m")

                    if ff == "P" or ff == "p":
                        how_many_to_buy = -how_many_to_buy
                        amount = int(a["amount"])
                        amount += how_many_to_buy
                        a["amount"] = str(amount)
                        if int(a["amount"])<0:
                            a["amount"] = "0"
                        self.update_medicine()
                        clear_console()
                        print("\n\n    HealthBase  |  İlaç Envanter Otomasyonu - İlaç Temin Et")
                        print("\n\n    İstediğiniz ilaçtan {} adet temin edildi.".format(how_many_to_buy))
                        clear_console()
                        print("\n\n    HealthBase  |  İlaç Envanter Otomasyonu - İlaç Temin Et")
                        b = input(
                            "\033[92m" + "\n\n      Geri dönmek için herhangi bir tuşa, "
                                         "yeni arama için T' harfine basınız " + "\033[39m")
                        if b == "T" or b == "t":
                            continue
                        else:
                            break
                    elif ff == "C" or ff == "c":  # azaltma geldiğinde buraya sadece onu yazcam
                        amount = int(a["amount"])
                        amount += how_many_to_buy
                        a["amount"] = str(amount)
                        self.update_medicine()
                        clear_console()
                        print("\n\n    HealthBase  |  İlaç Envanter Otomasyonu - İlaç Temin Et")
                        print("\n\n    İlaçtan {} adet satıldı.".format(-how_many_to_buy))
                        critical_level(a)
                    else:
                        clear_console()
                        print("\n\n    HealthBase  |  İlaç Envanter Otomasyonu - İlaç Temin Et")
                        intte = input("Ana Menüye dönmek için a'ya devam etmek için c'ye basın.")
                        if intte == "A" or intte == "a":
                            break
                        else:
                            continue

            else:
                print(
                    "\033[31m" + "\n   ARAMA BAŞARISIZ GİRMİŞ OLDUĞUNUZ ID'YE SAHİP "
                                 "BİR ÜRÜN BULUNMAMAKTADIR" + "\033[39m")
                a = input(
                    "\033[92m" + "\n\n      Geri dönmek için herhangi bir tuşa, yeni arama için "
                                 "T' harfine basınız var olan ürün listesini görmek için A'ya basın " + "\033[39m")
                if a == "T" or a == "t":
                    continue
                elif a == "A" or a == "a":
                    self.show_data()
                else:
                    break

    def sell_remove_medicine(self):
        while True:
            clear_console()
            print("\n\n    HealthBase  |  İlaç Envanter Otomasyonu - İlaç Sat, İmha Et")
            try:
                iddd = int(input("\n\n     Satılacak ilaç ID = "))
            except ValueError:
                a = input(
                    "\033[31m" + "\n\n      ID olarak INT değerler giriniz. (Geri dönmek için herhangi bir tuşa,"
                                 "\n      tekrar denemek için T' harfine basınız) " + "\033[39m")
                if a == "t" or a == "T":
                    continue
                clear_console()
                break

            index = -1
            control = False
            for i in self.data:
                index += 1
                if str(iddd) == i["id"]:
                    control = True
                    break
            if control:
                clear_console()
                a = self.data[index]  # a ilgili ürünü bulunduran bir sözlüğümüz var ilaç
                # temini olduğundan amountu güncelleyip updatei çağırıcaz
                try:
                    how_many_to_buy = int(input("\n\n     KAÇ ADET İLAÇ SATILACAK "))
                    if how_many_to_buy<0:
                        print("\033[92m" + "\n\n NE YAZIKKİ BURADAKİ DEĞERLER DİNAMİK OLMAYIP"
                                           " SADECE ÇIKARMA YAPABİLİYORUZ " + "\033[39m")
                        aaa = input("\033[92m" + "\n\n EĞER ÇIKARMA İŞLEMİNE DEVAM ETMEK İSTİYORSANIZ "
                                                 "C'YE İŞLEMİ DURDURMAK İSTİYORSANIZ S'YE BASIN" + "\033[39m")
                        if aaa == "c" or aaa == "C":
                            how_many_to_buy = -how_many_to_buy
                        else:
                            break
                except ValueError:
                    ah = input(
                        "\033[31m" + "\n\n      Değer olarak INT değerler giriniz. "
                                     "(Geri dönmek için herhangi bir tuşa,\n      tekrar denemek için "
                                     "T' harfine basınız) " + "\033[39m")
                    if ah == "t" or ah == "T":
                        continue
                    break

                amount = int(a["amount"])
                amount -= how_many_to_buy
                a["amount"] = str(amount)
                if int(a["amount"]) < 0:
                    a["amount"] = "0"
                self.update_medicine()
                clear_console()
                print("\n\n    HealthBase  |  İlaç Envanter Otomasyonu - İlaç Sat yada İmha Et")
                print("\n\n    İstediğiniz ilaçtan {} adet ilaç satıldı/imha edildi.".format(how_many_to_buy))
                critical_level(a)
                clear_console()
                print("\n\n    HealthBase  |  İlaç Envanter Otomasyonu - İlaç Sat yada İmha Et")
                b = input(
                    "\033[92m" + "\n\n      Geri dönmek için herhangi bir tuşa, "
                                 "yeni arama için T' harfine basınız " + "\033[39m")
                if b == "T" or b == "t":
                    continue
                else:
                    break

            else:
                print(
                    "\033[31m" + "\n   ARAMA BAŞARISIZ GİRMİŞ OLDUĞUNUZ ID'YE SAHİP "
                                 "BİR ÜRÜN BULUNMAMAKTADIR" + "\033[39m")
                a = input(
                    "\033[92m" + "\n\n      Geri dönmek için herhangi bir tuşa, yeni arama için "
                                 "T' harfine basınız var olan ürün listesini görmek için A'ya basın " + "\033[39m")
                if a == "T" or a == "t":
                    continue
                elif a == "A" or a == "a":
                    self.show_data()
                else:
                    break

    def new_medicine(self):
        while True:
            clear_console()
            print("\n\n    HealthBase  |  İlaç Envanter Otomasyonu - Yeni İlaç Ekle")
            medicine = input("\n\n     Yeni ilaç adı (max: 23 harf, min: 4 harf) = ")
            if len(medicine) < 4 or len(medicine) > 23:
                a = input("\033[31m"+"\n\n     Yeni ilaç adı istenilen karekter uzunluğunda değil.\n      "
                                     "(Ana menüye dönmek için herhangi bir tuşa,\n      tekrar denemek için "
                                     "T' harfine basınız) = "+"\033[39m")
                if a == "t" or a == "T":
                    continue
                break
            else:
                company = input("\n\n     Yeni ilaç üreticisi (max: 27 harf, min: 5 harf) = ")
                if len(company) < 5 or len(company) > 27:
                    a = input("\033[31m"+"\n\n     Yeni ilaç adı türü istenilen karekter "
                                         "uzunluğunda değil.\n      (Ana menüye dönmek için herhangi bir tuşa,"
                                         "\n      tekrar denemek için T' harfine basınız) = "+"\033[39m")
                    if a == "t" or a == "T":
                        continue
                    break
                else:
                    try:
                        medicine_count = int(input("\n\n     Yeni ilacın adeti (Tek seferde "
                                                   "2000 ilaç ekleyebilirsiniz.) = "))
                    except ValueError:  # adet int kontolü
                        a = input("\033[31m"+"\n\n      Adet olarak INT değerler giriniz. "
                                             "(Geri dönmek için herhangi bir tuşa,\n      "
                                             "tekrar denemek için T' harfine basınız) "+"\033[39m")
                        if a == "t" or a == "T":
                            continue
                        break
                    if medicine_count <= 0 or medicine_count > 2000:
                        a = input("\033[31m"+"\n\n     Yeni ilacın adedi istenilen aralıkta değil.\n      "
                                             "(Ana menüye dönmek için herhangi bir tuşa,\n      "
                                             "tekrar denemek için T' harfine basınız) = "+"\033[39m")
                        if a == "t" or a == "T":
                            continue
                        break
                    else:
                        datum = {"id": str(len(self.data)),
                                 "company": company,
                                 "medicine": medicine,
                                 "amount": str(medicine_count),
                                 "patient_count": "0"}  # hata vermesin diye 0 yapmak yerine
                        self.data.append(datum)
                        self.update_medicine()  # ardından dosyayı güncelleme
                        clear_console()
                        print("\n\n    HealthBase  |  İlaç Envanter Otomasyonu - Yeni İlaç Ekle")
                        input("\033[92m"+"\n\n      {} adlı ilaç Envantere eklenmiştir\n\n      Ana "
                                         "menüye dönmek için herhangi bir tuşa basınız ".format(medicine)+"\033[39m")
                        break

    def patient_system(self):
        while True:
            clear_console()
            print("\n\n    HealthBase  |  İlaç Envanter Otomasyonu - Hasta Sistemi")
            try:
                medicine_id_to_update = int(input("Güncellenecek ilacın ID'sini girin: "))
            except ValueError:  # adet int kontolü
                a = input(
                    "\033[31m" + "\n\n      ID olarak INT değerler giriniz. "
                                 "(Geri dönmek için herhangi bir tuşa,\n      "
                                 "tekrar denemek için T' harfine basınız) " + "\033[39m")
                if a == "t" or a == "T":
                    continue
                break
            index = -1
            control = False
            for i in self.data:
                index += 1
                if int(i["id"]) == medicine_id_to_update:
                    control = True
                    break
            if control:
                try:
                    clear_console()
                    print("\n\n    HealthBase  |  İlaç Envanter Otomasyonu - Hasta Sistemi \n\n")
                    new_patient_count = int(input(" Ne kadar yeni hasta bu ilacı kullanmaya başladı: "))
                except ValueError:
                    a = input(
                        "\033[31m" + "\n\n      ID olarak INT değerler giriniz. "
                                     "(Geri dönmek için herhangi bir tuşa,\n      "
                                     "tekrar denemek için T' harfine basınız) " + "\033[39m")
                    if a == "t" or a == "T":
                        continue
                    break
                i = self.data[index]

                i["patient_count"] = int(i["patient_count"])
                i["patient_count"] += new_patient_count
                i["patient_count"] = str(i["patient_count"])
                self.update_medicine()
                clear_console()
                print("\n\n    HealthBase  |  İlaç Envanter Otomasyonu - Yeni İlaç Ekle")
                critical_level(i)
                input("\033[92m" + "\n\n      {} adlı ilacı kullanan {} kişi olmuştur \n\n      Ana "
                                   "menüye dönmek için herhangi bir "
                                   "tuşa basınız ".format(i["medicine"], i["patient_count"]) + "\033[39m")
                break

            else:
                print(
                    "\033[31m" + "\n   ARAMA BAŞARISIZ GİRMİŞ OLDUĞUNUZ ID'YE SAHİP "
                                 "BİR ÜRÜN BULUNMAMAKTADIR" + "\033[39m")
                a = input(
                    "\033[92m" + "\n\n      Geri dönmek için herhangi bir tuşa, yeni arama için "
                                 "T' harfine basınız var olan ürün listesini görmek için A'ya basın " + "\033[39m")
                if a == "T" or a == "t":
                    continue
                elif a == "A" or a == "a":
                    self.show_data()
                else:
                    break

    def personel_settings(self):
        shutil.copy2("2439230.nazmi", "log_dir/personel_veri_eski")
        while True:
            clear_console()
            try:
                file = open("2439230.nazmi", "r+", encoding="utf-16")
            except FileNotFoundError:
                clear_console()
                print(
                    "\033[31m" + "\n\n      Güvenlik açığı tespit edildi. uygulamadan çıkışınız verilmiştir. " + "\033[39m" + "\n\n")
                quit()

            all_ida = []
            all_password = []
            c = -1

            try:
                for i in file:
                    c += 1
                    i = i[:-1]
                    gecici = i.split(",")
                    all_ida.append(gecici[0])
                    all_password.append(gecici[1])
                    if gecici[0] == self.idd:  # self.idd = kullanan personelin id si
                        zx = c
            except:
                pass

            print("\n\n    HealthBase | İlaç Envanter Otomasyonu - Personel ayarları")
            print("\n\n      1) Kullanıcı adı değiştir")
            print("\n\n      2) Şifre değiştir")
            print("\n\n      M) Bir önceki menüye dön")
            print("\n\n      Q) Çıkış")

            secim = input("\n\n   Seçim = ")
            if secim == "1":  # kullanıcı adı değiştirme
                while True:
                    clear_console()
                    print("\n\n    HealthBase | İlaç Envanter Otomasyonu - Personel ayarları")
                    new_username = input("\n\n      Yeni kullanıcı adı (min 6, max 9) ve bir harf maksimum "
                                "2 defa tekrar edebilir = ")
                    control = None
                    for i in all_ida:
                        if i == new_username:
                            control = True
                            break
                    if control:
                        a = input(
                            "\033[31m" + "\n\n      Bu Kullanıcı Adı Alınmıştır. (Geri dönmek için herhangi bir tuşa,\n      tekrar denemek için T' harfine basınız) = " + "\033[39m")
                        if a == "t" or a == "T":
                            continue
                        file.close()
                        break
                    elif len(new_username) < 6 or len(new_username) > 9:
                        a = input(
                            "\033[31m" + "\n\n      Kullanıcı adı beş ile on karekter arasında olmalıdır.\n      (Geri dönmek için herhangi bir tuşa,\n      tekrar denemek için T' harfine basınız) = " + "\033[39m")
                        if a == "t" or a == "T":
                            continue
                        file.close()
                        break
                    else:
                        control = None
                        for i in new_username:
                            if new_username.count(i) > 2:
                                control = True
                                break
                        if control:
                            a = input(
                                "\033[31m" + "\n\n      Kullanıcı adında bir karekter en fazla "
                                             "iki defa tekrar edebilir.\n      (Geri dönmek için herhangi bir tuşa,"
                                             "\n      "
                                             "tekrar denemek için T' harfine basınız) = " + "\033[39m")
                            if a == "t" or a == "T":
                                continue
                            file.close()
                            break
                        else:
                            clear_console()
                            print("\n\n    HealthBase | İlaç Envanter Otomasyonu - Onay")
                            old_password = input("\n\n     Yaptığınız işlemin onaylanması için şifrenizi giriniz = ")
                            if self.password != old_password:  # self password = old password
                                print(
                                    "\033[31m" + "\n\n      Şifre Hatalı. Güvenlik amaçlı uygulamadan atılıyorsunuz..." + "\033[39m")
                                sleep(4)
                                clear_console()
                                print("\n")
                                quit()
                            else:
                                clear_console()
                                # herşey sorunsuz ilerlerse onay amaçlı şifreniz istenir
                                # şifre onaylanırsa işlem gerçekleşir
                                # hatalıysa uygulamadan atılırsınız
                                print("\n\n    HealthBase | İlaç Envanter Otomasyonu - Onay")
                                print("\033[92m" + "\n\n     Şifre onaylandı...." + "\033[39m")
                                sleep(4)
                            file.close()  # döngü başındaki dosya kaptılır
                            try:
                                file = open("2439230.nazmi", "w", encoding="UTF-16")  # yazma kipinde açılır
                            # dosyayı bulamazsa veri güvenliği tehlikede olduğu için otomasyondan atılır.
                            except FileNotFoundError:
                                clear_console()
                                print(
                                    "\033[31m" + "\n\n      Güvenlik açığı tespit edildi. uygulamadan çıkışınız verilmiştir. " + "\033[39m" + "\n\n")
                                quit()
                            clear_console()
                            all_ida[zx] = new_username  # listedeki veri değistirilir
                            self.idd = new_username
                            for i in range(0, len(all_ida)):  # liste dosyaya yazılır.
                                file.write(all_ida[i])
                                file.write(",")
                                file.write(all_password[i])
                                file.write(",")
                                file.write("\n")
                            file.close()
                            print("\n\n    HealthBase | İlaç Envanter Otomasyonu - Personel ayarları")
                            input(
                                "\033[92m" + "\n\n     Kullanıcı adınız {} olarak değiştirilmiştir.\n     Bir önceki menüye dönmek için Enter'e basınız. ".format(
                                    new_username) + "\033[39m")
                            break
            elif secim == "2":  # şifre değiştirme
                while True:
                    clear_console()
                    print("\n\n    HealthBase | İlaç Envanter Otomasyonu - Personel ayarları")
                    new_password = input("\n\n     Yeni şifre  min 5 max 12 = ")
                    new_password_again = input("\n\n     Yeni şifre tekrar = ")

                    if new_password != new_password_again:
                        a = input(
                            "\033[31m" + "\n\n      Şifreler eşleşmemektedir. (Geri dönmek için herhangi bir tuşa,\n      tekrar denemek için T' harfine basınız) = " + "\033[39m")
                        if a == "t" or a == "T":
                            continue
                        file.close()
                        break
                    else:
                        if len(new_password) < 5 or len(new_password) > 11:
                            a = input(
                                "\033[31m" + "\n\n      Şifre 4 ile 12 karekter arasında olmalıdır.\n      (Ana menüye dönmek için herhangi bir tuşa,\n      tekrar denemek için T' harfine basınız) = " + "\033[39m")
                            if a == "t" or a == "T":
                                continue
                            file.close()
                            break
                        else:
                            control = None
                            for a in new_password:
                                if (ord(a) >= 32 and ord(a) <= 47) or (
                                        ord(a) >= 58 and ord(a) <= 64) or (
                                        ord(a) >= 91 and ord(a) <= 96) or (
                                        ord(a) >= 122 and ord(a) <= 126):
                                    control = True
                                    break
                            if control == None:
                                a = input(
                                    "\033[31m" + "\n\n      Şifre de en az bir tane alfanümerik karekter bulunmalı.\n      "
                                                 "(Ana menüye dönmek için herhangi bir tuşa,\n      "
                                                 "tekrar denemek için T' harfine basınız) = " + "\033[39m")
                                if a == "t" or a == "T":
                                    continue
                                file.close()
                                break
                            else:
                                if self.idd in new_password:
                                    a = input(
                                        "\033[31m" + "\n\n      Şifre içinde kullanıcı adınız olmamalı.\n      "
                                                     "(Ana menüye dönmek için herhangi bir tuşa,\n      "
                                                     "tekrar denemek için T' harfine basınız) = " + "\033[39m")
                                    if a == "t" or a == "T":
                                        continue
                                    file.close()
                                    break
                                else:
                                    clear_console()
                                    print("\n\n    HealthBase | İlaç Envanter Otomasyonu - Onay")
                                    old_password = input(
                                        "\n\n     Yaptığınız işlemin onaylanması için ESKİ şifrenizi giriniz = ")  # güvenlik amaçlı eski şifre istenilir
                                    # hatalı ise uygulamadan atılır
                                    if self.password != old_password:
                                        print(
                                            "\033[31m" + "\n\n      Şifre Hatalı. Güvenlik amaçlı "
                                                         "uygulamadan atılıyorsunuz..." + "\033[39m")
                                        sleep(4)
                                        clear_console()
                                        print("\n")
                                        quit()
                                    else:
                                        clear_console()
                                        print("\n\n    HealthBase | İlaç Envanter Otomasyonu - Onay")
                                        print("\033[92m" + "\n\n     Şifre onaylandı...." + "\033[39m")
                                        sleep(4)
                                        file.close()
                                        all_password[zx] = new_password  # sözlükte değişiklik yapılır
                                        self.password = new_password  # sonraki şeyler için hemen password'u güncelledik
                                        try:
                                            file = open("2439230.nazmi", "w", encoding="utf-16")
                                        except FileNotFoundError:
                                            clear_console()
                                            print(
                                                "\033[31m" + "\n\n      Güvenlik açığı tespit edildi. "
                                                             "uygulamadan çıkışınız verilmiştir. " + "\033[39m" + "\n\n")
                                            quit()
                                        for i in range(0, len(all_password)):
                                            # liste dosyaya yazılır.
                                            file.write(all_ida[i])
                                            file.write(",")
                                            file.write(all_password[i])
                                            file.write(",")
                                            file.write("\n")
                                        file.close()
                                        clear_console()
                                        print("\n\n    HealthBase | İlaç Envanter Otomasyonu - Personel ayarları")
                                        input(
                                            "\033[92m" + "\n\n      Yeni şifreniz onaylandı, Bir önceki menüye dönmek için Enter 'e basınız" + "\033[39m")
                                        break
            elif secim == "m" or secim == "M":
                clear_console()
                break
            elif secim == "q" or secim == "Q":
                quit()
            else:
                break


def usernames_and_passwords():
    try:
        file = open("2439230.nazmi", "r+", encoding="UTF-16")
    except FileNotFoundError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(
            "\033[31m" + "\n\n      Güvenlik açığı tespit edildi. uygulamadan çıkışınız verilmiştir. " + "\033[39m" + "\n\n")
        quit()
    passwords = []
    ids = []
    try:
        for i in file:
            i = i[:-1]
            temp_list = i.split(",")
            passwords.append(temp_list[1])
            ids.append(temp_list[0])
    except:
        pass
    file.close()
    yield ids
    yield passwords


def new_user():
    ids, passwords = usernames_and_passwords()
    control_for_kayit = 0
    while True:
        if control_for_kayit == 3:  # eğer üç defa hatalı personel eklenmeye çalışılırsa güvenlik amaçlı uygulamadan atılır.
            clear_console()
            print("\n\n    HealthBase | İlaç Envanter Otomasyonu - Personel Kayıt")
            print(
                "\033[31m" + "\n\n      Üç defa hatalı Personel eklemeye çalıştınız.\n      "
                             "güvenlik amaçlı atılıyorsunuz..." + "\033[39m")
            sleep(4)
            clear_console()
            print("\n")
            quit()
        clear_console()
        print("\n\n    HealthBase | İlaç Envanter Otomasyonu - Personel Kayıt")
        print(""" 

            Kullanıcı adı şartları :

            Daha önceden o kullanıcı adının alınmaması(Eşssiz olmalı),
            Kullanıcı adı 5 ile 10 karekter arasında olmalı (6,7,8,9),
            Kullanıcı adında bir karekter enfazla iki kere tekrar edebilir.""")
        id = input("\033[92m" + "\n\n     Kullanıcı adı  = " + "\033[39m")
        clear_console()
        print("\n\n    HealthBase | İlaç Envanter Otomasyonu - Personel Kayıt")
        print(""" 

            Şifre şartları :

            Şifre ve şifre tekrar birbirine eşit olmalı,
            Şifre 4 ile 10 karekter arasında olmalı (5,6,7,8,9),
            Şifre de en az bir tane alfanümerik karekter bulunmalı(*,/,-,+,{ gibi).
            Şifre içersinde kullanıcı adınız bulunmamalı""")
        password1 = input("\033[92m" + "\n\n     Şifre  = " + "\033[39m")
        password2 = input("\033[92m" + "\n\n     Şifre Tekrar  = " + "\033[39m")

        if id in ids:
            clear_console()
            print("\n\n    HealthBase | İlaç Envanter Otomasyonu - Personel Kayıt")
            a = input(
                "\033[31m" + "\n\n     Bu Kullanıcı Adı Alınmıştır. (Ana menüye dönmek için herhangi bir tuşa,\n     tekrar denemek için T' harfine basınız) = " + "\033[39m")
            control_for_kayit += 1
            if a == "t" or a == "T":
                continue
            return 0, "a", "a"

        elif len(id) < 6 or len(id) > 9:
            clear_console()
            print("\n\n    HealthBase | İlaç Envanter Otomasyonu - Personel Kayıt")
            a = input(
                    "\033[31m" + "\n\n     Kullanıcı adı beş ile on karekter arasında olmalıdır.\n     (Ana menüye dönmek için herhangi bir tuşa,\n     tekrar denemek için T' harfine basınız) = " + "\033[39m")
            control_for_kayit += 1
            if a == "t" or a == "T":
                continue
            return 0, "a", "a"

        else:
            control = None
            for i in id:  # kullanıcı adında bir karekterin en fazla iki kez tekrar etme kontrolü
                if id.count(i) > 2:
                    control = True
                    break

            if control:
                clear_console()
                print("\n\n    HealthBase | İlaç Envanter Otomasyonu - Personel Kayıt")
                a = input(
                    """\033[31m"+"\n\n     Kullanıcı adında bir karekter en fazla iki defa tekrar edebilir.\n     (Ana menüye dönmek için herhangi bir tuşa,\n     tekrar denemek için T' harfine basınız) = "+"\033[39m""")
                control_for_kayit += 1
                if a == "t" or a == "T":
                    continue
                return 0, "a", "a"
            else:
                if password2 != password1:  # girilen iki şifrenin aynı olması kontrolü
                    a = input(
                        "\033[31m" + "\n\n     Şifreler eşleşmemektedir. (Ana menüye dönmek için herhangi bir tuşa,\n     tekrar denemek için T' harfine basınız) = " + "\033[39m")
                    control_for_kayit += 1
                    if a == "t" or a == "T":
                        continue
                    return 0, "a", "a"

                elif 5 > len(password1) or len(password1) > 9:
                    clear_console()
                    print("\n\n    HealthBase | İlaç Envanter Otomasyonu - Personel Kayıt")
                    a = input("\033[31m" + "\n\n     Şifre istenilen uzunlukta değil. (Ana menüye dönmek için herhangi bir tuşa,\n     tekrar denemek için T' harfine basınız) = " + "\033[39m")
                    control_for_kayit += 1
                    if a == "t" or a == "T":
                        continue
                    return 0, "a", "a"

                else:
                    control = None
                    for a in password1:
                        if (ord(a) >= 32 and ord(a) <= 47) or (
                                ord(a) >= 58 and ord(a) <= 64) or (
                                ord(a) >= 91 and ord(a) <= 96) or (
                                ord(a) >= 122 and ord(a) <= 126):
                            control = True
                            break

                if control == None:
                    clear_console()
                    print("\n\n    HealthBase | İlaç Envanter Otomasyonu - Personel Kayıt")
                    a = input(
                        "\033[31m" + "\n\n      Şifre de en az bir tane alfanümerik karekter bulunmalı.\n      "
                                     "(Ana menüye dönmek için herhangi bir tuşa,\n      "
                                     "tekrar denemek için T' harfine basınız) = " + "\033[39m")
                    if a == "t" or a == "T":
                        continue
                    return 0, "a", "a"
                if id in password1:
                    clear_console()
                    print("\n\n    HealthBase | İlaç Envanter Otomasyonu - Personel Kayıt")
                    a = input(
                        "\033[31m" + "\n\n      Şifre içinde kullanıcı adınız olmamalı.\n      "
                                     "(Ana menüye dönmek için herhangi bir tuşa,\n      "
                                     "tekrar denemek için T' harfine basınız) = " + "\033[39m")
                    if a == "t" or a == "T":
                        continue
                    return 0, "a", "a"

                else:
                    clear_console()
                    print("\n\n    HealthBase | İlaç Envanter Otomasyonu - Personel Kayıt")
                    print("\n Kaydınız başarıyla yapıldı {}.".format(id))
                    try:
                        shutil.copy2("2439230.nazmi", "log_dir/personel_veri_eski")
                    except:
                        pass
                    text = id + "," + password1 + "," + "\n"
                    try:
                        file = open("2439230.nazmi", "a+", encoding="UTF-16")
                    except:
                        clear_console()
                        print(
                            "\033[31m" + "\n\n      Güvenlik açığı tespit edildi. uygulamadan çıkışınız verilmiştir. " + "\033[39m" + "\n\n")
                        quit()
                    date = take_time()
                    message = "{} id'lı kullanıcı sisteme başarıyla kaydedildi: ".format(id) + date + "\n"
                    file.write(text)
                    try:
                        lg = open("log_dir/enter_update_log/log.txt", "a+", encoding="utf-16")
                    except FileNotFoundError:
                        clear_console()
                        print(
                            "\033[31m" + "\n\n      Güvenlik açığı tespit edildi. uygulamadan çıkışınız verilmiştir. " + "\033[39m" + "\n\n")
                        quit()
                    print("         Başarıyla Sisteme Kaydolundu. ")
                    lg.write(message)
                    return 1, id, password1





def giris():
    ids, passwords = usernames_and_passwords()

    control_for_giris = 0

    while True:
        clear_console()
        print("\n\n    HealthBase | İlaç Envanter Otomasyonu - Personel Giriş")
        if control_for_giris >= 3:
            print(
                "\033[31m" + "\n\n      Üç defa hatalı Personel eklemeye çalıştınız.\n      "
                             "güvenlik amaçlı atılıyorsunuz..." + "\033[39m")
            quit()
        id = input("\n\n    Kullanıcı Adınız: ")
        password = input("\n\n            Şifreniz: ")
        index = -1
        control = False
        for i in ids:
            index += 1
            if i == id:
                control = True
                break
        if control:
            if passwords[index] == password:
                sleep(4)
                try:
                    # otomasyonda yapılan aktivite kaydedilir.
                    lg = open("log_dir/enter_update_log/log.txt", "a+", encoding="utf-16")
                # dosyayı bulamazsa veri güvenliği tehlikede olduğu için otomasyondan atılır.
                except FileNotFoundError:
                    clear_console()
                    print(
                        "\033[31m" + "\n\n      Güvenlik açığı tespit edildi. uygulamadan çıkışınız verilmiştir. " + "\033[39m" + "\n\n")
                    quit()
                print("         Giriş Başarılı")
                sleep(3)
                date = take_time()
                message = id + " Adlı Kullanıcı Sisteme Başarıyla Giriş Yaptı: " + date + "\n"
                lg.write(message)
                return 1, id, password
            else:
                control_for_giris += 1
                print("         Kullanıcı adınız veya şifreniz yanlış. ")
                a = input("  \033[31m" + "\n\n     Giriş hatalı eşleşmemektedir. (Ana menüye dönmek için herhangi bir tuşa,\n     tekrar denemek için T' harfine basınız) = " + "\033[39m")
                if a == "t" or a == "T":
                    continue
                return 0, id, password

        else:
            control_for_giris += 1
            print("         Kullanıcı adınız veya şifreniz yanlış. ")
            a = input("  \033[31m" + "\n\n     Giriş hatalı eşleşmemektedir. (Ana menüye dönmek için herhangi bir tuşa,\n     tekrar denemek için T' harfine basınız) = " + "\033[39m")
            if a == "t" or a == "T":
                continue
            return 0, id, password


def islem():
        secim = input(" Seçim: ")
        if secim == "1":
            clear_console()
            control, idd, password = giris()
            return control, idd, password, secim
        elif secim == "2":
            clear_console()
            control, idd, password = new_user()
            return control, idd, password, secim
        elif secim == "q" or secim == "Q":
            quit()
        else:
            pass


def main():
    while True:
        clear_console()
        print(""" 

           HealthBase | İlaç Envanter Otomasyonu

            1) Personel Giriş

            2) Yeni Personel Ekle

            Q) Çıkış

                    """)
        a, b, c, secim = islem()
        if secim == "1" and a == 1:
            HealthBase(b, c)
        if secim == "2" and a == 1:
            print(" Kullanıcı Başarıyla Kaydedildi. ")


if __name__ == "__main__":
    main()
