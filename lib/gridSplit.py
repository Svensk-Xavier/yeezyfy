"""
AUTHOR: Josh Nelsson-Smith
DESCRIPTION: This takes an image and a size and
splits the image into the given size of images
"""

def gridSplit(image, size):

    W, H = image.size[0]. image.size[1]
    m,n = size
    w, h = int(W/n), int(H/m)
    imgs = []
    for j in range(m):
        for i in range(n):
            imgs.append(image.crop((i*w, j*h, (i+1)*w, (j+1)*h)))
    return imgs