#!/usr/bin/env python3
"""
Financial calculations and statistics for the dashboard generator.
"""

import json


def calculate_statistics(records):
    """Calculate statistics from records."""
    projects = list(set(r['project'] for r in records if r['project']))
    event_types = list(set(r['event_type'] for r in records if r['event_type']))
    
    return {
        'projects': projects,
        'event_types': event_types
    }


def calculate_project_financials(records):
    """Calculate financials per project."""
    project_financials = {}
    
    for record in records:
        project = record['project'] or 'Unknown'
        if project not in project_financials:
            project_financials[project] = {
                'po_coverage': 0.0,  # Total PO amounts (budget)
                'invoices': 0.0,     # Total invoice amounts (informational only, not a cost)
                'working_time_costs': 0.0,  # Calculated costs from Working Time
                'purchase_costs': 0.0,  # Purchase amounts
                'tl_costs': 0.0,      # T&L amounts
                'deferment': 0.0,     # Deferment amounts (can be positive or negative)
                'total_hours': 0.0,
                'total_amount': 0.0
            }
        
        event_type = record['event_type']
        amount = record['amount'] or 0.0
        
        if event_type == 'PO':
            project_financials[project]['po_coverage'] += amount
        elif event_type == 'Invoice':
            project_financials[project]['invoices'] += amount
        elif event_type == 'Working Time':
            if record.get('calculated_cost'):
                project_financials[project]['working_time_costs'] += record['calculated_cost']
            project_financials[project]['total_hours'] += record['hours'] or 0.0
        elif event_type == 'Purchase':
            project_financials[project]['purchase_costs'] += amount
        elif event_type == 'T&L':
            project_financials[project]['tl_costs'] += amount
        elif event_type == 'Deferment':
            project_financials[project]['deferment'] += amount
        
        project_financials[project]['total_amount'] += amount
    
    return project_financials


def calculate_totals(project_financials, records):
    """Calculate total financials."""
    total_po_coverage = sum(pf['po_coverage'] for pf in project_financials.values())
    total_invoices = sum(pf['invoices'] for pf in project_financials.values())  # Informational only
    total_working_time_costs = sum(pf['working_time_costs'] for pf in project_financials.values())
    total_purchase_costs = sum(pf['purchase_costs'] for pf in project_financials.values())
    total_tl_costs = sum(pf['tl_costs'] for pf in project_financials.values())
    total_deferment = sum(pf['deferment'] for pf in project_financials.values())
    # Total costs = Working Time + Purchase + T&L + Deferment (Deferment can be positive or negative)
    total_costs = total_working_time_costs + total_purchase_costs + total_tl_costs + total_deferment
    total_hours = sum(r['hours'] for r in records)
    
    return {
        'total_po_coverage': total_po_coverage,
        'total_invoices': total_invoices,
        'total_working_time_costs': total_working_time_costs,
        'total_purchase_costs': total_purchase_costs,
        'total_tl_costs': total_tl_costs,
        'total_deferment': total_deferment,
        'total_costs': total_costs,
        'total_hours': total_hours
    }


def calculate_date_range(records):
    """Calculate date range from records."""
    dates = [r['date'] for r in records if r['date']]
    date_from = min(dates) if dates else ''
    date_to = max(dates) if dates else ''
    
    return {
        'date_from': date_from,
        'date_to': date_to
    }


def calculate_monthly_working_time(records):
    """Calculate monthly summaries for Working Time."""
    monthly_working_time = {}
    
    for record in records:
        if record['event_type'] == 'Working Time' and record.get('calculated_cost') and record.get('year_month'):
            month = record['year_month']
            if month not in monthly_working_time:
                monthly_working_time[month] = {
                    'hours': 0.0,
                    'cost': 0.0,
                    'projects': set()
                }
            monthly_working_time[month]['hours'] += record['hours'] or 0.0
            monthly_working_time[month]['cost'] += record['calculated_cost']
            if record['project']:
                monthly_working_time[month]['projects'].add(record['project'])
    
    # Convert sets to lists for JSON serialization
    for month in monthly_working_time:
        monthly_working_time[month]['projects'] = list(monthly_working_time[month]['projects'])
    
    return monthly_working_time


def prepare_json_data(records, project_financials, monthly_working_time):
    """Prepare data for JavaScript as JSON strings."""
    data_json = json.dumps(records, indent=2)
    financials_json = json.dumps(project_financials, indent=2)
    monthly_summary_json = json.dumps(monthly_working_time, indent=2)
    
    return {
        'data_json': data_json,
        'financials_json': financials_json,
        'monthly_summary_json': monthly_summary_json
    }
