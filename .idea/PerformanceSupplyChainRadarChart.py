import numpy as np
import matplotlib.pyplot as plt

# 🗂️ Étape 1 : Définir les KPI, les valeurs, les seuils et les maxima
kpis = [
    "Lead Time",
    "Order Fulfillment Rate",
    "Inventory Turnover",
    "Order Accuracy",
    "Supplier Lead Time",
    "Return Rate"
]

# Valeurs réelles des KPI
values = [5.16, 96.77, 3.59, 98.49, 6.48, 1.06]

# Seuils des KPI
seuils = [4, 95, 4, 98, 5, 2]

# Valeurs maximales théoriques des KPI
max_values = [10, 100, 10, 100, 15, 5]

# 🗂️ Étape 2 : Normalisation des valeurs et des seuils
normalized_values = [v / m * 100 for v, m in zip(values, max_values)]
normalized_seuils = [s / m * 100 for s, m in zip(seuils, max_values)]

# Calcul des moyennes des KPI
moyenne_valeurs = np.mean(normalized_values)
moyenne_seuils = np.mean(normalized_seuils)

# Ajouter pour boucler le graphique
normalized_values += normalized_values[:1]
normalized_seuils += normalized_seuils[:1]

# Angles pour le graphique
angles = np.linspace(0, 2 * np.pi, len(kpis), endpoint=False).tolist()
angles += angles[:1]

# 🎨 Étape 3 : Création du Radar Chart
fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(polar=True))  # Taille augmentée (9x9)

# Orientation et sens du graphique
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

# ⭕ Ajouter les grilles (cercles concentriques)
ax.set_rgrids(
    [20, 40, 60, 80, 100],
    labels=["20%", "40%", "60%", "80%", "100%"],
    angle=angles[0],
    color="gray",
    fontsize=10
)
ax.set_ylim(0, 100)

# 📍 Ajouter les noms des KPI autour du radar
ax.set_xticks(angles[:-1])
ax.set_xticklabels(
    kpis,
    fontsize=12,  # Taille légèrement augmentée
    fontweight="bold",
    color="black"
)

# 🔴 Tracer les seuils normés (en rouge pointillé avec remplissage)
ax.plot(angles, normalized_seuils, label="Seuils Minimum", linestyle="dashed", color="red", linewidth=2)
ax.fill(angles, normalized_seuils, color="red", alpha=0.1)

# 🔵 Tracer les valeurs réelles normées (en bleu plein avec remplissage)
ax.plot(angles, normalized_values, label="Valeurs Actuelles", color="blue", linewidth=2)
ax.fill(angles, normalized_values, color="skyblue", alpha=0.4)

# 🟢 Ajouter une ligne circulaire pour la moyenne des valeurs réelles
ax.plot(angles, [moyenne_valeurs] * len(angles), label=f"Valeurs Moyennes ({moyenne_valeurs:.2f}%)", linestyle="solid",
        color="green", linewidth=1.5)

# 🟠 Ajouter une ligne circulaire pour la moyenne des seuils
ax.plot(angles, [moyenne_seuils] * len(angles), label=f"Seuils Moyens ({moyenne_seuils:.2f}%)", linestyle="dotted",
        color="orange", linewidth=1.5)

# 🖋️ Configurer le titre avec espacement ajusté
ax.set_title("Performance Supply Chain - Radar Chart\n(Moyennes et Seuils)", fontsize=16, pad=30, color="black")

# Configurer la légende avec une position plus éloignée
ax.legend(
    loc="upper right",
    bbox_to_anchor=(1.3, 1.2),  # Placer la légende hors du graphique
    fontsize=10
)

# Ajustement final pour réduire le chevauchement
plt.tight_layout()
plt.show()

# 🖨️ Afficher les détails dans la console
print("=== Détails des KPI ===")
for i, kpi in enumerate(kpis):
    print(f"{kpi}: Valeur = {normalized_values[i]:.2f}%, Seuil = {normalized_seuils[i]:.2f}%")
print(f"\nMoyenne des Valeurs Réelles : {moyenne_valeurs:.2f}%")
print(f"Moyenne des Seuils : {moyenne_seuils:.2f}%")