#!/usr/bin/env python3
"""
HTML template for the dashboard generator.
"""

from datetime import datetime
from styles import get_css


def get_html_template(projects, event_types, total_po_coverage, total_costs, 
                     total_invoices, total_hours, date_from, date_to,
                     data_json, financials_json, monthly_summary_json):
    """Generate HTML template with embedded data."""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Talaria - Project Tracking Dashboard</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js@3.9.1/dist/chart.min.js"></script>
    <style>
{get_css()}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1><svg class="header-icon" viewBox="0 0 476 474" fill="currentColor" xmlns="http://www.w3.org/2000/svg"><g transform="translate(0,474) scale(0.1,-0.1)" stroke="none"><path d="M3935 4183 c-159 -63 -353 -138 -430 -168 -77 -30 -291 -113 -475 -185 -184 -73 -357 -140 -385 -150 -99 -36 -231 -92 -265 -113 -92 -55 -185 -161 -239 -272 -38 -79 -42 -95 -103 -417 -9 -49 -8 -61 6 -83 32 -49 104 -41 124 14 6 14 24 102 41 194 39 213 66 274 165 373 78 77 39 58 446 217 91 36 219 86 285 112 66 26 201 78 300 116 99 39 189 74 200 79 11 5 74 30 140 55 66 26 188 73 270 106 149 58 175 66 175 52 -1 -28 -54 -183 -75 -220 -32 -53 -101 -106 -175 -132 -30 -11 -86 -31 -125 -46 -67 -25 -187 -70 -380 -141 -49 -18 -182 -67 -295 -109 -113 -42 -272 -101 -355 -131 -82 -31 -159 -64 -169 -74 -38 -38 -10 -120 42 -120 14 0 230 78 652 235 444 165 582 215 596 215 18 0 18 -24 -1 -86 -21 -71 -70 -114 -180 -157 -49 -19 -151 -59 -225 -87 -212 -83 -455 -178 -575 -225 -60 -24 -141 -55 -180 -70 -38 -15 -76 -33 -84 -38 -39 -32 -31 -98 14 -119 20 -9 34 -9 63 1 53 19 313 120 337 131 11 5 90 36 175 69 85 33 226 87 313 121 87 34 161 60 164 57 3 -3 -3 -29 -13 -59 -12 -36 -33 -68 -68 -103 -54 -54 -51 -53 -461 -195 -60 -21 -155 -55 -211 -74 -91 -32 -129 -39 -375 -66 -151 -16 -341 -37 -422 -47 -167 -19 -152 -10 -226 -128 -95 -151 -350 -446 -610 -705 -226 -226 -275 -266 -426 -345 -136 -72 -201 -118 -221 -157 -15 -28 -14 -35 6 -92 66 -179 178 -236 370 -186 222 57 366 119 703 304 205 112 287 152 361 175 74 23 225 38 461 46 293 10 404 28 501 78 56 29 125 100 157 161 31 59 32 65 32 186 -1 112 -4 133 -29 200 -28 74 -89 198 -165 337 -63 116 -69 104 71 153 518 179 515 178 595 262 75 80 105 153 117 282 3 30 11 45 32 60 51 36 92 84 121 143 23 48 29 74 31 149 4 90 4 91 35 109 58 34 129 109 157 165 28 56 110 327 110 365 0 22 -24 62 -50 82 -31 25 -90 9 -375 -104z m-1065 -1621 c0 -4 -11 -42 -25 -85 -61 -195 -103 -430 -112 -635 l-6 -143 -45 3 -45 3 -13 64 c-43 209 -232 441 -480 587 -43 25 -81 48 -83 49 -1 2 7 22 20 44 26 47 6 42 284 72 110 11 247 26 305 34 125 15 200 18 200 7z m168 -249 c86 -166 105 -225 106 -328 1 -81 -2 -95 -26 -136 -32 -54 -83 -91 -159 -115 -71 -21 -89 -15 -89 29 0 168 81 647 110 647 4 0 30 -44 58 -97z m-995 -64 c175 -99 302 -221 385 -369 30 -54 68 -167 59 -176 -2 -2 -55 -9 -118 -15 -105 -9 -202 -23 -255 -35 -17 -4 -27 4 -47 39 -45 75 -159 188 -250 247 -48 30 -86 58 -87 62 0 3 30 42 68 85 37 43 90 106 117 141 28 34 51 62 53 62 1 0 35 -18 75 -41z m-343 -404 c36 -21 82 -52 104 -69 45 -34 146 -154 146 -172 0 -7 -48 -38 -107 -69 -147 -78 -232 -125 -268 -147 -16 -10 -34 -18 -40 -18 -5 0 -25 33 -43 74 -22 47 -51 91 -84 124 l-50 50 133 136 c73 74 136 133 139 132 3 -2 34 -20 70 -41z m-403 -369 c40 -35 97 -142 91 -172 -4 -18 -145 -83 -259 -119 -162 -51 -239 -43 -274 30 -21 46 -33 35 140 130 70 39 152 91 183 117 32 25 62 47 68 47 6 1 28 -14 51 -33z"/><path d="M3360 1610 c-30 -10 -262 -80 -515 -155 -253 -75 -471 -140 -485 -145 -14 -5 -97 -30 -185 -56 -88 -25 -212 -62 -275 -81 -63 -19 -173 -52 -245 -73 -137 -40 -337 -100 -520 -155 -60 -18 -144 -43 -185 -55 -201 -58 -219 -68 -220 -122 0 -34 32 -68 64 -68 14 0 82 17 153 39 70 21 200 60 288 86 88 26 239 71 335 100 261 79 712 213 1005 300 143 42 271 80 285 85 14 5 97 30 185 55 342 101 450 136 463 152 18 25 15 77 -6 96 -24 22 -72 20 -142 -3z"/></g></svg> Talaria - Project Tracking Dashboard</h1>
            <span class="header-info">Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</span>
        </header>
        
        <div class="toolbar-strip">
            <button class="toolbar-btn" id="themeToggle" title="Toggle dark mode">&#9790;</button>
            <div class="toolbar-divider"></div>
            <button class="toolbar-btn" id="helpIcon" title="Dashboard guide">?</button>
        </div>
        
        <div class="help-modal" id="helpModal">
            <div class="help-content">
                <button class="close-btn" id="closeHelp">&times;</button>
                <h2>Dashboard Guide</h2>

                <h3>Data Source</h3>
                <p>The dashboard reads <strong>all sheets/tabs</strong> from the input Excel file. Records from every sheet are merged into a single dataset. Each record tracks which sheet it originated from.</p>

                <h3>Event Types</h3>
                <ul>
                    <li><strong>PO (Purchase Order):</strong> Adds to the project budget.</li>
                    <li><strong>Working Time:</strong> A cost. Calculated as hours &times; hourly rate &times; (1 + additional rate). The calculated cost is shown instead of the Amount field.</li>
                    <li><strong>Purchase:</strong> A direct cost (e.g. software licenses, hardware).</li>
                    <li><strong>T&amp;L:</strong> Travel &amp; Logistics costs.</li>
                    <li><strong>Invoice:</strong> Invoiced amounts. Informational only &mdash; not a cost, not added to the budget. Used for the Missing Coverage / Overcovered calculation.</li>
                    <li><strong>Deferment:</strong> Positive deferment adds to the budget and counts as invoiced. Negative deferment reduces the budget. Not included in costs.</li>
                    <li><strong>Financial Record:</strong> Positive amounts are used in the Coverage calculation (Cost&nbsp;/&nbsp;(Invoiced&nbsp;+&nbsp;Positive&nbsp;Financial&nbsp;Record)) but are <em>not</em> counted as invoiced. Negative amounts reduce the budget. Not included in costs.</li>
                    <li><strong>Closure:</strong> Marks the project end date. The budget forecast extends to the closure month.</li>
                </ul>

                <h3>Summary Cards</h3>
                <p><strong>Cost/Invoiced:</strong> Ratio of total invoices to total costs, expressed as a percentage.</p>
                <p><strong>Total Projects:</strong> Number of unique projects in the dataset.</p>
                <p><strong>Project Status:</strong> Number of projects in each forecast status &mdash; green (positive), yellow (slightly negative), red (significantly negative).</p>
                <p><strong>Budget:</strong> Total Purchase Order coverage across all projects (includes positive Deferment and is reduced by negative Deferment and negative Financial Records).</p>
                <p><strong>Total Costs:</strong> Sum of Working Time + Purchases + T&amp;L. Deferment and Financial Record are not costs.</p>
                <p><strong>Total Invoices:</strong> Total invoiced amounts (includes Invoice events and positive Deferment). Positive Financial Records are <em>not</em> counted as invoiced.</p>
                <p><strong>Missing Coverage/Overcovered:</strong> (Invoiced + Positive Financial Record) minus Total Costs. Negative (red) = missing coverage; positive = overcovered.</p>
                <p><strong>Remaining Budget:</strong> Budget minus Total Costs.</p>
                <p><strong>Coverage:</strong> Shown next to each project name. Calculated as <em>Total Costs / (Invoiced + Positive Financial Record)</em>. This ratio indicates how much of the invoiced-or-planned amount has actually been spent. Positive Financial Records represent amounts that are expected to be invoiced in the future, so they widen the denominator without affecting costs or the invoice totals.</p>

                <h3>Charts</h3>
                <p><strong>Budget by Project:</strong> Shows Budget, Costs, Invoices, Deferment, Financial Record, and Remaining Budget grouped by project.</p>
                <p><strong>Timeline:</strong> Monthly costs and cumulative remaining budget over time.</p>
                <p><strong>Monthly Working Time Summary:</strong> Aggregated hours and costs by month.</p>
                <p><strong>Budget Forecast:</strong> Projects future budget trends based on average monthly costs from the last 2 months. Green = positive forecast, orange = negative.</p>

                <h3>Data Table</h3>
                <p>The data table shows all records with the following features:</p>
                <ul>
                    <li><strong>Event Type Filter:</strong> Filter the table by event type (Working Time, PO, Invoice, etc.) using the dropdown above the table.</li>
                    <li><strong>Column Sorting:</strong> Click any column header to sort. Click again to toggle between ascending and descending order. The active sort column shows an arrow indicator.</li>
                    <li><strong>Pagination:</strong> Choose page size (25, 50, 100, 250, or All rows) to control how many records are displayed at once.</li>
                    <li><strong>Sheet Filter:</strong> Filter the table to show records from a specific Excel sheet/tab.</li>
                    <li><strong>Search:</strong> Full-text search across all fields.</li>
                    <li><strong>Comment Column:</strong> A visible column showing comment text (truncated if long; hover to see the full text). Comments come from both a dedicated Comment column and cell-level Excel comments (sticky notes).</li>
                    <li><strong>Export:</strong> Export filtered data to CSV (includes Sheet and Comment columns).</li>
                </ul>

                <h3>Project Details</h3>
                <p>Each project card shows detailed financial information including:</p>
                <ul>
                    <li><strong>Budget:</strong> Total Purchase Order coverage for the project</li>
                    <li><strong>Total Costs:</strong> Sum of all cost types (Working Time + Purchase + T&amp;L)</li>
                    <li><strong>Closure Date:</strong> Project end date (from Closure events)</li>
                    <li><strong>EAC (Estimated At Completion):</strong> Forecasted remaining budget at closure</li>
                    <li><strong>Invoices:</strong> Total invoiced amounts</li>
                    <li><strong>Missing Coverage/Overcovered:</strong> (Invoiced + Positive Financial Record) minus Total Costs</li>
                    <li><strong>Remaining Budget:</strong> Current budget status (green if positive, red if negative)</li>
                    <li><strong>Working Time / Purchase / T&amp;L Costs:</strong> Breakdown by cost type</li>
                    <li><strong>Deferment:</strong> Positive adds to the budget and counts as invoiced. Negative reduces the budget. Not a cost.</li>
                    <li><strong>Financial Record:</strong> Positive amounts are used in the Coverage ratio. Negative reduces the budget. Not a cost.</li>
                    <li><strong>Coverage:</strong> Shown next to the project name. Calculated as Cost / (Invoiced + Positive Financial Record).</li>
                    <li><strong>Burndown Rate:</strong> Average monthly cost used for budget forecasting</li>
                </ul>

                <h3>Status Indicators</h3>
                <p><strong>Green box:</strong> Forecasted budget is positive</p>
                <p><strong>Yellow box:</strong> Forecasted budget is slightly negative (only in last month and within 10% of project budget)</p>
                <p><strong>Red box:</strong> Forecasted budget is significantly negative (beyond 10% threshold or current budget already negative)</p>

                <h3>Filters</h3>
                <p>Use the filter section to filter data by date range, project, or event type. Quick filters are available for financial years, quarters, and months.</p>
            </div>
        </div>

        <!-- Summary Cards -->
        <div class="summary-section">
            <div class="summary-card">
                <h3>Cost/Invoiced</h3>
                <div class="summary-value" id="costInvoicedRatio">-</div>
            </div>
            <div class="summary-card">
                <h3>Coverage</h3>
                <div class="summary-value" id="coverageRatio">-</div>
            </div>
            <div class="summary-card">
                <h3>Total Projects</h3>
                <div class="summary-value"><span id="totalProjects">{len(projects)}</span><span id="closedProjects" class="closed-count"></span></div>
            </div>
            <div class="summary-card">
                <h3>Project Status</h3>
                <div class="project-status-counts">
                    <span class="status-count-item green" id="greenProjectItem"><span class="status-count-num" id="greenProjectCount">0</span> <span class="status-count-label">Green</span></span>
                    <span class="status-count-item yellow" id="yellowProjectItem"><span class="status-count-num" id="yellowProjectCount">0</span> <span class="status-count-label">Yellow</span></span>
                    <span class="status-count-item red" id="redProjectItem"><span class="status-count-num" id="redProjectCount">0</span> <span class="status-count-label">Red</span></span>
                </div>
            </div>
            <div class="summary-card">
                <h3>Budget</h3>
                <div class="summary-value" id="totalPOCoverage">€{total_po_coverage:,.2f}</div>
            </div>
            <div class="summary-card">
                <h3>Total Costs</h3>
                <div class="summary-value" id="totalCosts">€{total_costs:,.2f}</div>
            </div>
            <div class="summary-card">
                <h3>Total Invoices</h3>
                <div class="summary-value" id="totalInvoices">€{total_invoices:,.2f}</div>
            </div>
            <div class="summary-card">
                <h3 id="missingInvoiceLabel">Missing Coverage/Overcovered</h3>
                <div class="summary-value" id="missingInvoice">€{total_invoices - total_costs:,.2f}</div>
            </div>
            <div class="summary-card">
                <h3>Remaining Budget</h3>
                <div class="summary-value" id="remainingBudget">€{total_po_coverage - total_costs:,.2f}</div>
            </div>
            <div class="summary-card">
                <h3>Total Hours</h3>
                <div class="summary-value" id="totalHours">{total_hours:,.0f}</div>
            </div>
        </div>

        <!-- Filters -->
        <details class="collapsible-section" open>
            <summary><h2>Filters</h2></summary>
            <div class="filters-section">
                <div class="filters">
                    <div class="filter-group">
                        <label for="eventTypeFilter">Event Type:</label>
                        <select id="eventTypeFilter">
                            <option value="all">All Types</option>
                            {''.join(f'<option value="{et}">{et}</option>' for et in sorted(event_types))}
                        </select>
                    </div>
                    <div class="filter-group">
                        <label for="dateFrom">Date From:</label>
                        <input type="date" id="dateFrom" value="{date_from}" />
                    </div>
                    <div class="filter-group">
                        <label for="dateTo">Date To:</label>
                        <input type="date" id="dateTo" value="{date_to}" />
                    </div>
                    <button id="clearFilters" class="btn-secondary">Clear Filters</button>
                </div>

                <!-- Quick Filters -->
                <div class="quick-filters">
                    <h3>Quick Filters</h3>
                    <div class="quick-filter-group">
                        <label>Projects:</label>
                        <div class="quick-filter-buttons" id="projectFilters"></div>
                    </div>
                    <div class="quick-filter-group">
                        <label>Financial Years & Quarters:</label>
                        <div class="quick-filter-buttons" id="financialFilters"></div>
                    </div>
                    <div class="quick-filter-group">
                        <label>Months:</label>
                        <div class="quick-filter-buttons" id="monthFilters"></div>
                    </div>
                </div>
            </div>
        </details>

        <!-- Charts Section -->
        <details class="collapsible-section" open>
            <summary><h2>Charts</h2></summary>
            <div class="charts-section">
                <div class="chart-container">
                    <h3>Budget by Project</h3>
                    <div class="chart-filters" id="projectAmountChartFilters" style="display: none;">
                        <div class="chart-filter-buttons">
                            <button type="button" class="chart-filter-btn" id="projectAmountChartSelectAll">All</button>
                            <button type="button" class="chart-filter-btn" id="projectAmountChartSelectNone">None</button>
                        </div>
                        <div class="chart-filter-checkboxes">
                            <label><input type="checkbox" class="chart-filter-checkbox" data-dataset="0" checked> Budget</label>
                            <label><input type="checkbox" class="chart-filter-checkbox" data-dataset="1" checked> Costs</label>
                            <label><input type="checkbox" class="chart-filter-checkbox" data-dataset="2" checked> Invoices</label>
                            <label><input type="checkbox" class="chart-filter-checkbox" data-dataset="3" checked> Deferment</label>
                            <label><input type="checkbox" class="chart-filter-checkbox" data-dataset="4" checked> Financial Record</label>
                            <label><input type="checkbox" class="chart-filter-checkbox" data-dataset="5" checked> Remaining Budget</label>
                        </div>
                    </div>
                    <canvas id="projectAmountChart"></canvas>
                    <div class="chart-placeholder" id="projectAmountChartPlaceholder">No data available for this chart</div>
                </div>
                <div class="chart-container">
                    <h3>Hours by Project</h3>
                    <canvas id="projectHoursChart"></canvas>
                    <div class="chart-placeholder" id="projectHoursChartPlaceholder">No data available for this chart</div>
                </div>
                <div class="chart-container">
                    <h3>Hours by Month</h3>
                    <canvas id="monthlyHoursChart"></canvas>
                    <div class="chart-placeholder" id="monthlyHoursChartPlaceholder">No data available for this chart</div>
                </div>
                <div class="chart-container">
                    <h3>Timeline</h3>
                    <canvas id="timelineChart"></canvas>
                    <div class="chart-placeholder" id="timelineChartPlaceholder">No data available for this chart</div>
                </div>
                <div class="chart-container">
                    <h3>Budget Forecast</h3>
                    <canvas id="forecastChart"></canvas>
                    <div class="chart-placeholder" id="forecastChartPlaceholder">No data available for this chart</div>
                </div>
            </div>
        </details>

        <!-- Data Table -->
        <details class="collapsible-section" open>
            <summary><h2>Data Table <span id="tableRecordCount" style="font-size: 0.7em; color: var(--color-text-muted); font-weight: normal;"></span></h2></summary>
            <div class="table-section">
                <div class="table-controls">
                    <input type="text" id="searchInput" placeholder="Search..." />
                    <select id="tableEventTypeFilter" style="padding: 10px; border: 1px solid var(--color-border); border-radius: 5px; font-size: 0.95em; background: var(--color-surface); color: var(--color-text);">
                        <option value="all">All Types</option>
                    </select>
                    <select id="tableSheetFilter" style="padding: 10px; border: 1px solid var(--color-border); border-radius: 5px; font-size: 0.95em; background: var(--color-surface); color: var(--color-text);">
                        <option value="all">All Sheets</option>
                    </select>
                    <select id="tablePageSize" style="padding: 10px; border: 1px solid var(--color-border); border-radius: 5px; font-size: 0.95em; background: var(--color-surface); color: var(--color-text);">
                        <option value="25">25 rows</option>
                        <option value="50" selected>50 rows</option>
                        <option value="100">100 rows</option>
                        <option value="250">250 rows</option>
                        <option value="all">All rows</option>
                    </select>
                    <button id="exportBtn" class="btn-primary">Export to CSV</button>
                </div>
                <div class="table-wrapper">
                    <table id="dataTable">
                        <thead>
                            <tr>
                                <th class="sortable" data-sort="index">#</th>
                                <th class="sortable" data-sort="date">Date</th>
                                <th class="sortable" data-sort="event_type">Event Type</th>
                                <th class="sortable" data-sort="project">Project</th>
                                <th class="sortable" data-sort="sheet">Sheet</th>
                                <th class="sortable" data-sort="hourly_rate">Hourly Rate</th>
                                <th class="sortable" data-sort="additional_rate">Additional Rate</th>
                                <th class="sortable" data-sort="hours">Hours</th>
                                <th class="sortable" data-sort="amount">Amount/Cost</th>
                                <th class="sortable" data-sort="comment">Comment</th>
                            </tr>
                        </thead>
                        <tbody id="tableBody">
                        </tbody>
                    </table>
                </div>
                <div class="table-pagination" id="tablePagination">
                    <button class="btn-secondary btn-sm" id="prevPage" disabled>&laquo; Previous</button>
                    <span id="pageInfo" style="padding: 6px 12px; color: var(--color-text-secondary);"></span>
                    <button class="btn-secondary btn-sm" id="nextPage">&raquo; Next</button>
                </div>
            </div>
        </details>

        <!-- Monthly Working Time Summary -->
        <details class="collapsible-section" open>
            <summary><h2>Monthly Working Time Summary</h2></summary>
            <div class="table-section">
                <div class="table-wrapper">
                    <table id="monthlySummaryTable">
                        <thead>
                            <tr>
                                <th>Month</th>
                                <th>Total Hours</th>
                                <th>Total Cost</th>
                                <th>Projects</th>
                            </tr>
                        </thead>
                        <tbody id="monthlySummaryBody">
                        </tbody>
                    </table>
                </div>
            </div>
        </details>

        <!-- Project Details -->
        <details class="collapsible-section" open>
            <summary><h2>Project Details</h2></summary>
            <div class="project-details-section">
                <div id="projectDetails"></div>
            </div>
        </details>
        
    </div>

    <script>
        // Theme management
        function getChartColors() {{
            const style = getComputedStyle(document.documentElement);
            return {{
                grid: style.getPropertyValue('--chart-grid').trim(),
                gridZero: style.getPropertyValue('--chart-grid-zero').trim(),
                text: style.getPropertyValue('--chart-text').trim(),
                po: style.getPropertyValue('--chart-po').trim(),
                costs: style.getPropertyValue('--chart-costs').trim(),
                invoices: style.getPropertyValue('--chart-invoices').trim(),
                deferment: style.getPropertyValue('--chart-deferment').trim(),
                budget: style.getPropertyValue('--chart-budget').trim(),
                hours: style.getPropertyValue('--chart-hours').trim(),
                financialRecord: style.getPropertyValue('--chart-financial-record').trim(),
                forecastNeg: style.getPropertyValue('--chart-forecast-neg').trim(),
                positive: style.getPropertyValue('--color-positive').trim(),
                negative: style.getPropertyValue('--color-negative').trim(),
            }};
        }}

        function applyChartDefaults() {{
            const c = getChartColors();
            Chart.defaults.color = c.text;
            Chart.defaults.borderColor = c.grid;
        }}

        function initTheme() {{
            const saved = localStorage.getItem('talaria-theme');
            if (saved === 'dark' || (!saved && window.matchMedia('(prefers-color-scheme: dark)').matches)) {{
                document.documentElement.setAttribute('data-theme', 'dark');
            }}
            applyChartDefaults();
        }}
        initTheme();
        // Set correct icon (sun in dark mode, moon in light mode) on load
        document.addEventListener('DOMContentLoaded', function() {{ updateThemeIcon(); }});

        function updateThemeIcon() {{
            const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
            document.getElementById('themeToggle').innerHTML = isDark ? '&#9788;' : '&#9790;';
        }}

        function toggleTheme() {{
            const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
            if (isDark) {{
                document.documentElement.removeAttribute('data-theme');
                localStorage.setItem('talaria-theme', 'light');
            }} else {{
                document.documentElement.setAttribute('data-theme', 'dark');
                localStorage.setItem('talaria-theme', 'dark');
            }}
            updateThemeIcon();
            applyChartDefaults();
            // Re-render charts with new theme colors
            applyFilters();
        }}

        // Embedded data
        const allData = {data_json};
        const projectFinancials = {financials_json};
        const monthlyWorkingTime = {monthly_summary_json};
        let filteredData = [...allData];

        // Initialize dashboard
        $(document).ready(function() {{
            // Theme toggle
            $('#themeToggle').on('click', toggleTheme);
            // Help modal functionality
            $('#helpIcon').on('click', function() {{
                $('#helpModal').addClass('active');
            }});
            
            $('#closeHelp').on('click', function() {{
                $('#helpModal').removeClass('active');
            }});
            
            $('#helpModal').on('click', function(e) {{
                if ($(e.target).is('#helpModal')) {{
                    $('#helpModal').removeClass('active');
                }}
            }});
            
            // Set date filters to first and last event dates
            const dates = allData.map(r => r.date).filter(d => d).map(d => {{
                // Ensure date is in YYYY-MM-DD format (remove time if present)
                if (d && typeof d === 'string' && d.length > 10) {{
                    return d.split(' ')[0];
                }}
                return d;
            }}).sort();
            if (dates.length > 0) {{
                $('#dateFrom').val(dates[0]);
                $('#dateTo').val(dates[dates.length - 1]);
            }}
            
            // Populate sheet filter dropdown
            const sheets = [...new Set(allData.map(r => r.sheet).filter(Boolean))].sort();
            sheets.forEach(s => {{
                $('#tableSheetFilter').append($('<option>').val(s).text(s));
            }});

            renderTable(allData);
            renderCharts(allData);
            renderProjectDetails(allData);
            renderMonthlySummary(allData, 'all');
            updateSummary(allData);
            renderForecastChart(allData);
            // Filter handlers
            $('#eventTypeFilter, #dateFrom, #dateTo').on('change', applyFilters);
            $('#clearFilters').on('click', clearFilters);

            // Initialize quick filters
            initializeQuickFilters();

            // Populate table event type filter
            const tableEventTypes = [...new Set(allData.map(r => r.event_type).filter(Boolean))].sort();
            tableEventTypes.forEach(et => {{
                $('#tableEventTypeFilter').append($('<option>').val(et).text(et));
            }});

            // Table search — also respects sheet and event type filters
            function applyTableFilters() {{
                const searchTerm = $('#searchInput').val().toLowerCase();
                const sheetFilter = $('#tableSheetFilter').val();
                const eventTypeFilter = $('#tableEventTypeFilter').val();
                let tableData = filteredData;
                if (sheetFilter !== 'all') {{
                    tableData = tableData.filter(row => row.sheet === sheetFilter);
                }}
                if (eventTypeFilter !== 'all') {{
                    tableData = tableData.filter(row => row.event_type === eventTypeFilter);
                }}
                if (searchTerm) {{
                    tableData = tableData.filter(row => {{
                        return Object.values(row).some(val =>
                            String(val).toLowerCase().includes(searchTerm)
                        );
                    }});
                }}
                renderTable(tableData);
            }}
            $('#searchInput').on('keyup', applyTableFilters);
            $('#tableSheetFilter').on('change', applyTableFilters);
            $('#tableEventTypeFilter').on('change', applyTableFilters);

            // Pagination controls
            $('#prevPage').on('click', function() {{
                if (currentPage > 1) {{
                    currentPage--;
                    renderTablePage();
                }}
            }});
            $('#nextPage').on('click', function() {{
                currentPage++;
                renderTablePage();
            }});
            $('#tablePageSize').on('change', function() {{
                currentPage = 1;
                renderTablePage();
            }});

            $('#exportBtn').on('click', exportToCSV);
        }});
        
        function applyFilters() {{
            // Get selected project from quick filter buttons
            const selectedProjectBtn = $('.quick-filter-btn[data-project].active');
            const project = selectedProjectBtn.length > 0 ? selectedProjectBtn.data('project') : 'all';
            
            const eventType = $('#eventTypeFilter').val();
            const dateFrom = $('#dateFrom').val();
            const dateTo = $('#dateTo').val();
            
            filteredData = allData.filter(row => {{
                if (project !== 'all' && row.project !== project) return false;
                if (eventType !== 'all' && row.event_type !== eventType) return false;
                if (dateFrom && row.date < dateFrom) return false;
                if (dateTo && row.date > dateTo) return false;
                return true;
            }});
            
            const projectFilter = project;
            renderTable(filteredData);
            renderCharts(filteredData);
            renderProjectDetails(filteredData);
            renderMonthlySummary(filteredData, projectFilter);
            updateSummary(filteredData);
            renderForecastChart(allData);
        }}
        
        function clearFilters() {{
            // Reset project filter to "All Projects"
            $('.quick-filter-btn[data-project]').removeClass('active');
            $('.quick-filter-btn[data-project][data-project="all"]').addClass('active');
            
            $('#eventTypeFilter').val('all');
            // Reset to first and last event dates
            const dates = allData.map(r => r.date).filter(d => d).map(d => {{
                if (d && typeof d === 'string' && d.length > 10) {{
                    return d.split(' ')[0];
                }}
                return d;
            }}).sort();
            if (dates.length > 0) {{
                $('#dateFrom').val(dates[0]);
                $('#dateTo').val(dates[dates.length - 1]);
            }} else {{
                $('#dateFrom').val('');
                $('#dateTo').val('');
            }}
            // Remove active class from quick filter buttons
            $('.quick-filter-btn').removeClass('active');
            filteredData = [...allData];
            // Get selected project from quick filter buttons
            const selectedProjectBtn = $('.quick-filter-btn[data-project].active');
            const projectFilter = selectedProjectBtn.length > 0 ? selectedProjectBtn.data('project') : 'all';
            renderTable(filteredData);
            renderCharts(filteredData);
            renderProjectDetails(filteredData);
            renderMonthlySummary(filteredData, projectFilter);
            updateSummary(filteredData);
            renderForecastChart(allData);
        }}
        
        function initializeQuickFilters() {{
            // Generate project quick filters
            const projectFilters = $('#projectFilters');
            projectFilters.empty();
            
            // Add "All Projects" button
            const allProjectsBtn = $('<button class="quick-filter-btn active" data-project="all">All Projects</button>');
            allProjectsBtn.on('click', function() {{
                $('.quick-filter-btn[data-project]').removeClass('active');
                $(this).addClass('active');
                applyFilters();
            }});
            projectFilters.append(allProjectsBtn);
            
            // Get unique projects from data
            const projects = [...new Set(allData.map(r => r.project).filter(p => p))].sort();
            
            // Add project buttons
            projects.forEach(project => {{
                const btn = $(`<button class="quick-filter-btn" data-project="${{project}}">${{project}}</button>`);
                btn.on('click', function() {{
                    $('.quick-filter-btn[data-project]').removeClass('active');
                    $(this).addClass('active');
                    applyFilters();
                }});
                projectFilters.append(btn);
            }});
            
            // Generate financial years and quarters (FY starts April 1)
            // Financial year format: FY26 = 2025-2026 financial year (April 1, 2025 - March 31, 2026)
            // FY26Q1 = April 1, 2025 - June 30, 2025
            const financialFilters = $('#financialFilters');
            financialFilters.empty();
            
            // Find date range from data
            const dates = allData.map(r => r.date).filter(d => d).map(d => {{
                if (d && typeof d === 'string' && d.length > 10) {{
                    return d.split(' ')[0];
                }}
                return d;
            }}).sort();
            
            if (dates.length > 0) {{
                const firstDate = new Date(dates[0]);
                const lastDate = new Date(dates[dates.length - 1]);
                
                // Generate financial years first
                // Financial year numbering: FY26 = FY that ends in 2026 (April 2025 - March 2026)
                // So FY number = last two digits of the calendar year when FY ends (March)
                
                let startYear = firstDate.getFullYear();
                let startMonth = firstDate.getMonth() + 1; // 1-12
                
                // Find the financial year that contains the first date
                // FY starts in April, so if month < 4, we're in the previous FY
                let fyStartYear = startYear;
                if (startMonth < 4) {{
                    fyStartYear = startYear - 1;
                }}
                
                // Generate full financial years
                const financialYears = [];
                let currentFYStartYear = fyStartYear;
                let doneYears = false;
                
                while (!doneYears) {{
                    const fyEndYear = currentFYStartYear + 1;
                    const fyStart = new Date(currentFYStartYear, 3, 1); // April 1
                    const fyEnd = new Date(fyEndYear, 2, 31); // March 31
                    
                    // Check if financial year overlaps with data range
                    if (fyEnd >= firstDate && fyStart <= lastDate) {{
                        const fyNumber = String(fyEndYear).slice(-2);
                        financialYears.push({{
                            label: `FY${{fyNumber}}`,
                            start: `${{currentFYStartYear}}-${{String(4).padStart(2, '0')}}-01`,
                            end: `${{fyEndYear}}-${{String(3).padStart(2, '0')}}-31`
                        }});
                    }}
                    
                    if (fyStart > lastDate) {{
                        doneYears = true;
                    }} else {{
                        currentFYStartYear++;
                        if (currentFYStartYear > lastDate.getFullYear() + 1) {{
                            doneYears = true;
                        }}
                    }}
                }}
                
                // Add financial year buttons
                financialYears.forEach(fy => {{
                    const btn = $(`<button class="quick-filter-btn" data-start="${{fy.start}}" data-end="${{fy.end}}">${{fy.label}}</button>`);
                    btn.on('click', function() {{
                        $('.quick-filter-btn').removeClass('active');
                        $(this).addClass('active');
                        $('#dateFrom').val(fy.start);
                        $('#dateTo').val(fy.end);
                        applyFilters();
                    }});
                    financialFilters.append(btn);
                }});
                
                // Generate quarters from first date to last date
                // FY26Q4 = January 1, 2026 - March 31, 2026
                
                // Reset for quarters
                currentFYStartYear = fyStartYear;
                const quarters = [];
                let done = false;
                
                while (!done) {{
                    // Q1: Apr-Jun, Q2: Jul-Sep, Q3: Oct-Dec, Q4: Jan-Mar
                    for (let q = 1; q <= 4; q++) {{
                        let startMonth, endMonth, startYear, endYear;
                        
                        if (q === 1) {{
                            // Q1: April 1 - June 30
                            startMonth = 4; endMonth = 6;
                            startYear = currentFYStartYear; endYear = currentFYStartYear;
                        }} else if (q === 2) {{
                            // Q2: July 1 - September 30
                            startMonth = 7; endMonth = 9;
                            startYear = currentFYStartYear; endYear = currentFYStartYear;
                        }} else if (q === 3) {{
                            // Q3: October 1 - December 31
                            startMonth = 10; endMonth = 12;
                            startYear = currentFYStartYear; endYear = currentFYStartYear;
                        }} else {{
                            // Q4: January 1 - March 31 (next calendar year)
                            startMonth = 1; endMonth = 3;
                            startYear = currentFYStartYear + 1; endYear = currentFYStartYear + 1;
                        }}
                        
                        const quarterStart = new Date(startYear, startMonth - 1, 1);
                        const quarterEnd = new Date(endYear, endMonth, 0); // Last day of month
                        
                        // Check if quarter overlaps with data range
                        if (quarterEnd >= firstDate && quarterStart <= lastDate) {{
                            // FY number = last two digits of the year when FY ends (March)
                            // FY26 ends in March 2026, so FY number = 26
                            const fyEndYear = currentFYStartYear + 1;
                            const fyNumber = String(fyEndYear).slice(-2);
                            const fyLabel = `FY${{fyNumber}}Q${{q}}`;
                            quarters.push({{
                                label: fyLabel,
                                start: `${{startYear}}-${{String(startMonth).padStart(2, '0')}}-01`,
                                end: `${{endYear}}-${{String(endMonth).padStart(2, '0')}}-${{String(quarterEnd.getDate()).padStart(2, '0')}}`
                            }});
                        }}
                        
                        // Stop if we've passed the last date
                        if (quarterStart > lastDate) {{
                            done = true;
                            break;
                        }}
                    }}
                    
                    currentFYStartYear++;
                    if (currentFYStartYear > lastDate.getFullYear() + 1) {{
                        done = true;
                    }}
                }}
                
                quarters.forEach(q => {{
                    const btn = $(`<button class="quick-filter-btn" data-start="${{q.start}}" data-end="${{q.end}}">${{q.label}}</button>`);
                    btn.on('click', function() {{
                        $('.quick-filter-btn').removeClass('active');
                        $(this).addClass('active');
                        $('#dateFrom').val(q.start);
                        $('#dateTo').val(q.end);
                        applyFilters();
                    }});
                    financialFilters.append(btn);
                }});
            }}
            
            // Generate months
            const monthFilters = $('#monthFilters');
            monthFilters.empty();
            
            if (dates.length > 0) {{
                const monthSet = new Set();
                dates.forEach(d => {{
                    const date = new Date(d);
                    const year = date.getFullYear();
                    const month = date.getMonth() + 1;
                    const monthStr = `${{year}}-${{String(month).padStart(2, '0')}}`;
                    monthSet.add(monthStr);
                }});
                
                const sortedMonths = Array.from(monthSet).sort();
                
                sortedMonths.forEach(monthStr => {{
                    const [year, month] = monthStr.split('-').map(Number);
                    const date = new Date(year, month - 1, 1);
                    const monthNames = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
                    const monthLabel = `${{monthNames[month - 1]}}-${{String(year).slice(-2)}}`;
                    
                    // Get first and last day of month
                    const firstDay = `${{year}}-${{String(month).padStart(2, '0')}}-01`;
                    const lastDay = new Date(year, month, 0);
                    const lastDayStr = `${{year}}-${{String(month).padStart(2, '0')}}-${{String(lastDay.getDate()).padStart(2, '0')}}`;
                    
                    const btn = $(`<button class="quick-filter-btn" data-start="${{firstDay}}" data-end="${{lastDayStr}}">${{monthLabel}}</button>`);
                    btn.on('click', function() {{
                        $('.quick-filter-btn').removeClass('active');
                        $(this).addClass('active');
                        $('#dateFrom').val(firstDay);
                        $('#dateTo').val(lastDayStr);
                        applyFilters();
                    }});
                    monthFilters.append(btn);
                }});
            }}
        }}
        
        // Helper function to format EUR amounts: remove decimals for values >= 100
        function formatEUR(value) {{
            if (value === null || value === undefined || value === '') return '';
            const numValue = typeof value === 'number' ? value : parseFloat(value);
            if (isNaN(numValue)) return '';
            if (Math.abs(numValue) >= 100) {{
                return '€' + Math.round(numValue).toLocaleString('en-US');
            }} else {{
                return '€' + numValue.toLocaleString('en-US', {{minimumFractionDigits: 2, maximumFractionDigits: 2}});
            }}
        }}
        
        function updateSummary(data) {{
            const projects = [...new Set(data.map(r => r.project).filter(p => p))];
            const totalHours = data.reduce((sum, r) => sum + (r.hours || 0), 0);
            
            // Calculate financials from filtered data
            let poCoverage = 0;
            let invoices = 0;  // Informational only, not a cost
            let workingTimeCosts = 0;
            let purchaseCosts = 0;
            let tlCosts = 0;
            let deferment = 0;
            let financialRecord = 0;
            let positiveFinancialRecord = 0;

            data.forEach(row => {{
                const eventType = row.event_type || '';
                const amount = row.amount || 0;

                if (eventType === 'PO') {{
                    poCoverage += amount;
                }} else if (eventType === 'Invoice') {{
                    invoices += amount;  // Track for information, but don't count as cost
                }} else if (eventType === 'Working Time' && row.calculated_cost) {{
                    workingTimeCosts += row.calculated_cost;
                }} else if (eventType === 'Purchase') {{
                    purchaseCosts += amount;
                }} else if (eventType === 'T&L') {{
                    tlCosts += amount;
                }} else if (eventType === 'Deferment') {{
                    deferment += amount;  // Can be positive or negative
                    // Positive deferment: add to PO coverage and count as invoiced
                    // Negative deferment: subtract from PO coverage
                    if (amount > 0) {{
                        poCoverage += amount;
                        invoices += amount;  // Count positive deferment as invoiced
                    }} else if (amount < 0) {{
                        poCoverage += amount;  // Subtract negative deferment from PO (amount is already negative)
                    }}
                }} else if (eventType === 'Financial Record') {{
                    financialRecord += amount;
                    if (amount > 0) {{
                        positiveFinancialRecord += amount;
                    }} else if (amount < 0) {{
                        // Negative: decrease budget (like negative deferment)
                        poCoverage += amount;
                    }}
                }}
            }});

            // Total costs = Working Time + Purchase + T&L (Deferment is NOT a cost)
            const totalCosts = workingTimeCosts + purchaseCosts + tlCosts;
            // Remaining budget = PO Coverage - Total Costs (invoices are informational only)
            const remainingBudget = poCoverage - totalCosts;
            // Coverage gap = (Invoiced + Positive Financial Record) - Total Costs
            // Negative = missing coverage, Positive = overcovered
            const coverageGap = (invoices + positiveFinancialRecord) - totalCosts;
            
            // Calculate Invoiced/Cost ratio as percentage
            let invoicedCostRatio = '-';
            if (totalCosts > 0) {{
                const ratio = (invoices / totalCosts) * 100;
                invoicedCostRatio = ratio.toFixed(1) + '%';
            }} else if (invoices > 0) {{
                invoicedCostRatio = '∞';
            }}
            
            // Calculate Coverage = Cost / (Invoiced + Positive Financial Record)
            let coverageRatioText = '-';
            const globalCoverageDenom = invoices + positiveFinancialRecord;
            if (globalCoverageDenom > 0 && totalCosts > 0) {{
                coverageRatioText = (totalCosts / globalCoverageDenom * 100).toFixed(1) + '%';
            }} else if (totalCosts === 0 && globalCoverageDenom >= 0) {{
                coverageRatioText = '0%';
            }}

            $('#costInvoicedRatio').text(invoicedCostRatio);
            $('#coverageRatio').text(coverageRatioText);
            // Count closed projects (those with a Closure event)
            const closedProjectSet = new Set();
            data.forEach(row => {{
                if (row.event_type === 'Closure' && row.project) {{
                    closedProjectSet.add(row.project);
                }}
            }});
            const closedCount = projects.filter(p => closedProjectSet.has(p)).length;
            const activeCount = projects.length - closedCount;
            $('#totalProjects').text(activeCount);
            if (closedCount > 0) {{
                $('#closedProjects').text(' +' + closedCount).attr('title', closedCount + ' closed');
            }} else {{
                $('#closedProjects').text('');
            }}
            $('#totalPOCoverage').text(formatEUR(poCoverage));
            $('#totalCosts').text(formatEUR(totalCosts));
            $('#totalInvoices').text(formatEUR(invoices));
            // Update Missing Coverage/Overcovered display
            const coverageGapElement = $('#missingInvoice');
            const coverageGapLabelElement = $('#missingInvoiceLabel');

            if (Math.abs(coverageGap) < 0.01) {{
                // Zero or very close to zero - show checkmark
                coverageGapLabelElement.text('Balanced');
                coverageGapElement.text('✓');
                coverageGapElement.css('color', 'var(--color-positive)');
            }} else if (coverageGap < 0) {{
                // Negative - missing coverage
                coverageGapLabelElement.text('Missing Coverage');
                coverageGapElement.text(formatEUR(coverageGap));
                coverageGapElement.css('color', 'var(--color-negative)');
            }} else {{
                // Positive - overcovered
                coverageGapLabelElement.text('Overcovered');
                coverageGapElement.text(formatEUR(coverageGap));
                coverageGapElement.css('color', '');
            }}
            $('#remainingBudget').text(formatEUR(remainingBudget));
            $('#totalHours').text(totalHours.toLocaleString('en-US', {{minimumFractionDigits: 0, maximumFractionDigits: 0}}));
        }}
        
        // Table pagination and sorting state
        let currentTableData = [];
        let currentPage = 1;
        let tableSortColumn = 'date';
        let tableSortDirection = 'asc';

        function getPageSize() {{
            const val = $('#tablePageSize').val();
            return val === 'all' ? Infinity : parseInt(val);
        }}

        function renderTablePage() {{
            const tbody = $('#tableBody');
            tbody.empty();

            const pageSize = getPageSize();
            const totalRows = currentTableData.length;
            const totalPages = pageSize === Infinity ? 1 : Math.max(1, Math.ceil(totalRows / pageSize));
            if (currentPage > totalPages) currentPage = totalPages;
            if (currentPage < 1) currentPage = 1;

            const startIdx = pageSize === Infinity ? 0 : (currentPage - 1) * pageSize;
            const endIdx = pageSize === Infinity ? totalRows : Math.min(startIdx + pageSize, totalRows);
            const pageData = currentTableData.slice(startIdx, endIdx);

            pageData.forEach(row => {{
                const tr = $('<tr>');

                tr.append($('<td>').text(row.index || ''));
                tr.append($('<td>').text(row.date || ''));
                tr.append($('<td>').text(row.event_type || ''));
                tr.append($('<td>').text(row.project || ''));
                tr.append($('<td>').text(row.sheet || ''));
                tr.append($('<td>').text(formatEUR(row.hourly_rate)));
                let additionalRateDisplay = '';
                if (row.additional_rate !== null && row.additional_rate !== undefined) {{
                    const percentage = row.additional_rate * 100;
                    additionalRateDisplay = percentage >= 100 ? Math.round(percentage) + '%' : percentage.toFixed(2) + '%';
                }}
                tr.append($('<td>').text(additionalRateDisplay));
                tr.append($('<td>').text(row.hours ? row.hours.toFixed(1) : ''));
                const displayAmount = (row.event_type === 'Working Time' && row.calculated_cost)
                    ? row.calculated_cost
                    : (row.amount || 0);
                tr.append($('<td>').text(formatEUR(displayAmount)));

                // Comment column
                const commentText = row.comment || '';
                const commentTd = $('<td>').addClass('comment-cell').text(commentText);
                tr.append(commentTd);
                tbody.append(tr);
            }});

            // Update pagination controls
            $('#prevPage').prop('disabled', currentPage <= 1);
            $('#nextPage').prop('disabled', currentPage >= totalPages);
            $('#pageInfo').text(totalRows === 0 ? 'No records' : `Page ${{currentPage}} of ${{totalPages}} (${{totalRows}} records)`);
            $('#tableRecordCount').text(`(${{totalRows}} records)`);

            // Show/hide pagination when all rows shown
            if (pageSize === Infinity || totalPages <= 1) {{
                $('#tablePagination').hide();
            }} else {{
                $('#tablePagination').show();
            }}
        }}

        function sortTableData(data) {{
            const col = tableSortColumn;
            const dir = tableSortDirection === 'asc' ? 1 : -1;
            const numericCols = ['index', 'hourly_rate', 'additional_rate', 'hours', 'amount'];
            return [...data].sort((a, b) => {{
                let valA, valB;
                if (col === 'amount') {{
                    valA = (a.event_type === 'Working Time' && a.calculated_cost) ? a.calculated_cost : (a.amount || 0);
                    valB = (b.event_type === 'Working Time' && b.calculated_cost) ? b.calculated_cost : (b.amount || 0);
                }} else {{
                    valA = a[col];
                    valB = b[col];
                }}
                if (numericCols.includes(col)) {{
                    return ((valA || 0) - (valB || 0)) * dir;
                }}
                return String(valA || '').localeCompare(String(valB || '')) * dir;
            }});
        }}

        function updateSortIndicators() {{
            $('#dataTable thead th.sortable').each(function() {{
                const th = $(this);
                const col = th.data('sort');
                // Remove existing indicators
                th.find('.sort-indicator').remove();
                if (col === tableSortColumn) {{
                    const arrow = tableSortDirection === 'asc' ? ' \u25B2' : ' \u25BC';
                    th.append($('<span>').addClass('sort-indicator').text(arrow));
                }}
            }});
        }}

        function renderTable(data) {{
            currentTableData = sortTableData(data);
            currentPage = 1;
            updateSortIndicators();
            renderTablePage();
        }}

        // Column sorting click handler
        $(document).on('click', '#dataTable thead th.sortable', function() {{
            const col = $(this).data('sort');
            if (tableSortColumn === col) {{
                tableSortDirection = tableSortDirection === 'asc' ? 'desc' : 'asc';
            }} else {{
                tableSortColumn = col;
                tableSortDirection = 'asc';
            }}
            currentTableData = sortTableData(currentTableData);
            currentPage = 1;
            updateSortIndicators();
            renderTablePage();
        }});

        function renderCharts(data) {{
            // Financials by Project
            const projectPOCoverage = {{}};
            const projectCosts = {{}};
            const projectInvoices = {{}};
            const projectDeferment = {{}};
            const projectFinancialRecord = {{}};
            const projectHours = {{}};
            
            // Timeline data: monthly costs and remaining budget
            const monthlyCosts = {{}};
            const monthlyPOCoverage = {{}};
            
            data.forEach(row => {{
                const project = row.project || 'Unknown';
                const eventType = row.event_type || 'Unknown';
                const date = row.date || '';
                const amount = row.amount || 0;
                
                // PO Coverage by project (includes PO events and positive deferment)
                if (eventType === 'PO' && amount) {{
                    projectPOCoverage[project] = (projectPOCoverage[project] || 0) + amount;
                }}
                
                // Deferment handling: positive adds to PO and counts as invoiced, negative reduces PO
                if (eventType === 'Deferment' && amount) {{
                    projectDeferment[project] = (projectDeferment[project] || 0) + amount;
                    if (amount > 0) {{
                        // Positive deferment: add to PO coverage and count as invoiced
                        projectPOCoverage[project] = (projectPOCoverage[project] || 0) + amount;
                        projectInvoices[project] = (projectInvoices[project] || 0) + amount;
                    }} else if (amount < 0) {{
                        // Negative deferment: subtract from PO coverage
                        projectPOCoverage[project] = (projectPOCoverage[project] || 0) + amount;
                    }}
                }}

                // Financial Record: negative reduces PO coverage; positive is used for Coverage ratio only
                if (eventType === 'Financial Record' && amount) {{
                    projectFinancialRecord[project] = (projectFinancialRecord[project] || 0) + amount;
                    if (amount < 0) {{
                        projectPOCoverage[project] = (projectPOCoverage[project] || 0) + amount;
                    }}
                }}
                
                // Costs by project (Working Time costs, Purchases, T&L - Deferment is NOT a cost)
                if (eventType === 'Working Time' && row.calculated_cost) {{
                    projectCosts[project] = (projectCosts[project] || 0) + row.calculated_cost;
                }} else if ((eventType === 'Purchase' || eventType === 'T&L') && amount) {{
                    projectCosts[project] = (projectCosts[project] || 0) + amount;
                }}
                
                // Invoices by project (includes Invoice events and positive deferment)
                if (eventType === 'Invoice' && amount) {{
                    projectInvoices[project] = (projectInvoices[project] || 0) + amount;
                }}
                
                // Hours by project
                if (row.hours) {{
                    projectHours[project] = (projectHours[project] || 0) + row.hours;
                }}
                
                // Timeline: aggregate by month (YYYY-MM)
                if (date && date.length >= 7) {{
                    const month = date.substring(0, 7);  // YYYY-MM
                    
                    // Monthly PO Coverage (includes PO events and deferment)
                    if (eventType === 'PO' && amount) {{
                        monthlyPOCoverage[month] = (monthlyPOCoverage[month] || 0) + amount;
                    }}
                    if (eventType === 'Deferment' && amount) {{
                        monthlyPOCoverage[month] = (monthlyPOCoverage[month] || 0) + amount;
                    }}
                    // Negative Financial Record reduces PO coverage
                    if (eventType === 'Financial Record' && amount < 0) {{
                        monthlyPOCoverage[month] = (monthlyPOCoverage[month] || 0) + amount;
                    }}

                    // Monthly Costs (Deferment is NOT a cost)
                    if (eventType === 'Working Time' && row.calculated_cost) {{
                        monthlyCosts[month] = (monthlyCosts[month] || 0) + row.calculated_cost;
                    }} else if ((eventType === 'Purchase' || eventType === 'T&L') && amount) {{
                        monthlyCosts[month] = (monthlyCosts[month] || 0) + amount;
                    }}
                }}
            }});
            
            // Aggregate hours by month and project
            const monthlyHoursByProject = {{}};
            const monthlyHoursMonthSet = new Set();
            const monthlyHoursProjectSet = new Set();
            data.forEach(row => {{
                if (row.hours && row.date && row.date.length >= 7) {{
                    const month = row.date.substring(0, 7);
                    const project = row.project || 'Unknown';
                    monthlyHoursMonthSet.add(month);
                    monthlyHoursProjectSet.add(project);
                    if (!monthlyHoursByProject[project]) monthlyHoursByProject[project] = {{}};
                    monthlyHoursByProject[project][month] = (monthlyHoursByProject[project][month] || 0) + row.hours;
                }}
            }});

            // Destroy existing charts
            if (window.projectFinancialChart && typeof window.projectFinancialChart.destroy === 'function') {{
                window.projectFinancialChart.destroy();
            }}
            if (window.projectHoursChart && typeof window.projectHoursChart.destroy === 'function') {{
                window.projectHoursChart.destroy();
            }}
            if (window.monthlyHoursChart && typeof window.monthlyHoursChart.destroy === 'function') {{
                window.monthlyHoursChart.destroy();
            }}
            if (window.timelineChart && typeof window.timelineChart.destroy === 'function') {{
                window.timelineChart.destroy();
            }}
            if (window.forecastChart && typeof window.forecastChart.destroy === 'function') {{
                window.forecastChart.destroy();
            }}
            
            // Financials by Project Chart (PO Coverage, Costs, Invoices, Deferment)
            const allProjects = [...new Set([...Object.keys(projectPOCoverage), ...Object.keys(projectCosts), ...Object.keys(projectInvoices), ...Object.keys(projectDeferment), ...Object.keys(projectFinancialRecord)])].sort();
            
            // Show/hide placeholder
            if (allProjects.length === 0) {{
                $('#projectAmountChartPlaceholder').addClass('show');
            }} else {{
                $('#projectAmountChartPlaceholder').removeClass('show');
            }}
            
            if (allProjects.length > 0) {{
                // Show filter checkboxes
                $('#projectAmountChartFilters').show();
                
                // Preserve checkbox states before creating new chart
                const checkboxStates = {{}};
                $('#projectAmountChartFilters .chart-filter-checkbox').each(function() {{
                    const datasetIndex = parseInt($(this).data('dataset'));
                    checkboxStates[datasetIndex] = $(this).is(':checked');
                }});
                
                // Remove old event listeners to prevent duplicates
                $('#projectAmountChartFilters .chart-filter-checkbox').off('change.chartFilter');
                $('#projectAmountChartSelectAll').off('click.chartFilter');
                $('#projectAmountChartSelectNone').off('click.chartFilter');
                
                const ctx1 = document.getElementById('projectAmountChart').getContext('2d');
                const cc1 = getChartColors();
                window.projectFinancialChart = new Chart(ctx1, {{
                type: 'bar',
                data: {{
                    labels: allProjects,
                    datasets: [
                        {{
                            label: 'Budget (€)',
                            data: allProjects.map(p => projectPOCoverage[p] || 0),
                            backgroundColor: cc1.po + '99',
                            borderColor: cc1.po,
                            borderWidth: 1,
                            hidden: !checkboxStates[0]
                        }},
                        {{
                            label: 'Costs (€)',
                            data: allProjects.map(p => projectCosts[p] || 0),
                            backgroundColor: cc1.costs + '99',
                            borderColor: cc1.costs,
                            borderWidth: 1,
                            hidden: !checkboxStates[1]
                        }},
                        {{
                            label: 'Invoices (€)',
                            data: allProjects.map(p => projectInvoices[p] || 0),
                            backgroundColor: cc1.invoices + '99',
                            borderColor: cc1.invoices,
                            borderWidth: 1,
                            hidden: !checkboxStates[2]
                        }},
                        {{
                            label: 'Deferment (€)',
                            data: allProjects.map(p => projectDeferment[p] || 0),
                            backgroundColor: cc1.deferment + '99',
                            borderColor: cc1.deferment,
                            borderWidth: 1,
                            hidden: !checkboxStates[3]
                        }},
                        {{
                            label: 'Financial Record (€)',
                            data: allProjects.map(p => projectFinancialRecord[p] || 0),
                            backgroundColor: cc1.financialRecord + '99',
                            borderColor: cc1.financialRecord,
                            borderWidth: 1,
                            hidden: !checkboxStates[4]
                        }},
                        {{
                            label: 'Remaining Budget (€)',
                            data: allProjects.map(p => (projectPOCoverage[p] || 0) - (projectCosts[p] || 0)),
                            backgroundColor: cc1.budget + '99',
                            borderColor: cc1.budget,
                            borderWidth: 1,
                            hidden: !checkboxStates[5]
                        }}
                    ]
                }},
                options: {{
                    responsive: true,
                    maintainAspectRatio: true,
                    scales: {{
                        y: {{
                            beginAtZero: true,
                            ticks: {{
                                callback: function(value) {{
                                    return formatEUR(value);
                                }}
                            }},
                            grid: {{
                                color: function(context) {{
                                    const c = getChartColors();
                                    if (context.tick.value === 0) {{
                                        return c.gridZero;
                                    }}
                                    return c.grid;
                                }},
                                lineWidth: function(context) {{
                                    if (context.tick.value === 0) {{
                                        return 3;
                                    }}
                                    return 1;
                                }}
                            }}
                        }}
                    }}
                }}
            }});
            
                // Apply preserved checkbox states to chart
                window.projectFinancialChart.data.datasets.forEach((dataset, index) => {{
                    if (checkboxStates[index] !== undefined) {{
                        const meta = window.projectFinancialChart.getDatasetMeta(index);
                        meta.hidden = !checkboxStates[index];
                    }}
                }});
                window.projectFinancialChart.update();
                
                // Add event listeners for filter checkboxes (using namespaced events)
                $('#projectAmountChartFilters .chart-filter-checkbox').on('change.chartFilter', function() {{
                    const datasetIndex = parseInt($(this).data('dataset'));
                    const isChecked = $(this).is(':checked');
                    
                    if (window.projectFinancialChart) {{
                        const meta = window.projectFinancialChart.getDatasetMeta(datasetIndex);
                        meta.hidden = !isChecked;
                        window.projectFinancialChart.update();
                    }}
                }});
                
                // Add event listeners for "All" and "None" buttons (using namespaced events)
                $('#projectAmountChartSelectAll').on('click.chartFilter', function() {{
                    $('#projectAmountChartFilters .chart-filter-checkbox').prop('checked', true).trigger('change.chartFilter');
                }});
                
                $('#projectAmountChartSelectNone').on('click.chartFilter', function() {{
                    $('#projectAmountChartFilters .chart-filter-checkbox').prop('checked', false).trigger('change.chartFilter');
                }});
            }} else {{
                // Hide filter checkboxes if no data
                $('#projectAmountChartFilters').hide();
            }}
            
            // Hours by Project Chart
            const hoursProjects = Object.keys(projectHours).sort();
            
            // Show/hide placeholder
            if (hoursProjects.length === 0) {{
                $('#projectHoursChartPlaceholder').addClass('show');
            }} else {{
                $('#projectHoursChartPlaceholder').removeClass('show');
            }}
            
            if (hoursProjects.length > 0) {{
                const ctx2 = document.getElementById('projectHoursChart').getContext('2d');
                const cc2 = getChartColors();
                window.projectHoursChart = new Chart(ctx2, {{
                    type: 'bar',
                    data: {{
                        labels: hoursProjects,
                        datasets: [{{
                            label: 'Hours',
                            data: hoursProjects.map(p => projectHours[p]),
                            backgroundColor: cc2.hours + '99',
                            borderColor: cc2.hours,
                            borderWidth: 1
                        }}]
                    }},
                    options: {{
                        responsive: true,
                        maintainAspectRatio: true,
                        scales: {{
                            y: {{
                                beginAtZero: true
                            }}
                        }}
                    }}
                }});
            }}

            // Hours by Month Chart (stacked by project)
            const hoursMonths = Array.from(monthlyHoursMonthSet).sort();
            const hoursProjects2 = Array.from(monthlyHoursProjectSet).sort();

            if (hoursMonths.length === 0) {{
                $('#monthlyHoursChartPlaceholder').addClass('show');
            }} else {{
                $('#monthlyHoursChartPlaceholder').removeClass('show');
            }}

            if (hoursMonths.length > 0) {{
                const ctx3 = document.getElementById('monthlyHoursChart').getContext('2d');
                // Generate a distinct color for each project
                const projectPalette = [
                    '#4f6bed', '#16a34a', '#dc2626', '#ca8a04', '#7c3aed',
                    '#ea580c', '#0891b2', '#be185d', '#4338ca', '#15803d',
                    '#b91c1c', '#a16207', '#6d28d9', '#c2410c', '#0e7490',
                    '#9d174d', '#3730a3', '#166534', '#991b1b', '#854d0e'
                ];
                const monthlyHoursDatasets = hoursProjects2.map((project, i) => {{
                    const color = projectPalette[i % projectPalette.length];
                    return {{
                        label: project,
                        data: hoursMonths.map(m => (monthlyHoursByProject[project] && monthlyHoursByProject[project][m]) || 0),
                        backgroundColor: color + 'cc',
                        borderColor: color,
                        borderWidth: 1
                    }};
                }});
                window.monthlyHoursChart = new Chart(ctx3, {{
                    type: 'bar',
                    data: {{
                        labels: hoursMonths,
                        datasets: monthlyHoursDatasets
                    }},
                    options: {{
                        responsive: true,
                        maintainAspectRatio: true,
                        scales: {{
                            x: {{ stacked: true }},
                            y: {{ stacked: true, beginAtZero: true }}
                        }},
                        plugins: {{
                            legend: {{ display: true }}
                        }}
                    }}
                }});
            }}

            // Timeline Chart: Monthly Costs and Remaining Budget
            const allMonths = [...new Set([...Object.keys(monthlyCosts), ...Object.keys(monthlyPOCoverage)])].sort();
            
            // Show/hide placeholder
            if (allMonths.length === 0) {{
                $('#timelineChartPlaceholder').addClass('show');
            }} else {{
                $('#timelineChartPlaceholder').removeClass('show');
            }}
            
            if (allMonths.length > 0) {{
                // Calculate cumulative values
                let cumulativePOCoverage = 0;
                let cumulativeCosts = 0;
                const cumulativeRemainingBudget = [];
                const monthlyCostsData = [];
                
                allMonths.forEach(month => {{
                    cumulativePOCoverage += (monthlyPOCoverage[month] || 0);
                    cumulativeCosts += (monthlyCosts[month] || 0);
                    monthlyCostsData.push(monthlyCosts[month] || 0);
                    cumulativeRemainingBudget.push(cumulativePOCoverage - cumulativeCosts);
                }});
                
                const ctx4 = document.getElementById('timelineChart').getContext('2d');
                const cc4 = getChartColors();
                window.timelineChart = new Chart(ctx4, {{
                    type: 'line',
                    data: {{
                        labels: allMonths,
                        datasets: [
                            {{
                                label: 'Monthly Costs (€)',
                                data: monthlyCostsData,
                                borderColor: cc4.costs,
                                backgroundColor: cc4.costs + '1a',
                                tension: 0,
                                fill: false,
                                yAxisID: 'y'
                            }},
                            {{
                                label: 'Remaining Budget (€)',
                                data: cumulativeRemainingBudget,
                                borderColor: cc4.po,
                                backgroundColor: cc4.po + '1a',
                                tension: 0,
                                fill: false,
                                yAxisID: 'y'
                            }}
                        ]
                    }},
                    options: {{
                        responsive: true,
                        maintainAspectRatio: true,
                        interaction: {{
                            mode: 'index',
                            intersect: false
                        }},
                        scales: {{
                            y: {{
                                beginAtZero: false,
                                ticks: {{
                                    callback: function(value) {{
                                        return '€' + value.toLocaleString();
                                    }}
                                }},
                                grid: {{
                                    color: function(context) {{
                                        const c = getChartColors();
                                        if (context.tick.value === 0) {{
                                            return c.gridZero;
                                        }}
                                        return c.grid;
                                    }},
                                    lineWidth: function(context) {{
                                        if (context.tick.value === 0) {{
                                            return 3;
                                        }}
                                        return 1;
                                    }}
                                }}
                            }}
                        }}
                    }}
                }});
            }}
        }}
        
        function calculateProjectForecast(projectData) {{
            // Calculate monthly data for a single project
            const monthlyCosts = {{}};
            const monthlyPOCoverage = {{}};
            let closureMonth = null;
            let closureDate = null;
            
            projectData.forEach(row => {{
                const eventType = row.event_type || '';
                const date = row.date || '';
                const amount = row.amount || 0;
                
                // Check for Closure event (project end date)
                if (eventType === 'Closure' && date) {{
                    closureDate = date;
                    if (date.length >= 7) {{
                        closureMonth = date.substring(0, 7);
                    }}
                }}
                
                if (date && date.length >= 7) {{
                    const month = date.substring(0, 7);
                    
                    // PO coverage (only from actual events in table)
                    if (eventType === 'PO' && amount) {{
                        monthlyPOCoverage[month] = (monthlyPOCoverage[month] || 0) + amount;
                    }}
                    
                    // Deferment: positive adds to PO, negative subtracts from PO
                    if (eventType === 'Deferment' && amount) {{
                        monthlyPOCoverage[month] = (monthlyPOCoverage[month] || 0) + amount;
                    }}
                    // Negative Financial Record reduces PO coverage
                    if (eventType === 'Financial Record' && amount < 0) {{
                        monthlyPOCoverage[month] = (monthlyPOCoverage[month] || 0) + amount;
                    }}

                    // Costs (for forecast trend calculation) - Deferment is NOT a cost
                    if (eventType === 'Working Time' && row.calculated_cost) {{
                        monthlyCosts[month] = (monthlyCosts[month] || 0) + row.calculated_cost;
                    }} else if ((eventType === 'Purchase' || eventType === 'T&L') && amount) {{
                        monthlyCosts[month] = (monthlyCosts[month] || 0) + amount;
                    }}
                }}
            }});
            
            const allMonths = [...new Set([...Object.keys(monthlyCosts), ...Object.keys(monthlyPOCoverage)])].sort();
            
            if (allMonths.length < 1) {{
                return null;
            }}
            
            // Calculate cumulative remaining budget for actual data
            let cumulativePOCoverage = 0;
            let cumulativeCosts = 0;
            const remainingBudgetData = [];
            
            allMonths.forEach(month => {{
                cumulativePOCoverage += (monthlyPOCoverage[month] || 0);
                cumulativeCosts += (monthlyCosts[month] || 0);
                remainingBudgetData.push(cumulativePOCoverage - cumulativeCosts);
            }});
            
            const n = allMonths.length;
            const lastActualBudget = remainingBudgetData[n - 1];
            
            // Calculate average monthly cost from last months
            let avgMonthlyCost = 0;
            const costMonths = Object.keys(monthlyCosts).sort();
            
            if (costMonths.length >= 2) {{
                const lastCostMonth = costMonths[costMonths.length - 1];
                const secondLastCostMonth = costMonths[costMonths.length - 2];
                const lastCost = monthlyCosts[lastCostMonth];
                const secondLastCost = monthlyCosts[secondLastCostMonth];
                avgMonthlyCost = (lastCost + secondLastCost) / 2;
            }} else if (costMonths.length === 1) {{
                avgMonthlyCost = monthlyCosts[costMonths[0]];
            }} else if (n >= 2) {{
                const lastIndex = n - 1;
                const secondLastIndex = n - 2;
                const lastValue = remainingBudgetData[lastIndex];
                const secondLastValue = remainingBudgetData[secondLastIndex];
                avgMonthlyCost = Math.max(0, secondLastValue - lastValue);
            }}
            
            // Calculate forecast
            // Important: Only use PO coverage up to the last actual month
            // After that, forecast only subtracts costs (no new PO coverage)
            const forecastMonths = [...allMonths];
            const forecastData = [...remainingBudgetData];
            const forecastLabels = [...allMonths];
            
            // Last actual month - no PO coverage after this in forecast
            const lastActualMonth = allMonths[allMonths.length - 1];
            
            let currentBudget = lastActualBudget;
            let forecastEndIndex = n;
            const maxForecastMonths = 12;
            
            let lastMonth = forecastMonths[forecastMonths.length - 1];
            const [startYear, startMonth] = lastMonth.split('-').map(Number);
            
            // Determine forecast end: if Closure exists, forecast only until Closure month
            let forecastUntilMonth = closureMonth;
            let closureBudget = null;
            
            for (let i = 0; i < maxForecastMonths; i++) {{
                let nextYear = startYear;
                let nextMonth = startMonth + i + 1;
                while (nextMonth > 12) {{
                    nextMonth -= 12;
                    nextYear += 1;
                }}
                const nextMonthStr = `${{nextYear}}-${{String(nextMonth).padStart(2, '0')}}`;
                
                // Stop if we've reached the Closure month
                if (forecastUntilMonth && nextMonthStr > forecastUntilMonth) {{
                    break;
                }}
                
                // Forecast: ONLY subtract costs, never increase budget
                // PO coverage from table is only used in actual data, not in forecast
                // Forecast can only decrease (costs), never increase
                currentBudget = currentBudget - avgMonthlyCost;
                
                // If this is the Closure month, save the budget value
                if (forecastUntilMonth && nextMonthStr === forecastUntilMonth) {{
                    closureBudget = currentBudget;
                }}
                
                forecastData.push(currentBudget);
                forecastLabels.push(nextMonthStr);
                forecastEndIndex = n + i + 1;
                
                // Stop if we've reached the Closure month exactly
                if (forecastUntilMonth && nextMonthStr === forecastUntilMonth) {{
                    // If Closure month is reached, extend forecast with closure budget for all remaining months
                    closureBudget = currentBudget;
                    // Extend forecast with closure budget for remaining forecast months
                    for (let j = i + 1; j < maxForecastMonths; j++) {{
                        let nextYear2 = startYear;
                        let nextMonth2 = startMonth + j + 1;
                        while (nextMonth2 > 12) {{
                            nextMonth2 -= 12;
                            nextYear2 += 1;
                        }}
                        const nextMonthStr2 = `${{nextYear2}}-${{String(nextMonth2).padStart(2, '0')}}`;
                        forecastData.push(closureBudget);
                        forecastLabels.push(nextMonthStr2);
                        forecastEndIndex = n + j + 1;
                    }}
                    break;
                }}
                
                // Stop if we've forecasted enough
                if (i >= maxForecastMonths - 1) break;
            }}
            
            // If Closure exists and we have closure budget, check if Closure is in actual data
            if (closureMonth && closureBudget === null) {{
                // Closure might be in actual data, calculate budget at Closure month
                const closureMonthIdx = allMonths.indexOf(closureMonth);
                if (closureMonthIdx >= 0 && closureMonthIdx < remainingBudgetData.length) {{
                    closureBudget = remainingBudgetData[closureMonthIdx];
                }}
            }}
            
            return {{
                allMonths: allMonths,
                remainingBudgetData: remainingBudgetData,
                forecastData: forecastData,
                forecastLabels: forecastLabels,
                forecastEndIndex: forecastEndIndex,
                n: n,
                lastActualMonth: allMonths[allMonths.length - 1],
                closureMonth: closureMonth,
                closureBudget: closureBudget
            }};
        }}
        
        function renderForecastChart(data) {{
            // Check if canvas element exists first
            const canvas = document.getElementById('forecastChart');
            if (!canvas) {{
                return;
            }}
            
            // Destroy existing chart first
            if (window.forecastChart) {{
                try {{
                    window.forecastChart.destroy();
                }} catch(e) {{
                    // Ignore errors
                }}
                window.forecastChart = null;
            }}
            
            // Clear canvas
            const ctx = canvas.getContext('2d');
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            
            // Determine if "All Projects" is selected
            const selectedProjectBtn = $('.quick-filter-btn[data-project].active');
            const selectedProject = selectedProjectBtn.length > 0 ? selectedProjectBtn.data('project') : 'all';
            const isAllProjects = !selectedProject || selectedProject === 'all';
            
            let allMonths, remainingBudgetData, forecastData, forecastLabels, forecastEndIndex, n;
            let projectForecasts = {{}};  // Initialize for both cases
            let forecast = null;  // Initialize for both cases
            let monthsWithCosts = new Set();  // Initialize for both cases
            let lastActualMonth = '';  // Initialize for both cases
            
            if (isAllProjects) {{
                // For "All Projects": calculate forecast for each project separately, then sum them
                const projects = [...new Set(allData.map(r => r.project).filter(p => p))];
                projectForecasts = {{}};
                
                // Initialize arrays
                remainingBudgetData = [];
                forecastData = [];
                forecastLabels = [];
                allMonths = [];
                n = 0;
                
                // Calculate forecast for each project
                projects.forEach(project => {{
                    const projectData = allData.filter(row => row.project === project);
                    const forecast = calculateProjectForecast(projectData);
                    if (forecast) {{
                        projectForecasts[project] = forecast;
                    }}
                }});
                
                // If no project forecasts, show empty chart
                if (Object.keys(projectForecasts).length === 0) {{
                    $('#forecastChartPlaceholder').addClass('show');
                    window.forecastChart = new Chart(ctx, {{
                        type: 'line',
                        data: {{ labels: [], datasets: [] }},
                        options: {{ responsive: true, maintainAspectRatio: true }}
                    }});
                    return;
                }}
                $('#forecastChartPlaceholder').removeClass('show');
                
                // Get all unique months across all projects (same logic as table)
                const allMonthsSet = new Set();
                Object.values(projectForecasts).forEach(forecast => {{
                    forecast.forecastLabels.forEach(month => allMonthsSet.add(month));
                }});
                allMonths = Array.from(allMonthsSet).sort();
                
                // Find last actual month across all projects (same logic as table)
                let lastActualMonth = '';
                Object.values(projectForecasts).forEach(forecast => {{
                    if (forecast.allMonths.length > 0) {{
                        const lastMonth = forecast.allMonths[forecast.allMonths.length - 1];
                        if (lastMonth > lastActualMonth) {{
                            lastActualMonth = lastMonth;
                        }}
                    }}
                }});
                
                // Find months that have cost events (same logic as table)
                monthsWithCosts = new Set();
                projects.forEach(project => {{
                    const projectData = allData.filter(row => row.project === project);
                    projectData.forEach(row => {{
                        const eventType = row.event_type || '';
                        const date = row.date || '';
                        
                        if (date && date.length >= 7) {{
                            const month = date.substring(0, 7);
                            if (eventType === 'Working Time' || eventType === 'Purchase' || 
                                eventType === 'T&L' || eventType === 'Deferment') {{
                                monthsWithCosts.add(month);
                            }}
                        }}
                    }});
                }});
                
                // Sum remaining budgets for all months (same logic as table)
                allMonths.forEach(month => {{
                    let sum = 0;
                    
                    Object.values(projectForecasts).forEach(forecast => {{
                        let projectBudget = null;
                        
                        // Check if this month is an actual month for this project
                        const actualMonthIdx = forecast.allMonths.indexOf(month);
                        if (actualMonthIdx >= 0) {{
                            // This is an actual month - use actual remaining budget
                            projectBudget = forecast.remainingBudgetData[actualMonthIdx];
                        }} else {{
                            // This is a forecast month
                            // Check if project has closure and if we're at or after closure month
                            if (forecast.closureMonth && month >= forecast.closureMonth) {{
                                // At or after Closure - use closure budget value
                                projectBudget = forecast.closureBudget;
                            }} else {{
                                // Before closure or no closure - use forecast data
                                const forecastIdx = forecast.forecastLabels.indexOf(month);
                                if (forecastIdx >= 0 && forecastIdx < forecast.forecastData.length) {{
                                    projectBudget = forecast.forecastData[forecastIdx];
                                }}
                            }}
                        }}
                        
                        if (projectBudget != null) {{
                            sum += projectBudget;
                        }}
                    }});
                    
                    remainingBudgetData.push(sum);
                }});
                
                // Initialize forecast arrays with all data
                forecastLabels = [...allMonths];
                forecastData = [...remainingBudgetData];
                
                // Count actual months with costs
                n = allMonths.filter(m => monthsWithCosts.has(m) && m <= lastActualMonth).length;
                
                // Get filtered date range
                const dateTo = $('#dateTo').val();
                let targetEndMonth = null;
                if (dateTo) {{
                    // Extract YYYY-MM from dateTo
                    targetEndMonth = dateTo.substring(0, 7);
                }}
                
                // Filter months based on date range if specified
                if (targetEndMonth) {{
                    forecastLabels = forecastLabels.filter(month => month <= targetEndMonth);
                    forecastData = forecastData.slice(0, forecastLabels.length);
                }}
                
                // Set forecastEndIndex to the length of forecast data
                forecastEndIndex = forecastData.length;
            }} else {{
                // For individual project: use existing logic
                // Always use allData for calculations, not filtered data
                const projectData = allData.filter(row => row.project === selectedProject);
                forecast = calculateProjectForecast(projectData);
                if (!forecast) {{
                    // No data - show empty chart
                    $('#forecastChartPlaceholder').addClass('show');
                    window.forecastChart = new Chart(ctx, {{
                        type: 'line',
                        data: {{ labels: [], datasets: [] }},
                        options: {{ responsive: true, maintainAspectRatio: true }}
                    }});
                    return;
                }}
                $('#forecastChartPlaceholder').removeClass('show');
                
                allMonths = forecast.allMonths;
                remainingBudgetData = forecast.remainingBudgetData;
                forecastData = forecast.forecastData;
                forecastLabels = forecast.forecastLabels;
                forecastEndIndex = forecast.forecastEndIndex;
                n = forecast.n;
                
                // Find months that have cost events for individual project
                monthsWithCosts = new Set();
                projectData.forEach(row => {{
                    const eventType = row.event_type || '';
                    const date = row.date || '';
                    
                    // Check if this is a cost event (not PO, Invoice, or Closure)
                    if (date && date.length >= 7) {{
                        const month = date.substring(0, 7);
                        if (eventType === 'Working Time' || eventType === 'Purchase' || 
                            eventType === 'T&L' || eventType === 'Deferment') {{
                            monthsWithCosts.add(month);
                        }}
                    }}
                }});
                
                // Find last actual month for individual project
                if (forecast.allMonths.length > 0) {{
                    lastActualMonth = forecast.allMonths[forecast.allMonths.length - 1];
                }}
                
                // If Closure exists, for individual projects: extend forecast to closure + 1 month
                if (forecast.closureMonth && forecast.closureBudget !== null) {{
                    // Find Closure month index in forecastLabels
                    const closureIdx = forecastLabels.indexOf(forecast.closureMonth);
                    if (closureIdx >= 0) {{
                        // For individual projects: extend forecast to closure + 1 month
                        const [closureYear, closureMonthNum] = forecast.closureMonth.split('-').map(Number);
                        // Add 1 month after closure
                        let nextYear = closureYear;
                        let nextMonth = closureMonthNum + 1;
                        while (nextMonth > 12) {{
                            nextMonth -= 12;
                            nextYear += 1;
                        }}
                        const nextMonthStr = `${{nextYear}}-${{String(nextMonth).padStart(2, '0')}}`;
                        
                        // Truncate to closure month, then add closure + 1 month
                        forecastData = forecastData.slice(0, closureIdx + 1);
                        forecastLabels = forecastLabels.slice(0, closureIdx + 1);
                        
                        // Add closure + 1 month with closure budget
                        forecastData.push(forecast.closureBudget);
                        forecastLabels.push(nextMonthStr);
                        forecastEndIndex = closureIdx + 2;
                    }}
                }}
            }}
            
            if (allMonths && allMonths.length >= 1 && remainingBudgetData && remainingBudgetData.length > 0) {{
                // Separate variable forecast from constant closure part
                let closureStartIdx = -1;
                let closureBudgetValue = null;
                
                // Check if there's a constant part (Closure)
                // Find the earliest closure month across all projects (for aggregated) or single project
                if (isAllProjects) {{
                    // For all projects, find earliest closure month and its budget value
                    Object.values(projectForecasts).forEach(projForecast => {{
                        if (projForecast.closureMonth) {{
                            const closureIdx = forecastLabels.indexOf(projForecast.closureMonth);
                            if (closureIdx >= 0 && (closureStartIdx === -1 || closureIdx < closureStartIdx)) {{
                                closureStartIdx = closureIdx;
                                closureBudgetValue = projForecast.closureBudget;
                            }}
                        }}
                    }});
                }} else {{
                    // For individual project - check if we already have the forecast
                    // (it was calculated above in the else branch)
                    if (forecast && forecast.closureMonth) {{
                        closureStartIdx = forecastLabels.indexOf(forecast.closureMonth);
                        closureBudgetValue = forecast.closureBudget;
                    }}
                }}
                
                // Check if forecast becomes constant (same value for multiple months)
                // This handles both Closure and naturally constant forecasts
                let constantStartIdx = -1;
                if (closureStartIdx < 0) {{
                    // No Closure, but check if forecast becomes constant naturally
                    for (let i = n; i < forecastData.length - 1; i++) {{
                        if (Math.abs(forecastData[i] - forecastData[i + 1]) < 0.01) {{
                            // Values are the same (within rounding error)
                            if (constantStartIdx === -1) {{
                                constantStartIdx = i;
                            }}
                        }} else if (constantStartIdx >= 0) {{
                            // Was constant but now changed, reset
                            constantStartIdx = -1;
                        }}
                    }}
                    if (constantStartIdx >= 0) {{
                        closureStartIdx = constantStartIdx;
                    }}
                }}
                
                // Find the last month where ANY project still has actual data
                // This determines where actual line ends and forecast line begins
                let lastMonthWithAnyActual = '';
                if (isAllProjects) {{
                    Object.values(projectForecasts).forEach(forecast => {{
                        if (forecast.allMonths.length > 0) {{
                            const lastMonth = forecast.allMonths[forecast.allMonths.length - 1];
                            if (lastMonth > lastMonthWithAnyActual) {{
                                lastMonthWithAnyActual = lastMonth;
                            }}
                        }}
                    }});
                }} else {{
                    if (forecast && forecast.allMonths.length > 0) {{
                        lastMonthWithAnyActual = forecast.allMonths[forecast.allMonths.length - 1];
                    }}
                }}
                
                // Find last actual month index (where actual line ends)
                let lastActualMonthIdx = -1;
                for (let i = forecastLabels.length - 1; i >= 0; i--) {{
                    const month = forecastLabels[i];
                    if (month <= lastMonthWithAnyActual) {{
                        lastActualMonthIdx = i;
                        break;
                    }}
                }}
                
                // Find first forecast month index (where forecast line begins)
                // This is the month after the last actual month
                let firstForecastMonthIdx = lastActualMonthIdx + 1;
                if (firstForecastMonthIdx >= forecastLabels.length) {{
                    firstForecastMonthIdx = -1;  // No forecast months
                }}
                
                // Create actual data line: includes all months up to and including last actual month
                // This line may include some projects that are already forecasting
                const actualData = forecastLabels.map((month, idx) => {{
                    if (idx <= lastActualMonthIdx) {{
                        return forecastData[idx];
                    }}
                    return null;
                }});
                
                // Create forecast data lines: split into positive (green) and negative (orange)
                // This is the purely forecasted part
                const forecastPositiveData = forecastLabels.map((month, idx) => {{
                    if (firstForecastMonthIdx >= 0 && idx >= firstForecastMonthIdx) {{
                        const value = forecastData[idx];
                        // Only include positive values (>= 0)
                        return (value !== null && value !== undefined && value >= 0) ? value : null;
                    }}
                    return null;
                }});
                
                const forecastNegativeData = forecastLabels.map((month, idx) => {{
                    if (firstForecastMonthIdx >= 0 && idx >= firstForecastMonthIdx) {{
                        const value = forecastData[idx];
                        // Only include negative values (< 0)
                        return (value !== null && value !== undefined && value < 0) ? value : null;
                    }}
                    return null;
                }});
                
                // Ensure seamless connection: include the last actual value in forecast lines
                // This ensures the lines connect without gaps
                if (lastActualMonthIdx >= 0 && firstForecastMonthIdx >= 0 && 
                    lastActualMonthIdx < forecastLabels.length - 1) {{
                    const lastActualValue = forecastData[lastActualMonthIdx];
                    if (lastActualValue !== null && lastActualValue !== undefined) {{
                        // Add the last actual value to the appropriate forecast dataset for seamless connection
                        if (lastActualValue >= 0) {{
                            forecastPositiveData[lastActualMonthIdx] = lastActualValue;
                        }} else {{
                            forecastNegativeData[lastActualMonthIdx] = lastActualValue;
                        }}
                    }}
                }}
                
                // Ensure seamless transitions when values cross zero (positive to negative or vice versa)
                // Include transition points in both datasets to prevent gaps
                for (let i = Math.max(0, firstForecastMonthIdx >= 0 ? firstForecastMonthIdx - 1 : 0); i < forecastLabels.length - 1; i++) {{
                    const currentValue = forecastData[i];
                    const nextValue = forecastData[i + 1];
                    
                    if (currentValue !== null && currentValue !== undefined && 
                        nextValue !== null && nextValue !== undefined) {{
                        // Check if sign changes between current and next value
                        const currentIsPositive = currentValue >= 0;
                        const nextIsPositive = nextValue >= 0;
                        
                        if (currentIsPositive !== nextIsPositive) {{
                            // Sign change detected - include transition point in both datasets
                            // This ensures the lines connect at the zero crossing
                            if (currentIsPositive) {{
                                // Current is positive, next is negative
                                // Include current value in negative dataset to connect to next value
                                forecastNegativeData[i] = currentValue;
                            }} else {{
                                // Current is negative, next is positive
                                // Include current value in positive dataset to connect to next value
                                forecastPositiveData[i] = currentValue;
                            }}
                        }}
                    }}
                }}
                
                // Use 0 tension for straight lines (no curves)
                const forecastTension = 0;
                
                // Create datasets array: actual line + two forecast lines (positive green, negative orange)
                const ccF = getChartColors();
                const datasets = [
                    {{
                        label: 'Actual',
                        data: actualData,
                        borderColor: ccF.po,
                        backgroundColor: ccF.po + '1a',
                        borderWidth: 3,
                        tension: 0,
                        fill: false,
                        pointRadius: 4,
                        pointHoverRadius: 6,
                        spanGaps: false
                    }},
                    {{
                        label: 'Forecast (Positive)',
                        data: forecastPositiveData,
                        borderColor: ccF.po,
                        backgroundColor: ccF.po + '1a',
                        borderWidth: 3,
                        borderDash: [5, 5],
                        tension: forecastTension,
                        fill: false,
                        pointRadius: 4,
                        pointHoverRadius: 6,
                        spanGaps: false
                    }},
                    {{
                        label: 'Forecast (Negative)',
                        data: forecastNegativeData,
                        borderColor: ccF.forecastNeg,
                        backgroundColor: ccF.forecastNeg + '1a',
                        borderWidth: 3,
                        borderDash: [5, 5],
                        tension: forecastTension,
                        fill: false,
                        pointRadius: 4,
                        pointHoverRadius: 6,
                        spanGaps: false
                    }}
                ];
                
                // Hide placeholder if we have data
                $('#forecastChartPlaceholder').removeClass('show');
                
                // Create new chart
                window.forecastChart = new Chart(ctx, {{
                    type: 'line',
                    data: {{
                        labels: forecastLabels,
                        datasets: datasets
                    }},
                    options: {{
                        responsive: true,
                        maintainAspectRatio: true,
                        interaction: {{
                            mode: 'index',
                            intersect: false
                        }},
                        plugins: {{
                            tooltip: {{
                                callbacks: {{
                                    label: function(context) {{
                                        let label = context.dataset.label || '';
                                        if (label) {{
                                            label += ': ';
                                        }}
                                        if (context.parsed.y !== null) {{
                                            label += formatEUR(context.parsed.y);
                                        }}
                                        return label;
                                    }}
                                }}
                            }},
                            legend: {{
                                display: true
                            }}
                        }},
                        scales: {{
                            y: {{
                                beginAtZero: false,
                                ticks: {{
                                    callback: function(value) {{
                                        return '€' + value.toLocaleString();
                                    }}
                                }},
                                grid: {{
                                    color: function(context) {{
                                        const c = getChartColors();
                                        if (context.tick.value === 0) {{
                                            return c.gridZero;
                                        }}
                                        return c.grid;
                                    }},
                                    lineWidth: function(context) {{
                                        if (context.tick.value === 0) {{
                                            return 3;
                                        }}
                                        return 1;
                                    }}
                                }}
                            }}
                        }}
                    }}
                }});
            }} else {{
                // No data - show empty chart
                $('#forecastChartPlaceholder').addClass('show');
                window.forecastChart = new Chart(ctx, {{
                    type: 'line',
                    data: {{
                        labels: [],
                        datasets: []
                    }},
                    options: {{
                        responsive: true,
                        maintainAspectRatio: true,
                        scales: {{
                            y: {{
                                beginAtZero: true
                            }}
                        }}
                    }}
                }});
            }}
        }}
        
        function renderMonthlySummary(data, projectFilter) {{
            const tbody = $('#monthlySummaryBody');
            tbody.empty();
            
            // Filter data by project if specified
            let filteredData = data;
            if (projectFilter && projectFilter !== 'all') {{
                filteredData = data.filter(row => row.project === projectFilter);
            }}
            
            // Calculate monthly summaries from filtered data
            const monthlySummary = {{}};
            
            filteredData.forEach(row => {{
                if (row.event_type === 'Working Time' && row.year_month) {{
                    const month = row.year_month;
                    if (!monthlySummary[month]) {{
                        monthlySummary[month] = {{
                            hours: 0,
                            cost: 0,
                            projects: new Set()
                        }};
                    }}
                    monthlySummary[month].hours += row.hours || 0;
                    if (row.calculated_cost) {{
                        monthlySummary[month].cost += row.calculated_cost;
                    }}
                    if (row.project) {{
                        monthlySummary[month].projects.add(row.project);
                    }}
                }}
            }});
            
            // Convert sets to arrays for display
            const sortedMonths = Object.keys(monthlySummary).sort();
            
            sortedMonths.forEach(month => {{
                const data = monthlySummary[month];
                const tr = $('<tr>');
                tr.append($('<td>').text(month));
                tr.append($('<td>').text(data.hours.toFixed(1)));
                tr.append($('<td>').text(formatEUR(data.cost)));
                tr.append($('<td>').text(Array.from(data.projects).join(', ')));
                tbody.append(tr);
            }});
        }}
        
        function renderProjectDetails(data) {{
            const projectStats = {{}};
            
            data.forEach(row => {{
                const project = row.project || 'Unknown';
                if (!projectStats[project]) {{
                    projectStats[project] = {{
                        poCoverage: 0,
                        invoices: 0,
                        workingTimeCosts: 0,
                        purchaseCosts: 0,
                        tlCosts: 0,
                        deferment: 0,
                        financialRecord: 0,
                        positiveFinancialRecord: 0,
                        totalHours: 0,
                        eventTypes: new Set(),
                        events: []
                    }};
                }}
                
                const eventType = row.event_type || '';
                const amount = row.amount || 0;
                
                if (eventType === 'PO') {{
                    projectStats[project].poCoverage += amount;
                }} else if (eventType === 'Invoice') {{
                    projectStats[project].invoices += amount;  // Informational only
                }} else if (eventType === 'Working Time' && row.calculated_cost) {{
                    projectStats[project].workingTimeCosts += row.calculated_cost;
                }} else if (eventType === 'Purchase') {{
                    projectStats[project].purchaseCosts += amount;
                }} else if (eventType === 'T&L') {{
                    projectStats[project].tlCosts += amount;
                }} else if (eventType === 'Deferment') {{
                    projectStats[project].deferment += amount;  // Can be positive or negative
                    // Positive deferment: add to PO coverage and count as invoiced
                    // Negative deferment: subtract from PO coverage
                    if (amount > 0) {{
                        projectStats[project].poCoverage += amount;
                        projectStats[project].invoices += amount;  // Count positive deferment as invoiced
                    }} else if (amount < 0) {{
                        projectStats[project].poCoverage += amount;  // Subtract negative deferment from PO (amount is already negative)
                    }}
                }} else if (eventType === 'Financial Record') {{
                    projectStats[project].financialRecord += amount;
                    if (amount > 0) {{
                        projectStats[project].positiveFinancialRecord += amount;
                    }} else if (amount < 0) {{
                        // Negative: decrease budget (like negative deferment)
                        projectStats[project].poCoverage += amount;
                    }}
                }}
                
                if (row.hours) projectStats[project].totalHours += row.hours;
                if (row.event_type) projectStats[project].eventTypes.add(row.event_type);
                projectStats[project].events.push(row);
            }});
            
            const detailsDiv = $('#projectDetails');
            detailsDiv.empty();
            let greenCount = 0, yellowCount = 0, redCount = 0;

            Object.keys(projectStats).sort().forEach(project => {{
                const stats = projectStats[project];
                // Total costs = Working Time + Purchase + T&L (Deferment is NOT a cost)
                const totalCosts = stats.workingTimeCosts + stats.purchaseCosts + stats.tlCosts;
                // Remaining budget = PO Coverage - Total Costs (invoices are informational only)
                const remainingBudget = stats.poCoverage - totalCosts;
                const budgetStatus = remainingBudget >= 0 ? 'positive' : 'negative';
                
                // Calculate monthly cost forecast rate (same logic as calculateProjectForecast)
                const monthlyCosts = {{}};
                stats.events.forEach(row => {{
                    const eventType = row.event_type || '';
                    const date = row.date || '';
                    const amount = row.amount || 0;
                    
                    if (date && date.length >= 7) {{
                        const month = date.substring(0, 7);
                        // Costs for forecast calculation - Deferment is NOT a cost
                        if (eventType === 'Working Time' && row.calculated_cost) {{
                            monthlyCosts[month] = (monthlyCosts[month] || 0) + row.calculated_cost;
                        }} else if ((eventType === 'Purchase' || eventType === 'T&L') && amount) {{
                            monthlyCosts[month] = (monthlyCosts[month] || 0) + amount;
                        }}
                    }}
                }});
                
                let avgMonthlyCost = 0;
                const costMonths = Object.keys(monthlyCosts).sort();
                if (costMonths.length >= 2) {{
                    const lastCostMonth = costMonths[costMonths.length - 1];
                    const secondLastCostMonth = costMonths[costMonths.length - 2];
                    const lastCost = monthlyCosts[lastCostMonth];
                    const secondLastCost = monthlyCosts[secondLastCostMonth];
                    avgMonthlyCost = (lastCost + secondLastCost) / 2;
                }} else if (costMonths.length === 1) {{
                    avgMonthlyCost = monthlyCosts[costMonths[0]];
                }}
                
                // Calculate forecast to get closure date and EAC
                const projectData = stats.events;
                const forecast = calculateProjectForecast(projectData);
                let closureDate = null;
                let eac = null;
                
                if (forecast) {{
                    // Get closure date from project data
                    projectData.forEach(row => {{
                        if (row.event_type === 'Closure' && row.date) {{
                            closureDate = row.date;
                        }}
                    }});
                    
                    // Get EAC (closure budget)
                    if (forecast.closureBudget !== null && forecast.closureBudget !== undefined) {{
                        eac = forecast.closureBudget;
                    }}
                }}
                
                // Calculate forecast status indicator
                let statusClass = 'green'; // Default to green
                
                // If project is closed, use EAC for status determination
                if (closureDate && eac !== null) {{
                    if (eac >= 0) {{
                        statusClass = 'green';
                    }} else {{
                        // Yellow if slightly below zero (within 10% of project budget)
                        const budgetThreshold = Math.abs(stats.poCoverage * 0.1);
                        if (Math.abs(eac) <= budgetThreshold) {{
                            statusClass = 'yellow';
                        }} else {{
                            // Red if significantly below zero
                            statusClass = 'red';
                        }}
                    }}
                }} else if (avgMonthlyCost > 0 && stats.poCoverage > 0) {{
                    // For open projects, calculate forecast for next month
                    let lastForecastBudget = remainingBudget - avgMonthlyCost;
                    
                    if (lastForecastBudget > 0) {{
                        statusClass = 'green';
                    }} else {{
                        // Yellow if slightly below zero (only in last month and not higher than 10% of project budget)
                        const budgetThreshold = Math.abs(stats.poCoverage * 0.1);
                        if (Math.abs(lastForecastBudget) <= budgetThreshold) {{
                            statusClass = 'yellow';
                        }} else {{
                            // Red if significantly below zero
                            statusClass = 'red';
                        }}
                    }}
                }} else if (remainingBudget > 0) {{
                    statusClass = 'green';
                }} else if (remainingBudget < 0) {{
                    // Red if current budget is negative (but not zero)
                    statusClass = 'red';
                }}
                
                if (statusClass === 'green') greenCount++;
                else if (statusClass === 'yellow') yellowCount++;
                else if (statusClass === 'red') redCount++;

                // Create tooltip text based on status
                let tooltipText = '';
                if (statusClass === 'green') {{
                    tooltipText = 'Forecasted budget is positive';
                }} else if (statusClass === 'yellow') {{
                    tooltipText = 'Forecasted budget is slightly negative (within 10% of project budget)';
                }} else if (statusClass === 'red') {{
                    tooltipText = 'Forecasted budget is significantly negative (beyond 10% threshold)';
                }}
                
                // Format EUR values
                const poCoverageFormatted = formatEUR(stats.poCoverage);
                const totalCostsFormatted = formatEUR(totalCosts);
                const invoicesFormatted = formatEUR(stats.invoices);
                // Coverage gap = (Invoiced + Positive Financial Record) - Total Costs
                // Negative = missing coverage, Positive = overcovered
                const coverageGap = (stats.invoices + stats.positiveFinancialRecord) - totalCosts;

                // Determine label and display value
                let missingInvoiceLabel = 'Missing Coverage/Overcovered';
                let missingInvoiceDisplay = '';
                let missingInvoiceColor = '';

                if (Math.abs(coverageGap) < 0.01) {{
                    // Zero or very close to zero - show checkmark
                    missingInvoiceLabel = 'Balanced';
                    missingInvoiceDisplay = '✓';
                    missingInvoiceColor = 'var(--color-positive)';
                }} else if (coverageGap < 0) {{
                    // Negative - missing coverage
                    missingInvoiceLabel = 'Missing Coverage';
                    missingInvoiceDisplay = formatEUR(coverageGap);
                    missingInvoiceColor = 'var(--color-negative)';
                }} else {{
                    // Positive - overcovered
                    missingInvoiceLabel = 'Overcovered';
                    missingInvoiceDisplay = formatEUR(coverageGap);
                    missingInvoiceColor = '';
                }}
                
                const missingInvoiceStyle = missingInvoiceColor ? `style="color: ${{missingInvoiceColor}}"` : '';
                const remainingBudgetFormatted = formatEUR(remainingBudget);
                const workingTimeCostsFormatted = formatEUR(stats.workingTimeCosts);
                const purchaseCostsFormatted = formatEUR(stats.purchaseCosts);
                const tlCostsFormatted = formatEUR(stats.tlCosts);
                const defermentFormatted = formatEUR(stats.deferment || 0);
                const financialRecordFormatted = formatEUR(stats.financialRecord || 0);
                const forecastRateFormatted = formatEUR(avgMonthlyCost);
                
                // Format closure date (already retrieved above)
                let closureDateFormatted = '-';
                    if (closureDate) {{
                        // Format closure date
                        if (closureDate.length > 10) {{
                            closureDateFormatted = closureDate.split(' ')[0];
                        }} else {{
                            closureDateFormatted = closureDate;
                        }}
                    }}
                    
                // Format EAC (already retrieved above)
                let eacFormatted = '-';
                if (eac !== null) {{
                    eacFormatted = formatEUR(eac);
                }}
                
                // Determine EAC color (red if negative)
                const eacColor = (forecast && forecast.closureBudget !== null && forecast.closureBudget !== undefined && forecast.closureBudget < 0) ? 'var(--color-negative)' : '';
                const eacStyle = eacColor ? `style="color: ${{eacColor}}"` : '';
                
                // Cost/Invoiced per project
                let costInvoicedFormatted = '-';
                if (totalCosts > 0 && stats.invoices > 0) {{
                    costInvoicedFormatted = (stats.invoices / totalCosts * 100).toFixed(1) + '%';
                }} else if (stats.invoices > 0) {{
                    costInvoicedFormatted = '∞';
                }} else if (totalCosts === 0) {{
                    costInvoicedFormatted = '-';
                }}

                // Coverage = Cost / (Invoiced + Positive Financial Record)
                const coverageDenom = stats.invoices + stats.positiveFinancialRecord;
                let coverageFormatted = '-';
                if (coverageDenom > 0 && totalCosts > 0) {{
                    coverageFormatted = (totalCosts / coverageDenom * 100).toFixed(1) + '%';
                }} else if (totalCosts === 0 && coverageDenom >= 0) {{
                    coverageFormatted = '0%';
                }}

                const statusIndicator = `<div class="project-status-indicator ${{statusClass}}" data-tooltip="${{tooltipText}}"></div>`;

                const card = $(`
                    <div class="project-card status-${{statusClass}}">
                        ${{statusIndicator}}
                        <h3>${{project}}</h3>
                        <div class="project-stats">
                            <div class="project-stat cost-highlight">
                                <div class="project-stat-label">Budget</div>
                                <div class="project-stat-value">${{poCoverageFormatted}}</div>
                            </div>
                            <div class="project-stat cost-highlight">
                                <div class="project-stat-label">Total Costs</div>
                                <div class="project-stat-value">${{totalCostsFormatted}}</div>
                            </div>
                            <div class="project-stat cost-highlight">
                                <div class="project-stat-label">EAC</div>
                                <div class="project-stat-value" ${{eacStyle}}>${{eacFormatted}}</div>
                            </div>
                            <div class="project-stat cost-highlight">
                                <div class="project-stat-label">Cost/Invoiced</div>
                                <div class="project-stat-value">${{costInvoicedFormatted}}</div>
                            </div>
                            <div class="project-stat cost-highlight">
                                <div class="project-stat-label">Coverage</div>
                                <div class="project-stat-value">${{coverageFormatted}}</div>
                            </div>
                            <div class="project-stat">
                                <div class="project-stat-label">Invoices</div>
                                <div class="project-stat-value">${{invoicesFormatted}}</div>
                            </div>
                            <div class="project-stat">
                                <div class="project-stat-label">${{missingInvoiceLabel}}</div>
                                <div class="project-stat-value" ${{missingInvoiceStyle}}>${{missingInvoiceDisplay}}</div>
                            </div>
                            <div class="project-stat">
                                <div class="project-stat-label">Remaining Budget</div>
                                <div class="project-stat-value" style="color: ${{budgetStatus === 'positive' ? 'var(--color-positive)' : 'var(--color-negative)'}}">${{remainingBudgetFormatted}}</div>
                            </div>
                            <div class="project-stat">
                                <div class="project-stat-label">Working Time Costs</div>
                                <div class="project-stat-value">${{workingTimeCostsFormatted}}</div>
                            </div>
                            <div class="project-stat">
                                <div class="project-stat-label">Purchase Costs</div>
                                <div class="project-stat-value">${{purchaseCostsFormatted}}</div>
                            </div>
                            <div class="project-stat">
                                <div class="project-stat-label">T&L Costs</div>
                                <div class="project-stat-value">${{tlCostsFormatted}}</div>
                            </div>
                            <div class="project-stat">
                                <div class="project-stat-label">Deferment</div>
                                <div class="project-stat-value" style="color: ${{(stats.deferment || 0) >= 0 ? 'var(--color-negative)' : 'var(--color-positive)'}}">${{defermentFormatted}}</div>
                            </div>
                            <div class="project-stat">
                                <div class="project-stat-label">Financial Record</div>
                                <div class="project-stat-value" style="color: ${{(stats.financialRecord || 0) > 0 ? 'var(--color-info)' : (stats.financialRecord || 0) < 0 ? 'var(--color-negative)' : 'inherit'}}">${{financialRecordFormatted}}</div>
                            </div>
                            <div class="project-stat">
                                <div class="project-stat-label">Total Hours</div>
                                <div class="project-stat-value">${{stats.totalHours.toFixed(1)}}</div>
                            </div>
                            <div class="project-stat">
                                <div class="project-stat-label">Burndown Rate</div>
                                <div class="project-stat-value">${{forecastRateFormatted}}</div>
                            </div>
                            <div class="project-stat">
                                <div class="project-stat-label">Closure Date</div>
                                <div class="project-stat-value">${{closureDateFormatted}}</div>
                            </div>
                        </div>
                    </div>
                `);
                detailsDiv.append(card);
            }});

            $('#greenProjectCount').text(greenCount);
            $('#yellowProjectCount').text(yellowCount);
            $('#redProjectCount').text(redCount);
            $('#greenProjectItem').toggle(greenCount > 0);
            $('#yellowProjectItem').toggle(yellowCount > 0);
            $('#redProjectItem').toggle(redCount > 0);
        }}

        function exportToCSV() {{
            const headers = ['#', 'Date', 'Event Type', 'Project', 'Sheet', 'Hourly Rate', 'Additional Rate', 'Hours', 'Amount', 'Calculated Cost', 'Comment'];
            const rows = filteredData.map(row => {{
                const displayAmount = (row.event_type === 'Working Time' && row.calculated_cost)
                    ? row.calculated_cost
                    : (row.amount || '');
                return [
                    row.index || '',
                    row.date || '',
                    row.event_type || '',
                    row.project || '',
                    row.sheet || '',
                    formatEUR(row.hourly_rate).replace('€', '') || '',
                    (() => {{
                        if (row.additional_rate !== null && row.additional_rate !== undefined) {{
                            const percentage = row.additional_rate * 100;
                            return percentage >= 100 ? Math.round(percentage) + '%' : percentage.toFixed(2) + '%';
                        }}
                        return '';
                    }})(),
                    row.hours || '',
                    formatEUR(displayAmount).replace('€', '') || '',
                    (row.event_type === 'Working Time' && row.calculated_cost) ? formatEUR(row.calculated_cost).replace('€', '') : '',
                    (row.comment || '').replace(/"/g, '""')
                ];
            }});
            
            const csvContent = [
                headers.join(','),
                ...rows.map(row => row.map(cell => `"${{cell}}"`).join(','))
            ].join('\\n');
            
            const blob = new Blob([csvContent], {{ type: 'text/csv' }});
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'project_data_' + new Date().toISOString().split('T')[0] + '.csv';
            a.click();
            window.URL.revokeObjectURL(url);
        }}
    </script>
</body>
</html>
"""
