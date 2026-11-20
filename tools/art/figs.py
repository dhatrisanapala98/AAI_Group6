"""Flat-vector Indian school illustrations: reusable figure helpers."""
import math

def face(skin, look='down', glasses=False, bindi=False, smile=True, earring=False, blush='#e08a7a'):
    s = []
    # ears
    s.append(f'<ellipse cx="-60" cy="6" rx="9" ry="14" fill="{skin}"/><ellipse cx="60" cy="6" rx="9" ry="14" fill="{skin}"/>')
    if earring:
        s.append('<circle cx="-60" cy="24" r="5" fill="#d9a441"/><circle cx="60" cy="24" r="5" fill="#d9a441"/>')
    s.append(f'<ellipse cx="0" cy="0" rx="58" ry="66" fill="{skin}"/>')
    s.append(f'<ellipse cx="-30" cy="26" rx="14" ry="8" fill="{blush}" opacity=".35"/><ellipse cx="30" cy="26" rx="14" ry="8" fill="{blush}" opacity=".35"/>')
    dy = 8 if look == 'down' else 0
    for x in (-24, 24):
        if look == 'down':
            s.append(f'<ellipse cx="{x}" cy="{3+dy//2}" rx="10" ry="6.5" fill="#ffffff"/><circle cx="{x}" cy="{6+dy//2}" r="5.2" fill="#2a1a14"/>'
                     f'<path d="M{x-12},{-1+dy//2} Q{x},{-6+dy//2} {x+12},{-1+dy//2}" fill="none" stroke="#2a1a14" stroke-width="3.4" stroke-linecap="round"/>')
        else:
            s.append(f'<ellipse cx="{x}" cy="-2" rx="6" ry="7.5" fill="#2a1a14"/><circle cx="{x+2}" cy="-4" r="2" fill="#fff"/>')
        s.append(f'<path d="M{x-14},{-17+dy//2} Q{x},{-25+dy//2} {x+14},{-17+dy//2}" fill="none" stroke="#1f130e" stroke-width="3.4" stroke-linecap="round"/>')
    s.append('<path d="M0,6 Q-4,18 2,22" fill="none" stroke="#00000030" stroke-width="3" stroke-linecap="round"/>')
    if smile:
        s.append('<path d="M-16,38 Q0,52 16,38" fill="none" stroke="#8a3b34" stroke-width="3.4" stroke-linecap="round"/>')
    else:
        s.append('<path d="M-10,42 L10,42" stroke="#8a3b34" stroke-width="3.4" stroke-linecap="round"/>')
    if bindi:
        s.append('<circle cx="0" cy="-30" r="4.5" fill="#c1272d"/>')
    if glasses:
        s.append('<g fill="#ffffff" fill-opacity=".12" stroke="#3b2a20" stroke-width="3"><circle cx="-24" cy="0" r="17"/><circle cx="24" cy="0" r="17"/></g><path d="M-7,-2 H7" stroke="#3b2a20" stroke-width="3"/>')
    return ''.join(s)

def hair_back(style, color):
    if style == 'bun':
        return f'<circle cx="0" cy="-78" r="26" fill="{color}"/><ellipse cx="0" cy="-12" rx="64" ry="74" fill="{color}"/>'
    if style == 'plaits':
        return f'<ellipse cx="0" cy="-12" rx="64" ry="72" fill="{color}"/>'
    if style == 'long':
        return f'<path d="M-66,-10 Q-70,110 -40,130 L40,130 Q70,110 66,-10 Q60,-80 0,-82 Q-60,-80 -66,-10Z" fill="{color}"/>'
    return f'<ellipse cx="0" cy="-14" rx="62" ry="70" fill="{color}"/>'

def hair_front(style, color):
    if style == 'short':
        return f'<path d="M-60,-6 Q-62,-70 0,-72 Q62,-70 60,-6 Q50,-40 12,-46 Q-30,-44 -60,-6Z" fill="{color}"/><path d="M-60,-6 Q-30,-44 12,-46" fill="none" stroke="#ffffff22" stroke-width="3"/>'
    # centre parting for girls/women
    return (f'<path d="M-60,4 Q-64,-70 0,-72 Q64,-70 60,4 Q58,-34 0,-48 Q-58,-34 -60,4Z" fill="{color}"/>'
            f'<path d="M0,-72 L0,-46" stroke="#c1272d" stroke-width="3.5" opacity=".9"/>')

def plaits(color, ribbon):
    out = []
    for sx in (-1, 1):
        x = sx * 70
        out.append(f'<path d="M{x},20 Q{x+sx*14},90 {x-sx*4},170 Q{x-sx*14},190 {x-sx*10},215" fill="none" stroke="{color}" stroke-width="26" stroke-linecap="round"/>')
        for k in range(5):
            yy = 50 + k * 30
            out.append(f'<path d="M{x-12},{yy} L{x+12},{yy+14}" stroke="#ffffff18" stroke-width="3"/>')
        out.append(f'<ellipse cx="{x-sx*9}" cy="205" rx="17" ry="9" fill="{ribbon}"/><ellipse cx="{x-sx*9-sx*14}" cy="214" rx="9" ry="12" fill="{ribbon}"/>')
    return ''.join(out)

def torso(kind, skin, uniform_main='#1b2f5b', accent='#c1272d', saree='#0f6b6e', border='#d9a441', width=1.0):
    w = 128 * width
    if kind == 'saree':
        return (f'<rect x="-14" y="52" width="28" height="44" rx="10" fill="{skin}"/>'
                f'<path d="M{-w},120 Q{-w},84 -34,82 L34,82 Q{w},84 {w},120 L{w+14},420 L{-w-14},420Z" fill="#7a1f2b"/>'  # blouse
                f'<path d="M{-w+6},330 L{w+14},330 L{w+14},420 L{-w-14},420Z" fill="{saree}"/>'
                f'<path d="M{-w*0.95},118 Q{-w*0.4},96 40,86 L{w*0.9},120 L{w*0.55},420 L{-w*0.2},420 Z" fill="{saree}"/>'  # pallu across chest
                f'<path d="M{-w*0.95},118 Q{-w*0.4},96 40,86 L52,100 Q{-w*0.4},112 {-w*0.95},138Z" fill="{border}"/>'
                f'<path d="M-30,86 Q0,128 30,86" fill="{skin}"/>'
                f'<path d="M{-w*0.2},420 L{w*0.55},420" stroke="{border}" stroke-width="10"/>'
                + ''.join(f'<path d="M{-w*0.1+i*26},{200+i*6} L{-w*0.3+i*30},420" stroke="#00000022" stroke-width="3"/>' for i in range(6)))
    if kind == 'kurta':
        return (f'<rect x="-14" y="52" width="28" height="44" rx="10" fill="{skin}"/>'
                f'<path d="M{-w},124 Q{-w},84 -34,82 L34,82 Q{w},84 {w},124 L{w+10},420 L{-w-10},420Z" fill="#e0a43a"/>'
                f'<path d="M-30,84 Q0,116 30,84 L30,92 Q0,130 -30,92Z" fill="#9c5f12"/>'
                f'<path d="M-70,100 Q-20,170 -90,300 L-60,300 Q10,170 40,98Z" fill="#fbf3e6"/>'  # dupatta
                f'<path d="M60,96 Q120,170 70,320 L100,320 Q150,170 80,92Z" fill="#fbf3e6"/>')
    if kind == 'girl':
        return (f'<rect x="-14" y="52" width="28" height="44" rx="10" fill="{skin}"/>'
                f'<path d="M{-w},124 Q{-w},84 -34,82 L34,82 Q{w},84 {w},124 L{w+10},420 L{-w-10},420Z" fill="#ffffff"/>'
                f'<path d="M{-w+10},170 L{w-10},170 L{w+6},420 L{-w-6},420Z" fill="{uniform_main}"/>'
                f'<path d="M-62,124 L-44,170 M62,124 L44,170" stroke="{uniform_main}" stroke-width="22" stroke-linecap="round"/>'
                f'<path d="M-34,82 L0,122 L-12,92Z M34,82 L0,122 L12,92Z" fill="#f1ede6" stroke="#cfc8bb" stroke-width="2"/>'
                f'<path d="M-9,118 L9,118 L12,178 L0,194 L-12,178Z" fill="{accent}"/>')
    if kind == 'boy':
        return (f'<rect x="-14" y="52" width="28" height="44" rx="10" fill="{skin}"/>'
                f'<path d="M{-w},124 Q{-w},84 -34,82 L34,82 Q{w},84 {w},124 L{w+10},420 L{-w-10},420Z" fill="#9fc4e8"/>'
                f'<path d="M-34,82 L0,124 L-14,94Z M34,82 L0,124 L14,94Z" fill="#c4dcf3" stroke="#7fa6cf" stroke-width="2"/>'
                f'<path d="M-9,116 L9,116 L12,190 L0,206 L-12,190Z" fill="{uniform_main}"/>'
                f'<path d="M-10,138 L10,128 M-11,156 L11,146 M-11,174 L11,164" stroke="{accent}" stroke-width="4"/>'
                f'<rect x="{-w*0.55}" y="150" width="34" height="38" rx="4" fill="#ffffff" opacity=".0"/>')
    raise ValueError(kind)

def arms(kind, skin, sleeve, reach=1.0, side='both'):
    """Forearms resting forward on a table. y positions relative to the head origin."""
    out = []
    for sx in (-1, 1):
        x0 = sx * 118
        out.append(f'<path d="M{x0},112 Q{sx*150},210 {sx*72*reach},300" fill="none" stroke="{sleeve}" stroke-width="42" stroke-linecap="round"/>')
        out.append(f'<ellipse cx="{sx*66*reach}" cy="318" rx="24" ry="17" fill="{skin}"/>')
    return ''.join(out)

def person(x, y, s, kind, skin, hair, hair_style, look='down', glasses=False, bindi=False, uniform='#1b2f5b', ribbon='#c1272d', saree='#0f6b6e', earring=False, sleeve=None, flip=False, part='all'):
    sl = sleeve or {'saree': '#7a1f2b', 'kurta': '#e0a43a', 'girl': '#ffffff', 'boy': '#9fc4e8'}[kind]
    g = [f'<g transform="translate({x},{y}) scale({-s if flip else s},{s})">']
    g.append(hair_back(hair_style, hair))
    g.append(torso(kind, skin, uniform_main=uniform, accent=ribbon, saree=saree))
    if hair_style == 'plaits':
        g.append(plaits(hair, ribbon))
    if part != 'body':
        pass
    g.append(face(skin, look, glasses, bindi, earring=earring))
    g.append(hair_front(hair_style, hair))
    g.append('</g>')
    body = ''.join(g)
    a = f'<g transform="translate({x},{y}) scale({-s if flip else s},{s})">' + arms(kind, skin, sl) + '</g>'
    return body, a
