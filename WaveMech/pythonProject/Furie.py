import numpy as np
import matplotlib.pyplot as plt

# Параметр a
a = 2
# Функция, для которой вычисляем преобразование Фурье
def f(x):
    return np.cos((np.pi * x) / (2 * a))

# Создаем массив x
x = np.linspace(-a, a, 1000)

# Вычисляем функцию f(x)g
y = f(x)

# Вычисляем прямое преобразование Фурье
fourier_transform = np.fft.fft(y)

# Вычисляем частоты
freq = np.fft.fftfreq(len(x), d=(2 * a / len(x)))

# Вычисляем обратное преобразование Фурье
inverse_fourier_transform = np.fft.ifft(fourier_transform)

# Создание графика
plt.figure(figsize=(10, 6))

# График исходной функции
plt.plot(x, y, label='Исходная функция $f(x) = \\cos\\left(\\frac{\\pi x}{2a}\\right)$', color='blue')

# График обратного преобразования Фурье
plt.plot(x, np.real(inverse_fourier_transform), label='Обратное преобразование Фурье', color='red', linestyle='dashed')

# Настройка графика
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Исходная функция и Обратное преобразование Фурье')
plt.grid()
plt.legend()

# Отображение графиков
plt.axhline(0, color='black', lw=0.5, ls='--')  # Добавление линии Y=0
plt.axvline(0, color='black', lw=0.5, ls='--')  # Добавление линии X=0

plt.show()