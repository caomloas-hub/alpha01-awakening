"""Mechanical resize/padding only; never redraw the commissioned artwork."""
import argparse
from pathlib import Path
from PIL import Image, ImageDraw

parser = argparse.ArgumentParser()
parser.add_argument('source', type=Path)
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
source = Image.open(args.source).convert('RGBA')
yellow = source.getpixel((0, 0))
background = Image.new('RGBA', (1080, 1080), yellow)
foreground = Image.new('RGBA', (1080, 1080), (0, 0, 0, 0))
source.thumbnail((620, 620), Image.Resampling.LANCZOS)
foreground.alpha_composite(source, ((1080-source.width)//2, (1080-source.height)//2))
background.save(root/'android-icon_background.png')
foreground.save(root/'android-icon_foreground.png')
# Preview Android's central visible area and circular launcher mask.
merged = Image.alpha_composite(background, foreground).crop((180, 180, 900, 900))
mask = Image.new('L', merged.size, 0)
ImageDraw.Draw(mask).ellipse((0, 0, 719, 719), fill=255)
merged.putalpha(mask)
out = root/'tests/screenshots'
out.mkdir(parents=True, exist_ok=True)
merged.resize((192, 192), Image.Resampling.LANCZOS).save(out/'android-icon-circle.png')
