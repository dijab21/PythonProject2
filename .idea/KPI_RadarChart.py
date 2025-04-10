import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colormaps
import os  # Pour manipuler des fichiers et ouvrir directement une image

# ---------------------------------------------
# Étape 1 : Données d'entrée
# ---------------------------------------------
# Liste des KPI
kpis = ["Lead Time", "Order Fulfillment Rate", "Inventory Turnover",
        "Order Accuracy", "Supplier Lead Time", "Return Rate"]

# Valeurs réelles et seuils minimaux à atteindre
values = [5.16, 96.77, 3.59, 98.49, 6.48, 1.06]
seuils = [4, 95, 4, 98, 5, 2]

# Valeurs maximales pour normalisation (hypothèses métiers)
max_values = [10, 100, 10, 100, 10, 5]

# Normalisation des valeurs et des seuils (échelle 0-100)
normalized_values = [v / m * 100 for v, m in zip(values, max_values)]
normalized_seuils = [s / m * 100 for s, m in zip(seuils, max_values)]

# Bouclage pour fermer le radar chart
normalized_values += normalized_values[:1]
normalized_seuils += normalized_seuils[:1]
angles = np.linspace(0, 2 * np.pi, len(kpis), endpoint=False).tolist()
angles += angles[:1]

# ---------------------------------------------
# Étape 2 : Création du radar chart
# ---------------------------------------------
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Palette de couleurs
colors = colormaps["tab10"].colors

# Alignement et direction des axes
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

# Ajouter les noms des KPI autour de la toile
ax.set_xticks(angles[:-1])
ax.set_xticklabels(kpis, fontsize=13, fontweight="bold")

# Ajouter des cercles concentriques (grilles)
ax.set_rgrids([20, 40, 60, 80, 100], labels=["Faible", "Moyenne", "Bonne", "Excellente", ""],
              angle=angles[0], color="gray", fontsize=11)
ax.set_ylim(0, 100)

# Tracer la zone des seuils (rouge, lignes pointillées)
ax.plot(angles, normalized_seuils, linestyle="dashed", color="red", linewidth=2, label="Seuils Minimaux")
ax.fill(angles, normalized_seuils, color="red", alpha=0.1)

# Tracer la zone des valeurs réelles (bleu, lignes pleines)
ax.plot(angles, normalized_values, color="blue", linewidth=2, label="Valeurs Actuelles")
ax.fill(angles, normalized_values, color="skyblue", alpha=0.4)

# Annoter chaque KPI avec sa valeur exacte
for angle, value, kpi, normalized_value in zip(angles[:-1], normalized_values[:-1], kpis, values):
    ax.text(
        angle, normalized_value + 8, f"{value:.2f}",
        color="blue", fontsize=12, fontweight="bold",
        ha="center", va="center", bbox=dict(facecolor="white", alpha=0.7, edgecolor="blue")
    )

# Titre et légende
ax.set_title("Radar Chart - Performance des KPI Supply Chain", fontsize=18, pad=20, color="black", fontweight="bold")
ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.2), fontsize=12, frameon=True, facecolor="white")

# ---------------------------------------------
# Étape 3 : Sauvegarde et affichage du résultat
# ---------------------------------------------
output_file = "radar_chart.png"  # Nom du fichier de sortie
plt.tight_layout()

# Sauvegarder le graphique dans un fichier PNG
plt.savefig(output_file, dpi=300)

# Ouvrir automatiquement le fichier PNG après sa sauvegarde
# Compatible avec Windows et d'autres systèmes
if os.name == "nt":  # Windows
    os.startfile(output_file)
else:  # macOS et Linux
    os.system(f"open {output_file}")

# Afficher dans la console si besoin
print(f"Le radar chart a été sauvegardé : {os.path.abspath(output_file)}")
