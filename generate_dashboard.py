#!/usr/bin/env python3
"""
Project Tracking Dashboard Generator
Reads an Excel file and generates an interactive static HTML dashboard.
"""

import sys
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


def main():
    """Main function."""
    if len(sys.argv) < 2:
        print("Usage: python generate_dashboard.py <excel_file> [output_file]")
        print("Example: python generate_dashboard.py data.xlsx dashboard.html")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else 'dashboard.html'

    if not Path(input_file).exists():
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)

    print(f"Reading Excel file: {input_file}")
    records = read_excel_data(input_file)
    print(f"Found {len(records)} records")

    print(f"Generating HTML dashboard: {output_file}")
    html_content = generate_html(records)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"Dashboard generated successfully: {output_file}")
    print(f"Open {output_file} in your browser to view the dashboard.")


if __name__ == '__main__':
    main()
