import cv2
import numpy as np

class ImageProcessor:
    @staticmethod
    def convert_to_rgb(img):
        """Converteer een BGR-afbeelding naar RGB."""
        img = np.clip(img, 0, 255).astype(np.uint8)
        return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    @staticmethod
    def crop_image(image, crop_region=None, save_path=None, show_image=False):
        """
        Snijd een afbeelding bij op basis van opgegeven coördinaten.

        Parameters:
        - image: De originele afbeelding (numpy array).
        - crop_region: Een tuple (x1, x2, y1, y2) die de crop-regio specificeert.
          Als dit None is, wordt een standaard crop-regio gebruikt.
        - save_path: Pad om de bijgesneden afbeelding op te slaan. Indien None, wordt niet opgeslagen.
        - show_image: Boolean om aan te geven of de afbeelding getoond moet worden.

        Returns:
        - cropped: De bijgesneden afbeelding (numpy array).
        """
        h, w, _ = image.shape
        if crop_region is None:
            crop_x1, crop_x2 = int(w * 0.15), int(w * 0.8)  # Houd 65% van de breedte
            crop_y1, crop_y2 = int(h * 0.25), int(h * 0.95)  # Houd 70% van de hoogte
        else:
            crop_x1, crop_x2, crop_y1, crop_y2 = crop_region

        cropped = image[crop_y1:crop_y2, crop_x1:crop_x2]

        if save_path:
            cv2.imwrite(save_path, cropped)
        
        if show_image:
            import matplotlib.pyplot as plt
            plt.imshow(cropped)
            plt.show()

        return cropped