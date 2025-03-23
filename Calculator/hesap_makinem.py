import math as m

def topla(numx, numy):
    return numx + numy
def çıkart(numx, numy):
    return numx - numy
def çarp(numx, numy):
    return numx * numy
def böl(numx, numy):
    return numx / numy
def karekök(numx):
    return m.sqrt(numx)
def kare(numx):
    return (numx * numx)
def küp(numx):
    return (numx * numx * numx)
def log(numx):
    return m.log10(numx)

print("Bir işlem seç.")
print("1 Topla")
print("2 Çıkart")
print("3 Çarp")
print("4 Böl")
print("5 Karekök al")
print("6 Kare al")
print("7 Küp al")
print("8 Log10 tabanında Log al")

while True:
    select = int(input("Hangi işlemi yapmak istediğinizi seçin(1,2,3...): "))

    if select == 5 or select == 6 or select == 7 or select == 8:
        number_x = float(input("Sayıyı giriniz: "))
    elif select == 1 or select == 2 or select == 3 or select == 4:
        number_x = float(input("İlk sayıyı giriniz: "))
        number_y = float(input("Diğer sayıyı giriniz: "))

    if select == 1:
        print(number_x, "+", number_y, "=", topla(number_x, number_y))
    elif select == 2:
        print(number_x, "-", number_y, "=", çıkart(number_x, number_y))
    elif select == 3:
        print(number_x, "x", number_y, "=", çarp(number_x, number_y))
    elif select == 4:
        print(number_x, "/", number_y, "=", böl(number_x, number_y))
    elif select == 5:
        print("√", number_x, "=", karekök(number_x))
    elif select == 6:
        print(number_x, "**", "=", kare(number_x))
    elif select == 7:
        print(number_x, "***", "=", küp(number_x))
    elif select == 8:
        print(number_x, "log10", "=", log(number_x))
    else: 
        print("Geçerli öğe giriniz.")

    devam = input("Başka işlem yapmak ister misiniz? (E/H): ")
    if devam == "h" or devam == "H":
        print("Umarım yardımcı olabilmişimdir.")
        break
    elif devam == "e" or devam == "E":
        continue