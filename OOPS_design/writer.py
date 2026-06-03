import json

from dataclasses import asdict

from pathlib import Path

from models import (
    SummaryResult,
    ProcessingError,
)


class ReportWriter:
    """Writes output reports."""

    def write(
        self,
        source_file: str,
        output_dir: Path,
        results: list[SummaryResult],
        errors: list[ProcessingError],
        total_tokens: int,
    ) -> None:

        output_dir.mkdir(
            exist_ok=True
        )

        base = (
            Path(source_file)
            .stem
        )

        with (
            output_dir
            / f"{base}_results.json"
        ).open(
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                [
                    asdict(result)
                    for result in results
                ],
                file,
                indent=2,
            )

        with (
            output_dir
            / f"{base}_errors.json"
        ).open(
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                [
                    asdict(error)
                    for error in errors
                ],
                file,
                indent=2,
            )

        report_file = (
            output_dir
            / f"{base}_report.txt"
        )

        with report_file.open(
            "w",
            encoding="utf-8",
        ) as file:

            file.write(
                "COMPLETIONS REPORT\n"
            )

            file.write(
                "==================\n"
            )

            file.write(
                f"processed: {len(results)}\n"
            )

            file.write(
                f"errors: {len(errors)}\n"
            )

            file.write(
                f"total_tokens: {total_tokens}\n"
            )