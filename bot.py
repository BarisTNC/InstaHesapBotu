import random
isimler=["kisim","eisim"]
erkekisimleri=["ali","ahmet","mehmet","nazif","eren","emre","aykut","sinan","ümit","adnan","yiğit","nazmican","hamza","kadir","uğur","kubilay","yusuf","yunus","osman","burak","bartuğ","engin","can","yavuz","umut","ömer","hüseyin","berkay","faruk","ismail","ebubekir","oğuzhan","oğuz","kağan","hakan","erkan","ensar","kemal","fatih","emir","emrehan","atakan","mesut","tahir","furkan","salih","salim","caner","bayram","yalçın","berk",]
kızisimleri=["ayşe","fatma","aynur","elif","zeynep","tuğba","kübra","aleyna","miray","beyza","rüya","nisa","öykü","pelin","sıla","beyzanur","ekim","filiz","sare","gülşah","deniz","sude","sudenaz","hacer","buket","bahar","begüm","yağmur","ırmak","ece","nursena","sena","özge","eda","berfin","kader","ecrin","burcu"]
soyisimleri=["tunç","çakmak","deniz","polat","zengin","bayrak","uçar","aydın","albayrak","görmez","tatlıcı","balta","tekin","uğur","baltacıoğlu","seçkin","menderes","güçlü","zalim","rüyacı","bayraktar","elmacı","elçi","yakut","bal","elmas","taş","umut","parlak","sönmez"]

eisim=random.choice(erkekisimleri)
kisim=random.choice(kızisimleri)
soyisim=random.choice(soyisimleri)
isimlik=random.choice(isimler)

#Kelimelerin harf düzeltmesi
def isimdüzeltme(isim):
    isim=isim.replace("ı","i")
    isim=isim.replace("ğ","g")
    isim=isim.replace("ş","s")
    isim=isim.replace("ü","u")
    isim=isim.replace("ç","c")
    isim=isim.replace("ö","o")
    print(isim)
    return isim
    
if isimlik=="kisim":
    print("kız ismi")
    isim=kisim
else:
    print("erkek ismi")
    isim=eisim
ad=isimdüzeltme(isim)
soyad=isimdüzeltme(soyisim)


