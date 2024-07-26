import queue
import random
import time
import threading
from colorama import init, Fore, Style

init()                                              # Ініціалізуємо colorama

request_queue = queue.Queue()                       # Створюємо чергу заявок

running = True                                      # Створюємо глобальну змінну для контролю роботи програми

def generate_request():
    """Створюємо нову заявку та додаємо її до черги."""
    while running:
        request_id = random.randint(1, 120)         # Створюємо унікальний номер заявки
        print(Fore.RED + f"Нова заявка: {request_id}" + Style.RESET_ALL)
        request_queue.put(request_id)                # Додаємо заявку до черги
        time.sleep(random.randint(1, 3))             # Очікуємо для імітації часу між новими заявками

def process_request():
    """Обробляємо заявку з черги."""
    while running:
        if not request_queue.empty():
            request_id = request_queue.get()         # Видаляємо заявку з черги
            print(f"Обробка заявки: {request_id}")
            time.sleep(random.randint(1, 5))         # Очікуємо, імітуючи обробку заявки
            print(Fore.GREEN + f"Заявка {request_id} оброблена." + Style.RESET_ALL)
        else:
            print("Черга пуста. Очікування нових заявок.")  # Очікуємо нові заявки
            time.sleep(2)                            # Очікуємо перед наступною перевіркою черги

if __name__ == "__main__":
    print("Для переривання роботи натисніть Ctrl+C") # Повідомлення для користувача

    try:
        generator_thread = threading.Thread(target=generate_request)  # Створюємо потоки для генерування заявок
        processor_thread = threading.Thread(target=process_request)   # Створюємо потоки для обробки заявок

        generator_thread.start()                                      # Запускаємо потоки
        processor_thread.start()                                   

        while True:
            time.sleep(1)                            # Очікуємо, поки користувач не завершить програму (натискання Ctrl+C)

    except KeyboardInterrupt:
        print("Завершення роботи програми...")       # Обробляємо завершення роботи за допомогою Ctrl+C
        running = False
        generator_thread.join()                      # Очікуємо завершення потоків
        processor_thread.join()                      
        print("Програма завершена.")
