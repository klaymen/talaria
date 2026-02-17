#!/usr/bin/env python3
"""
CSS styles for the dashboard generator.
"""


def get_css():
    """Return CSS styles as a string."""
    return """        * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        }

        body {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
        background: #f5f7fa;
        color: #333;
        line-height: 1.6;
        }

        .container {
        max-width: 1400px;
        margin: 0 auto;
        padding: 20px;
        }

        header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 15px 30px;
        border-radius: 10px;
        margin-bottom: 30px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
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

        .help-icon {
        position: fixed;
        top: 20px;
        right: 20px;
        width: 35px;
        height: 35px;
        background: #667eea;
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
        background: #5568d3;
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
        background: white;
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
        color: #667eea;
        }

        .help-content h3 {
        margin-top: 25px;
        margin-bottom: 12px;
        color: #667eea;
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
        background: #dc3545;
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
        background: #c82333;
        }

        .project-status-indicator {
        position: absolute;
        top: 15px;
        right: 15px;
        width: 20px;
        height: 20px;
        border-radius: 4px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
        cursor: help;
        }

        .project-status-indicator.green {
        background: #28a745;
        }

        .project-status-indicator.yellow {
        background: #ffc107;
        }

        .project-status-indicator.red {
        background: #dc3545;
        }

        .project-status-indicator::after {
        content: attr(data-tooltip);
        position: absolute;
        top: -40px;
        right: 0;
        background: #333;
        color: white;
        padding: 8px 12px;
        border-radius: 4px;
        font-size: 12px;
        white-space: nowrap;
        opacity: 0;
        pointer-events: none;
        transition: opacity 0.3s;
        z-index: 1000;
        box-shadow: 0 2px 8px rgba(0,0,0,0.2);
        }

        .project-status-indicator::before {
        content: '';
        position: absolute;
        top: -8px;
        right: 10px;
        border: 5px solid transparent;
        border-top-color: #333;
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
        background: white;
        padding: 25px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        text-align: center;
        }

        .summary-card h3 {
        color: #666;
        font-size: 0.9em;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 10px;
        }

        .summary-value {
        font-size: 2em;
        font-weight: bold;
        color: #667eea;
        }

        .filters-section {
        background: white;
        padding: 25px;
        border-radius: 10px;
        margin-bottom: 30px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }

        .filters-section h2 {
        margin-bottom: 20px;
        color: #333;
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
        color: #555;
        font-size: 0.9em;
        }

        .filter-group select,
        .filter-group input {
        padding: 8px 12px;
        border: 1px solid #ddd;
        border-radius: 5px;
        font-size: 0.95em;
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
        border-top: 2px solid #e0e0e0;
        }

        .quick-filters h3 {
        margin-bottom: 15px;
        color: #333;
        font-size: 1.1em;
        }

        .quick-filter-group {
        margin-bottom: 20px;
        }

        .quick-filter-group label {
        display: block;
        font-weight: 600;
        color: #555;
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
        background: #f8f9fa;
        color: #495057;
        border: 1px solid #dee2e6;
        border-radius: 5px;
        font-size: 0.9em;
        cursor: pointer;
        transition: all 0.2s;
        }

        .quick-filter-btn:hover {
        background: #e9ecef;
        border-color: #adb5bd;
        }

        .quick-filter-btn.active {
        background: #007bff;
        color: white;
        border-color: #007bff;
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
        background: white;
        padding: 25px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        position: relative;
        overflow: hidden;
        width: 100%;
        box-sizing: border-box;
        }

        .chart-container h2 {
        margin-bottom: 20px;
        color: #333;
        font-size: 1.3em;
        }
        
        .chart-filters {
        margin-bottom: 15px;
        padding: 10px;
        background: #f8f9fa;
        border-radius: 5px;
        }
        
        .chart-filter-buttons {
        display: flex;
        gap: 10px;
        margin-bottom: 10px;
        padding-bottom: 10px;
        border-bottom: 1px solid #dee2e6;
        }
        
        .chart-filter-btn {
        padding: 5px 12px;
        background: #667eea;
        color: white;
        border: none;
        border-radius: 4px;
        font-size: 0.85em;
        cursor: pointer;
        transition: background 0.2s;
        }
        
        .chart-filter-btn:hover {
        background: #5568d3;
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
        color: #555;
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
        color: #999;
        font-size: 16px;
        padding: 20px;
        background: rgba(255, 255, 255, 0.9);
        border-radius: 5px;
        display: none;
        z-index: 10;
        }
        .chart-placeholder.show {
        display: block;
        }

        .table-section {
        background: white;
        padding: 25px;
        border-radius: 10px;
        margin-bottom: 30px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }

        .table-section h2 {
        margin-bottom: 20px;
        color: #333;
        }

        .table-controls {
        display: flex;
        gap: 10px;
        margin-bottom: 15px;
        }

        .table-controls input {
        flex: 1;
        padding: 10px;
        border: 1px solid #ddd;
        border-radius: 5px;
        font-size: 0.95em;
        }

        .btn-primary {
        padding: 10px 20px;
        background: #667eea;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 0.95em;
        }

        .btn-primary:hover {
        background: #5568d3;
        }

        .table-wrapper {
        overflow-x: auto;
        }

        table {
        width: 100%;
        border-collapse: collapse;
        }

        th {
        background: #f8f9fa;
        padding: 12px;
        text-align: left;
        font-weight: 600;
        color: #555;
        border-bottom: 2px solid #dee2e6;
        }

        th.sortable {
        cursor: pointer;
        user-select: none;
        white-space: nowrap;
        }

        th.sortable:hover {
        background: #e9ecef;
        color: #333;
        }

        .sort-indicator {
        font-size: 0.75em;
        color: #667eea;
        }

        td {
        padding: 12px;
        border-bottom: 1px solid #dee2e6;
        }

        tr:hover {
        background: #f8f9fa;
        }

        td.comment-cell {
        max-width: 250px;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        color: #555;
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
        border-top: 1px solid #dee2e6;
        }

        .btn-sm {
        padding: 6px 14px;
        font-size: 0.85em;
        }

        .project-details-section {
        background: white;
        padding: 25px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }

        .project-details-section h2 {
        margin-bottom: 20px;
        color: #333;
        }

        .project-card {
        position: relative;
        margin-bottom: 20px;
        padding: 20px;
        background: #f8f9fa;
        border-radius: 8px;
        border-left: 4px solid #667eea;
        }

        .project-card h3 {
        color: #667eea;
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
        color: #666;
        margin-bottom: 5px;
        }

        .project-stat-value {
        font-size: 1.3em;
        font-weight: bold;
        color: #333;
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
