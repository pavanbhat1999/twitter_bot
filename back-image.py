# Importing the PIL library
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import textwrap
from get_quotes import get_quotes


# Open an Image
img = Image.open('your-name.png')

# Call draw Method to add 2D graphics in an image
I1 = ImageDraw.Draw(img)

# Custom font style and font size
myFont = ImageFont.truetype('SHOWG.TTF', 100)

# Add Text to an image and wrap texxt around the image
#text = "Nice Car lorem epsum koram gineva asd sadusa dasd asd"
text = get_quotes()
text = textwrap.fill(text=text, width=17)
I1.text((10,10),text,font=myFont ,fill =(255, 255, 255))

# Display edited image
img.show()

# Save the edited image
img.save("space1.png")
