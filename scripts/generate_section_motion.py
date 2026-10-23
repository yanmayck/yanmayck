"""Original section animations. Run from the repository root with Pillow installed.
Diagrams illustrate project capabilities, not live infrastructure telemetry.
"""
from pathlib import Path
import math
from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'assets'
FONT='/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'
def font(n): return ImageFont.truetype(FONT,n)
def save(frames,name):
    frames[0].save(OUT/name,save_all=True,append_images=frames[1:],duration=100,loop=0,optimize=True,disposal=1)
    print(name,(OUT/name).stat().st_size)

def flow(name, labels, accent):
    w,h=480,100
    frames=[]
    positions=[(66+i*116,49) for i in range(4)]
    for i in range(60):
        im=Image.new('RGB',(w,h),'#0D1117');d=ImageDraw.Draw(im)
        for j in range(3):
            x,y=positions[j];end=positions[j+1][0]
            d.line((x+26,y,end-26,y),fill='#303B54',width=2)
            t=(i/30-j*.2)%1;px=x+26+t*(end-x-52)
            d.ellipse((px-3,y-3,px+3,y+3),fill=accent)
        for j,(x,y) in enumerate(positions):
            active=(i//15)%4==j
            if active:d.ellipse((x-26,y-26,x+26,y+26),outline=accent,width=2)
            d.rounded_rectangle((x-19,y-19,x+19,y+19),radius=9,fill='#182136',outline=accent if active else '#45516B')
            # Abstract icons: message, inference, data, delivery.
            if j==0:
                d.rounded_rectangle((x-9,y-6,x+9,y+5),radius=3,outline=accent,width=2)
                d.line((x-5,y+5,x-8,y+10,x+1,y+5),fill=accent,width=2)
            elif j==1:
                for angle in [0,math.pi/2,math.pi,3*math.pi/2]:
                    px=x+9*math.cos(angle+i*math.tau/60);py=y+9*math.sin(angle+i*math.tau/60)
                    d.line((x,y,px,py),fill=accent,width=2);d.ellipse((px-2,py-2,px+2,py+2),fill=accent)
            elif j==2:
                for dy in [-6,0,6]:d.rounded_rectangle((x-9,y+dy-2,x+9,y+dy+2),radius=2,outline=accent)
            else:
                d.line((x-8,y+2,x-2,y+8,x+10,y-7),fill=accent,width=3)
            text=labels[j];tw=d.textlength(text,font=font(11))
            d.text((x-tw/2,82),text,font=font(11),fill=accent if active else '#94A3B8')
        frames.append(im)
    save(frames,name)

def stack():
    w,h=1100,144;frames=[]
    labels=['PYTHON','NEXT.JS','AGNO','POSTGRES','DOCKER','CLOUD']
    colors=['#38BDF8','#E2E8F0','#A78BFA','#38BDF8','#22D3EE','#FBBF24']
    for i in range(60):
        im=Image.new('RGB',(w,h),'#0D1117');d=ImageDraw.Draw(im)
        for j,(label,color) in enumerate(zip(labels,colors)):
            x=20+j*180;rise=int(4*math.sin(i*math.tau/60+j*.8));y=25+rise
            d.rounded_rectangle((x,y,x+158,y+89),radius=12,fill='#131C2D',outline='#303B54')
            # Progress sweep and rotating bracket symbols inside each tile.
            cx=x+79;cy=y+29
            d.arc((cx-15,cy-15,cx+15,cy+15),i*6+j*40,i*6+j*40+240,fill=color,width=2)
            d.text((cx-7,cy-10),'+',font=font(20),fill=color)
            tw=d.textlength(label,font=font(15));d.text((cx-tw/2,y+57),label,font=font(15),fill=color)
            d.line((x+12,y+85,x+12+(i*2+j*20)%134,y+85),fill=color,width=2)
        frames.append(im)
    save(frames,'stack-motion.gif')

def footer(en):
    w,h=1100,210;frames=[]
    for i in range(70):
        im=Image.new('RGB',(w,h),'#0D1117');d=ImageDraw.Draw(im)
        for x in range(0,w,44):d.line((x,0,x,h),fill='#151D2D')
        for y in range(0,h,35):d.line((0,y,w,y),fill='#151D2D')
        title='YAN MAYCK / BACKEND & AI' if en else 'YAN MAYCK / BACKEND E IA'
        tw=d.textlength(title,font=font(26));d.text(((w-tw)/2,30),title,font=font(26),fill='#E2E8F0')
        subtitle='Goiás, Brazil / Python / Next.js / Agno' if en else 'Goiás, Brasil / Python / Next.js / Agno'
        tw=d.textlength(subtitle,font=font(15));d.text(((w-tw)/2,76),subtitle,font=font(15),fill='#94A3B8')
        points=[]
        for k in range(241):
            t=k*math.tau/240
            points.append((w/2+150*math.cos(t)/(1+math.sin(t)**2),150+30*math.sin(t)*math.cos(t)/(1+math.sin(t)**2)))
        d.line(points,fill='#303B54',width=2)
        for tail in range(22):
            t=(i/70-tail/500)*math.tau
            x=w/2+150*math.cos(t)/(1+math.sin(t)**2);y=150+30*math.sin(t)*math.cos(t)/(1+math.sin(t)**2)
            strength=1-tail/22
            c=(int(40+100*strength),int(45+140*strength),int(70+180*strength))
            r=2+strength*2;d.ellipse((x-r,y-r,x+r,y+r),fill=c)
        frames.append(im)
    save(frames,'footer-en.gif' if en else 'footer-pt.gif')

if __name__=='__main__':
    flow('elloai-flow.gif',['WHATSAPP','AI + RAG','CRM','HANDOFF'],'#FBBA16')
    flow('cepi-flow.gif',['APP','SQLITE','SYNC','CLOUD'],'#34D399')
    stack()
    footer(False)
    footer(True)
