"""Create a close-up poster from the original Obsidian screenshot pixels."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

root = Path(__file__).resolve().parents[1]
fonts = Path('/System/Library/Fonts/Supplemental')
base = Image.open(root / 'assets/market-cover/original-cover.png').convert('RGB')
base = base.crop((0, 0, 1536, 115)).resize((1536, 1024), Image.Resampling.BICUBIC)
draw = ImageDraw.Draw(base)
draw.text((72, 65), 'BEAR STYLE / FOR OBSIDIAN', font=ImageFont.truetype(str(fonts / 'Arial.ttf'), 20), fill='#747474')
draw.text((68, 112), 'Closer look', font=ImageFont.truetype(str(fonts / 'Baskerville.ttc'), 102), fill='#292929')
draw.rectangle((600, 135, 604, 221), fill='#DD4C4F')
draw.text((72, 244), 'A quiet space to write. Every detail, a little closer.', font=ImageFont.truetype(str(fonts / 'Arial.ttf'), 25), fill='#737373')

shadow = Image.new('RGBA', base.size)
ImageDraw.Draw(shadow).rounded_rectangle((50, 353, 1486, 883), radius=20, fill=(25, 22, 18, 35))
base = Image.alpha_composite(base.convert('RGBA'), shadow.filter(ImageFilter.GaussianBlur(20)))
card = Image.new('RGB', (1436, 530), 'white')
note = Image.open(root / 'assets/market-cover/light.png').convert('RGB')
detail = note.crop((40, 25, 1300, 370)).resize((1386, 380), Image.Resampling.LANCZOS)
card.paste(detail, (25, 75))
mask = Image.new('L', card.size)
ImageDraw.Draw(mask).rounded_rectangle((0, 0, 1435, 529), radius=20, fill=255)
base.paste(card, (50, 335), mask)
draw = ImageDraw.Draw(base)
draw.text((72, 934), 'Real Obsidian capture · Light mode', font=ImageFont.truetype(str(fonts / 'Arial.ttf'), 20), fill='#747474')
draw.text((72, 976), 'Preview includes optional plugins & fonts.', font=ImageFont.truetype(str(fonts / 'Arial.ttf'), 16), fill='#858585')
base.convert('RGB').save(root / 'cover-closer-look.png')
