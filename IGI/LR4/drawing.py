"""
Lab Work #4 - Task 4: Shape Drawing Module
Version: 1.0
Developer: Variant 24
Date: 2024
Description: Draw GeometricFigure instances using matplotlib patches.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Polygon as MplPolygon
import os


def draw_figure(figure, label: str = "", output_file: str = "task4_figure.png"):
    """
    Draw the given geometric figure, fill it with its color, add a text label,
    and save to a PNG file.

    Args:
        figure: GeometricFigure instance with .vertices(), .color, .info().
        label (str): Caption text to display below the figure.
        output_file (str): PNG file path.
    """
    verts = figure.vertices()
    xs = [v[0] for v in verts]
    ys = [v[1] for v in verts]

    margin = max(max(xs) - min(xs), max(ys) - min(ys)) * 0.25 + 0.5

    fig, ax = plt.subplots(figsize=(8, 6))
    fig.patch.set_facecolor("#1e1e2e")
    ax.set_facecolor("#1e1e2e")

    poly = MplPolygon(verts, closed=True, facecolor=figure.color,
                      edgecolor="#cdd6f4", linewidth=2.0, alpha=0.85)
    ax.add_patch(poly)

    # Mark vertices
    for x, y in verts:
        ax.plot(x, y, "o", color="#cdd6f4", markersize=5, zorder=3)

    # Axes
    ax.axhline(0, color="#45475a", linewidth=0.6)
    ax.axvline(0, color="#45475a", linewidth=0.6)

    ax.set_xlim(min(xs) - margin, max(xs) + margin)
    ax.set_ylim(min(ys) - margin, max(ys) + margin)
    ax.set_aspect("equal")
    ax.tick_params(colors="#cdd6f4")
    for spine in ax.spines.values():
        spine.set_color("#45475a")

    # Figure info as text box
    info_text = figure.info()
    fig.text(0.02, 0.98, info_text, transform=fig.transFigure,
             fontsize=8, color="#cdd6f4", verticalalignment="top",
             fontfamily="monospace",
             bbox=dict(facecolor="#313244", edgecolor="#45475a",
                       boxstyle="round,pad=0.5"))

    # User label
    caption = label if label else figure.__class__.__name__
    ax.set_title(caption, color="#cdd6f4", fontsize=13, pad=10)

    plt.tight_layout()
    plt.savefig(output_file, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"[Draw] Фигура сохранена → {output_file}")
