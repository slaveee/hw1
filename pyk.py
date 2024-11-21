# def cheto(int_list):
#     produktik = 1  
#     for num in int_list:
#         produktik *= num  
#     return produktik

# listik = [1, 2, 3, 4]
# result = cheto(listik)
# print(f"произведение списка: {result}")

# def naiti(cheto):
#     if not cheto: 
#         return None  

#     minimum = cheto[0]  
#     for num in cheto:
#         if num < minimum:  
#             minimum = num 
#     return minimum 

# chetko = [3, 1, 4, 1, 5, 9, 2]
# result = naiti(chetko)
# print(f"минимум в списке: {result}")

# def naiti(listik):
#     is_prime = lambda x: x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1))
#     prime_count = sum(1 for number in listik if is_prime(number))
#     return prime_count

# cheto = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# result = naiti(cheto)
# print(f"простых чисел: {result}")

# def cheto(listik, remove):
#     orig = len(listik)
    
#     listik[:] = list(filter(lambda x: x != remove, listik))
    
#     removed_count = orig - len(listik)  
#     return removed_count

# chetko = [1, 2, 3, 4, 2, 5, 2, 6]
# remove = 2
# result = cheto(chetko, remove)

# print(f"удалено: {result}")
# print(f"обновленный список: {chetko}")

# def merge(list1, list2):
#     return list1 + list2

# list_a = [1, 2, 3]
# list_b = [4, 5, 6]
# merged = merge(list_a, list_b)

# print(f"объединенный список: {merged}")

# def kakieto_elements(input_list, cheto):
#     chetko = lambda x: x ** cheto
#     return list(map(chetko, input_list))

# numbers = [1, 2, 3, 4]
# cheto = 2
# result = kakieto_elements(numbers, cheto)

# print(f"результат: {result}")