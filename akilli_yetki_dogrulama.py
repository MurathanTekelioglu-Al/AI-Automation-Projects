tip = input("Kullanıcı tipi (admin/personel/misafir): ").strip().lower()
yas = int(input("Yaş: "))
mesaj = input("Mesaj içeriği: ").strip().lower()
aktif = input ("Kullanıcı aktif mi? (evet/hayır): ").strip().lower()
saat = int(input("Giriş saati (0-23):"))



aktif_mi = (aktif == "evet")
gece_modu = (saat >= 22 or saat < 6)

print("\n--- Karar Süreci Başladı ---")

if "acil" in mesaj and aktif_mi:
    print("Sonuç: ACİL DURUM - Sistem geçiş izni verildi.")


elif tip == "admin" and yas >= 18 and aktif_mi:
    print("Sonuç: Tam yetki (Admin).")


elif tip == "personel" and yas >= 18 and aktif_mi and not gece_modu:
    print("Sonuç: Personel yetkisi(Gece modu: Kapalı).")


elif tip == "personel" and yas >= 18 and aktif_mi and gece_modu:
    print("Sonuç: Personel yetkisi sınırlı (Gece modu devrede).")

elif tip == "misafir" and aktif_mi:
    print("Sonuç: Misafir yetkisi - yalnızca okuma izni.")



elif not aktif_mi:
    print("Sonuç:  - Kullanıcı pasif - giriş reddedildi.")


else:
    print("Sonuç: Yetki verilmedi - kurallara uymuyor.")