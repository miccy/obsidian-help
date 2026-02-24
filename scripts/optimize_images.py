import os
import sys
from PIL import Image

def optimize_image(filepath):
    try:
        if not os.path.exists(filepath):
            print(f"File not found: {filepath}")
            return

        original_size = os.path.getsize(filepath)

        with Image.open(filepath) as img:
            # Optimize: quantize to 256 colors, method 2 (fast octree)
            # This is effective for screenshots and diagrams common in documentation
            optimized_img = img.quantize(colors=256, method=2)
            optimized_img.save(filepath, optimize=True)

        new_size = os.path.getsize(filepath)
        reduction = original_size - new_size
        percent = (reduction / original_size) * 100

        if reduction > 0:
            print(f"Optimized {filepath}: {original_size/1024:.2f}KB -> {new_size/1024:.2f}KB (-{percent:.1f}%)")
        else:
            print(f"Skipped {filepath}: No reduction achieved.")

    except Exception as e:
        print(f"Error optimizing {filepath}: {e}")

if __name__ == "__main__":
    # List of files to target for this specific optimization pass
    # These were identified as the largest PNGs in the en/Attachments folder
    files_to_optimize = [
        "en/Attachments/bases-map-places.png",
        "en/Attachments/notion-token.png",
        "en/Attachments/Roam-Importer-importing.png",
        "en/Attachments/linking-to-a-header-with-double-hashtags.png",
        "en/Attachments/application-installer-current-version.png",
        "en/Attachments/link-to-a-double-block.png",
        "en/Attachments/version-history-collaboration.png",
        "en/Attachments/Style-guide-modal-example.png",
        "en/Attachments/notion-export-2.png",
        "en/Attachments/Mac-OS-DateTime.png"
    ]

    print("Starting optimization...")
    # Adjust paths to be relative to repo root if running from scripts/
    # Assumes script is run from repo root: python3 scripts/optimize_images.py
    for file in files_to_optimize:
        if os.path.exists(file):
            optimize_image(file)
        else:
            # Try adjusting for script location if run from inside scripts/
            adjusted_path = os.path.join("..", file)
            if os.path.exists(adjusted_path):
                optimize_image(adjusted_path)
            else:
                print(f"Could not find {file}")

    print("Optimization complete.")
