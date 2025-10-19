from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = Path(__file__).resolve().parents[1]
output_path = BASE_DIR / "img" / "og-image.png"
output_path.parent.mkdir(parents=True, exist_ok=True)

img = Image.new("RGB", (1200, 630), "#1d4ed8")
draw = ImageDraw.Draw(img)

font_title = None
font_subtitle = None
font_path = Path("C:/Windows/Fonts/arial.ttf")
if font_path.exists():
    font_title = ImageFont.truetype(str(font_path), 96)
    font_subtitle = ImageFont.truetype(str(font_path), 44)
else:
    font_title = ImageFont.load_default()
    font_subtitle = ImageFont.load_default()

title = "IndiaMoneyCalc"
subtitle = "Free Financial Calculators"

title_bbox = draw.textbbox((0, 0), title, font=font_title)
title_width = title_bbox[2] - title_bbox[0]
title_height = title_bbox[3] - title_bbox[1]

subtitle_bbox = draw.textbbox((0, 0), subtitle, font=font_subtitle)
subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
subtitle_height = subtitle_bbox[3] - subtitle_bbox[1]

draw.text(((1200 - title_width) / 2, 200), title, fill="white", font=font_title)
draw.text(((1200 - subtitle_width) / 2, 320), subtitle, fill="white", font=font_subtitle)

img.save(output_path, format="PNG")
print(f"OG image written to {output_path}")
