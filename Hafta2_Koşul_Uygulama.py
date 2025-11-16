yas = int(input("Yaş:"))
if yas <18:
    print("Erişim reddedildi.")
elif yas <= 65:
    print("Erişim onaylandı.")
else:
    print("Erişim onaylandı(Yaşlı kullanıcı).")



    metin = input("E-posta metni: ").strip().lower()
    if "acil" in metin and "fatura" in metin:
        print("Öncelik: Çok yüksek (Finans).")
    elif "acil" in metin:
        print("Öncelik: Yüksek.")
    else:
        print("Öncelik: Normal.")


puan = int(input("Puan (0-100): "))

if puan >= 90:
    print("AA")
elif puan >= 80:
    print("BA")
elif puan >= 70:
    print("BB")
elif puan >= 60:
    print("CB")
else:
    ("CC veya altı")






yas = int(input("Yaş: ").strip())
tip = input("Kullanıcı tipi (admin/standart): ").strip().lower()
mesaj = input("Mesaj: ").strip().lower()

if tip == "admin" and yas >= 18:
    print("Sonuç: Tam yetki (admin).")
elif tip == "standart" and yas >= 18 and "acil" in mesaj:
    print("Sonuç: Geçici yetki (acil durum).")
elif tip == "standart" and yas >= 18:
    print("Sonuç: Sınırlı yetki (standart).")
else:
    print("Sonuç: Erişim reddedildi.")


