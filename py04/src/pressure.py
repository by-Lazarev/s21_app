import random
import time

def emit_gel(step):
    """Генератор, который создает значения давления жидкости."""
    pressure = random.uniform(20, 80)  # Начальное давление в безопасных пределах
    while True:
        # Случайное изменение давления в пределах [0, step]
        change = random.uniform(0, step)
        pressure += change

        if pressure > 100:
            yield 100  # Верхний предел
        else:
            yield pressure
        
        # Экстренное завершение, если давление выходит за пределы 10-90
        if pressure > 90 or pressure < 10:
            print("Emergency break: Pressure out of bounds (10, 90). Shutting down...")
            return  # Завершаем генератор

def valve(step):
    """Управление давлением с учетом пределов и изменением шага."""
    generator = emit_gel(step)
    current_step = step
    pressure = next(generator)
    
    while True:
        print(f"Current pressure: {pressure:.2f}")
        
        if pressure < 20 or pressure > 80:
            # Изменяем знак шага
            current_step = -current_step
            generator = emit_gel(abs(current_step))
        
        if 10 < pressure < 90:
            pressure += current_step
        else:
            break
        
        # Ждем перед следующим измерением для избежания нагрузки на процессор
        time.sleep(0.1)

if __name__ == "__main__":
    valve(5)  # Пример с шагом 5

