import os
import cv2

if __name__ == "__main__":
    img_path = os.path.abspath(os.sys.argv[1])  

    img = cv2.imread(img_path)

    #cv2.imshow("Original Image", img)
    #cv2.waitKey(0)  

    x, y, w, h = cv2.selectROI("Select ROI", img, fromCenter=False, showCrosshair=True)
    print(f" {x = } {y = } {w = } {h = }")

    cropped_img = img[y:y + h, x:x + w]
    cv2.imshow("Cropped Image", img)
    cv2.waitKey(0)

    cv2.destroyAllWindows()