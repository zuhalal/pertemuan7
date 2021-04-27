# Dictionary
# Dictionary adalah tipe data key:value pairs yang sekuensial, dapat diubah, dan tidak mengizinkan duplikat
this_is_dict = {
    'first_name': 'John',
    'last_name': 'Doe',
    'email': 'johndoe@mail.com'
}

#key itu bisa string, integer, tuple
# print('this_is_dict: ', this_is_dict, ' is type of ', type(this_is_dict))

#membuat dict dari tuple atau list
tuple_of_tuples = (
    ("Indonesia", "Jakarta"),
    ("Italy", "Rome"),
    ("Germany", "Berlin")
)

capitals = dict(tuple_of_tuples)
print(capitals) # {'Indonesia': 'Jakarta', 'Italy': 'Rome', 'Germany': 'Berlin'}

list_of_tuples = [
    ["Indonesia", "Jakarta"],
    ["Italy", "Rome"],
    ["Germany", "Berlin"]
]
capitals = dict(list_of_tuples)
print(capitals) # {'Indonesia': 'Jakarta', 'Italy': 'Rome', 'Germany': 'Berlin'}

# Akses item dalam dict
#jadi ga bisa make indeks, harus manggil key
print(this_is_dict['first_name'])
print(this_is_dict.get('first_name'))
print(this_is_dict.get("middle_name", "Key tidak tersedia"))


print(this_is_dict.keys())

print(this_is_dict.values())

# print(this_is_dict.items())

# Mengubah nilai
this_is_dict['first_name'] = 'Jono'
# print(this_is_dict)

# Menambahkan nilai
this_is_dict['password'] = 'thisispassword'
print(this_is_dict)

tambahan = {"middle_name": "Jona", "job":"developer"}
this_is_dict.update(tambahan)
print(this_is_dict)

# Menghapus nilai
this_is_dict.pop('last_name')
#del this_is_dict['last_name']
print(this_is_dict)

#perulangan pada dictionary
for key in this_is_dict:
    print(key)
    print(this_is_dict[key])

for keys, values in this_is_dict.items():
    print(keys, values)