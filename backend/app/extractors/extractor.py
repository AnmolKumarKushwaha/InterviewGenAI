from pathlib import Path

from app.extractors.docx_extractor import DOCXExtractor
from app.extractors.pdf_extractor import PDFExtractor


class ResumeExtractor:

    @staticmethod
    def extract(file_path: str) -> str:

        extension = Path(file_path).suffix.lower()

        if extension == ".pdf":

            return PDFExtractor.extract(file_path)

        if extension == ".docx":

            return DOCXExtractor.extract(file_path)

        raise ValueError(
            "Unsupported resume format."
        )