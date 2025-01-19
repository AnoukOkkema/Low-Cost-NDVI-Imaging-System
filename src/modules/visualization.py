import matplotlib.pyplot as plt

class NDVIVisualizer:
    @staticmethod
    def visualize_ndvi(original_rgb, color_mapped_image_grey, color_mapped_image_fastie, ndvi_value, padding_colorbar):
        """Visualiseer NDVI-resultaten."""
        fig, axes = plt.subplots(1, 3, figsize=(18, 6))
        axes[0].imshow(original_rgb)
        axes[0].set_title("Original RGB")
        axes[0].axis("off")

        axes[1].imshow(color_mapped_image_grey)
        axes[1].set_title("NDVI (Greyscale Colormap)")
        axes[1].axis("off")

        img = axes[2].imshow(color_mapped_image_fastie)
        axes[2].set_title(f"NDVI ({ndvi_value:.4f})")
        axes[2].axis("off")

        cbar = fig.colorbar(img, ax=axes[2], orientation="horizontal", fraction=0.05, pad=padding_colorbar)
        cbar.set_ticks([0, 64, 128, 192, 255])
        cbar.set_ticklabels(["-1", "-0.5", "0", "0.5", "1"])
        cbar.set_label("NDVI Range (-1 to 1)")

        normalized_value = int((ndvi_value + 1) / 2 * 255)
        cbar.ax.axvline(x=normalized_value, color="red", lw=2)

        plt.tight_layout()
        plt.show()