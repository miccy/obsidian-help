## 2025-02-18 - Pillow vs pngquant for PNG Optimization
**Learning:** Python's Pillow library `optimize=True` can sometimes INCREASE the file size of PNGs if the original was already highly optimized or uses a complex palette. `pngquant` (lossy quantization) is often necessary for significant reduction (e.g., 65% reduction for a 1.3MB screenshot) while maintaining acceptable quality for documentation.
**Action:** For documentation images, prefer `pngquant` or similar lossy compressors over simple lossless re-encoding when size reduction is critical.
