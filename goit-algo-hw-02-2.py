from collections import deque

def is_palindrome(input_string):
    
    cleaned_string = ''.join(char.lower() for char in input_string if char.isalnum())  # Видаляємо пробіли та перетворюємо всі символи на нижній регістр

   
    char_deque = deque(cleaned_string)                   # Створюємо deque і заповнює його очищеними символами рядка

    # Порівнюємо символи з обох кінців черги
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():     # Видаляємо символи з обох кінців і порівнюємо їх
            return f'"{input_string}" - Це непаліндром'  # Якщо символи не збігаються, повертаємо результат, що рядок не є паліндромом
    
    return f'"{input_string}" - Це паліндром'            # Якщо всі символи збігаються, повертаємо результат що рядок є паліндромом

print(is_palindrome("Zaraz"))
print(is_palindrome('A baba na Voli - CILovana baba'))
print(is_palindrome("Radio GaGa"))

