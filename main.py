import p5
from datetime import datetime
import math
# Gerekli içe aktarmalar

# Pencere boyutları içn genişlik ve yükseklik değerleri
width, height = 500, 500

# Akrep kolu uzunluğu 120px
r_h = 120
# Yelkovan kolu uzunluğu 180px
r_m = 180
# Saniye kolu uzunluğu 200px
r_s = 200
# Saatin etrafındaki noktaların merkezden uzaklığı 240px
r_d = 240


# Kutupsal koordinat sisteminden
# kartezyen koordinat sistemine dönüşüm
def pol2car(r, angle):
    # x = r cos(theta)
    x = r * math.cos(math.radians(angle))
    # y = r sin(theta)
    y = r * math.sin(math.radians(angle))

    # Hesaplanan x ve y değerlerini return et
    return x, y


# p5 başlangıç fonksiyonu
# 1 defa çalışır
def setup():
    # Pencere boyutunu ayarla
    p5.size(width, height)


# Çizme fonksiyonu
# Frame rate'çe (60 FPT için saniyede 60 defa) çalışır
def draw():
    # Arka planı siyah yap
    p5.background(0)
    # Orijini pencerenin merkezine taşı
    p5.translate(width/2, height/2)

    # clock fonsiyonundan gelen değerleri
    # sırasıyla h, m ve s değişkenlerine ata
    h, m, s = clock()

    # Çevre çizgisi çizme
    p5.no_stroke()

    # [0, 360) aralığında 6'şar derece aralıklarla değer oluştur
    # 0, 6, 12, ...,  342, 348, 354
    for i in range(0, 360, 6):

        # Kutupsal koordinat sisteminde
        # (r_d, i) değerini kartezyen koordinat sistemine dönüştür
        d_x, d_y = pol2car(r_d, i)

        # i değeri 30'un tam katıysa,
        if i % 30 == 0:
            # saat değerleri için nokta koyacağız
            p5.fill(255, 0, 0)
            r = 15
        else:
            # dakika/saniye değerleri için nokta koyacağız
            p5.fill(255)
            r = 10

        # Belirlenen özelliklerle hesaplanan noktada
        # bir daire çiz
        p5.circle((d_x, d_y), r)

    # Akrep kolunun ucunun konumunu hesala
    h_x, h_y = pol2car(r_h, h)
    # Akrep kolunun şekil ayarlarını yap
    p5.stroke(255)
    p5.stroke_weight(5)
    # Akrep konu çiz
    p5.line((0, 0), (h_x, h_y))

    # Yelkovan kolunun ucunun konumunu hesala
    m_x, m_y = pol2car(r_m, m)
    # Yelkovan kolunun şekil ayarlarını yap
    p5.stroke(255)
    p5.stroke_weight(3)
    # Yelkovan konu çiz
    p5.line((0, 0), (m_x, m_y))

    # Saniye kolunun ucunun konumunu hesala
    s_x, s_y = pol2car(r_s, s)
    # Saniye kolunun şekil ayarlarını yap
    p5.stroke(255, 0, 0)
    p5.stroke_weight(1)
    # Saniye konu çiz
    p5.line((0, 0), (s_x, s_y))


# Saat kollarının açılarını hesaplar
def clock():
    """Saat bilgisini alıp,
    akrep, yelkovan ve saniye kollarının
    açılarını, bilgisayar ekranına uygun
    veren fonskiyon"""
    # Şimdiki zamanı al
    now = datetime.now()
    # saat, dakika ve saniye değerlerini
    # Sırasıyla h, m, s değşkenlerine ata
    h = now.hour
    m = now.minute
    s = now.second

    # Saniye kolunun açısını hesapla
    angle_s = s * 6
    # Yelkovan kolunun açısını hesapla
    angle_m = m * 6 + (angle_s / 60)
    # Akrep kolunun açısını hesapla
    angle_h = (h % 12) * 30 + (angle_m/12)

    # Bu değerleri bilgisayar ekranına uygun döndür
    return angle_h - 90, angle_m - 90, angle_s - 90


# p5'i çalıştır
if __name__ == "__main__":
    p5.run()
