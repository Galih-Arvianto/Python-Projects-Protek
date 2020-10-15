tarifA=200000
tarifB=10000
Rentalawal=06.00
RentalAkhir=23.50
totalrental=RentalAkhir-Rentalawal
waktuRentalnext=int(totalrental-12)
totaltarifB=waktuRentalnext * tarifB
totalbiaya=tarifA+totaltarifB
print(totalbiaya)