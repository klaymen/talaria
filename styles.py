#!/usr/bin/env python3
"""
CSS styles for the dashboard generator.
"""


def get_css():
    """Return CSS styles as a string."""
    return """        :root {
        /* Primary palette */
        --color-primary: #3b5998;
        --color-primary-hover: #2d4373;
        --color-primary-subtle: rgba(59, 89, 152, 0.07);

        /* Gradient */
        --gradient-header: linear-gradient(135deg, #2c3e6b 0%, #3b5998 100%);

        /* Surfaces */
        --color-bg: #f4f5f7;
        --color-surface: #ffffff;
        --color-surface-alt: #f8f9fa;
        --color-surface-hover: #eef0f3;

        /* Text */
        --color-text: #1e2328;
        --color-text-secondary: #5a6270;
        --color-text-muted: #848a96;

        /* Borders */
        --color-border: #d4d8df;
        --color-border-light: #e6e9ed;

        /* Semantic */
        --color-positive: #2e7d52;
        --color-negative: #c0392b;
        --color-warning: #b8860b;
        --color-info: #2b6cb0;

        /* Shadows */
        --shadow-sm: 0 1px 3px rgba(0,0,0,0.05), 0 1px 2px rgba(0,0,0,0.03);
        --shadow-md: 0 4px 12px rgba(0,0,0,0.07);

        /* Chart grid */
        --chart-grid: rgba(0, 0, 0, 0.06);
        --chart-grid-zero: rgba(0, 0, 0, 0.6);
        --chart-text: #5a6270;

        /* Chart dataset colors */
        --chart-po: #2e7d52;
        --chart-costs: #c0392b;
        --chart-invoices: #3b5998;
        --chart-deferment: #6b7280;
        --chart-budget: #8b6914;
        --chart-hours: #5b4a9e;
        --chart-forecast-neg: #c75b2a;
        }

        [data-theme="dark"] {
        --color-primary: #7a9ec9;
        --color-primary-hover: #95b3d8;
        --color-primary-subtle: rgba(122, 158, 201, 0.12);

        --gradient-header: linear-gradient(135deg, #263858 0%, #3b5998 100%);

        --color-bg: #12141a;
        --color-surface: #1b1e26;
        --color-surface-alt: #232730;
        --color-surface-hover: #2c303b;

        --color-text: #d9dbe0;
        --color-text-secondary: #969baa;
        --color-text-muted: #666d7e;

        --color-border: #2e323e;
        --color-border-light: #262a34;

        --color-positive: #4caf6e;
        --color-negative: #e07265;
        --color-warning: #d4a94c;
        --color-info: #6a9fd8;

        --shadow-sm: 0 1px 3px rgba(0,0,0,0.3), 0 1px 2px rgba(0,0,0,0.2);
        --shadow-md: 0 4px 12px rgba(0,0,0,0.4);

        --chart-grid: rgba(255, 255, 255, 0.07);
        --chart-grid-zero: rgba(255, 255, 255, 0.45);
        --chart-text: #969baa;

        --chart-po: #4caf6e;
        --chart-costs: #e07265;
        --chart-invoices: #7a9ec9;
        --chart-deferment: #8b9099;
        --chart-budget: #d4a94c;
        --chart-hours: #9484c4;
        --chart-forecast-neg: #d48050;
        }

        * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        }

        body {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
        background: var(--color-bg);
        color: var(--color-text);
        line-height: 1.6;
        transition: background 0.3s, color 0.3s;
        }

        .container {
        max-width: 1400px;
        margin: 0 auto;
        padding: 20px;
        }

        header {
        background: var(--gradient-header);
        color: white;
        padding: 15px 30px;
        border-radius: 10px;
        margin-bottom: 30px;
        box-shadow: var(--shadow-md);
        display: flex;
        justify-content: space-between;
        align-items: center;
        }

        header h1 {
        font-size: 1.8em;
        margin: 0;
        }

        header .header-info {
        font-size: 0.9em;
        opacity: 0.9;
        }

        /* Toolbar strip – fixed right edge */
        .toolbar-strip {
        position: fixed;
        top: 18px;
        right: 0;
        display: flex;
        flex-direction: column;
        align-items: center;
        background: var(--color-primary);
        border-radius: 8px 0 0 8px;
        box-shadow: -2px 2px 10px rgba(0,0,0,0.18);
        z-index: 1000;
        padding: 6px 4px;
        gap: 2px;
        }

        .toolbar-btn {
        width: 34px;
        height: 34px;
        background: transparent;
        color: white;
        border: none;
        border-radius: 6px;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        font-size: 18px;
        font-weight: bold;
        transition: background 0.2s;
        }

        .toolbar-btn:hover {
        background: rgba(255,255,255,0.2);
        }

        .toolbar-divider {
        width: 22px;
        height: 1px;
        background: rgba(255,255,255,0.35);
        margin: 2px 0;
        }

        .help-modal {
        display: none;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0,0,0,0.5);
        z-index: 2000;
        align-items: center;
        justify-content: center;
        }

        .help-modal.active {
        display: flex;
        }

        .help-content {
        background: var(--color-surface);
        color: var(--color-text);
        padding: 30px 40px;
        border-radius: 10px;
        max-width: 600px;
        max-height: 80vh;
        overflow-y: auto;
        box-shadow: 0 4px 20px rgba(0,0,0,0.3);
        position: relative;
        line-height: 1.6;
        }

        .help-content h2 {
        margin-top: 0;
        margin-bottom: 20px;
        color: var(--color-primary);
        }

        .help-content h3 {
        margin-top: 25px;
        margin-bottom: 12px;
        color: var(--color-primary);
        font-size: 1.1em;
        }

        .help-content p {
        margin-bottom: 12px;
        }

        .help-content ul {
        margin-top: 8px;
        margin-bottom: 15px;
        padding-left: 25px;
        }

        .help-content li {
        margin-bottom: 8px;
        }

        .help-content .close-btn {
        position: absolute;
        top: 15px;
        right: 15px;
        background: var(--color-negative);
        color: white;
        border: none;
        border-radius: 50%;
        width: 30px;
        height: 30px;
        cursor: pointer;
        font-size: 18px;
        display: flex;
        align-items: center;
        justify-content: center;
        }

        .help-content .close-btn:hover {
        opacity: 0.85;
        }

        .project-status-indicator {
        position: absolute;
        top: 15px;
        right: 15px;
        width: 20px;
        height: 20px;
        border-radius: 4px;
        box-shadow: var(--shadow-sm);
        cursor: help;
        }

        .project-status-indicator.green {
        background: var(--color-positive);
        }

        .project-status-indicator.yellow {
        background: var(--color-warning);
        }

        .project-status-indicator.red {
        background: var(--color-negative);
        }

        .project-status-indicator::after {
        content: attr(data-tooltip);
        position: absolute;
        top: -40px;
        right: 0;
        background: var(--color-text);
        color: var(--color-bg);
        padding: 8px 12px;
        border-radius: 4px;
        font-size: 12px;
        white-space: nowrap;
        opacity: 0;
        pointer-events: none;
        transition: opacity 0.3s;
        z-index: 1000;
        box-shadow: var(--shadow-md);
        }

        .project-status-indicator::before {
        content: '';
        position: absolute;
        top: -8px;
        right: 10px;
        border: 5px solid transparent;
        border-top-color: var(--color-text);
        opacity: 0;
        pointer-events: none;
        transition: opacity 0.3s;
        z-index: 1001;
        }

        .project-status-indicator:hover::after,
        .project-status-indicator:hover::before {
        opacity: 1;
        }

        .summary-section {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 20px;
        margin-bottom: 30px;
        }

        .summary-card {
        background: var(--color-surface);
        padding: 25px;
        border-radius: 10px;
        box-shadow: var(--shadow-sm);
        text-align: center;
        }

        .summary-card h3 {
        color: var(--color-text-muted);
        font-size: 0.9em;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 10px;
        }

        .summary-value {
        font-size: 2em;
        font-weight: bold;
        color: var(--color-primary);
        }

        .project-status-counts {
        display: flex;
        justify-content: center;
        gap: 16px;
        }

        .status-count {
        font-size: 2em;
        font-weight: bold;
        }

        .status-count.green {
        color: var(--color-positive);
        }

        .status-count.yellow {
        color: var(--color-warning);
        }

        .status-count.red {
        color: var(--color-negative);
        }

        .filters-section {
        background: var(--color-surface);
        padding: 14px 18px;
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: var(--shadow-sm);
        }

        .filters {
        display: flex;
        flex-wrap: wrap;
        gap: 12px;
        align-items: end;
        }

        .filter-group {
        display: flex;
        flex-direction: column;
        gap: 3px;
        }

        .filter-group label {
        font-weight: 600;
        color: var(--color-text-secondary);
        font-size: 0.8em;
        }

        .filter-group select,
        .filter-group input {
        padding: 5px 10px;
        border: 1px solid var(--color-border);
        border-radius: 4px;
        font-size: 0.85em;
        background: var(--color-surface);
        color: var(--color-text);
        }

        .filter-group select {
        min-width: 160px;
        height: 32px;
        }

        .btn-secondary {
        padding: 6px 14px;
        background: #6c757d;
        color: white;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        font-size: 0.85em;
        }

        .btn-secondary:hover {
        background: #5a6268;
        }

        .quick-filters {
        margin-top: 10px;
        padding-top: 10px;
        border-top: 1px solid var(--color-border-light);
        }

        .quick-filters h3 {
        display: none;
        }

        .quick-filter-group {
        margin-bottom: 6px;
        display: flex;
        align-items: center;
        gap: 8px;
        flex-wrap: wrap;
        }

        .quick-filter-group label {
        font-weight: 600;
        color: var(--color-text-secondary);
        font-size: 0.8em;
        margin: 0;
        white-space: nowrap;
        min-width: 70px;
        }

        .quick-filter-buttons {
        display: flex;
        flex-wrap: wrap;
        gap: 5px;
        }

        .quick-filter-btn {
        padding: 4px 10px;
        background: var(--color-surface-alt);
        color: var(--color-text-secondary);
        border: 1px solid var(--color-border);
        border-radius: 4px;
        font-size: 0.8em;
        cursor: pointer;
        transition: all 0.2s;
        }

        .quick-filter-btn:hover {
        background: var(--color-surface-hover);
        border-color: var(--color-text-muted);
        }

        .quick-filter-btn.active {
        background: var(--color-primary);
        color: white;
        border-color: var(--color-primary);
        }

        .charts-section {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(500px, 1fr));
        gap: 20px;
        margin-bottom: 30px;
        }

        @media (max-width: 1200px) {
        .charts-section {
        grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
        }
        }

        .chart-container {
        background: var(--color-surface);
        padding: 25px;
        border-radius: 10px;
        box-shadow: var(--shadow-sm);
        position: relative;
        overflow: hidden;
        width: 100%;
        box-sizing: border-box;
        }

        .chart-container h3 {
        margin-bottom: 20px;
        color: var(--color-text);
        font-size: 1.3em;
        }

        .chart-filters {
        margin-bottom: 15px;
        padding: 10px;
        background: var(--color-surface-alt);
        border-radius: 5px;
        }

        .chart-filter-buttons {
        display: flex;
        gap: 10px;
        margin-bottom: 10px;
        padding-bottom: 10px;
        border-bottom: 1px solid var(--color-border);
        }

        .chart-filter-btn {
        padding: 5px 12px;
        background: var(--color-primary);
        color: white;
        border: none;
        border-radius: 4px;
        font-size: 0.85em;
        cursor: pointer;
        transition: background 0.2s;
        }

        .chart-filter-btn:hover {
        background: var(--color-primary-hover);
        }

        .chart-filter-checkboxes {
        display: flex;
        flex-wrap: wrap;
        gap: 15px;
        }

        .chart-filter-checkboxes label {
        display: flex;
        align-items: center;
        gap: 5px;
        font-size: 0.9em;
        color: var(--color-text-secondary);
        cursor: pointer;
        }

        .chart-filter-checkboxes input[type="checkbox"] {
        cursor: pointer;
        }

        .chart-container canvas {
        max-width: 100%;
        height: auto !important;
        }
        .chart-placeholder {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        text-align: center;
        color: var(--color-text-muted);
        font-size: 16px;
        padding: 20px;
        background: var(--color-surface);
        border-radius: 5px;
        display: none;
        z-index: 10;
        }
        .chart-placeholder.show {
        display: block;
        }

        .table-section {
        background: var(--color-surface);
        padding: 25px;
        border-radius: 10px;
        margin-bottom: 30px;
        box-shadow: var(--shadow-sm);
        }

        .table-controls {
        display: flex;
        gap: 10px;
        margin-bottom: 15px;
        }

        .table-controls input {
        flex: 1;
        padding: 10px;
        border: 1px solid var(--color-border);
        border-radius: 5px;
        font-size: 0.95em;
        background: var(--color-surface);
        color: var(--color-text);
        }

        .table-controls select {
        background: var(--color-surface);
        color: var(--color-text);
        border: 1px solid var(--color-border);
        }

        .btn-primary {
        padding: 10px 20px;
        background: var(--color-primary);
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 0.95em;
        }

        .btn-primary:hover {
        background: var(--color-primary-hover);
        }

        .table-wrapper {
        overflow-x: auto;
        }

        table {
        width: 100%;
        border-collapse: collapse;
        }

        th {
        background: var(--color-surface-alt);
        padding: 12px;
        text-align: left;
        font-weight: 600;
        color: var(--color-text-secondary);
        border-bottom: 2px solid var(--color-border);
        }

        th.sortable {
        cursor: pointer;
        user-select: none;
        white-space: nowrap;
        }

        th.sortable:hover {
        background: var(--color-surface-hover);
        color: var(--color-text);
        }

        .sort-indicator {
        font-size: 0.75em;
        color: var(--color-primary);
        }

        td {
        padding: 12px;
        border-bottom: 1px solid var(--color-border-light);
        }

        tr:hover {
        background: var(--color-primary-subtle);
        }

        td.comment-cell {
        max-width: 250px;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        color: var(--color-text-secondary);
        font-size: 0.9em;
        }

        td.comment-cell:hover {
        white-space: normal;
        overflow: visible;
        word-break: break-word;
        }

        .table-pagination {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 8px;
        margin-top: 15px;
        padding-top: 15px;
        border-top: 1px solid var(--color-border-light);
        }

        .btn-sm {
        padding: 6px 14px;
        font-size: 0.85em;
        }

        .project-details-section {
        background: var(--color-surface);
        padding: 25px;
        border-radius: 10px;
        box-shadow: var(--shadow-sm);
        }

        .project-card {
        position: relative;
        margin-bottom: 20px;
        padding: 20px;
        background: var(--color-surface-alt);
        border-radius: 8px;
        border-left: 4px solid var(--color-primary);
        border-right: 4px solid var(--color-primary);
        }

        .project-card.status-green {
        border-left-color: var(--color-positive);
        border-right-color: var(--color-positive);
        }

        .project-card.status-yellow {
        border-left-color: var(--color-warning);
        border-right-color: var(--color-warning);
        }

        .project-card.status-red {
        border-left-color: var(--color-negative);
        border-right-color: var(--color-negative);
        }

        .project-card h3 {
        color: var(--color-primary);
        margin-bottom: 15px;
        }

        .project-stats {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
        gap: 15px;
        margin-top: 15px;
        }

        .project-stat {
        text-align: center;
        }

        .project-stat-label {
        font-size: 0.85em;
        color: var(--color-text-muted);
        margin-bottom: 5px;
        }

        .project-stat-value {
        font-size: 1.3em;
        font-weight: bold;
        color: var(--color-text);
        }

        .project-stat.cost-highlight {
        background: var(--color-primary-subtle);
        border-radius: 8px;
        padding: 8px 4px;
        }

        /* Collapsible sections */
        .collapsible-section {
        margin-bottom: 30px;
        }

        .collapsible-section > summary {
        cursor: pointer;
        list-style: none;
        user-select: none;
        }

        .collapsible-section > summary::-webkit-details-marker {
        display: none;
        }

        .collapsible-section > summary h2 {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        color: var(--color-text);
        padding: 10px 0;
        }

        .collapsible-section > summary h2::before {
        content: '\\25BC';
        font-size: 0.6em;
        transition: transform 0.2s;
        color: var(--color-text-muted);
        }

        .collapsible-section:not([open]) > summary h2::before {
        transform: rotate(-90deg);
        }

        .collapsible-section > .filters-section,
        .collapsible-section > .table-section,
        .collapsible-section > .project-details-section {
        margin-bottom: 0;
        }

        @media (max-width: 768px) {
        .charts-section {
        grid-template-columns: 1fr;
        }

        .filters {
        flex-direction: column;
        }

        .quick-filter-group {
        flex-direction: column;
        align-items: flex-start;
        }

        .chart-container {
        padding: 15px;
        min-height: 350px;
        }
        }
"""
