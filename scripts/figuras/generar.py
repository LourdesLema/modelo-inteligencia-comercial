"""Genera figuras descriptivas a partir de las tablas agregadas del repositorio."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
EVIDENCE = ROOT / "evidencias"
OUTPUT = ROOT / "salidas_figuras"
OUTPUT.mkdir(exist_ok=True)

COLORS = {
    "Referencia H": "#737373",
    "Regresión lineal": "#B45C16",
    "Random Forest RF09": "#126C8A",
}

# Figura 1: compara el MAE por modelo y corte, sin interpretar la línea como
# continuidad temporal ni como evidencia de estacionalidad.
mae = pd.read_csv(EVIDENCE / "figuras_datos_mae.csv")
mae["corte"] = pd.to_datetime(mae["corte"])
labels = {"2011-03-01": "Marzo\nValidación", "2011-06-01": "Junio\nValidación", "2011-09-01": "Septiembre\nPrueba final"}
fig, ax = plt.subplots(figsize=(8, 5))
for model, group in mae.groupby("modelo", sort=False):
    group = group.sort_values("corte")
    ax.plot(group["corte"], group["MAE_GBP"], marker="o", linewidth=2,
            label=model, color=COLORS[model])
ax.set_xticks(sorted(mae["corte"].unique()))
ax.set_xticklabels([labels[d.strftime("%Y-%m-%d")] for d in sorted(mae["corte"].unique())])
ax.set_ylabel("MAE (GBP)")
ax.set_title("Error absoluto medio por corte y alternativa")
ax.grid(axis="y", alpha=.22)
ax.legend(frameon=False)
fig.tight_layout()
fig.savefig(OUTPUT / "mae_por_corte.png", dpi=300)
fig.savefig(OUTPUT / "mae_por_corte.svg")
plt.close(fig)

# Figura 2: diferencia de concentración frente a H en puntos porcentuales.
concentration = pd.read_csv(EVIDENCE / "figuras_datos_concentracion.csv")
concentration = concentration[concentration["modelo"] != "H"].copy()
concentration["corte"] = pd.to_datetime(concentration["corte"])
concentration["escenario"] = concentration.apply(
    lambda row: f"{row['corte']:%b %Y} · {int(row['capacidad_pct'])} %", axis=1
)
order = concentration[["corte", "capacidad_pct", "escenario"]].drop_duplicates().sort_values(
    ["corte", "capacidad_pct"]
)["escenario"].tolist()
fig, ax = plt.subplots(figsize=(9, 6))
for model, marker in [("Regresión lineal", "s"), ("Random Forest RF09", "^")]:
    group = concentration[concentration["modelo"] == model].set_index("escenario").reindex(order)
    y = range(len(order))
    ax.scatter(group["diferencia_pp"], y, marker=marker, s=48,
               label=model, color=COLORS[model])
ax.axvline(0, color="#555555", linewidth=1)
ax.set_yticks(range(len(order)), order)
ax.invert_yaxis()
ax.set_xlabel("Diferencia frente a H (puntos porcentuales)")
ax.set_title("Concentración retrospectiva por capacidad hipotética")
ax.grid(axis="x", alpha=.22)
ax.legend(frameon=False)
fig.tight_layout()
fig.savefig(OUTPUT / "diferencia_concentracion.png", dpi=300)
fig.savefig(OUTPUT / "diferencia_concentracion.svg")
plt.close(fig)

print(f"Figuras guardadas en: {OUTPUT}")
