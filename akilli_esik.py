mesaj = input("Mesaj: ").lower()

puan = 0

if "acil" in mesaj:
    puan += 5

if "şikayet" in mesaj or "sikayet" in mesaj:
    puan += 4

if "fatura" in mesaj:
    puan += 2


print(f"\nToplam önem/risk puanı: {ouan}")



if puan >= 5:
    print("Sonuç: BU MESAJ ÖNEMLİ / ÖNCELIKLI ELE ALINMALI.")
else:
    print("Sonuç: Bu mesaj normal öncelikli")