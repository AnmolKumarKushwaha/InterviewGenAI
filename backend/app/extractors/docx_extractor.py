from docx import Document


class DOCXExtractor:

    @staticmethod
    def extract(file_path: str) -> str:

        document = Document(file_path)

        return "\n".join(
            paragraph.text
            for paragraph in document.paragraphs
        )