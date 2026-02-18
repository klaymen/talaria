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
    calculate_project_financials,
    calculate_totals,
    calculate_date_range,
    calculate_monthly_working_time,
    prepare_json_data
)
from templates import get_html_template


def generate_html(records):
    """Generate static HTML dashboard with embedded data."""
    
    # Calculate statistics
    stats = calculate_statistics(records)
    projects = stats['projects']
    event_types = stats['event_types']
    
    # Calculate financials per project
    project_financials = calculate_project_financials(records)
    
    # Calculate totals
    totals = calculate_totals(project_financials, records)
    total_po_coverage = totals['total_po_coverage']
    total_invoices = totals['total_invoices']
    total_charges = totals['total_charges']
    total_hours = totals['total_hours']
    
    # Find date range
    date_range = calculate_date_range(records)
    date_from = date_range['date_from']
    date_to = date_range['date_to']
    
    # Calculate monthly summaries for Working Time
    monthly_working_time = calculate_monthly_working_time(records)
    
    # Prepare JSON data
    json_data = prepare_json_data(records, project_financials, monthly_working_time)
    data_json = json_data['data_json']
    financials_json = json_data['financials_json']
    monthly_summary_json = json_data['monthly_summary_json']
    
    # Generate HTML template
    html_template = get_html_template(
        projects=projects,
        event_types=event_types,
        total_po_coverage=total_po_coverage,
        total_charges=total_charges,
        total_invoices=total_invoices,
        total_hours=total_hours,
        date_from=date_from,
        date_to=date_to,
        data_json=data_json,
        financials_json=financials_json,
        monthly_summary_json=monthly_summary_json
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
