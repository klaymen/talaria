#!/usr/bin/env python3
"""
Calculations and data preparation for the dashboard generator.
"""

import json


def calculate_statistics(records):
    """Calculate statistics from records."""
    event_types = list(set(r['event_type'] for r in records if r['event_type']))

    return {
        'event_types': event_types
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


def prepare_json_data(records):
    """Prepare record data for JavaScript as a JSON string."""
    return json.dumps(records, indent=2)
