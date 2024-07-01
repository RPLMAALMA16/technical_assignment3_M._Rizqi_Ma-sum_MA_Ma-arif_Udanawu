import matplotlib.pyplot as plt
import cv2
import numpy as np

fig, axs = plt.subplots(2, 2, figsize=(10, 10))
img = cv2.imread("saya.jpeg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

hh, ww = img.shape[:2]
mask = np.zeros_like(img)
mask = cv2.circle(mask, (ww//2, hh//2), 100, 255, -1)

axs[0][0].imshow(img)
axs[0][0].set_title("saya sendiri")
axs[0][1].imshow(cv2.Canny(img, 127, 255), cmap='gray')
axs[0][1].set_title("saya jadi hitam") 
axs[1][0].imshow(cv2.GaussianBlur(img, (45, 45), 0))
axs[1][0].set_title("saya kurang jelas")
img_merah = img.copy()
img_merah[:,:,1] = 0  
img_merah[:,:,2] = 0  
axs[1][1].imshow(img_merah)
axs[1][1].set_title("saya jadi merah")


plt.show()
