###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.r
    b = color.rgb.r
    new_color = (r, g, b)
    rgb_colors.append(new_color)
    
print(rgb_colors)