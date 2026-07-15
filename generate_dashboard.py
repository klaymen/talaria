#!/usr/bin/env python3
"""
Project Tracking Dashboard Generator
Reads an Excel file and generates an interactive static HTML dashboard.
"""

import argparse
from pathlib import Path

from parsers import read_excel_data
from calculations import (
    calculate_statistics,
    calculate_date_range,
    prepare_json_data
)
from templates import get_html_template


def generate_html(records):
    """Generate static HTML dashboard with embedded data."""

    # Calculate statistics
    stats = calculate_statistics(records)
    event_types = stats['event_types']

    # Find date range
    date_range = calculate_date_range(records)
    date_from = date_range['date_from']
    date_to = date_range['date_to']

    # Prepare JSON data for JavaScript
    data_json = prepare_json_data(records)

    # Generate HTML template
    html_template = get_html_template(
        event_types=event_types,
        date_from=date_from,
        date_to=date_to,
        data_json=data_json
    )

    return html_template


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate an interactive HTML dashboard from a project tracking Excel file."
    )
    parser.add_argument(
        "input",
        help="Path to the Excel input file.",
    )
    parser.add_argument(
        "--output-dir",
        default="output",
        help="Directory where dashboard.html is written (default: output/).",
    )
    parser.add_argument(
        "--output-file",
        default="dashboard.html",
        help="Output filename (default: dashboard.html).",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    input_file = Path(args.input)
    output_dir = Path(args.output_dir)
    output_file = output_dir / args.output_file

    if not input_file.exists():
        print(f"Error: File '{input_file}' not found.")
        raise SystemExit(1)

    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Reading Excel file: {input_file}")
    records = read_excel_data(input_file)
    print(f"Found {len(records)} records")

    print(f"Generating HTML dashboard: {output_file}")
    html_content = generate_html(records)

    output_file.write_text(html_content, encoding='utf-8')

    print(f"Dashboard generated successfully: {output_file}")
    print(f"Open {output_file} in your browser to view the dashboard.")


if __name__ == '__main__':
    main()
