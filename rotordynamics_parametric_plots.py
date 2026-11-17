"""
Parametric Rotordynamics & Centrifugal Stress Visualization
Author: Wahid Eman Kalyan (Jadavpur University - Mechanical Engineering)
Generates summary charts from ANSYS 2023 R2 modal & static structural results.
"""

import os
import matplotlib.pyplot as plt
import numpy as np

# 1. ANSYS Simulation Datasets
stiffness_labels = ["1", "10³", "10⁵", "10⁷", "10⁹"]
crit_speed_vs_k = [16188, 16188, 16255, 21648, 26861]  # rpm

radii_crit_mm = [50, 75, 100, 125, 150]
crit_speed_vs_r = [73495, 26861, 15132, 9766.3, 6799]  # rpm

rpm_stress = [10000, 18000, 20000, 30000, 40000]
stress_vs_rpm_mpa = [39.08, 126.62, 156.32, 351.73, 625.30]  # MPa

radii_stress_mm = [50, 100, 125, 150]
stress_vs_r_mpa = [14.88, 294.81, 493.97, 701.78]  # MPa

# Structural Steel limits (ANSYS Engineering Data)
YIELD_MPA = 250.0
UTS_MPA = 460.0

plt.style.use("seaborn-v0_8-whitegrid")
fig, axes = plt.subplots(2, 2, figsize=(13, 9), dpi=160)
fig.suptitle(
    "High-Speed Rotor Parametric FEA Summary (ANSYS 2023 R2 — Structural Steel)",
    fontsize=14,
    fontweight="bold",
    y=0.98,
)

# Panel A: 1st Critical Speed vs Bearing Stiffness
ax = axes[0, 0]
bars = ax.bar(stiffness_labels, crit_speed_vs_k, color="#4f46e5", width=0.55)
ax.set_title("1st Critical Speed vs. Bearing Stiffness", fontweight="bold")
ax.set_xlabel("Bearing Stiffness k (N/m)")
ax.set_ylabel("1st Critical Speed (rpm)")
ax.set_ylim(0, 32000)
for bar in bars:
    h = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, h + 600, f"{h:,.0f}", ha="center", va="bottom", fontsize=9)

# Panel B: 1st Critical Speed vs Outer Radius
ax = axes[0, 1]
ax.plot(radii_crit_mm, crit_speed_vs_r, marker="o", linewidth=2.5, markersize=7, color="#0284c7")
for x, y in zip(radii_crit_mm, crit_speed_vs_r):
    ax.annotate(f"{y:,.0f}", (x, y), textcoords="offset points", xytext=(0, 8), ha="center", fontsize=8.5)
ax.set_title("1st Critical Speed vs. Rotor Outer Radius (k = 10⁹ N/m)", fontweight="bold")
ax.set_xlabel("Outer Radius r (mm)")
ax.set_ylabel("1st Critical Speed (rpm)")
ax.set_ylim(0, 84000)

# Panel C: Peak von-Mises Stress vs Rotational Speed
ax = axes[1, 0]
ax.plot(rpm_stress, stress_vs_rpm_mpa, marker="s", linewidth=2.5, markersize=7, color="#dc2626", label="Peak von-Mises Stress")
ax.axhline(YIELD_MPA, color="#d97706", linestyle="--", linewidth=1.5, label="Yield Strength (250 MPa)")
ax.axhline(UTS_MPA, color="#7f1d1d", linestyle=":", linewidth=1.8, label="Ultimate Tensile Strength (460 MPa)")
for x, y in zip(rpm_stress, stress_vs_rpm_mpa):
    ax.annotate(f"{y:.1f}", (x, y), textcoords="offset points", xytext=(0, 8), ha="center", fontsize=8.5)
ax.set_title("Centrifugal Stress vs. Rotational Speed", fontweight="bold")
ax.set_xlabel("Rotational Speed (rpm)")
ax.set_ylabel("Equivalent Stress (MPa)")
ax.set_ylim(0, 720)
ax.legend(fontsize=8.5, loc="upper left")

# Panel D: Peak von-Mises Stress vs Rotor Outer Radius
ax = axes[1, 1]
ax.plot(radii_stress_mm, stress_vs_r_mpa, marker="^", linewidth=2.5, markersize=7, color="#9333ea", label="Peak von-Mises Stress")
ax.axhline(YIELD_MPA, color="#d97706", linestyle="--", linewidth=1.5, label="Yield Strength (250 MPa)")
ax.axhline(UTS_MPA, color="#7f1d1d", linestyle=":", linewidth=1.8, label="Ultimate Tensile Strength (460 MPa)")
for x, y in zip(radii_stress_mm, stress_vs_r_mpa):
    ax.annotate(f"{y:.1f}", (x, y), textcoords="offset points", xytext=(0, 8), ha="center", fontsize=8.5)
ax.set_title("Centrifugal Stress vs. Rotor Outer Radius", fontweight="bold")
ax.set_xlabel("Outer Radius r (mm)")
ax.set_ylabel("Equivalent Stress (MPa)")
ax.set_ylim(0, 800)
ax.legend(fontsize=8.5, loc="upper left")

plt.tight_layout(rect=[0, 0, 1, 0.95])
out_path = os.path.join(os.path.dirname(__file__), "..", "images", "07_parametric_trends.png")
plt.savefig(out_path, dpi=160)
print("Saved:", os.path.abspath(out_path))
