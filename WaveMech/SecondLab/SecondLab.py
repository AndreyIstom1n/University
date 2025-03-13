import numpy as np
import matplotlib.pyplot as plt

c = 1
H = 1
eps_omega = 0.1
omegas = np.linspace(eps_omega, 10, 100)

alphas = []
for i in range(100):
    cur_alphas = [omegas[i] / c]
    kappa_sq = omegas[i]**2 / c**2
    k = 1
    under_sqrt = kappa_sq - np.pi**2 * k**2 / H**2
    while under_sqrt > 0:
        cur_alphas.append(np.sqrt(under_sqrt))
        k += 1
        under_sqrt = kappa_sq - np.pi**2 * k**2 / H**2
    alphas.append(cur_alphas)

plt.figure()
for i in range(100):
    for k in range(len(alphas[i])):
        color = (k / len(alphas[i]), 0, 1 - k / len(alphas[i]))
        plt.scatter(omegas[i], alphas[i][k], color=color)
plt.xlabel('Частота (ω)')
plt.ylabel('α')
plt.title('Дисперсионное соотношение')
plt.show()