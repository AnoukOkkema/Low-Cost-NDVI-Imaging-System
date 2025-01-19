# main.py
from modules.image_processing import ImageProcessor
from modules.ndvi_calculations import NDVICalculator
from modules.visualization import NDVIVisualizer
from modules.segmentation import PlantSegmenter
import numpy as np
import cv2

image_path = "images/image_raspberry-pi-noir-with_blue_filter.png"
image = cv2.imread(image_path)

# Stap 1: Converteer de afbeelding naar RGB
rgb_image = ImageProcessor.convert_to_rgb(image)

# Stap 2: Bereken NDVI van de bijgesneden afbeelding
ndvi_image = NDVICalculator.calculate_ndvi(rgb_image)

# Stap 4: Pas colormaps toe
ndvi_greyscale = NDVICalculator.apply_colormap(ndvi_image, "greyscale")
ndvi_fastie = NDVICalculator.apply_colormap(ndvi_image, "fastie")

# Stap 5: Segmenteer de plant
binary_mask = PlantSegmenter.segment_plant_with_morphology(
    rgb_image, threshold_value=150
)
segmented_image = cv2.bitwise_and(rgb_image, rgb_image, mask=binary_mask)

# Bereken gemiddelde NDVI-waarde na segmentatie
ndvi_segmented = NDVICalculator.calculate_ndvi(segmented_image)
avg_ndvi_value = np.nanmean((ndvi_segmented / 127) - 1)

# Stap 6: Visualiseer de resultaten
NDVIVisualizer.visualize_ndvi(
    image,
    ndvi_greyscale,
    ndvi_fastie,
    avg_ndvi_value,
    padding_colorbar=0.045
)