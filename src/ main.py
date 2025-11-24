import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

# 轴标签
likelihood_labels = [
    "Improbable\n(Risk Unlikely to Occur)",
    "Possible\n(Risk Will Likely Occur)",
    "Probable\n(Risk Will Occur)"
]
impact_labels = [
    "0 Acceptable\n(Little or No Effect)",
    "1 Tolerable\n(Effects Felt but Not Critical)",
    "2 Unacceptable\n(Serious Impact)",
    "3 Intolerable\n(Could Result in Disasters)"
]

# 风险等级栅格（0=绿, 1=黄, 2=橙, 3=红）——按示例配色布局
risk_grid = np.array([
    [0, 1, 1, 2],  # Improbable
    [1, 1, 2, 3],  # Possible
    [1, 2, 2, 3],  # Probable
], dtype=int)

# 离散配色
cmap = ListedColormap(["#4caf50", "#ffeb3b", "#ff9800", "#f44336"])

fig, ax = plt.subplots(figsize=(9, 4))
im = ax.imshow(risk_grid, cmap=cmap, vmin=0, vmax=3, aspect="auto")

# 坐标轴与标题
ax.set_yticks(np.arange(len(likelihood_labels)))
ax.set_yticklabels(likelihood_labels)
ax.set_xticks(np.arange(len(impact_labels)))
ax.set_xticklabels(impact_labels, rotation=0, ha="center")
ax.xaxis.set_label_position('top'); ax.xaxis.tick_top()
ax.set_xlabel("Impact"); ax.set_ylabel("Likelihood")
ax.set_title("Likelihood vs. Impact Risk Matrix", pad=35)

# 画白色网格线
for i in range(risk_grid.shape[0] + 1):
    ax.axhline(i - 0.5, color="white", linewidth=1)
for j in range(risk_grid.shape[1] + 1):
    ax.axvline(j - 0.5, color="white", linewidth=1)

# ——可选——在矩阵中标注你的残余风险（li：行=可能性，ii：列=影响）
# 0=Improbable, 1=Possible, 2=Probable；影响列 0..3 如上 labels
example_risks = [
    ("Alg. Bias", 1, 2),   # Possible × Unacceptable
    ("Drift", 2, 1),       # Probable × Tolerable
    ("Privacy", 0, 3),     # Improbable × Intolerable
]
for label, li, ii in example_risks:
    ax.text(ii, li, label, ha="center", va="center",
            fontsize=10, color="black", weight="bold")

plt.tight_layout()
plt.savefig("risk_matrix.png", dpi=200, bbox_inches="tight")
plt.show()

