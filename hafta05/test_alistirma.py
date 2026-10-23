# Alıştırma 4: Testleri bu dosyaya SİZ yazacaksınız.
#
# Aşağıda örnek olarak bir test var. Yanına kendi testlerinizi ekleyin.
# Çalıştırmak için bu klasörde:  python -m pytest -v

import pytest

from alistirma import indirim_orani, sepet_toplami, en_pahali_urun


def test_sepet_toplami():
    sepet = [
        {"urun": "çay", "fiyat": 20, "adet": 2},
        {"urun": "simit", "fiyat": 15, "adet": 3},
        {"urun": "tost", "fiyat": 60, "adet": 1},
    ]
    assert sepet_toplami(sepet) == 145



@pytest.mark.parametrize(
    "tutar,beklenen",
    [
        (0, 0),
        (99, 0),
        (100, 5),
        (499, 5),
        (500, 10),
        (999, 10),
        (1000, 15),
        (1500, 15),
    ]
)
def test_indirim_orani(tutar, beklenen):
    assert indirim_orani(tutar) == beklenen


def test_indirim_negatif():
    with pytest.raises(ValueError):
        indirim_orani(-1)



def test_sepet_bos():
    assert sepet_toplami([]) == 0


@pytest.mark.parametrize("adet", [0, -1])
def test_sepet_gecersiz_adet(adet):
    sepet = [
        {"urun": "çay", "fiyat": 20, "adet": adet}
    ]

    with pytest.raises(ValueError):
        sepet_toplami(sepet)



def test_en_pahali_urun():
    sepet = [
        {"urun": "çay", "fiyat": 20, "adet": 2},
        {"urun": "tost", "fiyat": 60, "adet": 1},
        {"urun": "simit", "fiyat": 15, "adet": 3},
    ]
    assert en_pahali_urun(sepet) == "tost"


def test_en_pahali_esit_fiyat():
    sepet = [
        {"urun": "çay", "fiyat": 60, "adet": 1},
        {"urun": "tost", "fiyat": 60, "adet": 2},
    ]
    assert en_pahali_urun(sepet) == "çay"


def test_en_pahali_bos():
    assert en_pahali_urun([]) is None


def test_en_pahali_birim_fiyat():
    sepet = [
        {"urun": "çay", "fiyat": 20, "adet": 10},
        {"urun": "tost", "fiyat": 60, "adet": 1},
    ]
    assert en_pahali_urun(sepet) == "tost"
