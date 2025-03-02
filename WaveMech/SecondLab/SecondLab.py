import numpy as np
import matplotlib.pyplot as plt

# Параметры
c = 1
H = 1
eps_omega = 0.1
omegas = np.linspace(eps_omega, 10, 100)
a = 1  # Параметр 'a' для функции Q(alpha)

# Вычисление alphas
alphas = []
for i in range(len(omegas)):
    cur_alphas = [omegas[i] / c]
    kappa_sq = omegas[i]**2 / c**2
    k = 1
    under_sqrt = kappa_sq - np.pi**2 * k**2 / H**2
    while under_sqrt > 0:
        cur_alphas.append(np.sqrt(under_sqrt))
        k += 1
        under_sqrt = kappa_sq - np.pi**2 * k**2 / H**2
    alphas.append(cur_alphas)

# Функция Q(alpha)
def Q(alpha, a):
    numerator = -np.pi * np.cos(a * alpha)
    denominator = a * (alpha**2 - (np.pi / (2 * a))**2)
    return numerator / denominator

# Вычисление Q(alpha) для каждого alpha
Q_values = []
for i in range(len(alphas)):
    Q_cur = []
    for alpha in alphas[i]:
        Q_cur.append(Q(alpha, a))
    Q_values.append(Q_cur)

# Построение графика Q(alpha)
plt.figure()
for i in range(len(omegas)):
    for k in range(len(alphas[i])):
        plt.scatter(omegas[i], Q_values[i][k], color=(k/5, 0, 1-k/5))

plt.xlabel('omegas')
plt.ylabel('Q(alpha)')
plt.title('График Q(alpha) в зависимости от omegas')
plt.show()