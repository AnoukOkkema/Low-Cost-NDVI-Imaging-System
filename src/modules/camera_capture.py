import cv2
import numpy as np
import time
from picamera2 import Picamera2
import matplotlib.pyplot as plt

class CameraHandler:
    def __init__(self):
        self.cam = Picamera2()
        self.camera_config = self.cam.create_preview_configuration(
            raw={"size": (1640, 1232)}, main={"format": "RGB888"}
        )
        self.cam.configure(self.camera_config)

    def start_camera(self):
        """Start de camera en wacht tot deze stabiel is."""
        self.cam.start()
        time.sleep(2)  # Wacht even om de camera te stabiliseren

    def capture_image(self, save_path="images/image.png", show_image=False):
        """Maak een foto, sla deze op en toon de afbeelding optioneel."""
        original = self.cam.capture_array()
        original = cv2.flip(original, 0)  # Flip de afbeelding indien nodig
        cv2.imwrite(save_path, original)
        if show_image:
            plt.imshow(original)
            plt.show()
        return original