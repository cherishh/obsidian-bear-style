"""Compose an editorial dark cover with untouched Obsidian screenshot crops."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
ROOT=Path(__file__).resolve().parents[1]
W,H=1800,1200
im=Image.new('RGB',(W,H),'#111315')
d=ImageDraw.Draw(im)
fonts=Path('/System/Library/Fonts/Supplemental')
def font(name,size):return ImageFont.truetype(str(fonts/name),size)
def text(pos,s,size=24,color='#a2a3a4',name='Arial.ttf'):
 d.text(pos,s,font=font(name,size),fill=color)
# Brand and message occupy the top band; the genuine note takes the whole lower band.
text((90,62),'BEAR STYLE  /  FOR OBSIDIAN',21,'#91a5b3')
text((84,106),'A quiet space to write.',112,'#e6e8e9','Baskerville.ttc')
d.rectangle((92,259,160,263),fill='#44a2e5')
text((186,246),'Familiar type. Room to think. A softer kind of dark.',27,'#a2a3a4')
text((1407,69),'DARK GRAPHITE',20,'#44a2e5')
# Two editorial crops of the same real note; no text or icons are recreated.
shot=Image.open(ROOT/'assets/market-cover/dark.png').convert('RGB')
card=(80,347,1720,1045)
d.rounded_rectangle(card,radius=22,fill='#1d1e1f',outline='#33373b',width=2)
d.line((903,397,903,994),fill='#34383b',width=1)
left=shot.crop((30,25,1410,765)).resize((760,408),Image.Resampling.LANCZOS)
right=shot.crop((30,780,1410,1530)).resize((760,413),Image.Resampling.LANCZOS)
im.paste(left,(111,420));im.paste(right,(936,420))
text((126,945),'01   /   CAPTURE A THOUGHT',18,'#8194a1')
text((954,945),'02   /   GIVE IT ROOM',18,'#8194a1')
# A small functional palette key anchors the otherwise spacious second column.
for i,c in enumerate(['#ccdbe5','#44a2e5','#355f3a','#a2a3a4']):
 x=957+i*43
 d.ellipse((x,877,x+15,892),fill=c)
text((90,1100),'Bear Style',31,'#dfe0e0','Baskerville.ttc')
text((1290,1107),'Real notes. Actual theme.',20,'#91a5b3')
text((90,1150),'Preview includes optional plugins & fonts.',17,'#727d84')
im.save(ROOT/'cover-dark-editorial.png')
