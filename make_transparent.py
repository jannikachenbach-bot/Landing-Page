from PIL import Image, ImageDraw

img = Image.open('images/favicon.png').convert("RGBA")
width, height = img.size

min_x = width
min_y = height
max_x = 0
max_y = 0

pixels = img.load()
for y in range(height):
    for x in range(width):
        r, g, b, a = pixels[x, y]
        if max(r,g,b) - min(r,g,b) > 15 or (r<30 and g<30 and b<30):
            if x < min_x: min_x = x
            if x > max_x: max_x = x
            if y < min_y: min_y = y
            if y > max_y: max_y = y

print(f"Bounding box: {min_x}, {min_y}, {max_x}, {max_y}")

scale = 4
mask = Image.new('L', (width * scale, height * scale), 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((min_x * scale, min_y * scale, max_x * scale, max_y * scale), fill=255)
mask = mask.resize((width, height), Image.Resampling.LANCZOS)

img.putalpha(mask)
img.save('images/favicon-transparent.png')
