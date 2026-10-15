# Lab, Bölüm 2: Testleri bu dosyaya SİZ yazacaksınız.
#
# Aşağıda örnek olarak bir test var. Yanına her fonksiyon için kendi testlerinizi ekleyin.
# Çalıştırmak için bu klasörde:  python -m pytest test_bolum2.py test_hatali_surumler.py -v

import pytest

from bolum2 import sifre_gucu, otopark_ucreti, yuzde_degisim

def test_kisa_sifre_zayif():
    assert sifre_gucu("abc") == "zayıf"

def test_orta_sifre():
    assert sifre_gucu("abcdefgh") == "orta"

def test_guclu_sifre():
    assert sifre_gucu("abcdefghijkl") == "güçlü"

def test_bos_sifre():
    with pytest.raises(ValueError):
        sifre_gucu("")
      
##------------------------

def test_otopark_sifir_dakika():
    assert otopark_ucreti(0) == 0

def test_otopark_15_dakika():
    assert otopark_ucreti(15) == 0

def test_otopark_16_dakika():
    assert otopark_ucreti(16) == 20

def test_otopark_60_dakika():
    assert otopark_ucreti(60) == 20

def test_otopark_61_dakika():
    assert otopark_ucreti(61) == 40

def test_otopark_180_dakika():
    assert otopark_ucreti(180) == 40

def test_otopark_181_dakika():
    assert otopark_ucreti(181) == 60

def test_otopark_negatif():
    with pytest.raises(ValueError):
        otopark_ucreti(-1)


##-----------------------

def test_yuzde_artis():
    assert yuzde_degisim(200, 250) == 25.0

def test_yuzde_azalis():
    assert yuzde_degisim(200, 150) == -25.0

def test_yuzde_degisim_yok():
    assert yuzde_degisim(100, 100) == 0.0

def test_yuzde_eski_sifir():
    with pytest.raises(ValueError):
        yuzde_degisim(0, 100)


