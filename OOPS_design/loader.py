import csv
from pathlib import Path
from models import FeedbackRow


class CsvLoader:
    """Loads feedback rows from CSV."""

    def load(
        self,
        file_path: Path,
    ) -> list[FeedbackRow]:

        rows: list[FeedbackRow] = []

        with file_path.open(
            "r",
            encoding="utf-8",
            newline="",
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:

                rows.append(
                    FeedbackRow(
                        customer_id=row.get(
                            "customer_id",
                            "unknown",
                        ),
                        feedback=row.get(
                            "feedback",
                            "",
                        ),
                        category=row.get(
                            "category",
                            "general",
                        ),
                    )
                )

        return rows