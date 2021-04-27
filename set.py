# Set
# Set adalah tipe data yang non-sekuensial, tak dapat diubah, dan tidak mengizinkan duplikasi
this_is_set = {"oke", 10, "oke",  9.0, 10}
print("this_is_set : ", this_is_set, " is type of ", type(this_is_set))

# Akses item dalam set
# Karena set adalah tipe data non-sekuensial, set tidak memiliki index sehingga kita tidak dapat
# mengakses set menggunakan index, tapi kita dapat melakukan perulangan untuk mengakses data dalam set
# for data in this_is_set:
#     print(data)
# # Hal ini juga yang membuat kita tidak dapat mengubah data yang ada pada set

# Namun, kita dapat menambahkan item ke dalam set
this_is_set.add("uwu")
print("this_is_set: ", this_is_set)


this_is_additional_set = {'owo', 'owi'}
this_is_list = [4+1j, 0.4]

# this_is_set.add(this_is_additional_set)
this_is_set.update(this_is_additional_set)
this_is_set.update(this_is_list)
#print("this_is_set: ", this_is_set)

# Selain kita bisa menambahkan element ke dalam set, kita juga bisa menghapusnya
# this_is_set.discard('owo')
# print("this_is_set: ", this_is_set)

# this_is_set.remove(0.4)
# print("this_is_set: ", this_is_set)

# this_is_set.pop()
# print("this_is_set: ", this_is_set)

# this_is_set.clear()
# print("this_is_set: ", this_is_set)

# Join set
this_is_aux_set = {"uwu", 30, 0.3, 4+1j}


#union (gabungan) A v B = this_is_set v this_is_aux_set
this_is_union_set = this_is_set.union(this_is_aux_set)
print(this_is_union_set | this_is_aux_set)
print('this_is_union_set: ', this_is_union_set)

# #intersection (irisan) [2,3,4] ^ [1,3,5] = 3
this_is_intersection_set = this_is_set.intersection(this_is_aux_set)
print(this_is_set & this_is_aux_set)
print('this_is_intersection_set: ', this_is_intersection_set)

# #difference [2,3,4] - [1,3,5] = [2,4]
print(this_is_set - this_is_aux_set)

# #symemetric difference A v B - A ^ B
this_is_symmetric_difference_set = this_is_set.symmetric_difference(this_is_aux_set)
print(this_is_set ^ this_is_aux_set)
print('this_is_symmetric_difference_set: ', this_is_symmetric_difference_set)

#subset dan superset
#himpunan bagian: A ada di B tapi boleh A=B
#himpunan bagian sejati contoh: A himp sejati B = A itu ada di B tapi A != B
s1 = {1, 2}
s2 = {1, 2, 3}
s3 = {3, 4}

print(s1 <= s2) # True
print(s2 >= s1) # True
print(s1 <= s3) # False
print(s1 <= s1) # True