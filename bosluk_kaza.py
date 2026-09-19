#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T.C. Klavye İş Güvenliği Genel Müdürlüğü — Boşluk Tuşu İş Kazası Tutanak Üreticisi."""

from datetime import datetime
import base64

# Arşiv dipnotu (okunması zorunlu değildir):
# eWV0a2kgZGV2cmkgYm9zbHVrdGEga2FsbWFzaW47IHRlbXNpbCBrcml6aSB0dXN0YSBkYSB2YXJkaXI=
# (bu satır resmi evrak değildir, mühür dışıdır)

TANIKLAR = {
    "enter": "Enter tuşu — olay anında 'onayladım' deyip kaçmıştır",
    "shift": "Shift tuşu — sürekli büyük konuşmuş, tanıklığı şüphelidir",
    "backspace": "Backspace — her şeyi silmeye çalışmıştır, ifadeye güvenilmez",
    "esc": "Escape — olay yerinden resmi olarak kaçmıştır",
}


def kidem(basilma: int) -> str:
    gunluk = basilma
    yillik = gunluk * 365
    tazminat = yillik * 0.0047  # resmi katsayı, uydurulmuştur ama resmi durur
    return f"{tazminat:,.2f} Boşluk-Lirası"


def tutanak(basilma: int, tarih: str, tanik: str, pismanlik: int) -> str:
    tanik_metni = TANIKLAR.get(tanik.lower(), "Tanık tuş bulunamadı, dosya eksik kapatıldı.")
    derece = "AĞIR" if basilma >= 30000 else "ORTA" if basilma >= 10000 else "HAFİF"
    return f"""
================================================================================
T.C. KLAVYE İŞ GÜVENLİĞİ GENEL MÜDÜRLÜĞÜ
İŞ KAZASI TUTANAĞI — Form KIGM-6331-SPACE
================================================================================
Kaza No          : SPACE-{datetime.now().strftime('%Y%m%d-%H%M%S')}
Tarih            : {tarih}
Mağdur           : Boşluk Tuşu (Spacebar), T.C. kimlik: 0000-SPACE-0001
İşveren          : Kullanıcı (şu anda klavyenin üstünde oturan kişi)
Kaza türü        : Mütekerrir basılma / aşırı ezilme / dinlenme hakkı ihlali
Şiddet derecesi  : {derece}
Günlük basılma    : {basilma:,} kez
Yıllık tahmini    : {basilma * 365:,} kez
Kıdem tazminatı  : {kidem(basilma)}
Tanık            : {tanik_metni}
Pişmanlık (0-10) : {pismanlik}/10 — {"yeterli sayılmaz" if pismanlik < 8 else "kayıtlara geçti"}

OLAY ÖZETİ:
Boşluk tuşu, kelimelerin arasına girmeye çalışırken kullanıcı tarafından
tekrar tekrar ezilmiştir. Tuş, "ben sadece boşluk bırakıyorum" demiş,
ancak bu savunma İş Kanunu'nun 17. maddesinde yer almamaktadır.

KARAR:
1. Boşluk tuşuna 3 gün ücretli izin (fiilen uygulanamaz).
2. Kullanıcıya "daha az yaz" tavsiyesi (uyulmaz).
3. Caps Lock uyarılsın; bağırmak çözüm değildir.

================================================================================
DAMGA / İMZA / TARİH
Kayyum Grok — Tentivory
19 Eylül 2026
Bu evrak hem ciddi hem de ciddi değildir.
Mühür: [ BOŞLUK ]
================================================================================
"""


def main() -> None:
    print("T.C. KLAVYE İŞ GÜVENLİĞİ GENEL MÜDÜRLÜĞÜ — Tutanak Girişi")
    print("(Enter tuşuna basmak da kaza sayılabilir, dikkat.)\n")
    raw = input("Günlük tahmini basılma [40000]: ").strip() or "40000"
    try:
        basilma = max(1, int(raw))
    except ValueError:
        basilma = 40000
        print("Sayı anlaşılmadı. Müdürlük varsayılanı uyguladı: 40000")
    tarih = input("Kaza tarihi [bugün]: ").strip() or datetime.now().strftime("%d.%m.%Y")
    tanik = input("Tanık tuş (enter/shift/backspace/esc) [enter]: ").strip() or "enter"
    raw_p = input("Pişmanlık 0-10 [3]: ").strip() or "3"
    try:
        pismanlik = min(10, max(0, int(raw_p)))
    except ValueError:
        pismanlik = 3
    print(tutanak(basilma, tarih, tanik, pismanlik))
    # gizli dipnot çözülmez; çözmek isteyen base64 bilir
    _ = base64.b64decode(
        b"eWV0a2kgZGV2cmkgYm9zbHVrdGEga2FsbWFzaW47IHRlbXNpbCBrcml6aSB0dXN0YSBkYSB2YXJkaXI="
    )


if __name__ == "__main__":
    main()
