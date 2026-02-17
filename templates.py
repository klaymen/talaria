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
            <h1>Talaria - Project Tracking Dashboard</h1>
            <span class="header-info">Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</span>
        </header>
        
        <div class="help-icon" id="helpIcon">?</div>
        
        <div class="help-modal" id="helpModal">
            <div class="help-content">
                <button class="close-btn" id="closeHelp">&times;</button>
                <h2>Dashboard Guide</h2>

                <h3>Data Source</h3>
                <p>The dashboard reads <strong>all sheets/tabs</strong> from the input Excel file. Records from every sheet are merged into a single dataset. Each record tracks which sheet it originated from.</p>

                <h3>Event Types</h3>
                <ul>
                    <li><strong>PO (Purchase Order):</strong> Adds to the project budget (PO Coverage).</li>
                    <li><strong>Working Time:</strong> A cost. Calculated as hours &times; hourly rate &times; (1 + additional rate). The calculated cost is shown instead of the Amount field.</li>
                    <li><strong>Purchase:</strong> A direct cost (e.g. software licenses, hardware).</li>
                    <li><strong>T&amp;L:</strong> Travel &amp; Logistics costs.</li>
                    <li><strong>Invoice:</strong> Invoiced amounts. Informational only &mdash; not a cost, not added to PO coverage. Used for the Missing Invoice / Overinvoiced calculation.</li>
                    <li><strong>Deferment:</strong> Positive deferment adds to PO coverage and counts as invoiced. Negative deferment reduces PO coverage. Not included in costs.</li>
                    <li><strong>Financial Record:</strong> Positive amounts count as invoiced (marking amounts that will be invoiced later, so they don&rsquo;t appear as uninvoiced). Negative amounts reduce PO coverage (decreasing the budget). Not included in costs.</li>
                    <li><strong>Closure:</strong> Marks the project end date. The budget forecast extends to the closure month.</li>
                </ul>

                <h3>Summary Cards</h3>
                <p><strong>Cost/Invoiced:</strong> Ratio of total invoices to total costs, expressed as a percentage.</p>
                <p><strong>Total Projects:</strong> Number of unique projects in the dataset.</p>
                <p><strong>PO Coverage:</strong> Total Purchase Order coverage across all projects (includes positive Deferment and is reduced by negative Deferment and negative Financial Records).</p>
                <p><strong>Total Costs:</strong> Sum of Working Time + Purchases + T&amp;L. Deferment and Financial Record are not costs.</p>
                <p><strong>Total Invoices:</strong> Total invoiced amounts (includes Invoice events, positive Deferment, and positive Financial Records).</p>
                <p><strong>Missing Invoice/Overinvoiced:</strong> Total Invoices minus Total Costs. Negative (red) = missing invoices; positive = overinvoiced.</p>
                <p><strong>Remaining Budget:</strong> PO Coverage minus Total Costs.</p>

                <h3>Charts</h3>
                <p><strong>Amount by Project:</strong> Shows PO Coverage, Costs, Invoices, Deferment, and Remaining Budget grouped by project.</p>
                <p><strong>Timeline:</strong> Monthly costs and cumulative remaining budget over time.</p>
                <p><strong>Monthly Working Time Summary:</strong> Aggregated hours and costs by month.</p>
                <p><strong>Budget Forecast:</strong> Projects future budget trends based on average monthly costs from the last 2 months. Green = positive forecast, orange = negative.</p>

                <h3>Data Table</h3>
                <p>The data table shows all records with the following features:</p>
                <ul>
                    <li><strong>Pagination:</strong> Choose page size (25, 50, 100, 250, or All rows) to control how many records are displayed at once.</li>
                    <li><strong>Sheet Filter:</strong> Filter the table to show records from a specific Excel sheet/tab.</li>
                    <li><strong>Search:</strong> Full-text search across all fields.</li>
                    <li><strong>Comments:</strong> Records with comments show a blue dot (&bull;) next to the amount. Hover over the row to see the full comment. Comments come from both a dedicated Comment column and cell-level Excel comments (sticky notes).</li>
                    <li><strong>Export:</strong> Export filtered data to CSV (includes Sheet and Comment columns).</li>
                </ul>

                <h3>Project Details</h3>
                <p>Each project card shows detailed financial information including:</p>
                <ul>
                    <li><strong>PO Coverage:</strong> Total Purchase Order coverage for the project</li>
                    <li><strong>Total Costs:</strong> Sum of all cost types (Working Time + Purchase + T&amp;L)</li>
                    <li><strong>Closure Date:</strong> Project end date (from Closure events)</li>
                    <li><strong>EAC (Estimated At Completion):</strong> Forecasted remaining budget at closure</li>
                    <li><strong>Invoices:</strong> Total invoiced amounts</li>
                    <li><strong>Missing Invoice/Overinvoiced:</strong> Total Invoices minus Total Costs</li>
                    <li><strong>Remaining Budget:</strong> Current budget status (green if positive, red if negative)</li>
                    <li><strong>Working Time / Purchase / T&amp;L Costs:</strong> Breakdown by cost type</li>
                    <li><strong>Deferment:</strong> Positive adds to PO coverage and counts as invoiced. Negative reduces PO coverage. Not a cost.</li>
                    <li><strong>Financial Record:</strong> Positive counts as invoiced. Negative reduces PO coverage. Not a cost.</li>
                    <li><strong>Monthly Cost Forecast Rate:</strong> Average monthly cost used for budget forecasting</li>
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
                <h3>Total Projects</h3>
                <div class="summary-value" id="totalProjects">{len(projects)}</div>
            </div>
            <div class="summary-card">
                <h3>PO Coverage</h3>
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
                <h3 id="missingInvoiceLabel">Missing Invoice/Overinvoiced</h3>
                <div class="summary-value" id="missingInvoice">€{total_invoices - total_costs:,.2f}</div>
            </div>
            <div class="summary-card">
                <h3>Remaining Budget</h3>
                <div class="summary-value" id="remainingBudget">€{total_po_coverage - total_costs:,.2f}</div>
            </div>
            <div class="summary-card">
                <h3>Total Hours</h3>
                <div class="summary-value" id="totalHours">{total_hours:,.2f}</div>
            </div>
        </div>

        <!-- Filters -->
        <div class="filters-section">
            <h2>Filters</h2>
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

        <!-- Charts Section -->
        <div class="charts-section">
            <div class="chart-container">
                <h2>Amount by Project</h2>
                <div class="chart-filters" id="projectAmountChartFilters" style="display: none;">
                    <div class="chart-filter-buttons">
                        <button type="button" class="chart-filter-btn" id="projectAmountChartSelectAll">All</button>
                        <button type="button" class="chart-filter-btn" id="projectAmountChartSelectNone">None</button>
                    </div>
                    <div class="chart-filter-checkboxes">
                        <label><input type="checkbox" class="chart-filter-checkbox" data-dataset="0" checked> PO Coverage</label>
                        <label><input type="checkbox" class="chart-filter-checkbox" data-dataset="1" checked> Costs</label>
                        <label><input type="checkbox" class="chart-filter-checkbox" data-dataset="2" checked> Invoices</label>
                        <label><input type="checkbox" class="chart-filter-checkbox" data-dataset="3" checked> Deferment</label>
                        <label><input type="checkbox" class="chart-filter-checkbox" data-dataset="4" checked> Remaining Budget</label>
                    </div>
                </div>
                <canvas id="projectAmountChart"></canvas>
                <div class="chart-placeholder" id="projectAmountChartPlaceholder">No data available for this chart</div>
            </div>
            <div class="chart-container">
                <h2>Hours by Project</h2>
                <canvas id="projectHoursChart"></canvas>
                <div class="chart-placeholder" id="projectHoursChartPlaceholder">No data available for this chart</div>
            </div>
            <div class="chart-container">
                <h2>Timeline</h2>
                <canvas id="timelineChart"></canvas>
                <div class="chart-placeholder" id="timelineChartPlaceholder">No data available for this chart</div>
            </div>
            <div class="chart-container">
                <h2>Budget Forecast</h2>
                <canvas id="forecastChart"></canvas>
                <div class="chart-placeholder" id="forecastChartPlaceholder">No data available for this chart</div>
            </div>
        </div>

        <!-- Data Table -->
        <div class="table-section">
            <h2>Data Table <span id="tableRecordCount" style="font-size: 0.7em; color: #888; font-weight: normal;"></span></h2>
            <div class="table-controls">
                <input type="text" id="searchInput" placeholder="Search..." />
                <select id="tableSheetFilter" style="padding: 10px; border: 1px solid #ddd; border-radius: 5px; font-size: 0.95em;">
                    <option value="all">All Sheets</option>
                </select>
                <select id="tablePageSize" style="padding: 10px; border: 1px solid #ddd; border-radius: 5px; font-size: 0.95em;">
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
                            <th>#</th>
                            <th>Date</th>
                            <th>Event Type</th>
                            <th>Project</th>
                            <th>Sheet</th>
                            <th>Hourly Rate</th>
                            <th>Additional Rate</th>
                            <th>Hours</th>
                            <th>Amount/Cost</th>
                        </tr>
                    </thead>
                    <tbody id="tableBody">
                    </tbody>
                </table>
            </div>
            <div class="table-pagination" id="tablePagination">
                <button class="btn-secondary btn-sm" id="prevPage" disabled>&laquo; Previous</button>
                <span id="pageInfo" style="padding: 6px 12px; color: #555;"></span>
                <button class="btn-secondary btn-sm" id="nextPage">&raquo; Next</button>
            </div>
        </div>

        <!-- Monthly Working Time Summary -->
        <div class="table-section">
            <h2>Monthly Working Time Summary</h2>
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

        <!-- Project Details -->
        <div class="project-details-section">
            <h2>Project Details</h2>
            <div id="projectDetails"></div>
        </div>
        
    </div>

    <script>
        // Embedded data
        const allData = {data_json};
        const projectFinancials = {financials_json};
        const monthlyWorkingTime = {monthly_summary_json};
        let filteredData = [...allData];
        
        // Initialize dashboard
        $(document).ready(function() {{
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

            // Table search — also respects sheet filter
            function applyTableFilters() {{
                const searchTerm = $('#searchInput').val().toLowerCase();
                const sheetFilter = $('#tableSheetFilter').val();
                let tableData = filteredData;
                if (sheetFilter !== 'all') {{
                    tableData = tableData.filter(row => row.sheet === sheetFilter);
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
                        // Positive: count as invoiced (will be invoiced later)
                        invoices += amount;
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
            // Missing Invoice = Total Invoices - Total Costs
            // Negative = missing invoices (not enough invoiced), Positive = overinvoiced
            const missingInvoice = invoices - totalCosts;
            
            // Calculate Invoiced/Cost ratio as percentage
            let invoicedCostRatio = '-';
            if (totalCosts > 0) {{
                const ratio = (invoices / totalCosts) * 100;
                invoicedCostRatio = ratio.toFixed(1) + '%';
            }} else if (invoices > 0) {{
                invoicedCostRatio = '∞';
            }}
            
            $('#costInvoicedRatio').text(invoicedCostRatio);
            $('#totalProjects').text(projects.length);
            $('#totalPOCoverage').text(formatEUR(poCoverage));
            $('#totalCosts').text(formatEUR(totalCosts));
            $('#totalInvoices').text(formatEUR(invoices));
            // Update Missing Invoice/Overinvoiced display
            const missingInvoiceElement = $('#missingInvoice');
            const missingInvoiceLabelElement = $('#missingInvoiceLabel');
            
            if (Math.abs(missingInvoice) < 0.01) {{
                // Zero or very close to zero - show checkmark
                missingInvoiceLabelElement.text('Balanced');
                missingInvoiceElement.text('✓');
                missingInvoiceElement.css('color', '#28a745'); // Green checkmark
            }} else if (missingInvoice < 0) {{
                // Negative - missing invoices
                missingInvoiceLabelElement.text('Missing Invoice');
                missingInvoiceElement.text(formatEUR(missingInvoice));
                missingInvoiceElement.css('color', '#dc3545'); // Red
            }} else {{
                // Positive - overinvoiced
                missingInvoiceLabelElement.text('Overinvoiced');
                missingInvoiceElement.text(formatEUR(missingInvoice));
                missingInvoiceElement.css('color', ''); // Default color
            }}
            $('#remainingBudget').text(formatEUR(remainingBudget));
            $('#totalHours').text(totalHours.toLocaleString('en-US', {{minimumFractionDigits: 2, maximumFractionDigits: 2}}));
        }}
        
        // Table pagination state
        let currentTableData = [];
        let currentPage = 1;

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
                const hasComment = row.comment && row.comment.length > 0;
                const tr = $('<tr>');
                if (hasComment) tr.addClass('has-comment');

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
                tr.append($('<td>').text(row.hours ? row.hours.toFixed(2) : ''));
                const displayAmount = (row.event_type === 'Working Time' && row.calculated_cost)
                    ? row.calculated_cost
                    : (row.amount || 0);

                // Last cell: amount + comment tooltip
                const amountTd = $('<td>').addClass('comment-cell');
                amountTd.append($('<span>').text(formatEUR(displayAmount)));
                if (hasComment) {{
                    amountTd.append($('<span>').addClass('comment-indicator').attr('title', row.comment));
                    amountTd.append($('<div>').addClass('comment-tooltip').text(row.comment));
                }}
                tr.append(amountTd);
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

        function renderTable(data) {{
            // Sort by date (ascending)
            currentTableData = [...data].sort((a, b) => {{
                const dateA = a.date || '';
                const dateB = b.date || '';
                return dateA.localeCompare(dateB);
            }});
            currentPage = 1;
            renderTablePage();
        }}
        
        function renderCharts(data) {{
            // Financials by Project
            const projectPOCoverage = {{}};
            const projectCosts = {{}};
            const projectInvoices = {{}};
            const projectDeferment = {{}};
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

                // Financial Record: positive counts as invoiced, negative reduces PO coverage
                if (eventType === 'Financial Record' && amount) {{
                    if (amount > 0) {{
                        projectInvoices[project] = (projectInvoices[project] || 0) + amount;
                    }} else if (amount < 0) {{
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
            
            // Destroy existing charts
            if (window.projectFinancialChart && typeof window.projectFinancialChart.destroy === 'function') {{
                window.projectFinancialChart.destroy();
            }}
            if (window.projectHoursChart && typeof window.projectHoursChart.destroy === 'function') {{
                window.projectHoursChart.destroy();
            }}
            if (window.timelineChart && typeof window.timelineChart.destroy === 'function') {{
                window.timelineChart.destroy();
            }}
            if (window.forecastChart && typeof window.forecastChart.destroy === 'function') {{
                window.forecastChart.destroy();
            }}
            
            // Financials by Project Chart (PO Coverage, Costs, Invoices, Deferment)
            const allProjects = [...new Set([...Object.keys(projectPOCoverage), ...Object.keys(projectCosts), ...Object.keys(projectInvoices), ...Object.keys(projectDeferment)])];
            
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
                window.projectFinancialChart = new Chart(ctx1, {{
                type: 'bar',
                data: {{
                    labels: allProjects,
                    datasets: [
                        {{
                            label: 'PO Coverage (€)',
                            data: allProjects.map(p => projectPOCoverage[p] || 0),
                            backgroundColor: 'rgba(40, 167, 69, 0.6)',
                            borderColor: 'rgba(40, 167, 69, 1)',
                            borderWidth: 1,
                            hidden: !checkboxStates[0]
                        }},
                        {{
                            label: 'Costs (€)',
                            data: allProjects.map(p => projectCosts[p] || 0),
                            backgroundColor: 'rgba(220, 53, 69, 0.6)',
                            borderColor: 'rgba(220, 53, 69, 1)',
                            borderWidth: 1,
                            hidden: !checkboxStates[1]
                        }},
                        {{
                            label: 'Invoices (€)',
                            data: allProjects.map(p => projectInvoices[p] || 0),
                            backgroundColor: 'rgba(102, 126, 234, 0.6)',
                            borderColor: 'rgba(102, 126, 234, 1)',
                            borderWidth: 1,
                            hidden: !checkboxStates[2]
                        }},
                        {{
                            label: 'Deferment (€)',
                            data: allProjects.map(p => projectDeferment[p] || 0),
                            backgroundColor: 'rgba(128, 128, 128, 0.6)',
                            borderColor: 'rgba(128, 128, 128, 1)',
                            borderWidth: 1,
                            hidden: !checkboxStates[3]
                        }},
                        {{
                            label: 'Remaining Budget (€)',
                            data: allProjects.map(p => (projectPOCoverage[p] || 0) - (projectCosts[p] || 0)),
                            backgroundColor: 'rgba(255, 193, 7, 0.6)',
                            borderColor: 'rgba(255, 193, 7, 1)',
                            borderWidth: 1,
                            hidden: !checkboxStates[4]
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
                                    // Make zero line thick and black
                                    if (context.tick.value === 0) {{
                                        return 'rgba(0, 0, 0, 1)';
                                    }}
                                    return 'rgba(0, 0, 0, 0.1)';
                                }},
                                lineWidth: function(context) {{
                                    // Make zero line thicker
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
            const hoursProjects = Object.keys(projectHours);
            
            // Show/hide placeholder
            if (hoursProjects.length === 0) {{
                $('#projectHoursChartPlaceholder').addClass('show');
            }} else {{
                $('#projectHoursChartPlaceholder').removeClass('show');
            }}
            
            if (hoursProjects.length > 0) {{
                const ctx2 = document.getElementById('projectHoursChart').getContext('2d');
                window.projectHoursChart = new Chart(ctx2, {{
                    type: 'bar',
                    data: {{
                        labels: hoursProjects,
                        datasets: [{{
                            label: 'Hours',
                            data: hoursProjects.map(p => projectHours[p]),
                            backgroundColor: 'rgba(118, 75, 162, 0.6)',
                            borderColor: 'rgba(118, 75, 162, 1)',
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
                window.timelineChart = new Chart(ctx4, {{
                    type: 'line',
                    data: {{
                        labels: allMonths,
                        datasets: [
                            {{
                                label: 'Monthly Costs (€)',
                                data: monthlyCostsData,
                                borderColor: 'rgba(220, 53, 69, 1)',
                                backgroundColor: 'rgba(220, 53, 69, 0.1)',
                                tension: 0,
                                fill: false,
                                yAxisID: 'y'
                            }},
                            {{
                                label: 'Remaining Budget (€)',
                                data: cumulativeRemainingBudget,
                                borderColor: 'rgba(40, 167, 69, 1)',
                                backgroundColor: 'rgba(40, 167, 69, 0.1)',
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
                                        // Make zero line thick and black
                                        if (context.tick.value === 0) {{
                                            return 'rgba(0, 0, 0, 1)';
                                        }}
                                        return 'rgba(0, 0, 0, 0.1)';
                                    }},
                                    lineWidth: function(context) {{
                                        // Make zero line thicker
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
                const datasets = [
                    {{
                        label: 'Actual',
                        data: actualData,
                        borderColor: 'rgba(40, 167, 69, 1)',  // Green
                        backgroundColor: 'rgba(40, 167, 69, 0.1)',
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
                        borderColor: 'rgba(40, 167, 69, 1)',  // Green
                        backgroundColor: 'rgba(40, 167, 69, 0.1)',
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
                        borderColor: 'rgba(255, 152, 0, 1)',  // Orange
                        backgroundColor: 'rgba(255, 152, 0, 0.1)',
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
                                        // Make zero line thick and black
                                        if (context.tick.value === 0) {{
                                            return 'rgba(0, 0, 0, 1)';
                                        }}
                                        return 'rgba(0, 0, 0, 0.1)';
                                    }},
                                    lineWidth: function(context) {{
                                        // Make zero line thicker
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
                tr.append($('<td>').text(data.hours.toFixed(2)));
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
                        // Positive: count as invoiced (will be invoiced later)
                        projectStats[project].invoices += amount;
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
                // Missing Invoice = Total Invoices - Total Costs
                // Negative = missing invoices (not enough invoiced), Positive = overinvoiced, Zero = balanced
                const missingInvoice = stats.invoices - totalCosts;
                
                // Determine label and display value
                let missingInvoiceLabel = 'Missing Invoice/Overinvoiced';
                let missingInvoiceDisplay = '';
                let missingInvoiceColor = '';
                
                if (Math.abs(missingInvoice) < 0.01) {{
                    // Zero or very close to zero - show checkmark
                    missingInvoiceLabel = 'Balanced';
                    missingInvoiceDisplay = '✓';
                    missingInvoiceColor = '#28a745'; // Green checkmark
                }} else if (missingInvoice < 0) {{
                    // Negative - missing invoices
                    missingInvoiceLabel = 'Missing Invoice';
                    missingInvoiceDisplay = formatEUR(missingInvoice);
                    missingInvoiceColor = '#dc3545'; // Red
                }} else {{
                    // Positive - overinvoiced
                    missingInvoiceLabel = 'Overinvoiced';
                    missingInvoiceDisplay = formatEUR(missingInvoice);
                    missingInvoiceColor = ''; // Default color
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
                const eacColor = (forecast && forecast.closureBudget !== null && forecast.closureBudget !== undefined && forecast.closureBudget < 0) ? '#dc3545' : '';
                const eacStyle = eacColor ? `style="color: ${{eacColor}}"` : '';
                
                const statusIndicator = `<div class="project-status-indicator ${{statusClass}}" data-tooltip="${{tooltipText}}"></div>`;
                
                const card = $(`
                    <div class="project-card">
                        ${{statusIndicator}}
                        <h3>${{project}}</h3>
                        <div class="project-stats">
                            <div class="project-stat">
                                <div class="project-stat-label">PO Coverage</div>
                                <div class="project-stat-value">${{poCoverageFormatted}}</div>
                            </div>
                            <div class="project-stat">
                                <div class="project-stat-label">Total Costs</div>
                                <div class="project-stat-value">${{totalCostsFormatted}}</div>
                            </div>
                            <div class="project-stat">
                                <div class="project-stat-label">Closure Date</div>
                                <div class="project-stat-value">${{closureDateFormatted}}</div>
                            </div>
                            <div class="project-stat">
                                <div class="project-stat-label">EAC</div>
                                <div class="project-stat-value" ${{eacStyle}}>${{eacFormatted}}</div>
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
                                <div class="project-stat-value" style="color: ${{budgetStatus === 'positive' ? '#28a745' : '#dc3545'}}">${{remainingBudgetFormatted}}</div>
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
                                <div class="project-stat-value" style="color: ${{(stats.deferment || 0) >= 0 ? '#dc3545' : '#28a745'}}">${{defermentFormatted}}</div>
                            </div>
                            <div class="project-stat">
                                <div class="project-stat-label">Financial Record</div>
                                <div class="project-stat-value" style="color: ${{(stats.financialRecord || 0) > 0 ? '#007bff' : (stats.financialRecord || 0) < 0 ? '#dc3545' : 'inherit'}}">${{financialRecordFormatted}}</div>
                            </div>
                            <div class="project-stat">
                                <div class="project-stat-label">Total Hours</div>
                                <div class="project-stat-value">${{stats.totalHours.toFixed(2)}}</div>
                            </div>
                            <div class="project-stat">
                                <div class="project-stat-label">Monthly Cost Forecast Rate</div>
                                <div class="project-stat-value">${{forecastRateFormatted}}</div>
                            </div>
                        </div>
                    </div>
                `);
                detailsDiv.append(card);
            }});
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
