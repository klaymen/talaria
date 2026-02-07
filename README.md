# Project Tracking Dashboard Generator

A Python tool that reads Excel files containing project tracking data and generates an interactive static HTML dashboard.

## Features

- **Excel File Parsing**: Reads Excel files with project tracking data
- **Interactive Dashboard**: Generates a static HTML file with embedded data
- **Cost Calculations**: 
  - Working Time costs are automatically calculated as: `hours × hourly_rate × (1 + additional_rate/100)`
  - Monthly summaries for Working Time events
- **Financial Tracking**:
  - PO (Purchase Orders) represent coverage/budget for projects
  - Invoices deduct from PO coverage
  - Purchases and T&L are tracked as costs
  - Remaining budget calculation per project
- **Visualizations**: Multiple charts including:
  - Amount by Project (PO Coverage, Costs, Invoices, Remaining Budget)
  - Hours by Project (bar chart)
  - Timeline (monthly costs and remaining budget)
  - Budget Forecast (with actual and forecasted data)
- **Filtering**: 
  - Quick filters for projects (clickable buttons)
  - Filter by event type
  - Filter by date range (auto-set to data range)
  - Quick filters for financial years, quarters, and months
- **Search**: Search functionality in the data table
- **Export**: Export filtered data to CSV
- **Project Details**: Detailed financial statistics for each project including:
  - Status indicators (green/yellow/red) based on forecasted budget
  - Closure date and EAC (Estimated At Completion)
  - Monthly cost forecast rate
- **Monthly Summary**: Monthly breakdown of Working Time hours and costs
- **Budget Forecast**: Projects future budget trends based on average monthly costs

## Project Structure

The codebase is organized into modular components for better maintainability:

- **`generate_dashboard.py`** - Main entry point that orchestrates the dashboard generation
- **`parsers.py`** - Excel file parsing functions (amount, hours, rates, dates)
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

The Excel file should contain the following columns:

- **#**: Row number (optional)
- **Date**: Date in format YYYY-MM-DD or other common formats
- **Event Type**: Type of event (e.g., "Working Time", "PO", "Invoice", "T&L", "Purchase", "Deferment", "Closure")
- **Project**: Project name
- **Hourly Rate**: Hourly rate (can include € symbol)
- **Additional Rate**: Additional rate percentage (can include % symbol)
- **Hours**: Number of hours
- **Amount**: Amount (can include € symbol and commas)

### Example Data

| # | Date | Event Type | Project | Hourly Rate | Additional Rate | Hours | Amount |
|---|------|------------|---------|-------------|-----------------|-------|--------|
| 1 | 2026-01-01 | Working Time | Project_1 | €50.0 | 0.05% | 100.0 | |
| 2 | 2026-01-01 | Working Time | Project_2 | €50.0 | 0.05% | 200.0 | |
| 10 | 2026-01-01 | PO | Project_1 | | | | €100,000.00 |
| 11 | 2026-02-01 | PO | Project_2 | | | | €50,000.00 |
| 13 | 2026-02-01 | Invoice | Project_1 | | | | €20,000.00 |
| 17 | 2026-02-15 | T&L | Project_3 | | | | €5,000.00 |
| 18 | 2026-03-14 | Purchase | Project_1 | | | | €1,250.00 |
| 19 | 2026-08-01 | Closure | Project_1 | | | | |
| 24 | 2026-01-01 | Deferment | Project_4 | | | | €4,000.00 |

## Dashboard Features

### Summary Cards
- Total Projects
- PO Coverage (total budget from Purchase Orders)
- Total Costs (Working Time + Purchases + T&L)
- Total Invoices (deducted from PO coverage)
- Remaining Budget (PO Coverage - Invoices - Costs)
- Total Hours

### Filters
- Filter by Project
- Filter by Event Type
- Filter by Date Range
- Clear all filters

### Charts
- **Amount by Project**: Bar chart showing PO Coverage, Costs, Invoices, and Remaining Budget per project
- **Hours by Project**: Bar chart showing total hours per project
- **Timeline**: Line chart showing monthly costs and cumulative remaining budget over time
- **Budget Forecast**: Line chart showing actual and forecasted remaining budget, with color-coded forecast (green for positive, orange for negative)

### Data Table
- Sortable table with all records
- Search functionality
- Export to CSV

### Project Details
- Detailed financial statistics for each project:
  - Status indicator (green/yellow/red box) based on forecasted budget
  - PO Coverage
  - Total Costs (broken down by Working Time, Purchases, T&L, Deferment)
  - Invoices
  - Closure Date (if project has a Closure event)
  - EAC (Estimated At Completion - forecasted remaining budget at closure)
  - Remaining Budget (color-coded: green if positive, red if negative)
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

- **Parsers** (`parsers.py`): Handle Excel file reading and data parsing
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

- **Working Time Cost Calculation**: For "Working Time" events, the cost is automatically calculated as `hours × hourly_rate × (1 + additional_rate/100)`. This calculated cost is displayed instead of the Amount field for Working Time events.
- **PO Coverage**: Purchase Orders (PO) represent the total budget/coverage available for a project. This is the amount that can be invoiced.
- **Invoices**: Invoice amounts are deducted from the PO coverage to track how much budget has been used.
- **Costs**: Working Time (calculated), Purchases, T&L, and Deferment are all tracked as costs that reduce the remaining budget.
- **Deferment**: Can be positive or negative, representing deferred costs or recovered costs.
- **Closure**: A special event type that marks the end of a project. The forecast extends to the closure date + 1 month for individual projects.
- **Forecast Logic**: The forecast uses the average monthly cost from the last 2 months to project future budget. For "All Projects" view, it sums individual project forecasts.
- **Status Indicators**: Color-coded boxes (green/yellow/red) show forecasted budget status:
  - Green: Forecasted budget is positive
  - Yellow: Forecasted budget is slightly negative (within 10% of project budget)
  - Red: Forecasted budget is significantly negative (beyond 10% threshold)
- **Remaining Budget**: Calculated as `PO Coverage - Invoices - Total Costs`. Negative values indicate over-budget situations.
- **Date Range**: The date filters are automatically set to the first and last event dates in the data.
- The script automatically handles various date formats
- Currency symbols (€, $) and formatting (commas) are automatically parsed
- Percentage values are recognized and parsed correctly
- Empty rows are automatically skipped
- The dashboard is fully responsive and works on desktop and mobile devices
