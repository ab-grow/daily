"""
make_icon.py — turn any photo into a square app icon for the Rule of Life tracker.

Usage:
    python3 make_icon.py my_photo.jpg

Produces icon.png (512x512) in the same folder, ready to replace the
existing icon.png before you deploy.

Requires Pillow: pip install Pillow --break-system-packages
"""
import sys
from PIL import Image, ImageOps, ImageDraw

def make_icon(source_path, output_path="icon.png", size=512, rounded=True):
    img = Image.open(source_path).convert("RGB")

    # Crop to a centered square, then resize
    img = ImageOps.fit(img, (size, size), method=Image.LANCZOS, centering=(0.5, 0.5))

    if rounded:
        # Soft rounded corners so it doesn't look like a hard-edged sticker
        # next to the OS's own rounded icons
        mask = Image.new("L", (size, size), 0)
        draw = ImageDraw.Draw(mask)
        radius = int(size * 0.18)
        draw.rounded_rectangle([0, 0, size, size], radius=radius, fill=255)
        out = Image.new("RGBA", (size, size), (0, 0, 0, 0))
        out.paste(img, (0, 0), mask)
        out.save(output_path)
    else:
        img.save(output_path)

    print(f"Saved {output_path} ({size}x{size})")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 make_icon.py <path-to-photo>")
        sys.exit(1)
    make_icon(sys.argv[1])
