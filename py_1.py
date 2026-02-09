# sentence_one = "Hello world"
# sentence_two = "Hello " + "world"
# Відображення змінних
# print(sentence_one, sentence_two, sep='\n')
#
# # Перевірка рівності і ідентичності
# print(f'Are sentence equal? {sentence_one == sentence_two}')
# print(f'Are sentence identical? {sentence_one is sentence_two}')
#
# # Перевірка місця збереження у памяті
# print(f'Path of sentence in memory {id(sentence_one)}')
# print(f'Path of sentence in memory {id(sentence_two)}')
# FLOORS = 5
# APARTMENTS_PER_FLOOR = 4
#
# apartment_number = int(input('Enter apartment number: '))
# apartments_per_entrance = FLOORS * APARTMENTS_PER_FLOOR
# entrance_number = (apartment_number - 1) // apartments_per_entrance + 1
# floor_number = ((apartment_number - 1) % apartments_per_entrance) // APARTMENTS_PER_FLOOR + 1
# print(f"Entrance number {entrance_number}, Floor number {floor_number}")

# my_list = [[1, 2, 3, 5], [7, 346, 235, 235], 347, -435, -23, 0]
#
# print(my_list.index)
# print(my_list[1][1:3])


# def analyze_number(number):
#     if number > 0 and number % 2 == 0:
#         return "Positive even number"
#     elif number > 0 and number % 2 == 1:
#         return "Positive odd number"
#     elif number < 0 and number % 2 == 0:
#         return "Negative even number"
#     elif number < 0 and number % 2 != 0:
#         return "Negative odd number"
#     else:
#         return "Zero"


# number = int(input("Enter a number: "))
# print(analyze_number(number))


