import cv2
import numpy as np
import matplotlib.pyplot as plt
import urllib.request

# ---- Load a dummy image from URL ----
url = "https://via.placeholder.com/500"
resp = urllib.request.urlopen(url)
img_array = np.asarray(bytearray(resp.read()), dtype=np.uint8)
image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

# Convert BGR → RGB for display
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# ---- Rotate the image by 45 degrees around its center ----
(h, w) = image.shape[:2]
center = (w // 2, h // 2)

M = cv2.getRotationMatrix2D(center, 45, 1.0)   # rotate by 45 degrees
rotated = cv2.warpAffine(image, M, (w, h))

rotated_rgb = cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB)
plt.imshow(rotated_rgb)
plt.title("Rotated Image")
plt.show()

# ---- Increase brightness by adding +50 to all pixels ----
brightness_matrix = np.ones(image.shape, dtype="uint8") * 50
brighter = cv2.add(image, brightness_matrix)

brighter_rgb = cv2.cvtColor(brighter, cv2.COLOR_BGR2RGB)
plt.imshow(brighter_rgb)
plt.title("Brighter Image")
plt.show()
