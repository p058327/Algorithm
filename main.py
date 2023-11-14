import cv2
import numpy as np

# img = cv2.imread("mazes/58cc0d.png")
print('start')

black_image = np.zeros((512, 512, 3), np.uint8)
cv2.imshow('Black Image', black_image)
def draw_circles(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(black_image, (x, y), 40, (255, 255, 255), -1)
while True:
    cv2.setMouseCallback('win', draw_circles)
    cv2.imshow('win', black_image)
    if cv2.waitKey(20) == 27:
        break
cv2.destroyAllWindows()
