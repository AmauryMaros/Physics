import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as constant

# Définition des paramètres
hbar = constant.hbar
omega_0 = 1
omega_1 = 1
Omega = np.sqrt(omega_0**2 + omega_1**2)

# Hamiltonien
H = (hbar / 2) * np.array([[omega_0, omega_1], [omega_1, -omega_0]])

# Diagonalisation de l'Hamiltonien
E, V = np.linalg.eigh(H)

# Définition de l'état initial
psi_plus = np.array([1, 0])
psi_minus = np.array([0, 1])    

# Changement de base
coeffs = np.dot(V.T.conj(), psi_plus)

# Définition de la fonction d'évolution temporelle
def evolution(t):
    return coeffs[0] * np.exp(-1j * E[0] * t / hbar) * V[:, 0] + coeffs[1] * np.exp(-1j * E[1] * t / hbar) * V[:, 1]

# Calcul de la probabilité de transition P+-(t)
def proba(t):
    psi_t = evolution(t)
    return np.abs(np.dot(psi_minus.conj(), psi_t))**2

# Génération des données pour le tracé
t_vals = np.linspace(0, 10, 1000)
P_vals = np.array([proba(t) for t in t_vals])

# Formule de Rabi analytique
P_analytic = (omega_1/Omega)**2 * np.sin(Omega * t_vals / 2)**2

# Calcul de la dérivée numérique
dP_dt = np.gradient(P_vals, t_vals)

# Trouver les indices où la dérivée change de signe
maxima_indices = np.where((dP_dt[:-1] > 0) & (dP_dt[1:] < 0))[0]
minima_indices = np.where((dP_dt[:-1] < 0) & (dP_dt[1:] > 0))[0]

# Fréquence d'oscillation graphique
T = t_vals[maxima_indices[1]] - t_vals[maxima_indices[0]]
omega_rabi = 1/T

print(f"Fréquence d'oscillation analyique: {Omega / (2*np.pi)} Hz")
print(f"Fréquence d'oscillation graphique: {omega_rabi} Hz")

# Tracé
plt.figure(figsize=(10, 5))
# Tracés de P analytique et P numerique
plt.plot(t_vals, P_vals, color = 'blue', label=r"Numérique", linestyle="-")
plt.plot(t_vals, P_analytic, color = 'red', label=r"Analytique", linestyle="--")
# Tracés des min et max locaux
plt.scatter(t_vals[maxima_indices], P_vals[maxima_indices], color='orange', label='Maxima locaux')
plt.scatter(t_vals[minima_indices], P_vals[minima_indices], color='green', label='Minima locaux')
# Frequence de Rabi
# plt.text(x=7.5, y=0.35, s=f"Fréquence de Rabi = {omega_rabi:.3f} Hz")
plt.xlabel(r"Temps $t$")
plt.ylabel(r"$P_{+-}(t)$")
plt.title(r"Représentation graphique de la formule de Rabi")
plt.legend()
plt.xlim((0, 3*np.pi))
plt.grid(False)
plt.show()


# Définition des couples (omega_0, omega_1)
# couples = [(1, 1), (1, 2), (1, 5), (2, 2), (2, 5), (5, 5)]
couples = [(1, 1), (1, 2), (1, 5), (1, 5), (2, 5), (5, 5)]

fig, axs = plt.subplots(2, 3, figsize=(18, 10))
axs = axs.flatten()

hbar = constant.hbar
for ax, (omega_0, omega_1) in zip(axs, couples):
    Omega = np.sqrt(omega_0**2 + omega_1**2)
    H = (hbar / 2) * np.array([[omega_0, omega_1], [omega_1, -omega_0]])
    E, V = np.linalg.eigh(H)

    psi_plus = np.array([1, 0])
    psi_minus = np.array([0, 1])    
    coeffs = np.dot(V.T.conj(), psi_plus)

    def evolution(t):
        return coeffs[0] * np.exp(-1j * E[0] * t / hbar) * V[:, 0] + coeffs[1] * np.exp(-1j * E[1] * t / hbar) * V[:, 1]

    def proba(t):
        psi_t = evolution(t)
        return np.abs(np.dot(psi_minus.conj(), psi_t))**2

    t_vals = np.linspace(0, 10, 1000)
    P_vals = np.array([proba(t) for t in t_vals])
    P_analytic = (omega_1/Omega)**2 * np.sin(Omega * t_vals / 2)**2

    dP_dt = np.gradient(P_vals, t_vals)
    maxima_indices = np.where((dP_dt[:-1] > 0) & (dP_dt[1:] < 0))[0]
    minima_indices = np.where((dP_dt[:-1] < 0) & (dP_dt[1:] > 0))[0]

    T = t_vals[maxima_indices[1]] - t_vals[maxima_indices[0]]
    omega_rabi = 1 / T

    ax.plot(t_vals, P_vals, color='blue', label="Numérique", linestyle="-")
    ax.plot(t_vals, P_analytic, color='red', label="Analytique", linestyle="--")
    ax.scatter(t_vals[maxima_indices], P_vals[maxima_indices], color='orange', label='Maxima locaux')
    ax.scatter(t_vals[minima_indices], P_vals[minima_indices], color='green', label='Minima locaux')

    ax.set_xlim((0, 3*np.pi))
    ax.set_ylim((0, 1))
    ax.set_xlabel(r"Temps $t$")
    ax.set_ylabel(r"$P_{+-}(t)$")
    ax.set_title(fr"$\omega_0$ = {omega_0}, $\omega_1$ = {omega_1}")
    ax.grid(False)

# Légende commune
handles, labels = axs[0].get_legend_handles_labels()
fig.legend(handles, labels, loc='lower center', ncol=4, bbox_to_anchor=(0.5, -0.02))

plt.tight_layout()
plt.subplots_adjust(bottom=0.12)
plt.show()
