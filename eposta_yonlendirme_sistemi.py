# -----------------------------------------
# E-posta Otomatik Yönlendirme Sistemi
# -----------------------------------------

gonderen_tipi = input("Gönderen tipi (musteri/tedarikci/ic): ").strip().lower()
konu = input("E-posta konusu: ").strip().lower()
icerik = input("E-posta içeriği: ").strip().lower()
onemli = input("Bu e-posta önemli mi? (evet/hayir): ").strip().lower()
saat = int(input("E-posta saati (0-23): "))

onemli_mi = (onemli == "evet")
mesai_ici = (9 <= saat < 18)  # 09:00 - 18:00 arası mesai içi

print("\n--- E-posta Yönlendirme Karar Süreci Başladı ---")

# 1) ACİL / ÖNEMLİ MAİLLER ÖNCE
if "acil" in konu or "acil" in icerik or onemli_mi:
    print("Sonuç: E-posta YÖNETİM'e yönlendirildi (ACİL/ÖNEMLİ).")

# 2) FATURA / ÖDEME / TAHSİLAT → MUHASEBE
elif ("fatura" in konu or "ödeme" in konu or "tahsilat" in konu or
      "fatura" in icerik or "ödeme" in icerik or "tahsilat" in icerik):
    print("Sonuç: E-posta MUHASEBE'ye yönlendirildi.")

# 3) ŞİKAYET / DESTEK TALEBİ → MÜŞTERİ DESTEK
elif ("şikayet" in konu or "sikayet" in konu or "destek" in konu or
      "şikayet" in icerik or "sikayet" in icerik or "destek" in icerik):
    print("Sonuç: E-posta MÜŞTERİ DESTEK ekibine yönlendirildi.")

# 4) TEKLİF / SATIŞ FIRSATI → SATIŞ
elif ("teklif" in konu or "fiyat" in konu or "sipariş" in konu or
      "teklif" in icerik or "fiyat" in icerik or "sipariş" in icerik):
    print("Sonuç: E-posta SATIŞ ekibine yönlendirildi.")

# 5) TEDARİKÇİDEN GELEN VE FATURA/ÖDEME İÇERMEYEN MAİLLER → TEDARİK/ZİNCİR
elif gonderen_tipi == "tedarikci":
    print("Sonuç: E-posta TEDARİK/ZİNCİR ekibine yönlendirildi.")

# 6) İÇ EKİPTEN GELEN MAİLLER VE MESAI DIŞI DURUMU
elif gonderen_tipi == "ic" and not mesai_ici:
    print("Sonuç: E-posta İÇ EKİP - MESAI DIŞI klasörüne alındı.")

elif gonderen_tipi == "ic" and mesai_ici:
    print("Sonuç: E-posta İÇ EKİP klasörüne alındı.")

# 7) MÜŞTERİ AMA HİÇBİR KRİTİK KELİME YOKSA → GENEL MÜŞTERİ KUTUSU
elif gonderen_tipi == "musteri":
    print("Sonuç: E-posta GENEL MÜŞTERİ kutusuna alındı.")

# 8) DİĞER TÜM DURUMLAR → GENEL INFO
else:
    print("Sonuç: E-posta GENEL INFO kutusuna alındı.")
