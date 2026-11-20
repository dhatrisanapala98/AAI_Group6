import subprocess, sys
sys.path.insert(0, __import__('os').path.dirname(__file__))
from figs import person

NAVY = '#0e1d3d'
def wrap(w, h, inner, defs=''):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><defs>{defs}</defs>{inner}</svg>'

def clip(id_, x, y, w, h):
    return f'<clipPath id="{id_}"><rect x="{x}" y="{y}" width="{w}" height="{h}"/></clipPath>'

def bottom_fade(w, h, start):
    return (f'<linearGradient id="bf" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{NAVY}" stop-opacity="0"/><stop offset="1" stop-color="{NAVY}" stop-opacity=".96"/></linearGradient>'
            , f'<rect x="0" y="{start}" width="{w}" height="{h-start}" fill="url(#bf)"/>')

def plant(x, y, s=1):
    leaves = ''.join(f'<ellipse cx="0" cy="-{30+i*18}" rx="14" ry="30" fill="{c}" transform="rotate({a})"/>' for i, (a, c) in enumerate([(-50,'#3f7d3a'),(-20,'#4f9144'),(0,'#3f7d3a'),(22,'#4f9144'),(52,'#3f7d3a')]))
    return (f'<g transform="translate({x},{y}) scale({s})">{leaves}'
            '<path d="M-34,0 L34,0 L26,70 L-26,70Z" fill="#b5532e"/><rect x="-38" y="-8" width="76" height="14" rx="5" fill="#c96a3d"/></g>')

def window_arch(x, y, w, h):
    return (f'<g><path d="M{x},{y+h} V{y+w/2} A{w/2},{w/2} 0 0 1 {x+w},{y+w/2} V{y+h}Z" fill="url(#sky)" stroke="#6a4a2c" stroke-width="14"/>'
            f'<path d="M{x+w/2},{y} V{y+h} M{x},{y+h*0.5} H{x+w}" stroke="#6a4a2c" stroke-width="8"/>'
            f'<circle cx="{x+w*0.72}" cy="{y+h*0.3}" r="34" fill="#ffe29a" opacity=".9"/></g>')

def jaali(x, y, w, h):
    # decorative lattice screen (jaali), a common Indian architectural motif
    cells = []
    n = 6
    for i in range(n):
        for j in range(n):
            cx = x + (i + .5) * w / n; cy = y + (j + .5) * h / n
            cells.append(f'<path d="M{cx},{cy-w/n*0.4} L{cx+w/n*0.4},{cy} L{cx},{cy+w/n*0.4} L{cx-w/n*0.4},{cy}Z" fill="none" stroke="#b8864a" stroke-width="3"/>')
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="#efd9b2"/>' + ''.join(cells)

SKY = '<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8fd0f0"/><stop offset="1" stop-color="#e9f6ff"/></linearGradient>'

def table(w, top, bot):
    return (f'<rect x="0" y="{top}" width="{w}" height="{bot-top}" fill="#9b6a3d"/>'
            f'<rect x="0" y="{top}" width="{w}" height="14" fill="#b98250"/>'
            + ''.join(f'<path d="M0,{top+30+k*22} H{w}" stroke="#00000014" stroke-width="3"/>' for k in range(5)))

def workbook(cx, cy, w=360, h=130):
    return (f'<g transform="translate({cx},{cy})"><path d="M{-w/2},0 L0,-10 L{w/2},0 L{w/2},{h} L0,{h+14} L{-w/2},{h}Z" fill="#ffffff"/>'
            f'<path d="M0,-10 V{h+14}" stroke="#c9c3b5" stroke-width="4"/>'
            + ''.join(f'<path d="M{-w/2+24},{22+k*20} H-18 M18,{22+k*20} H{w/2-24}" stroke="#7a9cc8" stroke-width="2.5"/>' for k in range(5))
            + f'<rect x="{-w/2+24}" y="{h-30}" width="70" height="8" rx="4" fill="#e9b44c"/>'
            f'<g transform="translate(70,60) rotate(-18)"><rect x="0" y="0" width="120" height="9" rx="4" fill="#f2b705"/><path d="M120,0 L138,4.5 L120,9Z" fill="#e9c9a0"/><path d="M131,2.5 L138,4.5 L131,6.5Z" fill="#333"/></g></g>')

# ---------------- parent portrait (1024x1536)
def parent():
    W, H = 1024, 1536
    defs = SKY
    d2, fade = bottom_fade(W, H, 930)
    inner = [f'<rect width="{W}" height="{H}" fill="#f1dfc0"/>',
             f'<rect y="1000" width="{W}" height="{H-1000}" fill="#c9a77a"/>',
             f'<rect width="{W}" height="1000" fill="#f3e2c4"/>']
    inner.append(window_arch(690, 170, 250, 420))
    inner.append(jaali(60, 190, 190, 190))
    # shelf with books, brass lamp
    inner.append('<rect x="40" y="520" width="330" height="16" fill="#7a4c28"/>')
    for i, c in enumerate(['#c1272d', '#1b4f72', '#e0a43a', '#2e7d4f', '#7d3c98', '#c1272d']):
        inner.append(f'<rect x="{62+i*28}" y="{440-(i%3)*10}" width="24" height="{80+(i%3)*10}" fill="{c}"/>')
    inner.append('<path d="M270,520 L300,520 L292,470 L278,470Z" fill="#d4a017"/><path d="M262,470 Q285,440 308,470Z" fill="#e8b92b"/><path d="M285,440 Q278,420 285,404 Q292,420 285,440Z" fill="#ff8c1a"/>')
    inner.append(plant(110, 835, 1.1))
    mb, ma = person(390, 600, 1.18, 'saree', '#b9814f', '#1c1210', 'bun', look='down', bindi=True, earring=True, saree='#0f6b6e')
    db, da = person(660, 690, .98, 'girl', '#c58f5c', '#150d0b', 'plaits', look='down', uniform='#1b2f5b')
    inner.append(f'<g clip-path="url(#cut)">{mb}{db}</g>')
    inner.append(table(W, 905, 1100))
    inner.append(workbook(525, 935))
    inner.append(ma + da)
    # tiffin box + school bag on table edge
    inner.append('<g transform="translate(850,930)"><rect width="120" height="26" rx="8" fill="#b8c2cc"/><rect y="30" width="120" height="26" rx="8" fill="#9aa6b2"/><rect y="60" width="120" height="26" rx="8" fill="#b8c2cc"/><path d="M14,-8 Q60,-34 106,-8" fill="none" stroke="#7a8794" stroke-width="6"/></g>')
    inner.append(fade)
    defs += clip('cut', 0, 0, W, 905) + d2
    return wrap(W, H, ''.join(inner), defs)

# ---------------- classroom (1024x1536)
def classroom():
    W, H = 1024, 1536
    d2, fade = bottom_fade(W, H, 960)
    defs = SKY + d2 + clip('cut2', 0, 0, W, 930)
    inner = [f'<rect width="{W}" height="{H}" fill="#e9dcc0"/>',
             '<rect x="40" y="150" width="944" height="470" rx="10" fill="#7a4c28"/>',
             '<rect x="62" y="172" width="900" height="426" rx="4" fill="#27523f"/>',
             '<path d="M120,250 H520 M120,300 H430 M120,350 H560" stroke="#ffffffc0" stroke-width="7" stroke-linecap="round" opacity=".8"/>',
             '<path d="M640,230 L700,230 L700,290 L640,290Z M700,290 L760,290 L760,350 L700,350Z" fill="none" stroke="#ffffffa0" stroke-width="5"/>',
             '<rect x="62" y="580" width="900" height="18" fill="#6a3f20"/>',
             '<g fill="#fff"><rect x="120" y="560" width="46" height="14" rx="3"/><rect x="190" y="562" width="30" height="12" rx="3" fill="#f6c453"/></g>']
    # ceiling fan
    inner.append('<g transform="translate(512,70)"><rect x="-4" y="-70" width="8" height="70" fill="#555"/><ellipse cx="0" cy="0" rx="36" ry="14" fill="#444"/>'
                 '<ellipse cx="-170" cy="6" rx="130" ry="10" fill="#d8d2c4"/><ellipse cx="170" cy="6" rx="130" ry="10" fill="#d8d2c4"/></g>')
    inner.append(window_arch(40, 650, 150, 260) if False else '')
    tb, ta = person(500, 730, 1.12, 'kurta', '#b27b4b', '#171010', 'bun', glasses=True, bindi=True, earring=True, look='down')
    s1b, s1a = person(255, 830, .92, 'boy', '#c58f5c', '#140d0b', 'short', look='down')
    s2b, s2a = person(770, 820, .92, 'girl', '#bb8452', '#140d0b', 'plaits', look='down', uniform='#1b2f5b', ribbon='#c1272d')
    inner.append(f'<g clip-path="url(#cut2)">{s1b}{s2b}{tb}</g>')
    inner.append('<rect y="925" width="1024" height="200" fill="#a8774a"/><rect y="925" width="1024" height="14" fill="#c08a58"/>')
    inner.append(workbook(512, 960, 420, 140))
    inner.append(ta + s1a + s2a)
    inner.append(f'<rect y="1125" width="{W}" height="{H-1125}" fill="#8c5e36"/>')
    inner.append(fade)
    return wrap(W, H, ''.join(inner), defs)

# ---------------- school building (1080x1440)
def school():
    W, H = 1080, 1440
    defs = ('<linearGradient id="sk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffb066"/><stop offset=".35" stop-color="#ffd9a1"/><stop offset="1" stop-color="#cfeaf7"/></linearGradient>'
            '<linearGradient id="gr" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#7fae5a"/><stop offset="1" stop-color="#4f8a3f"/></linearGradient>')
    i = [f'<rect width="{W}" height="{H}" fill="url(#sk)"/>', '<circle cx="860" cy="300" r="80" fill="#fff1c9" opacity=".85"/>']
    i.append('<path d="M0,760 Q300,700 600,760 T1080,740 V1000 H0Z" fill="#7aa86a" opacity=".5"/>')
    # main building
    B = '#d98a5c'; C = '#f7ead0'
    i.append(f'<rect x="120" y="640" width="840" height="400" fill="{B}"/>')
    i.append(f'<rect x="120" y="640" width="840" height="30" fill="{C}"/><rect x="120" y="1010" width="840" height="30" fill="{C}"/>')
    # centre block with dome (chhatri)
    i.append(f'<rect x="380" y="500" width="320" height="540" fill="{B}"/><rect x="380" y="500" width="320" height="26" fill="{C}"/>')
    i.append(f'<path d="M420,500 Q540,300 660,500Z" fill="{C}"/><path d="M450,500 Q540,340 630,500Z" fill="#e8bb86"/>')
    i.append(f'<rect x="525" y="250" width="30" height="130" fill="#8b5a2b"/><path d="M540,280 Q590,262 640,282 Q590,300 540,300Z" fill="#e0782c"/>')
    for k, x in enumerate([150, 230, 310, 700, 780, 860]):
        for row in (700, 850):
            i.append(f'<path d="M{x},{row+110} V{row+30} A32,32 0 0 1 {x+64},{row+30} V{row+110}Z" fill="#fbe7a8" stroke="{C}" stroke-width="8"/><path d="M{x+32},{row} V{row+110} M{x},{row+60} H{x+64}" stroke="{C}" stroke-width="4"/>')
    # central arched entrance
    i.append(f'<path d="M450,1040 V820 A90,90 0 0 1 630,820 V1040Z" fill="#6a3f20" stroke="{C}" stroke-width="12"/>')
    i.append('<path d="M540,730 V1040" stroke="#4a2b14" stroke-width="5"/>')
    # signboard (fictional name)
    i.append('<rect x="395" y="560" width="290" height="64" rx="8" fill="#12305e"/><text x="540" y="588" font-family="DejaVu Sans, Arial, sans-serif" font-size="22" font-weight="700" fill="#ffffff" text-anchor="middle">STUDENT360</text><text x="540" y="613" font-family="DejaVu Sans, Arial, sans-serif" font-size="17" fill="#f5d27a" text-anchor="middle">VIDYALAYA</text>')
    # ground / courtyard
    i.append('<rect y="1040" width="1080" height="400" fill="url(#gr)"/>')
    i.append('<path d="M420,1040 L660,1040 L860,1440 L220,1440Z" fill="#d9c7a0"/>')
    # trees (neem-like)
    def tree(x, y, s):
        return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-16" y="0" width="32" height="170" fill="#6b4423"/>'
                '<circle cx="0" cy="-30" r="96" fill="#3f7d3a"/><circle cx="-70" cy="20" r="70" fill="#4f9144"/><circle cx="72" cy="16" r="74" fill="#478a3f"/><circle cx="10" cy="-80" r="62" fill="#5aa04d"/></g>')
    i.append(tree(90, 790, 1.0)); i.append(tree(1000, 800, .95))
    # students in uniform (small figures)
    sf = [(300, 1210, .26, 'girl', '#c58f5c', 'plaits'), (370, 1250, .24, 'boy', '#b9814f', 'short'), (720, 1230, .26, 'girl', '#bb8452', 'plaits'), (800, 1265, .24, 'boy', '#c58f5c', 'short'), (560, 1300, .30, 'girl', '#b27b4b', 'plaits')]
    for x, y, s, k, sk, hs in sf:
        b, a = person(x, y, s, k, sk, '#140d0b', hs, look='front')
        cid = f'f{x}'
        defs += clip(cid, x-60, y-40, 120, 40+int(300*s))
        i.append(f'<g clip-path="url(#{cid})">{b}</g>')
        i.append(f'<ellipse cx="{x}" cy="{y+int(300*s)}" rx="{int(70*s*3)}" ry="{int(20*s*3)}" fill="#3f7d3a"/><ellipse cx="{x-int(40*s*3)}" cy="{y+int(300*s)+6}" rx="{int(40*s*3)}" ry="{int(14*s*3)}" fill="#4f9144"/><circle cx="{x+int(30*s*3)}" cy="{y+int(300*s)-4}" r="7" fill="#e84a6f"/><circle cx="{x-int(20*s*3)}" cy="{y+int(300*s)}" r="6" fill="#f6c453"/>')
    i.append('<rect width="1080" height="1440" fill="none"/>')
    return wrap(W, H, ''.join(i), defs)

def render(svg, name, w):
    p = f'./{name}.svg'
    open(p, 'w').write(svg)
    subprocess.run(['rsvg-convert', '-w', str(w), p, '-o', f'./{name}.png'], check=True)

if __name__ == '__main__':
    render(parent(), 'parent_portrait', 1024)
    render(classroom(), 'school_portrait', 1024)
    render(school(), 'school_building', 1080)
    print('done')
