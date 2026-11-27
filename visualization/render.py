"""Render a schematic of primitive orbit lifts with Pillow."""
from math import cos, pi, sin
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

W, H = 720, 376
BG, INK, MUTED = "#fbf8f1", "#173b46", "#47636b"
PALE, GREEN, RUST = "#a3b4b1", "#0a7265", "#b74324"

def font(size):
    try:
        return ImageFont.truetype("DejaVuSans.ttf", size)
    except OSError:
        try:
            return ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", size)
        except OSError:
            return ImageFont.load_default(size=size)

def pose(cx, angle, rotation):
    u, v = cos(angle + rotation), sin(angle + rotation)
    return cx + 117*u, 202 + 57*v + 13*u

def frame(step):
    im=Image.new("RGB", (W,H), BG)
    d=ImageDraw.Draw(im)
    def label(x,y,txt,size,col=INK): d.text((x,y),txt,fill=col,font=font(size))
    def line(cx,start,end,rot,col,width):
        d.line([pose(cx,start+(end-start)*i/120,rot) for i in range(121)], fill=col, width=width)
    def dot(pos,rad,col):
        x,y=pos; d.ellipse((x-rad,y-rad,x+rad,y+rad), fill=col)
    phase=min(1.,step/36)
    rot=-0.8+0.24*sin(2*pi*step/48)
    label(28,14,"Two orbits downstairs, two different lifts",28)
    label(29,59,"Deck group of order 3. Each ring represents a circle in the covering space.",16,MUTED)
    label(30,103,"Nonpolar orbit",21,GREEN);label(394,103,"Polar orbit",21,RUST)
    d.line((359,102,359,333),fill="#dbded7",width=2)
    for cx,turn,col in [(180,1,GREEN),(535,1/3,RUST)]:
        line(cx,0,2*pi,rot,PALE,3)
        if turn<1:
            for j in range(3):dot(pose(cx,2*pi*j/3,rot),5,INK)
        start=pose(cx,0,rot);dot(start,8,INK);dot(start,4,BG)
        line(cx,0,phase*turn*2*pi,rot,col,5)
        dot(pose(cx,phase*turn*2*pi,rot),6,col)
    label(30,292,"One full turn closes upstairs.",17)
    label(394,292,"One third-turn ends on sheet 1.",17)
    label(30,331,"The full lifted circle contracts in the Kotschick manifold.",16,MUTED)
    return im

if __name__=="__main__":
    frames=[frame(i) for i in range(48)]
    target=Path(__file__).with_name("construction.gif")
    frames[0].save(target,save_all=True,append_images=frames[1:],duration=80,loop=0,optimize=True)
