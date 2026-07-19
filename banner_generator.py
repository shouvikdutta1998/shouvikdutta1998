from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 1500, 500
BG = (13, 17, 23)
ACCENT = (255, 59, 59)
WHITE = (255, 255, 255)
DIM = (171, 181, 194)
MID = (90, 100, 120)

img = Image.new('RGB', (WIDTH, HEIGHT), BG)
draw = ImageDraw.Draw(img)

# Top-right glow
for r in range(360, 10, -18):
    draw.ellipse((WIDTH - 360 - r, -70 - r, WIDTH + 120 + r, 210 + r), outline=ACCENT, width=2)

# Subtle diagonal lines
for i in range(-WIDTH, WIDTH, 90):
    draw.line((i, 0, i + HEIGHT, HEIGHT), fill=(30, 35, 43), width=1)

# Accent line at top
for x in range(80, WIDTH - 80, 18):
    draw.line((x, 42, x + 62, 42), fill=ACCENT, width=2)

# Text fonts
name_font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 50)
subtitle_font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 28)
small_font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 22)
mini_font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 18)

# Left content
x0 = 88

draw.text((x0, 80), 'Shouvik Dutta', fill=WHITE, font=name_font)
draw.text((x0, 148), 'Senior Security Consultant', fill=WHITE, font=subtitle_font)
draw.text((x0, 202), 'Application Security | Offensive Security', fill=DIM, font=small_font)
draw.text((x0, 242), 'OSCP • CRTO • CEH', fill=ACCENT, font=small_font)

# Accent underline
for x in range(88, 385, 14):
    draw.line((x, 132, x + 48, 132), fill=ACCENT, width=2)

# Bottom-left tagline
for x in range(88, 1230, 24):
    draw.line((x, 362, x + 42, 362), fill=ACCENT, width=2)
draw.text((88, 410), '@Warlockrootx', fill=WHITE, font=subtitle_font)

# Cyber illustration on the right
cx, cy = 1110, 245
shield = [
    (cx - 100, cy - 132),
    (cx, cy - 160),
    (cx + 100, cy - 132),
    (cx + 138, cy + 12),
    (cx + 60, cy + 142),
    (cx, cy + 120),
    (cx - 60, cy + 142),
    (cx - 138, cy + 12),
]
draw.polygon(shield, outline=ACCENT, width=3)

prompt_box = (cx - 180, cy - 70, cx + 180, cy + 92)
draw.rounded_rectangle(prompt_box, radius=14, outline=MID, width=2)
draw.text((cx - 154, cy - 55), '>_', fill=ACCENT, font=subtitle_font)
draw.text((cx - 112, cy - 55), 'root@warlockrootx:~$', fill=WHITE, font=small_font)
draw.text((cx - 112, cy - 22), 'nmap -sV target.local', fill=DIM, font=small_font)
draw.text((cx - 112, cy + 10), 'security -validate -trust', fill=DIM, font=small_font)

# Circuit lines and nodes
circuit = [
    ((cx - 228, cy + 108), (cx - 160, cy + 108), (cx - 125, cy + 71), (cx - 62, cy + 71), (cx - 28, cy + 108), (cx + 40, cy + 108)),
    ((cx + 20, cy - 142), (cx + 82, cy - 142), (cx + 112, cy - 102), (cx + 182, cy - 102)),
]
for line in circuit:
    draw.line(line, fill=ACCENT, width=2)

nodes = [
    (cx - 228, cy + 108), (cx - 160, cy + 108), (cx - 125, cy + 71), (cx - 62, cy + 71),
    (cx - 28, cy + 108), (cx + 40, cy + 108), (cx + 82, cy - 142), (cx + 112, cy - 102), (cx + 182, cy - 102)
]
for nx, ny in nodes:
    draw.ellipse((nx - 4, ny - 4, nx + 4, ny + 4), fill=ACCENT)

# Binary detail
for idx, value in enumerate(['01011010', '10101101', '00110101', '11000110', '01101001']):
    draw.text((cx + 205, cy + 130 + idx * 22), value, fill=(76, 84, 96), font=mini_font)

# Right edge accent detail
for y in range(40, HEIGHT - 40, 18):
    draw.line((WIDTH - 38, y, WIDTH - 12, y + 10), fill=ACCENT, width=1)

img.save('banner.png')
print('banner.png created successfully')
