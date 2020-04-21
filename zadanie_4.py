'''
Instructions from your teacher:
Rzuty kostką
Gramy w grę polegającą na rzucaniu typową sześcienną kostką.

W każdej kolejce gracz dwukrotnie rzuca kością. Po dwukrotnym rzuceniu kością wynikiem gracza jest suma wyrzuconych oczek z rzutu numer 1 oraz rzutu numer 2.

Napisz program, który do słownika dict przypisuje pary key i value, gdzie:
key - to możliwy do uzyskania wynik w jednej kolejce (suma oczek w dwóch rzutach)
value - to wszystkie kombinacje rzutów, które składają się na dany key

Wszystkie możliwe kombinacje do uzyskania danego wyniku przechowuj jako zbiór, w którym każdy kolejny element to krotka, której pierwsza wartość to rezultat pierwszego rzutu, a druga wartość to rezultat drugiego rzutu.

Na przykład wywołując:
dice[7]

Wynik powinien zawierać następujące elementy:
{(1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1)}
'''

dice = {}
kostka =[]
liczba=[]

for k in range(1,7):
  if k not in kostka:
    kostka.append(k)

minim = min(kostka)
maxim = max(kostka)
sum_min = min(kostka) + min(kostka)
sum_max = max(kostka) + max(kostka)
oczka = [i for i in range(sum_min, sum_max)]


def T(suma):
    for x in kostka:
        for y in kostka:
            if x+y==suma:
                i=tuple([x, y])
                liczba.append(i)
    return liczba        
# ta funkcja u dołu nie działa
for i in oczka:
    dice[i]=[T(i)]
print(dice)

