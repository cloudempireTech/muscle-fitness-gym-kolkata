import os
from PIL import Image, ImageDraw

img_dir = r"C:\Users\dasan\.gemini\antigravity\scratch\muscle-fitness-gym-kolkata\assets\images"
os.makedirs(img_dir, exist_ok=True)

# 1. logo.svg
logo_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 80" width="460" height="80">
  <defs>
    <linearGradient id="cyanVolt" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00E5FF" />
      <stop offset="100%" stop-color="#76FF03" />
    </linearGradient>
    <linearGradient id="shieldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1E293B" />
      <stop offset="100%" stop-color="#0F172A" />
    </linearGradient>
  </defs>

  <!-- Athletic Shield & Dumbbell Emblem -->
  <g transform="translate(10, 8)">
    <polygon points="32,2 60,14 54,50 32,62 10,50 4,14" fill="url(#shieldGrad)" stroke="url(#cyanVolt)" stroke-width="2.5" />
    <!-- Stylized Dumbbell -->
    <rect x="18" y="29" width="28" height="6" rx="2" fill="url(#cyanVolt)" />
    <rect x="14" y="23" width="6" height="18" rx="2" fill="#FFFFFF" />
    <rect x="22" y="20" width="4" height="24" rx="1.5" fill="url(#cyanVolt)" />
    <rect x="44" y="23" width="6" height="18" rx="2" fill="#FFFFFF" />
    <rect x="38" y="20" width="4" height="24" rx="1.5" fill="url(#cyanVolt)" />
  </g>

  <!-- Typography -->
  <text x="86" y="37" font-family="'Plus Jakarta Sans', -apple-system, sans-serif" font-size="22" font-weight="900" letter-spacing="1.2" fill="#FFFFFF">
    MUSCLE FITNESS <tspan fill="url(#cyanVolt)">GYM 2</tspan>
  </text>
  <text x="88" y="56" font-family="'Plus Jakarta Sans', -apple-system, sans-serif" font-size="11" font-weight="700" letter-spacing="3" fill="#94A3B8">
    MAHABIRTALA &bull; TOLLYGUNGE
  </text>
</svg>"""

with open(os.path.join(img_dir, "logo.svg"), "w", encoding="utf-8") as f:
    f.write(logo_svg)

# 2. favicon.svg
favicon_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">
  <defs>
    <linearGradient id="favVolt" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00E5FF" />
      <stop offset="100%" stop-color="#76FF03" />
    </linearGradient>
  </defs>
  <rect width="64" height="64" rx="16" fill="#0A0D12" stroke="url(#favVolt)" stroke-width="2.5"/>
  <!-- Dumbbell Icon -->
  <rect x="18" y="29" width="28" height="6" rx="2" fill="url(#favVolt)" />
  <rect x="12" y="22" width="7" height="20" rx="2" fill="#FFFFFF" />
  <rect x="45" y="22" width="7" height="20" rx="2" fill="#FFFFFF" />
</svg>"""

with open(os.path.join(img_dir, "favicon.svg"), "w", encoding="utf-8") as f:
    f.write(favicon_svg)

# 3. Render raster favicons (512x512, 180x180, 32x32, favicon.ico)
size = (512, 512)
img = Image.new("RGBA", size, (10, 13, 18, 255))
draw = ImageDraw.Draw(img)

# Outer Hex Shield / Ring
draw.rectangle([32, 32, 480, 480], outline=(0, 229, 255, 255), width=16)
# Dumbbell plates & bar
draw.rectangle([140, 236, 372, 276], fill=(0, 229, 255, 255)) # bar
draw.rectangle([90, 170, 150, 342], fill=(255, 255, 255, 255)) # outer left
draw.rectangle([160, 150, 200, 362], fill=(118, 255, 3, 255)) # inner left
draw.rectangle([362, 170, 422, 342], fill=(255, 255, 255, 255)) # outer right
draw.rectangle([312, 150, 352, 362], fill=(118, 255, 3, 255)) # inner right

# Save 512x512
img.save(os.path.join(img_dir, "logo-512.png"), "PNG")

# Save Apple Touch Icon (180x180)
apple_icon = img.resize((180, 180), Image.Resampling.LANCZOS)
apple_icon.save(os.path.join(img_dir, "apple-touch-icon.png"), "PNG")

# Save 32x32
fav32 = img.resize((32, 32), Image.Resampling.LANCZOS)
fav32.save(os.path.join(img_dir, "favicon-32x32.png"), "PNG")

# Save favicon.ico
fav32.save(os.path.join(img_dir, "favicon.ico"), format="ICO", sizes=[(32, 32), (16, 16)])

print("Favicon suite successfully generated in assets/images!")
