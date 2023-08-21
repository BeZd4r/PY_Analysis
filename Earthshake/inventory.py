from plotly import colors

filename = "inventory/color_scales.txt"
with open(filename, "w") as f:
    for color_scale in colors.PLOTLY_SCALES.keys():
        f.write(f"{color_scale}\n")