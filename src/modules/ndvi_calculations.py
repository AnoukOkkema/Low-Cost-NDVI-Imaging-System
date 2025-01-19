import cv2
import numpy as np
import json

class NDVICalculator:
    @staticmethod
    def calculate_ndvi(image, lower_limit=5):
        """Bereken de NDVI-waarden van een RGB-afbeelding."""
        b, g, r = cv2.split(image)
        top = (b.astype(float) - r.astype(float))
        bottom = (b.astype(float) + r.astype(float))
        bottom[bottom < lower_limit] = lower_limit
        ndvi = (((top / bottom) + 1) * 127).astype('uint8')
        return ndvi

    @staticmethod
    def apply_colormap(ndvi, colormap_name):
        """Pas een colormap toe op de NDVI-afbeelding."""
        custom_colormap = NDVICalculator.create_colormap_from_json(colormap_name)
        return cv2.applyColorMap(ndvi, custom_colormap)

    @staticmethod
    def create_colormap_from_json(colormap_name="default"):
        """Maak een colormap op basis van JSON-specificaties."""
        with open('lib/colormaps.json', 'r') as f:
            colormaps = json.load(f)
        colormap_ranges = colormaps[f"{colormap_name}"]["colormapRanges"]
        colormap = np.zeros((256, 1, 3), dtype=np.uint8)
        for i in range(256):
            t = i / 255.0
            for j in range(len(colormap_ranges) - 1):
                if colormap_ranges[j][0] <= t <= colormap_ranges[j + 1][0]:
                    t_range = (t - colormap_ranges[j][0]) / (colormap_ranges[j + 1][0] - colormap_ranges[j][0])
                    color1 = np.array(colormap_ranges[j][1])
                    color2 = np.array(colormap_ranges[j + 1][1])
                    color = (1 - t_range) * color1 + t_range * color2
                    colormap[i, 0, :] = color
                    break
        return colormap