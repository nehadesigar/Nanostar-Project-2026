import zarr
import json
import numpy as np
import napari
from napari.utils import Colormap
import os

def make_alpha_bounded_red_colormap(alpha_min, alpha_max, n_control=256):
    t = np.linspace(0, 1, n_control)
    alpha = alpha_min + t * (alpha_max - alpha_min)
    colors = np.zeros((n_control, 4))
    colors[:, 0] = 1.0
    colors[:, 3] = alpha
    return Colormap(colors, name="red_bounded_alpha")

def load_and_view(output_dir):
    zarr_path = os.path.join(output_dir, "final_density.zarr")
    with open(os.path.join(output_dir, "render_metadata.json")) as f:
        meta = json.load(f)

    rho = zarr.open(zarr_path, mode="r")   # lazy — not loaded into memory yet

    cmap = make_alpha_bounded_red_colormap(meta["alpha_min"], meta["alpha_max"])

    viewer = napari.Viewer(ndisplay=3)
    viewer.add_image(
        rho,
        name="component_1",
        colormap=cmap,
        rendering="translucent",
        contrast_limits=meta["contrast_limits"],
        blending="translucent",
        interpolation3d="linear",
    )
    return viewer

sim_name = input("Enter simulation name (format 3D_A_20_B2_2190): ")
output_dir = os.path.join("OUTPUTS", sim_name)

viewer = load_and_view("OUTPUTS/3D_A_20_B2_2190")
napari.run()