# Hafta 3: Testleri bu dosyaya SİZ yazacaksınız.
#
# Aşağıda örnek olarak bir test var. Yanına her fonksiyon için kendi testlerinizi ekleyin.
# Çalıştırmak için bu klasörde:  python -m pytest -v

import pytest

from alistirma import kargo_ucreti, bilet_fiyati, ortalama

def test_kargo_buyuk_sipariste_ucretsiz():
    assert kargo_ucreti(800) == 0

def test_kargo_tam_sinirda():
    assert kargo_ucreti(500) == 0

def test_kargo_sifir_tutar():
    assert kargo_ucreti(0) == 50

def test_kargo_negatif_tutar():
    with pytest.raises(ValueError):
        kargo_ucreti(-1)


#------------------------

def test_bilet_ucretsiz():
    assert bilet_fiyati(6) == 0

def test_bilet_ogrenci():
    assert bilet_fiyati(17) == 50

def test_bilet_tam():
    assert bilet_fiyati(18) == 100

def test_bilet_indirimli():
    assert bilet_fiyati(65) == 60

def test_bilet_negatif():
    with pytest.raises(ValueError):
        bilet_fiyati(-1)

##--------------------------------


def test_ortalama_ondalik():
    assert ortalama([70, 85]) == 77.5


def test_ortalama_bos():
    with pytest.raises(ValueError):
        ortalama([])



