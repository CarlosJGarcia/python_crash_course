from city_functions import funcion

def test_city_country():
    ret = funcion('santiago', 'chile')
    assert ret == 'Santiago, Chile'

def test_city_country_population():
    ret = funcion('santiago', 'chile', 5000000)
    assert ret == 'Santiago, Chile - Population 5000000'




