import time

from client import CompletionClient

from models import (
    FeedbackRow,
    SummaryResult,
    ProcessingError,
)


class PipelineProcessor:
    """Processes customer feedback."""

    def __init__(
        self,
        client: CompletionClient,
    ) -> None:

        self.client = client

        self.results: list[
            SummaryResult
        ] = []

        self.errors: list[
            ProcessingError
        ] = []

    def process(
        self,
        rows: list[FeedbackRow],
    ) -> None:

        for row in rows:

            if not row.feedback.strip():

                self.errors.append(
                    ProcessingError(
                        customer_id=
                            row.customer_id,
                        reason=
                            "empty feedback",
                    )
                )

                continue

            prompt = (
                "Summarise this "
                "customer feedback "
                "in one sentence:\n\n"
                f"{row.feedback}"
            )

            summary = (
                self.client.summarize(
                    prompt,
                    row.customer_id,
                )
            )

            if summary:

                self.results.append(
                    SummaryResult(
                        customer_id=
                            row.customer_id,
                        category=
                            row.category,
                        original=
                            row.feedback,
                        summary=
                            summary,
                    )
                )

            else:

                self.errors.append(
                    ProcessingError(
                        customer_id=
                            row.customer_id,
                        reason=
                            "api failure",
                    )
                )

            time.sleep(0.5)