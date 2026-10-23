"""Generate original profile animations. Run from repository root with Pillow installed."""
from pathlib import Path
import math
from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parents[1] / 'assets'
FONTS = Path('/usr/share/fonts/truetype/dejavu')
def font(size, bold=False):
    return ImageFont.truetype(str(FONTS / ('DejaVuSansMono-Bold.ttf' if bold else 'DejaVuSansMono.ttf')), size)
def save(frames, name):
    frames[0].save(OUT / name, save_all=True, append_images=frames[1:], duration=90, loop=0, optimize=True, disposal=1)
    print(name, (OUT / name).stat().st_size, 'bytes')

def header():
    w,h=1200,300
    base=Image.new('RGB',(w,h))
    pix=base.load()
    for y in range(h):
        for x in range(w):
            glow=max(0,1-math.hypot((x-950)/780,(y-140)/370))
            pix[x,y]=(int(9+14*glow),int(13+7*glow),int(24+32*glow))
    d=ImageDraw.Draw(base)
    for x in range(0,w,40):d.line((x,0,x,h),fill='#1A2032')
    for y in range(0,h,40):d.line((0,y,w,y),fill='#1A2032')
    d.text((44,30),'YANMAYCK / SOFTWARE DEVELOPER',font=font(14),fill='#22D3EE')
    d.text((40,76),'Yan Mayck',font=font(72,True),fill='#F8FAFC')
    d.text((44,178),'BACKEND & APPLIED AI',font=font(23,True),fill='#C4B5FD')
    d.text((44,230),'GOIÁS, BRASIL / PYTHON / NEXT.JS',font=font(15),fill='#94A3B8')
    d.rounded_rectangle((772,56,1150,246),radius=14,fill='#090D18',outline='#3B3B60',width=2)
    d.line((773,94,1149,94),fill='#353553')
    for x,c in [(795,'#FB7185'),(815,'#FBBF24'),(835,'#34D399')]:d.ellipse((x-5,70,x+5,80),fill=c)
    d.text((794,112),'~/yanmayck',font=font(17),fill='#94A3B8')
    d.text((814,205),'~/projects',font=font(16),fill='#34D399')
    frames=[]
    for i in range(120):
        im=base.copy();d=ImageDraw.Draw(im)
        phase=i%40
        command=['python main.py','git push origin main','cd ~/projects'][i//40]
        visible=command[:min(len(command),int(phase*0.8))]
        d.text((794,152),'$ '+visible,font=font(17),fill='#22D3EE')
        if phase%10<6:
            x=794+int(d.textlength('$ '+visible,font=font(17)))
            d.rectangle((x+3,154,x+11,173),fill='#A78BFA')
        pulse=0.5+0.5*math.sin(i*math.tau/40)
        d.ellipse((795,211,803,219),fill=(30,int(140+70*pulse),140))
        # Moving signal along the baseline, with a fading tail.
        d.line((44,278,1150,278),fill='#29334D',width=2)
        x=44+(i/119)*1106
        for tail in range(80,0,-1):
            xx=int(x-tail)
            if xx>=44:
                v=1-tail/80
                d.line((xx,277,xx,280),fill=(int(25+9*v),int(40+171*v),int(70+168*v)))
        d.ellipse((x-3,275,x+3,281),fill='#67E8F9')
        # Orbiting dots keep movement visible even while text pauses.
        for j in range(3):
            angle=i*math.tau/120+j*math.tau/3
            px=700+32*math.cos(angle);py=150+66*math.sin(angle)
            d.ellipse((px-3,py-3,px+3,py+3),fill=['#22D3EE','#A78BFA','#34D399'][j])
        frames.append(im)
    save(frames,'profile-header.gif')

def terminal(en):
    lines=(['$ whoami','Developer in Goiás, Brazil. Python first.','$ cat focus.txt','Backend / applied AI / products in production','$ cat learning.txt','C++ / planning to study Computer Science'] if en else ['$ whoami','Sou o Yan, de Goiás. Programo em Python.','$ cat focus.txt','Backend / IA aplicada / produtos em produção','$ cat learning.txt','C++ / quero cursar Ciência da Computação'])
    base=Image.new('RGB',(1000,262),'#0D1117');d=ImageDraw.Draw(base)
    d.rounded_rectangle((1,1,998,260),radius=15,outline='#30394E',width=2)
    d.line((2,38,997,38),fill='#30394E')
    for x,c in [(23,'#FB7185'),(43,'#FBBF24'),(63,'#34D399')]:d.ellipse((x-4,16,x+4,24),fill=c)
    d.text((100,10),'yan@dev:~ / about',font=font(13),fill='#94A3B8')
    frames=[]
    for i in range(120):
        im=base.copy();d=ImageDraw.Draw(im)
        current=min(5,i//17)
        for row in range(current+1):
            value=lines[row]
            if row==current: value=value[:min(len(value),int((i-current*17)/12*len(value)))]
            y=52+row*31
            d.text((24,y),value,font=font(18),fill='#22D3EE' if row%2==0 else '#CBD5E1')
            if row==current and i%10<6:
                x=24+int(d.textlength(value,font=font(18)))
                d.rectangle((x+3,y+3,x+11,y+20),fill='#A78BFA')
        frames.append(im)
    save(frames,'terminal-en.gif' if en else 'terminal-pt.gif')

if __name__=='__main__':
    header()
    terminal(False)
    terminal(True)
