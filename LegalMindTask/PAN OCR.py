import cv2
import pytesseract
import re
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
image = cv2.imread("three.jpg")


rot_data = pytesseract.image_to_osd(image)
rot = re.search('(?<=Rotate: )\d+', rot_data).group(0)
print(rot_data)
angle = float(rot)
if angle > 0:
    print("rotation required.")
    angle = 360 - angle
else:
    print("no rotation required")

# rotate the image
(h, w) = image.shape[:2]
cx,cy = (w // 2, h // 2)
M = cv2.getRotationMatrix2D((cx,cy), angle, 1.0)
nh,nw=w,h
M[0][2] += (nw/2) - cx
M[1][2] += (nh/2) - cy
rotated = cv2.warpAffine(image, M, (nw, nh),
flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)	


ocr_text = pytesseract.image_to_string(rotated,lang="eng")
ocr_text = ''.join(re.findall(r'[0-9a-zA-Z]+',ocr_text)) #remove unnecessary chars
pan = re.findall(r'PermanentAccountNumberCard[A-Za-z0-9]{10}',ocr_text)[0]
pan1=pan[-10:]
print(pan1)
ocr_text1 = pytesseract.image_to_string(rotated,config="--psm 12")
DOB = re.findall(r'\d+/\d+/\d+',ocr_text1)[0]
print(DOB)
