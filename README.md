# Project Tracking Dashboard Generator

A Python tool that reads Excel files containing project tracking data and generates an interactive static HTML dashboard.

## Features

- **Multi-Sheet Excel Parsing**: Reads all sheets/tabs from an Excel file and merges them into a single dataset
- **Interactive Dashboard**: Generates a static HTML file with embedded data
- **Cost Calculations**:
  - Working Time costs are automatically calculated as: `hours × hourly_rate × (1 + additional_rate)`
  - Monthly summaries for Working Time events
- **Financial Tracking**:
  - PO (Purchase Orders) represent coverage/budget for projects
  - Invoices are tracked as informational (not a cost)
  - Purchases and T&L are tracked as costs
  - Deferment: positive adds to budget and counts as invoiced, negative reduces budget
  - Financial Record: positive is used for the Coverage calculation, negative reduces budget
  - Remaining budget calculation per project
- **Comments**: Supports both a dedicated Comment column and cell-level Excel comments (sticky notes), displayed as tooltips on hover in the data table
- **Visualizations**: Multiple charts including:
  - Amount by Project (Budget, Costs, Invoices, Deferment, Remaining Budget)
  - Hours by Project (bar chart)
  - Timeline (monthly costs and remaining budget)
  - Budget Forecast (with actual and forecasted data)
- **Filtering**:
  - Quick filters for projects (clickable buttons)
  - Filter by event type
  - Filter by date range (auto-set to data range)
  - Quick filters for financial years, quarters, and months
- **Data Table**:
  - Event type filter dropdown (filter by Working Time, PO, Invoice, etc.)
  - Column sorting (click headers to sort ascending/descending)
  - Paginated display (25, 50, 100, 250, or all rows)
  - Sheet filter to show records from specific tabs
  - Full-text search across all fields
  - Visible Comment column (truncated with full text on hover)
  - Export filtered data to CSV (includes Sheet and Comment columns)
- **Project Details**: Detailed financial statistics for each project including:
  - Status indicators (green/yellow/red) based on forecasted budget
  - Closure date and EAC (Estimated At Completion)
  - Coverage ratio (Cost / (Invoiced + Positive Financial Record)) shown next to the project name
  - Burndown Rate (average monthly cost)
- **Monthly Summary**: Monthly breakdown of Working Time hours and costs
- **Budget Forecast**: Projects future budget trends based on average monthly costs

## Project Structure

The codebase is organized into modular components for better maintainability:

- **`generate_dashboard.py`** - Main entry point that orchestrates the dashboard generation
- **`parsers.py`** - Excel file parsing functions (reads all sheets, extracts comments)
- **`calculations.py`** - Financial calculations and statistics
- **`styles.py`** - CSS styles for the dashboard
- **`templates.py`** - HTML and JavaScript template generation

## Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

## Usage

```bash
python generate_dashboard.py <excel_file> [output_file]
```

### Examples

```bash
# Generate dashboard.html from data.xlsx
python generate_dashboard.py data.xlsx

# Specify custom output file
python generate_dashboard.py data.xlsx my_dashboard.html
```

## Excel File Format

The input Excel file can contain **multiple sheets/tabs** — all sheets are read and merged into a single dataset. Each sheet should contain the following columns:

- **#**: Row number (optional)
- **Date**: Date in format YYYY-MM-DD or other common formats
- **Event Type**: Type of event (see Event Types below)
- **Project**: Project name
- **Hourly Rate**: Hourly rate (can include € symbol)
- **Additional Rate**: Additional rate as a decimal (e.g. 0.05 = 5%)
- **Hours**: Number of hours
- **Amount**: Amount (can include € symbol and commas)
- **Comment**: Optional comment text (displayed as tooltip in the dashboard)

### Event Types

| Event Type | Description |
|---|---|
| **Working Time** | Work hours. Cost = hours × hourly rate × (1 + additional rate). Not entered as Amount. |
| **PO** | Purchase Order. Adds to the project budget. |
| **Invoice** | Invoiced amount. Informational only — not a cost. Used for Missing Invoice calculation. |
| **Purchase** | Direct cost (e.g. software licenses, hardware). |
| **T&L** | Travel & Logistics cost. |
| **Deferment** | Positive: adds to budget and counts as invoiced. Negative: reduces budget. Not a cost. |
| **Financial Record** | Positive: used in Coverage calculation (Cost / (Invoiced + Positive Financial Record)), *not* counted as invoiced. Negative: reduces budget. Not a cost. |
| **Closure** | Marks the project end date. The budget forecast extends to this month. |

### Example Data

| # | Date | Event Type | Project | Hourly Rate | Additional Rate | Hours | Amount | Comment |
|---|------|------------|---------|-------------|-----------------|-------|--------|---------|
| 1 | 2026-01-01 | Working Time | Project_1 | 50 | 0.05 | 100 | | |
| 2 | 2026-01-01 | PO | Project_1 | | | | 100000 | Initial PO |
| 3 | 2026-02-01 | Invoice | Project_1 | | | | 20000 | INV-2026-001 |
| 4 | 2026-02-15 | T&L | Project_3 | | | | 5000 | Conference travel |
| 5 | 2026-03-14 | Purchase | Project_1 | | | | 1250 | Software license |
| 6 | 2026-01-01 | Deferment | Project_4 | | | | 4000 | Carried forward |
| 7 | 2026-03-01 | Financial Record | Project_1 | | | | 15000 | Planned invoice for Q1 |
| 8 | 2026-02-01 | Financial Record | Project_3 | | | | -3000 | Budget reduction |
| 9 | 2026-08-01 | Closure | Project_1 | | | | | |

### Cell Comments

In addition to the Comment column, the dashboard also reads **cell-level Excel comments** (sticky notes). These are merged with any Comment column text and displayed together in the tooltip.

## Dashboard Features

### Summary Cards
- **Cost/Invoiced**: Ratio of total invoices to total costs as a percentage
- **Total Projects**: Number of unique projects
- **Budget**: Total budget from Purchase Orders (adjusted by Deferment and negative Financial Records)
- **Total Costs**: Working Time + Purchases + T&L
- **Total Invoices**: Invoice + positive Deferment amounts (positive Financial Records are *not* included in invoices)
- **Missing Invoice/Overinvoiced**: Total Invoices minus Total Costs
- **Remaining Budget**: Budget minus Total Costs
- **Total Hours**: Sum of all hours

### Filters
- Filter by Project (quick-filter buttons)
- Filter by Event Type
- Filter by Date Range
- Quick filters for financial years, quarters, and months
- Clear all filters

### Charts
- **Amount by Project**: Bar chart showing Budget, Costs, Invoices, Deferment, and Remaining Budget per project
- **Hours by Project**: Bar chart showing total hours per project
- **Timeline**: Line chart showing monthly costs and cumulative remaining budget over time
- **Budget Forecast**: Line chart showing actual and forecasted remaining budget, with color-coded forecast (green for positive, orange for negative)

### Data Table
- Event type filter dropdown to show only specific event types (Working Time, PO, Invoice, etc.)
- Column sorting: click any column header to sort ascending/descending (active sort shown with arrow indicator)
- Paginated display with configurable page size (25, 50, 100, 250, or all)
- Sheet filter dropdown to show records from a specific Excel tab
- Full-text search across all fields
- Comment column: always visible, truncated with full text shown on hover
- Sheet column shows which Excel tab each record came from
- Export to CSV (includes Sheet and Comment columns)

### Project Details
- Detailed financial statistics for each project:
  - Status indicator (green/yellow/red box) based on forecasted budget
  - Budget
  - Total Costs (broken down by Working Time, Purchases, T&L)
  - Invoices
  - Missing Invoice/Overinvoiced
  - Closure Date (if project has a Closure event)
  - EAC (Estimated At Completion — forecasted remaining budget at closure)
  - Remaining Budget (color-coded: green if positive, red if negative)
  - Deferment (with color coding)
  - Financial Record (blue if positive, red if negative)
  - Monthly Cost Forecast Rate
  - Total Hours

### Monthly Working Time Summary
- Monthly breakdown of Working Time events:
  - Total Hours per month
  - Total Cost per month (calculated)
  - Projects involved per month

## Output

The script generates a standalone HTML file that includes:
- All data embedded as JSON
- jQuery for DOM manipulation (via CDN)
- Chart.js for visualizations (via CDN)
- Embedded CSS styles
- All JavaScript functionality inline
- No external file dependencies required (CDN links are used)

Simply open the generated HTML file in any modern web browser.

## Development

The codebase follows a modular architecture:

- **Parsers** (`parsers.py`): Handle Excel file reading across all sheets, data parsing, and comment extraction
- **Calculations** (`calculations.py`): Perform all financial and statistical calculations
- **Styles** (`styles.py`): Contains all CSS styling rules
- **Templates** (`templates.py`): Generates the HTML structure and JavaScript code
- **Main** (`generate_dashboard.py`): Orchestrates the workflow and coordinates all modules

This structure makes it easy to:
- Modify parsing logic without affecting calculations
- Update styles independently
- Maintain and test individual components
- Extend functionality in a clean, organized way

## Notes

- **Multi-Sheet Support**: All sheets/tabs in the Excel file are read. Records from every sheet are merged and each record tracks which sheet it came from.
- **Working Time Cost Calculation**: For "Working Time" events, the cost is automatically calculated as `hours × hourly_rate × (1 + additional_rate)`. This calculated cost is displayed instead of the Amount field for Working Time events.
- **Budget**: Purchase Orders (PO) represent the total budget/coverage available for a project.
- **Invoices**: Invoice amounts are informational — they track how much has been billed but do not affect costs or budget directly.
- **Costs**: Working Time (calculated), Purchases, and T&L reduce the remaining budget. Deferment and Financial Record are NOT costs.
- **Deferment**: Positive deferment adds to budget and counts as invoiced. Negative deferment reduces budget.
- **Financial Record**: Positive amounts are used in the Coverage calculation (`Cost / (Invoiced + Positive Financial Record)`) and are *not* counted as invoiced. Negative amounts reduce budget (budget decrease).
- **Closure**: A special event type that marks the end of a project. The forecast extends to the closure date + 1 month for individual projects.
- **Forecast Logic**: The forecast uses the average monthly cost from the last 2 months to project future budget. For "All Projects" view, it sums individual project forecasts.
- **Status Indicators**: Color-coded boxes (green/yellow/red) show forecasted budget status:
  - Green: Forecasted budget is positive
  - Yellow: Forecasted budget is slightly negative (within 10% of project budget)
  - Red: Forecasted budget is significantly negative (beyond 10% threshold)
- **Remaining Budget**: Calculated as `Budget - Total Costs`. Negative values indicate over-budget situations.
- **Date Range**: The date filters are automatically set to the first and last event dates in the data.
- The script automatically handles various date formats
- Currency symbols (€, $) and formatting (commas) are automatically parsed
- Percentage values are recognized and parsed correctly
- Empty rows are automatically skipped
- The dashboard is fully responsive and works on desktop and mobile devices
