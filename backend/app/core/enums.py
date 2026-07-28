from enum import Enum


class ResumeStatus(str, Enum):

    UPLOADED = "UPLOADED"

    PARSING = "PARSING"

    ANALYZING = "ANALYZING"

    COMPLETED = "COMPLETED"

    FAILED = "FAILED"