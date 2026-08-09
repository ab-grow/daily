"""
make_icon.py — Turn any photo into polished square app icons.

Usage examples:
    python3 make_icon.py photo.png
    python3 make_icon.py photo.png --size 512 --radius 0.2
    python3 make_icon.py photo.png --sizes 512 256 192 128
    python3 make_icon.py photo.png --no-round --output my_icon.png
"""

import argparse
import sys
from pathlib import Path
from PIL import Image, ImageOps, ImageDraw

def make_icon(
    source_path: str,
    output_path: str = None,
    size: int = 512,
    radius: float = 0.18,
    rounded: bool = True,
):
    source = Path(source_path)
    if not source.exists():
        raise FileNotFoundError(f"Image not found: {source}")

    img = Image.open(source).convert("RGBA")

    # Crop to centered square + high-quality resize
    img = ImageOps.fit(img, (size, size), method=Image.Resampling.LANCZOS, centering=(0.5, 0.5))

    if rounded:
        # Soft rounded corners
        mask = Image.new("L", (size, size), 0)
        draw = ImageDraw.Draw(mask)
        corner_radius = int(size * radius)
        draw.rounded_rectangle([0, 0, size - 1, size - 1], radius=corner_radius, fill=255)

        output = Image.new("RGBA", (size, size), (0, 0, 0, 0))
        output.paste(img, (0, 0), mask)
    else:
        output = img

    # Decide output filename
    if output_path is None:
        output_path = source.with_name(f"icon_{size}.png")

    output.save(output_path, "PNG")
    print(f"✓ Saved {output_path}  ({size}×{size})")
    return output_path

def main():
    parser = argparse.ArgumentParser(
        description="Create square app icons from any photo",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument("image", help="Path to the source image (PNG, JPG, etc.)")
    parser.add_argument("-o", "--output", help="Custom output filename")
    parser.add_argument("-s", "--size", type=int, default=512, help="Icon size in pixels (default: 512)")
    parser.add_argument("--sizes", nargs="+", type=int, help="Create multiple sizes (e.g. --sizes 512 256 128)")
    parser.add_argument("-r", "--radius", type=float, default=0.18,
                        help="Corner radius as fraction of size (0.0–0.5, default: 0.18)")
    parser.add_argument("--no-round", action="store_true", help="Disable rounded corners")

    args = parser.parse_args()

    try:
        if args.sizes:
            for s in args.sizes:
                out = None
                if args.output:
                    # e.g. icon.png → icon_512.png
                    p = Path(args.output)
                    out = str(p.with_name(f"{p.stem}_{s}{p.suffix}"))
                make_icon(
                    args.image,
                    output_path=out,
                    size=s,
                    radius=args.radius,
                    rounded=not args.no_round,
                )
        else:
            make_icon(
                args.image,
                output_path=args.output,
                size=args.size,
                radius=args.radius,
                rounded=not args.no_round,
            )
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()