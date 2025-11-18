giris = input("Giriş tipi (admin/standart): ").strip().lower()
yas = int(input("Yaş: "))
acil = input("Acil durum var mı? (evet/hayır): ").strip().lower()


if acil == "evet":
    print("Sonuç: Acil durum - geçici yetki verildi.")


elif giris == "admin" and yas >= 18:
    print("Sonuç: Tam yetki.")



elif giris == "standart" and yas >= 18:
    print("Sonuç: Sınırlı yetki.")


else:
    print("Sonuç: Erişim reddedildi.")