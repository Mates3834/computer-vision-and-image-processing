import cv2

class HaarFaceDetector:
    """OpenCV Haar Cascade frontal-face detector."""

    def __init__(self, cascade_path=None):
        if cascade_path is None:
            cascade_path = (
                cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
            )
        self.detector = cv2.CascadeClassifier(cascade_path)
        if self.detector.empty():
            raise ValueError("Could not load Haar Cascade classifier.")

    def detect(self, image, scale_factor=1.1, min_neighbors=5):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) if image.ndim == 3 else image
        return self.detector.detectMultiScale(
            gray,
            scaleFactor=scale_factor,
            minNeighbors=min_neighbors,
        )

    def annotate(self, image, faces=None):
        output = image.copy()
        if faces is None:
            faces = self.detect(image)
        for x, y, w, h in faces:
            cv2.rectangle(output, (x, y), (x+w, y+h), (0, 255, 0), 2)
        return output
