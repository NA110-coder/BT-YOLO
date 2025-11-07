import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Data (percentages from the sample)
labels = ['Slice A', 'Slice B', 'Slice C', 'Slice D', 'Slice E']
sizes  = [20, 40, 17, 23, 25]  # matches your example

# Normalize to fractions
total = sum(sizes)
fracs = [s / total for s in sizes]

# Colors (IEEE-friendly palette)
colors = ['#1f77b4', '#17becf', '#2ca02c', '#ff7f0e', '#7f7f7f']

# Compute start/end angles
angles = np.cumsum([0] + [f * 2*np.pi for f in fracs])
start_angles = angles[:-1]
end_angles   = angles[1:]

# Dome & base heights
radius      = 1.0
base_height = 0.3
dome_bulge  = 0.15
resolution  = 200

def build_dome_slice(start, end, radius, base_h, dome_h, color):
    thetas = np.linspace(start, end, resolution)
    x_out = radius * np.cos(thetas)
    y_out = radius * np.sin(thetas)

    # Bottom face (z=0)
    verts_bot = [(x_out[i], y_out[i], 0) for i in range(len(thetas))]
    verts_bot.append((0, 0, 0))
    bottom_polys = []
    for i in range(len(verts_bot)-2):
        bottom_polys.append([verts_bot[i], verts_bot[i+1], verts_bot[-1]])

    # Top face (domed)
    frac = np.linspace(0, 1, resolution)
    z_top_vals = base_h + dome_h * np.sin(np.pi * frac)
    verts_top = [(x_out[i], y_out[i], z_top_vals[i]) for i in range(len(thetas))]
    verts_top.append((0,0,base_h))
    top_polys = []
    for i in range(len(verts_top)-2):
        top_polys.append([verts_top[i], verts_top[i+1], verts_top[-1]])

    # Side walls (outer)
    wall_polys = []
    for i in range(len(thetas)-1):
        bl = (x_out[i], y_out[i], 0)
        br = (x_out[i+1], y_out[i+1], 0)
        tr = (x_out[i+1], y_out[i+1], z_top_vals[i+1])
        tl = (x_out[i], y_out[i], z_top_vals[i])
        wall_polys.append([bl, br, tr])
        wall_polys.append([bl, tr, tl])

    # Radial edges
    x_s, y_s = radius*np.cos(start), radius*np.sin(start)
    x_e, y_e = radius*np.cos(end),   radius*np.sin(end)
    z_s = base_h + dome_h * np.sin(0)
    z_e = base_h + dome_h * np.sin(1*np.pi)
    tri_left  = [(0,0,0), (x_s,y_s,0), (x_s,y_s,z_s)]
    tri_right = [(0,0,0), (x_e,y_e,0), (x_e,y_e,z_e)]

    all_polys = bottom_polys + top_polys + wall_polys + [tri_left, tri_right]
    coll = Poly3DCollection(all_polys, facecolors=color, edgecolors='k', linewidths=0.2)
    coll.set_alpha(1.0)
    return coll

fig = plt.figure(figsize=(12,8))
ax  = fig.add_subplot(111, projection='3d')
ax.view_init(elev=30, azim=-50)

# Draw slices
for (s,e,c) in zip(start_angles, end_angles, colors):
    poly = build_dome_slice(s, e, radius, base_height, dome_bulge, c)
    ax.add_collection3d(poly)

# Leader lines & labels
for i, (s,e) in enumerate(zip(start_angles, end_angles)):
    mid = 0.5*(s+e)
    x_mid = radius*np.cos(mid)
    y_mid = radius*np.sin(mid)
    z_mid = base_height + dome_bulge

    x_lbl = 1.3*np.cos(mid)
    y_lbl = 1.3*np.sin(mid)
    z_lbl = z_mid + 0.02

    ax.plot([x_mid, x_lbl], [y_mid, y_lbl], [z_mid, z_lbl], 'gray', linestyle='--', linewidth=1)
    ax.text(x_lbl, y_lbl, z_lbl, f"{sizes[i]}%", ha='center', va='center',
            fontsize=12, fontweight='bold',
            bbox=dict(boxstyle="circle,pad=0.3", facecolor='white', edgecolor='none'))

# Clean up axes
ax.set_xticks([]); ax.set_yticks([]); ax.set_zticks([])
ax.xaxis.pane.fill = False; ax.yaxis.pane.fill = False; ax.zaxis.pane.fill = False
ax.grid(False)
ax.set_box_aspect((1,1,0.6))

# Title
ax.set_title("3D CHART DIAGRAM\nINFOGRAPHIC", fontsize=20, fontweight='bold', pad=40)

# Save at high resolution
plt.savefig('/data/abbas/Data/graphs/infographic_3d_pie_matplotlib.png', dpi=300, bbox_inches='tight')
plt.show()
