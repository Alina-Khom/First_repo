#print("Hello World")

#print("Hello Git")
# Введення (отримання даних)
#ім_я = input("Введіть ваше ім'я:Alina ")

# Перетворення (обробка даних)
#вітання = f"Привіт, {ім_я}!"

# Виведення (виведення даних)
#print(вітання)
def discount_price(price: int, discount: float) -> float:
    def apply_discount():
        nonlocal price
        price = price * (1 - discount)

    apply_discount()
    return price