from dataclasses import dataclass


@dataclass(slots=True)
class FeedbackRow:
    """Customer feedback input row."""

    customer_id: str
    feedback: str
    category: str


@dataclass(slots=True)
class SummaryResult:
    """Successful summary result."""

    customer_id: str
    category: str
    original: str
    summary: str


@dataclass(slots=True)
class ProcessingError:
    """Processing error."""

    customer_id: str
    reason: str