import cv2
import matplotlib.pyplot as plt

from src.face_detection.haar_face_detector import HaarFaceDetector

image = cv2.imread("data/face_example.jpg")
if image is None:
    raise FileNotFoundError("Place an image at data/face_example.jpg")

detector = HaarFaceDetector()
faces = detector.detect(image)
annotated = detector.annotate(image, faces)

print("Detected faces:", len(faces))

plt.figure()
plt.imshow(cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB))
plt.title("Haar Cascade Face Detection")
plt.axis("off")
plt.show()
