import random
import math

proizvodi = [
    "Laptop",
    "Miš",
    "Tastatura",
    "Monitor",
    "Slušalice",
    "Web kamera",
    "USB kabl",
    "Eksterni hard disk"
]

cene = {
    "Laptop": 950.99,
    "Miš": 19.99,
    "Tastatura": 49.99,
    "Monitor": 199.99,
    "Slušalice": 89.99,
    "Web kamera": 59.99,
    "USB kabl": 9.99,
    "Eksterni hard disk": 129.99
}

print("=== SVI PROIZVODI ===")
for proizvod in proizvodi:
    print(f"{proizvod} - {cene[proizvod]:.2f} €")

budzet = float(input("\nUnesite vaš budžet (€): "))

print("\n=== PROIZVODI KOJE MOŽETE DA PRIUŠTITE ===")
moze_priustiti = False
for proizvod in proizvodi:
    if cene[proizvod] <= budzet:
        print(f"{proizvod} - {cene[proizvod]:.2f} €")
        moze_priustiti = True

if not moze_priustiti:
    print("Nažalost, nemate dovoljno budžeta ni za jedan proizvod.")

def najskuplji_proizvod(cene_dict):
    najskuplji = max(cene_dict, key=cene_dict.get)
    return najskuplji, cene_dict[najskuplji]

naziv, cena = najskuplji_proizvod(cene)
print(f"\nNajskuplji proizvod je: {naziv} - {cena:.2f} €")

nasumican = random.choice(proizvodi)
print(f"\nKorisniku je privukao pažnju proizvod: {nasumican}")

prosecna_cena = sum(cene.values()) / len(cene)
prosecna_cena = math.floor(prosecna_cena * 100) / 100  
print(f"\nProsečna cena svih proizvoda je: {prosecna_cena:.2f} €")

prodate_kolicine = [10, 50, 30, 20, 25, 15, 100, 12]

ukupan_prihod = 0
for i in range(len(proizvodi)):
    proizvod = proizvodi[i]
    kolicina = prodate_kolicine[i]
    ukupan_prihod += cene[proizvod] * kolicina

print(f"\nUkupan prihod je: {ukupan_prihod:.2f} €")

novi_proizvod = "Pametni sat"
nova_cena = 149.99

proizvodi.append(novi_proizvod)
cene[novi_proizvod] = nova_cena

print("\n=== AŽURIRANA LISTA PROIZVODA ===")
for proizvod in proizvodi:
    print(proizvod)

print("\n=== PROIZVODI SORTIRANI PO CENI ===")
sortirani = sorted(cene.items(), key=lambda x: x[1])

for proizvod, cena in sortirani:
    print(f"{proizvod} - {cena:.2f} €")