from PIL import Image
import os

images_to_optimize = [
    ("possum_creek.jpg", 1600, 85, "possum_creek.webp"),
    ("elliott_crop.jpg", 800, 85, "elliott_crop.webp"),
    ("micah_crop.jpg", 800, 85, "micah_crop.webp"),
    ("kevin_crop.jpg", 800, 85, "kevin_crop.webp"),
    ("band_photo_2026_landscape.JPG", 1600, 85, "band_photo_2026_landscape_web.webp"),
    ("band_photo_2026_portrait.JPG", 1200, 85, "band_photo_2026_portrait_web.webp"),
    ("band_live.JPEG", 1600, 85, "band_live_web.webp")
]

pub_dir = "public/assets"
ass_dir = "assets"

print("--- OPTIMIZING WEB DISPLAY IMAGES ---")
for orig, max_dim, quality, out_name in images_to_optimize:
    in_path = os.path.join(pub_dir, orig)
    if os.path.exists(in_path):
        img = Image.open(in_path)
        orig_size = os.path.getsize(in_path) / 1024.0 # KB
        
        # Resize proportionally if larger than max_dim
        w, h = img.size
        if max(w, h) > max_dim:
            if w > h:
                new_w = max_dim
                new_h = int(h * (max_dim / float(w)))
            else:
                new_h = max_dim
                new_w = int(w * (max_dim / float(h)))
            img = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
        
        out_pub_path = os.path.join(pub_dir, out_name)
        out_ass_path = os.path.join(ass_dir, out_name)
        
        img.save(out_pub_path, "WEBP", quality=quality)
        img.save(out_ass_path, "WEBP", quality=quality)
        
        new_size = os.path.getsize(out_pub_path) / 1024.0 # KB
        reduction = (1 - (new_size / orig_size)) * 100
        print(f"✅ {orig} ({orig_size:.1f} KB) -> {out_name} ({new_size:.1f} KB) [{reduction:.1f}% reduction]")

