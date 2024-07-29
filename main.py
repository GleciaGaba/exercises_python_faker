from faker import Faker

"""
Le package Faker en Python est une bibliothèque très utile pour générer des données factices (faux). 
Il est couramment utilisé pour les tests, le prototypage et la simulation de données. 
Voici quelques points clés à propos de Faker :

"""

fake = Faker(locale="fr_FR")  # ce package

print(fake.unique.name()) # création de données uniques en fonction de ce qui on souhaite générer

# Générer une adresse
print(fake.address())

# Générer une date de naissance
print(fake.date_of_birth())

# Générer une entreprise
print(fake.company())

print(fake.text())


numbers = [fake.unique.random_int() for _ in range(500)]
assert len(numbers) == len(set(numbers))
print(numbers
      )



