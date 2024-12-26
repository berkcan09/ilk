import random
karakter="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

uzunluk=int(input("kac karekterli bir sifre olsun"))
sifre=""

for i in range(uzunluk):
    sifre+=random.choice(karakter)
print(sifre)
