import cv2
import numpy as np

class PlantSegmenter:
    @staticmethod
    def segment_plant_with_morphology(image, threshold_value=30, kernel_size=5):
        """Segmenteer de plant met een bilateraal filter en morfologische operaties."""
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.bilateralFilter(gray, d=9, sigmaColor=75, sigmaSpace=75)
        blurred_uint8 = np.uint8(255 * (blurred / np.max(blurred)))
        _, binary_mask = cv2.threshold(blurred_uint8, threshold_value, 255, cv2.THRESH_BINARY)
        return binary_mask