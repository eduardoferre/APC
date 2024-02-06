data = str(input())

dd, mm, aa = data[0:2], data[3:5], data[6:8]

print(f'{dd}-{mm}-{aa}')
print(f'{mm}-{dd}-{aa}')
print(f'{aa}/{mm}/{dd}')


