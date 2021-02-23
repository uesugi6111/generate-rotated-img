import cv2

INPUT_PATH = "img/"
INPUT_IMG_NAME = "my_icon.jpg"
TARGET_PATH = "img/target/"


def write(img, degree, file_name):
    """
    write file
    """

    height, width, _ = img.shape
    mat = cv2.getRotationMatrix2D((width / 2, height / 2), degree, 1)
    affine_img = cv2.warpAffine(img, mat, (width, height))
    cv2.imwrite(TARGET_PATH+file_name+".jpg", affine_img)


input_img = cv2.imread(INPUT_PATH+INPUT_IMG_NAME)

for num in range(0, 12):
    write(input_img, 360-360//12*num, str(num))
