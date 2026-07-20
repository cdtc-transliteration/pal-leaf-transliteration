from abc import ABC, abstractmethod
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = \
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"


# Base Agent
class Agent(ABC):
    @abstractmethod
    def execute(self, data):
        pass


# Image Enhancement Agent
class EnhancementAgent(Agent):
    def execute(self, image_path):
        img = cv2.imread(image_path, 0)
        enhanced = cv2.equalizeHist(img)
        return enhanced


# Segmentation Agent
class SegmentationAgent(Agent):
    def execute(self, image):
        _, thresh = cv2.threshold(
            image, 0, 255,
            cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )
        return thresh


# OCR Agent
class OCRAgent(Agent):
    def execute(self, segmented_image):
        text = pytesseract.image_to_string(segmented_image)
        return text


# Transliteration Agent
class TransliterationAgent(Agent):
    def __init__(self):
        self.mapping = {
            "அ": "a",
            "ஆ": "aa",
            "இ": "i",
            "க": "ka",
            "ங": "nga"
        }

    def execute(self, text):
        result = ""
        for char in text:
            result += self.mapping.get(char, char)
        return result


# Validation Agent
class ValidationAgent(Agent):
    def execute(self, transliterated_text):
        if len(transliterated_text.strip()) == 0:
            return "Validation Failed"
        return transliterated_text


# Agent Orchestrator
class PalmLeafPipeline:
    def __init__(self):
        self.enhancer = EnhancementAgent()
        self.segmenter = SegmentationAgent()
        self.ocr = OCRAgent()
        self.transliterator = TransliterationAgent()
        self.validator = ValidationAgent()

    def run(self, image_path):
        image = self.enhancer.execute(image_path)
        segmented = self.segmenter.execute(image)
        text = self.ocr.execute(segmented)

        print("Recognized Text:")
        print(text)

        transliterated = self.transliterator.execute(text)
        validated = self.validator.execute(transliterated)

        return validated


if __name__ == "__main__":
    pipeline = PalmLeafPipeline()

    output = pipeline.run("1A1.jpg")

    print("\nTransliterated Output:")
    print(output)
