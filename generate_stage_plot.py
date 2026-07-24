from PIL import Image, ImageDraw, ImageFont
import os

# Create 1600x1200 Canvas with light cream background
width, height = 1600, 1200
bg_color = (246, 243, 235)  # Earthy cream #f6f3eb
text_main = (27, 67, 44)    # Forest green #1b432c
burgundy = (156, 36, 53)    # Burgundy red #9c2435
card_bg = (255, 253, 248)   # Warm white #fffdf8
border_col = (200, 195, 180) # Soft border
dark_gray = (60, 60, 60)

img = Image.new("RGB", (width, height), bg_color)
draw = ImageDraw.Draw(img)

# Try loading fonts
try:
    font_title = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 42)
    font_subtitle = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 24)
    font_heading = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 28)
    font_bold = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 22)
    font_body = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 18)
    font_small = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 15)
except Exception:
    font_title = font_subtitle = font_heading = font_bold = font_body = font_small = ImageFont.load_default()

# 1. HEADER SECTION
draw.rectangle([50, 40, 1550, 160], fill=card_bg, outline=text_main, width=3)
draw.text((80, 60), "POSSUM CREEK PICKERS", fill=burgundy, font=font_title)
draw.text((80, 115), "OFFICIAL STAGE PLOT & TECHNICAL RIDER", fill=text_main, font=font_subtitle)
draw.text((1150, 75), "Location: Chattanooga, TN", fill=dark_gray, font=font_body)
draw.text((1150, 105), "Contact: possumcreekpickers@gmail.com", fill=dark_gray, font=font_body)

# 2. STAGE DIAGRAM BOX
draw.rectangle([50, 180, 1550, 720], fill=card_bg, outline=border_col, width=2)
# Stage Border Title
draw.rectangle([50, 180, 1550, 230], fill=text_main)
draw.text((700, 190), "AUDIENCE / FRONT OF HOUSE", fill=(255, 255, 255), font=font_bold)

# Stage Back Line
draw.line([(80, 690), (1520, 690)], fill=border_col, width=4)
draw.text((740, 695), "[ STAGE BACKLINE ]", fill=dark_gray, font=font_small)

# Position 1: Left - Elliott Brown (Guitar / Lead Vocal)
draw.rectangle([120, 270, 520, 520], fill=(240, 245, 240), outline=text_main, width=2)
draw.rectangle([120, 270, 520, 315], fill=text_main)
draw.text((140, 280), "ELLIOTT BROWN (STAGE LEFT)", fill=(255, 255, 255), font=font_bold)
draw.text((140, 330), "• Lead Vocals (Mic on Boom Stand)", fill=dark_gray, font=font_body)
draw.text((140, 365), "• Acoustic Guitar (DI Box / Mic)", fill=dark_gray, font=font_body)
draw.text((140, 400), "• Channel 1 (Vocal) + Channel 2 (Guitar)", fill=dark_gray, font=font_small)
# Monitor Wedge 1
draw.polygon([(260, 540), (380, 540), (400, 580), (240, 580)], fill=burgundy)
draw.text((275, 550), "MONITOR 1", fill=(255, 255, 255), font=font_bold)

# Position 2: Center - Micah Courey (Mandolin / Backup Vocal)
draw.rectangle([600, 270, 1000, 520], fill=(240, 245, 240), outline=text_main, width=2)
draw.rectangle([600, 270, 1000, 315], fill=text_main)
draw.text((620, 280), "MICAH COURY (CENTER STAGE)", fill=(255, 255, 255), font=font_bold)
draw.text((620, 330), "• Backup Vocals (Mic on Boom Stand)", fill=dark_gray, font=font_body)
draw.text((620, 365), "• Mandolin (DI Box / Mic)", fill=dark_gray, font=font_body)
draw.text((620, 400), "• Channel 3 (Vocal) + Channel 4 (Mando)", fill=dark_gray, font=font_small)
# Monitor Wedge 2
draw.polygon([(740, 540), (860, 540), (880, 580), (720, 580)], fill=burgundy)
draw.text((755, 550), "MONITOR 2", fill=(255, 255, 255), font=font_bold)

# Position 3: Right - Kevin Taylor (Upright Bass / Backup Vocal)
draw.rectangle([1080, 270, 1480, 520], fill=(240, 245, 240), outline=text_main, width=2)
draw.rectangle([1080, 270, 1480, 315], fill=text_main)
draw.text((1100, 280), "KEVIN TAYLOR (STAGE RIGHT)", fill=(255, 255, 255), font=font_bold)
draw.text((1100, 330), "• Backup Vocals (Mic on Stand)", fill=dark_gray, font=font_body)
draw.text((1100, 365), "• Upright Bass (DI Box / Mic)", fill=dark_gray, font=font_body)
draw.text((1100, 400), "• Channel 5 (Vocal) + Channel 6 (Bass)", fill=dark_gray, font=font_small)
# Monitor Wedge 3
draw.polygon([(1220, 540), (1340, 540), (1360, 580), (1200, 580)], fill=burgundy)
draw.text((1235, 550), "MONITOR 3", fill=(255, 255, 255), font=font_bold)

# Power Drop Symbol
draw.rectangle([720, 620, 880, 665], fill=(255, 230, 200), outline=burgundy, width=2)
draw.text((735, 632), "120V AC POWER", fill=burgundy, font=font_bold)

# 3. INPUT CHANNEL LIST TABLE & TECH SPECS
draw.rectangle([50, 740, 900, 1150], fill=card_bg, outline=border_col, width=2)
draw.rectangle([50, 740, 900, 785], fill=text_main)
draw.text((70, 750), "INPUT CHANNEL PATCH LIST", fill=(255, 255, 255), font=font_heading)

channels = [
    ("CH 1", "Lead Vocals", "Elliott Brown", "Shure SM58 / Equivalent (Boom Stand)"),
    ("CH 2", "Acoustic Guitar", "Elliott Brown", "Active DI Box / Instrument Mic"),
    ("CH 3", "Backup Vocals", "Micah Courey", "Shure SM58 / Equivalent (Boom Stand)"),
    ("CH 4", "Mandolin", "Micah Courey", "Active DI Box / Condenser Mic"),
    ("CH 5", "Backup Vocals", "Kevin Taylor", "Shure SM58 / Equivalent (Boom Stand)"),
    ("CH 6", "Upright Bass", "Kevin Taylor", "Bass Pickup DI Box / Mic"),
]

y_pos = 800
for ch, name, performer, mic in channels:
    draw.rectangle([70, y_pos, 140, y_pos + 40], fill=burgundy)
    draw.text((80, y_pos + 10), ch, fill=(255, 255, 255), font=font_bold)
    draw.text((160, y_pos + 10), f"{name} ({performer})", fill=text_main, font=font_bold)
    draw.text((500, y_pos + 10), mic, fill=dark_gray, font=font_body)
    draw.line([(70, y_pos + 50), (880, y_pos + 50)], fill=border_col, width=1)
    y_pos += 56

# 4. VENUE & SYSTEM REQUIREMENTS BOX
draw.rectangle([930, 740, 1550, 1150], fill=card_bg, outline=border_col, width=2)
draw.rectangle([930, 740, 1550, 785], fill=text_main)
draw.text((950, 750), "TECHNICAL REQUIREMENTS & SPECS", fill=(255, 255, 255), font=font_heading)

tech_specs = [
    ("Power Requirements", "1x Standard 120V AC Quad Outlet at stage center."),
    ("Monitors", "2 to 3 independent monitor mixes (Center, Left, Right)."),
    ("PA System", "Stereo PA suited for venue capacity with clean headroom."),
    ("Soundcheck Time", "15–20 minutes soundcheck preferred prior to performance."),
    ("Acoustic Flexibility", "Band can perform fully amplified or acoustic/unplugged."),
    ("Band Lineup", "3-Piece: Guitar/Lead Vocals, Mandolin/Vocals, Bass/Vocals.")
]

y_pos = 805
for title, desc in tech_specs:
    draw.text((950, y_pos), f"• {title}:", fill=burgundy, font=font_bold)
    draw.text((950, y_pos + 26), f"  {desc}", fill=dark_gray, font=font_body)
    y_pos += 56

# Save PNG image
img.save("public/assets/possum_creek_stage_plot.png", quality=95)
img.save("assets/possum_creek_stage_plot.png", quality=95)

print("Generated Stage Plot graphic at public/assets/possum_creek_stage_plot.png!")

