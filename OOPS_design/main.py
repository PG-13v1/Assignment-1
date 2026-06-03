from pathlib import Path

from client import (
    RequestsCompletionClient,
)

from loader import CsvLoader

import sys
from processor import (
    PipelineProcessor,
)

from writer import ReportWriter

API_URL = (
    "http://localhost:8000/completions"
)

API_KEY = "replace-me"

MODEL = "gpt-4o"

SYSTEM_PROMPT = (
    "You are a helpful assistant "
    "that summarises customer "
    "feedback."
)


def main(
    csv_file: str,
) -> None:

    loader = CsvLoader()

    client = (
        RequestsCompletionClient(
            API_URL,
            API_KEY,
            MODEL,
            SYSTEM_PROMPT,
        )
    )

    processor = (
        PipelineProcessor(
            client
        )
    )

    writer = ReportWriter()

    rows = loader.load(
        Path(csv_file)
    )

    processor.process(
        rows
    )

    writer.write(
        source_file=csv_file,
        output_dir=Path(
            "output"
        ),
        results=
            processor.results,
        errors=
            processor.errors,
        total_tokens=
            client.total_tokens,
    )


if __name__ == "__main__":

    import sys

    if len(sys.argv) != 2:
        raise SystemExit(
            "Usage: "
            "python main.py "
            "feedback.csv"
        )

    main(sys.argv[1])