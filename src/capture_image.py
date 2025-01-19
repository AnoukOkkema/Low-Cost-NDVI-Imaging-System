from modules.camera_capture import CameraHandler
from modules.image_processing import ImageProcessor
import numpy as np

# Initialiseer de CameraHandler
camera_handler = CameraHandler()

# Start de camera en maak een foto
camera_handler.start_camera()
captured_image = camera_handler.capture_image(save_path="images/image_name.png", show_image=False)

# Stap 2: Bijsnijden van de afbeelding. 
# Note: Dit is alleen als je Arducam 5MP gebruikt of als je de afbeelding wil croppen

# cropped_image = ImageProcessor.crop_image(
#     rgb_image,
#     save_path="images/cropped_image.png",
#     show_image=True
# )