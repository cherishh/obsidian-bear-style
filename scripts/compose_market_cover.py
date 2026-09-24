from PIL import Image, ImageDraw, ImageFilter
from pathlib import Path
import argparse
parser=argparse.ArgumentParser()
parser.add_argument('--mode', choices=['light', 'dark'], default='light')
mode=parser.parse_args().mode
root=Path(__file__).resolve().parents[1]
base=Image.open(root/'assets/market-cover/original-cover.png').convert('RGB')
# Keep the original left branding; remove the old right card using its blank backdrop.
backdrop=base.crop((630,0,1536,115)).resize((906,1024),Image.Resampling.BICUBIC)
base.paste(backdrop,(630,0))
if mode == 'dark':
    # Recolor only the original branding; preserve its exact raster letterforms.
    # The document screenshot below is never recolored.
    pixels=[]
    for r,g,b in base.getdata():
        ink=max(0,min(1,(248-(r+g+b)/3)/210))
        if r-g > 45 and r-b > 40:
            ink=max(0,min(1,(r-g)/145))
            fg=(68,162,229)
        else:
            fg=(223,224,224)
        pixels.append(tuple(round(bg+(f-bg)*ink) for bg,f in zip((23,24,25),fg)))
    base.putdata(pixels)
note=Image.open(root/f'assets/market-cover/{mode}.png').convert('RGB')
card=note.resize((860,850),Image.Resampling.LANCZOS)
rounded=Image.new('L',card.size);ImageDraw.Draw(rounded).rounded_rectangle((0,0,859,849),radius=18,fill=255)
shadow=Image.new('RGBA',base.size)
ImageDraw.Draw(shadow).rounded_rectangle((650,88,1510,938),radius=18,fill=(0,0,0,100) if mode == 'dark' else (25,22,18,35))
shadow=shadow.filter(ImageFilter.GaussianBlur(18))
base=Image.alpha_composite(base.convert('RGBA'),shadow)
base.paste(card,(650,70),rounded)
if mode == 'dark':
    ImageDraw.Draw(base).rounded_rectangle((650,70,1509,919),radius=18,outline=(51,53,55),width=1)
base.convert('RGB').save(root/f'cover-{mode}.png')
