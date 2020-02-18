# Tuples Unpacking Task

products = (('No. 5', 'perfume', 'Chanel'),
            ('Inflallible', 'cosmetic', "L'Oreal"),
            ('Poison', 'perfume', 'Dior'),
            ('Double Wear', 'cosmetic', 'Estee Lauder'),
            ('Wonder Wing', 'cosmetic', 'Rimmel London')
            )

# printing all the companies only
print("Company:")
for product in products:
    name, product_type, company = product
    print(company)

print()
# printing all the product names only
print("Product name:")
for product in products:
    name, product_type, company = product
    print(name)
