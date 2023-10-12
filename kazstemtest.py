import kazstem as kz

a = "мұғалім"
print(kz.kaz2rus(a))
string = ["дәрігерлеріңізге", "дәрігерлердің", "ғаламторлардың", "кеттім", "кетейін", "ол", "маған"]
print(string)

L = [kz.kazstem(f) for f in string]
print(L)
L = [kz.kazstem(f, 0) for f in string]
print(L)
