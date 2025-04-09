import numpy as np
import matplotlib.pyplot as plt

# 🗂️ Étape 1 : Définir les KPI, les valeurs et les seuils
kpis = ["Lead Time", "Order Fulfillment Rate", "Inventory Turnover",
        "Order Accuracy", "Supplier Lead Time", "Return Rate"]

# Valeurs réelles des KPI (exemple)
values = [5.16, 96.77, 3.59, 98.49, 6.48, 1.06]

# Seuils des KPI (elles représentent les valeurs minimales attendues pour être en "OK")
seuils = [4, 95, 4, 98, 5, 2]

# Hypothèses pour normaliser les KPI (valeurs maximales possibles pour chaque KPI)
max_values = [10, 100, 10, 100, 10, 5]  # Exemple de max pour chaque KPI
normalized_values = [v / m * 100 for v, m in zip(values, max_values)]  # Normalisation des valeurs
normalized_seuils = [s / m * 100 for s, m in zip(seuils, max_values)]  # Normalisation des seuils

# 🗂️ Étape 2 : Préparation des données pour boucler le diagramme
normalized_values += normalized_values[:1]  # Ajouter la première valeur pour boucler
normalized_seuils += normalized_seuils[:1]  # Ajouter le premier seuil pour boucler
angles = np.linspace(0, 2 * np.pi, len(kpis), endpoint=False).tolist()
angles += angles[:1]  # Ajouter le premier angle pour boucler le graphe

# 🎨 Étape 3 : Création d'un Radar Chart propre et organisé
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))  # Taille et graphe polaire
ax.set_theta_offset(np.pi / 2)  # Alignement à 12h
ax.set_theta_direction(-1)  # Sens anti-horaire

# ⭕ Ajouter les toiles du radar chart (cercles concentriques)
ax.set_rgrids([20, 40, 60, 80, 100], labels=["20%", "40%", "60%", "80%", "100%"],
              angle=angles[0], color="gray", fontsize=10)
ax.set_ylim(0, 100)  # Plage de valeurs fixes pour le Y (de 0 à 100)

# 📍 Ajouter les noms des KPI autour du radar chart
ax.set_xticks(angles[:-1])
ax.set_xticklabels(kpis, fontsize=12, fontweight="bold", color="black")

# 🔴 Tracer les chiffres "seuils" (en rouge, pointillés)
ax.plot(angles, normalized_seuils, label="Seuils", linestyle="dashed", color="red", linewidth=2)
ax.fill(angles, normalized_seuils, color="red", alpha=0.1)  # Transparence des seuils

# 🔵 Tracer les "valeurs actuelles" (en bleu, pleines)
ax.plot(angles, normalized_values, label="Valeurs Actuelles", color="blue", linewidth=2)
ax.fill(angles, normalized_values, color="skyblue", alpha=0.4)  # Transparence des valeurs réelles

# 🖋️ Ajouter un titre et personnaliser la mise en page
ax.set_title("Performance Supply Chain - Radar Chart", fontsize=16, pad=20, color="black")
ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.2), fontsize=12)  # Légende ajustée à droite

# Appliquer une mise en page propre
plt.tight_layout()
plt.show()