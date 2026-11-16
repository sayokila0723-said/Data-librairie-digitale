from PIL import Image, ImageFilter, ImageOps
import os, sys
sys.path.insert(0, '/home/claude/brand')
import real_catalog as RC
os.makedirs('real/photos', exist_ok=True)
S = 600
for r in RC.R:
    key = f"{r[0]}_{r[1]:02d}"
    if (r[0], r[1]) in RC.NO_PHOTO: continue
    im = Image.open(f"real/crops/{key}.png").convert("RGB")
    w, h = im.size
    box = int(S * 0.80)
    sc = min(box / w, box / h, 4.5)
    nw, nh = max(1, round(w * sc)), max(1, round(h * sc))
    big = im.resize((nw, nh), Image.LANCZOS)
    big = big.filter(ImageFilter.UnsharpMask(radius=1.6, percent=70, threshold=2))
    can = Image.new("RGB", (S, S), (255, 255, 255))
    can.paste(big, ((S - nw) // 2, (S - nh) // 2))
    can.save(f"real/photos/{key}.jpg", quality=86, optimize=True, progressive=True)
print(len(os.listdir('real/photos')))
