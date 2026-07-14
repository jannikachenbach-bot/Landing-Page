from PIL import Image

# 1. black_white.png
img_bw = Image.open('images/black_white.png').convert('RGBA')
pixels_bw = img_bw.load()
for y in range(img_bw.height):
    for x in range(img_bw.width):
        r, g, b, a = pixels_bw[x, y]
        # Extract black drawing: white becomes transparent, black stays black
        alpha = 255 - r
        pixels_bw[x, y] = (0, 0, 0, alpha)
img_bw.save('images/black_white.png')

# 2. red_red.png
img_red = Image.open('images/red_red.png').convert('RGBA')
pixels_red = img_red.load()
bg_color = (252, 29, 30)
for y in range(img_red.height):
    for x in range(img_red.width):
        r, g, b, a = pixels_red[x, y]
        dist = abs(r - bg_color[0]) + abs(g - bg_color[1]) + abs(b - bg_color[2])
        if dist < 10:
            pixels_red[x, y] = (r, g, b, 0)
        else:
            # Smooth alpha based on distance
            alpha = min(255, max(0, int((dist - 10) * 8)))
            pixels_red[x, y] = (r, g, b, alpha)
img_red.save('images/red_red.png')
print("Logos converted to transparent successfully.")
