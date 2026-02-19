# Talaria — Project Tracking Dashboard Generator

A Python tool that reads Excel files containing project tracking data and generates an interactive static HTML dashboard.

## Features

- **Multi-Sheet Excel Parsing**: Reads all sheets/tabs from an Excel file and merges them into a single dataset
- **Interactive Dashboard**: Generates a static HTML file with embedded data — all filtering, sorting, and charting happens client-side
- **Billable Amount Calculations**: Working Time fees are automatically calculated as `hours × billing_rate × (1 + surcharge_rate)`
- **Financial Tracking**:
  - PO (Purchase Orders) represent budget for projects
  - Invoices are tracked as informational (not a charge)
  - Purchases and T&L are tracked as expenses
  - Deferment: positive adds to budget and counts as invoiced, negative reduces budget
  - Financial Record: positive is used for the Coverage calculation, negative reduces budget
  - Remaining budget calculation per project
- **Comments**: Supports both a dedicated Comment column and cell-level Excel comments (sticky notes)
- **Charts**: Budget by Project, Hours by Project, Hours by Month, Timeline, Budget Forecast
- **Filtering**: Quick filters for projects, financial years, quarters, months; event type and date range filters
- **Data Table**: Sortable columns, pagination, full-text search, sheet filter, CSV export
- **Project Details**: Per-project financial breakdown with status indicators (green/yellow/red)
- **Dark Mode**: Automatic (follows OS preference) or manual toggle

## Quick Start

```bash
pip install -r requirements.txt
python generate_dashboard.py data.xlsx
open dashboard.html
```

## Project Structure

```
generate_dashboard.py   Main entry point — orchestrates the pipeline
parsers.py              Excel parsing, value cleaning, billable amount calculation
calculations.py         Statistics, date range, JSON serialization
styles.py               CSS (light + dark themes)
templates.py            HTML structure + all JavaScript (filtering, charts, tables)
test_parsers.py         Unit tests for parsing functions
test_calculations.py    Unit tests for calculation functions
test_integration.py     Integration tests using test_input.xlsx
```

All financial logic (aggregation, filtering, forecasting) lives in the JavaScript inside `templates.py`. Python is responsible for parsing the Excel file and serializing records to JSON — the browser handles everything else, which is what enables interactive filtering.

## Testing

```bash
pip install pytest
pytest -v
```

71 tests covering:
- **Parsers** (39): `parse_amount`, `parse_hours`, `parse_rate`, billable amount formula
- **Calculations** (11): `calculate_statistics`, `calculate_date_range`, `prepare_json_data`
- **Integration** (21): Excel parsing with real data, field validation, HTML generation

## Usage

```bash
python generate_dashboard.py <excel_file> [output_file]

# Examples
python generate_dashboard.py data.xlsx
python generate_dashboard.py data.xlsx my_dashboard.html
```

## Excel File Format

The input Excel file can contain **multiple sheets/tabs** — all are read and merged. Each sheet should have these columns:

| Column | Description |
|---|---|
| **#** | Row number (optional) |
| **Date** | Date (YYYY-MM-DD or other common formats) |
| **Event Type** | One of the types listed below |
| **Project** | Project name |
| **Hourly Rate** | Billing rate (can include € or $ symbol) |
| **Additional Rate** | Surcharge rate as a decimal (e.g. 0.05 = 5%) |
| **Hours** | Number of hours worked |
| **Amount** | Monetary amount (can include € or $ and commas) |
| **Comment** | Optional comment text |

### Event Types

| Event Type | Description |
|---|---|
| **Working Time** | Billable hours. Amount = `hours × billing rate × (1 + surcharge rate)`. |
| **PO** | Purchase Order. Adds to the project budget. |
| **Invoice** | Invoiced amount. Informational — not a charge. Used for coverage calculations. |
| **Purchase** | Direct expense (e.g. software licenses, hardware). |
| **T&L** | Travel & Logistics expense. |
| **Deferment** | Positive: adds to budget and counts as invoiced. Negative: reduces budget. Not a charge. |
| **Financial Record** | Positive: used in Coverage ratio. Negative: reduces budget. Not a charge. |
| **Closure** | Marks the project end date. Forecast extends to this month. |

### Example Data

| # | Date | Event Type | Project | Hourly Rate | Additional Rate | Hours | Amount | Comment |
|---|------|------------|---------|-------------|-----------------|-------|--------|---------|
| 1 | 2026-01-01 | Working Time | Project_1 | 50 | 0.05 | 100 | | |
| 2 | 2026-01-01 | PO | Project_1 | | | | 100000 | Initial PO |
| 3 | 2026-02-01 | Invoice | Project_1 | | | | 20000 | INV-2026-001 |
| 4 | 2026-02-15 | T&L | Project_3 | | | | 5000 | Conference travel |
| 5 | 2026-03-14 | Purchase | Project_1 | | | | 1250 | Software license |
| 6 | 2026-01-01 | Deferment | Project_4 | | | | 4000 | Carried forward |
| 7 | 2026-03-01 | Financial Record | Project_1 | | | | 15000 | Planned invoice |
| 8 | 2026-02-01 | Financial Record | Project_3 | | | | -3000 | Budget reduction |
| 9 | 2026-08-01 | Closure | Project_1 | | | | | |

Cell-level Excel comments (sticky notes) are also read and merged with Comment column text.

## Dashboard Guide

### Summary Cards

| Card | Meaning |
|---|---|
| **Charges/Invoiced** | Ratio of total invoices to total charges (%) |
| **Coverage** | Total Charges / (Invoiced + Positive Financial Record) |
| **Total Projects** | Counts by category: Planned, Active, Closed |
| **Project Status** | Counts by forecast status: Green, Yellow, Red |
| **Budget** | Total PO coverage (adjusted by Deferment and negative Financial Records) |
| **Total Charges** | Working Time fees + Purchase expenses + T&L expenses |
| **Total Invoices** | Invoice amounts + positive Deferment |
| **Missing Coverage / Overcovered** | (Invoiced + Positive Financial Record) − Total Charges |
| **Remaining Budget** | Budget − Total Charges |
| **Total Hours** | Sum of all hours |

### Charts

- **Budget by Project**: Budget, Charges, Invoices, Deferment, Financial Record, Remaining Budget (with toggleable datasets)
- **Hours by Project**: Total hours per project
- **Hours by Month**: Stacked by project
- **Timeline**: Monthly charges and cumulative remaining budget
- **Budget Forecast**: Actual + forecasted remaining budget (green = positive, orange = negative)

### Status Indicators

- **Green**: Forecasted budget is positive
- **Yellow**: Slightly negative (within 10% of project budget, only in last forecast month)
- **Red**: Significantly negative (beyond 10% threshold or currently negative)

### Key Calculations

- **Total Charges** = Working Time fees + Purchase expenses + T&L expenses (Deferment is NOT a charge)
- **Remaining Budget** = Budget − Total Charges
- **Billable Amount** = hours × billing rate × (1 + surcharge rate)
- **Forecast** uses average monthly charges from last 2 months to project future budget
- **Closure** stops cost accrual in the forecast at the closure month

## Output

The generated HTML file is fully standalone:
- All data embedded as JSON
- jQuery and Chart.js loaded via CDN
- CSS and JavaScript inline
- No other external dependencies

Open the file in any modern browser.

## Dependencies

- Python 3.8+
- pandas >= 1.5.0
- openpyxl >= 3.0.0
- pytest (for running tests)
