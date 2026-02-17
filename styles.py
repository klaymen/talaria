#!/usr/bin/env python3
"""
CSS styles for the dashboard generator.
"""


def get_css():
    """Return CSS styles as a string."""
    return """        :root {
        /* Primary palette */
        --color-primary: #4f6bed;
        --color-primary-hover: #3d56c6;
        --color-primary-subtle: rgba(79, 107, 237, 0.08);

        /* Gradient */
        --gradient-header: linear-gradient(135deg, #4f6bed 0%, #6941c6 100%);

        /* Surfaces */
        --color-bg: #f0f2f5;
        --color-surface: #ffffff;
        --color-surface-alt: #f5f6f8;
        --color-surface-hover: #ebedf0;

        /* Text */
        --color-text: #1a1d23;
        --color-text-secondary: #5f6571;
        --color-text-muted: #8b8f9a;

        /* Borders */
        --color-border: #d8dbe0;
        --color-border-light: #e8eaef;

        /* Semantic */
        --color-positive: #16a34a;
        --color-negative: #dc2626;
        --color-warning: #d97706;
        --color-info: #2563eb;

        /* Shadows */
        --shadow-sm: 0 1px 3px rgba(0,0,0,0.06), 0 1px 2px rgba(0,0,0,0.04);
        --shadow-md: 0 4px 12px rgba(0,0,0,0.08);

        /* Chart grid */
        --chart-grid: rgba(0, 0, 0, 0.08);
        --chart-grid-zero: rgba(0, 0, 0, 0.7);
        --chart-text: #5f6571;

        /* Chart dataset colors */
        --chart-po: #16a34a;
        --chart-costs: #dc2626;
        --chart-invoices: #4f6bed;
        --chart-deferment: #71717a;
        --chart-budget: #ca8a04;
        --chart-hours: #7c3aed;
        --chart-forecast-neg: #ea580c;
        }

        [data-theme="dark"] {
        --color-primary: #6d8cff;
        --color-primary-hover: #8aa2ff;
        --color-primary-subtle: rgba(109, 140, 255, 0.12);

        --gradient-header: linear-gradient(135deg, #4f6bed 0%, #6941c6 100%);

        --color-bg: #111318;
        --color-surface: #1a1d24;
        --color-surface-alt: #22252e;
        --color-surface-hover: #2a2e38;

        --color-text: #e4e5e9;
        --color-text-secondary: #9ca0ab;
        --color-text-muted: #6b7080;

        --color-border: #2e323c;
        --color-border-light: #252830;

        --color-positive: #22c55e;
        --color-negative: #f87171;
        --color-warning: #fbbf24;
        --color-info: #60a5fa;

        --shadow-sm: 0 1px 3px rgba(0,0,0,0.3), 0 1px 2px rgba(0,0,0,0.2);
        --shadow-md: 0 4px 12px rgba(0,0,0,0.4);

        --chart-grid: rgba(255, 255, 255, 0.08);
        --chart-grid-zero: rgba(255, 255, 255, 0.5);
        --chart-text: #9ca0ab;

        --chart-po: #22c55e;
        --chart-costs: #f87171;
        --chart-invoices: #6d8cff;
        --chart-deferment: #a1a1aa;
        --chart-budget: #facc15;
        --chart-hours: #a78bfa;
        --chart-forecast-neg: #fb923c;
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

        /* Theme toggle */
        .theme-toggle {
        position: fixed;
        top: 20px;
        right: 62px;
        width: 35px;
        height: 35px;
        background: var(--color-primary);
        color: white;
        border: none;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        font-size: 18px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.2);
        z-index: 1000;
        transition: background 0.3s;
        }

        .theme-toggle:hover {
        background: var(--color-primary-hover);
        }

        .help-icon {
        position: fixed;
        top: 20px;
        right: 20px;
        width: 35px;
        height: 35px;
        background: var(--color-primary);
        color: white;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        font-size: 20px;
        font-weight: bold;
        box-shadow: 0 2px 8px rgba(0,0,0,0.2);
        z-index: 1000;
        transition: background 0.3s;
        }

        .help-icon:hover {
        background: var(--color-primary-hover);
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

        .filters-section {
        background: var(--color-surface);
        padding: 25px;
        border-radius: 10px;
        margin-bottom: 30px;
        box-shadow: var(--shadow-sm);
        }

        .filters-section h2 {
        margin-bottom: 20px;
        color: var(--color-text);
        }

        .filters {
        display: flex;
        flex-wrap: wrap;
        gap: 20px;
        align-items: end;
        }

        .filter-group {
        display: flex;
        flex-direction: column;
        gap: 5px;
        }

        .filter-group label {
        font-weight: 600;
        color: var(--color-text-secondary);
        font-size: 0.9em;
        }

        .filter-group select,
        .filter-group input {
        padding: 8px 12px;
        border: 1px solid var(--color-border);
        border-radius: 5px;
        font-size: 0.95em;
        background: var(--color-surface);
        color: var(--color-text);
        }

        .filter-group select {
        min-width: 200px;
        height: 38px;
        }

        .btn-secondary {
        padding: 10px 20px;
        background: #6c757d;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 0.95em;
        }

        .btn-secondary:hover {
        background: #5a6268;
        }

        .quick-filters {
        margin-top: 25px;
        padding-top: 25px;
        border-top: 2px solid var(--color-border-light);
        }

        .quick-filters h3 {
        margin-bottom: 15px;
        color: var(--color-text);
        font-size: 1.1em;
        }

        .quick-filter-group {
        margin-bottom: 20px;
        }

        .quick-filter-group label {
        display: block;
        font-weight: 600;
        color: var(--color-text-secondary);
        font-size: 0.9em;
        margin-bottom: 10px;
        }

        .quick-filter-buttons {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        }

        .quick-filter-btn {
        padding: 8px 16px;
        background: var(--color-surface-alt);
        color: var(--color-text-secondary);
        border: 1px solid var(--color-border);
        border-radius: 5px;
        font-size: 0.9em;
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

        .chart-container h2 {
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

        .table-section h2 {
        margin-bottom: 20px;
        color: var(--color-text);
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

        .project-details-section h2 {
        margin-bottom: 20px;
        color: var(--color-text);
        }

        .project-card {
        position: relative;
        margin-bottom: 20px;
        padding: 20px;
        background: var(--color-surface-alt);
        border-radius: 8px;
        border-left: 4px solid var(--color-primary);
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

        @media (max-width: 768px) {
        .charts-section {
        grid-template-columns: 1fr;
        }

        .filters {
        flex-direction: column;
        }

        .chart-container {
        padding: 15px;
        min-height: 350px;
        }
        }
"""
