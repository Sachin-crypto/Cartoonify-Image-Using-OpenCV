import cv2

while True:
    # reading and resizing image
    img = cv2.imread("RDJ.jpg")
    resize = cv2.resize(img, (700, 500), interpolation=cv2.INTER_CUBIC)
    cv2.imshow('RDJ', resize)

    # converting to gray scale
    gray = cv2.cvtColor(resize, cv2.COLOR_RGB2GRAY)
    gray = cv2.medianBlur(gray, 7)
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 9)

    # cartoonifying the image
    img_col = cv2.bilateralFilter(resize, 5, 250, 250)
    cartoon = cv2.bitwise_and(img_col, img_col, mask=thresh)
    cv2.imshow('Cartoon', cartoon)

    if cv2.waitKey(10) == ord('q'):
        break
