#!/usr/bin/env python3
"""Tests for calculations.py"""

import json
import pytest
from calculations import calculate_statistics, calculate_date_range, prepare_json_data


def _make_record(**overrides):
    """Create a minimal record with sensible defaults."""
    record = {
        'index': 1,
        'date': '2026-01-15',
        'event_type': 'Working Time',
        'project': 'TestProject',
        'billing_rate': 50.0,
        'surcharge_rate': 0.05,
        'hours': 10.0,
        'amount': 0.0,
        'billable_amount': 525.0,
        'comment': '',
        'sheet': 'Sheet1',
        'year_month': '2026-01'
    }
    record.update(overrides)
    return record


# ── calculate_statistics ──────────────────────────────────────────────────

class TestCalculateStatistics:
    def test_extracts_event_types(self):
        records = [
            _make_record(event_type='Working Time'),
            _make_record(event_type='PO'),
            _make_record(event_type='Working Time'),
            _make_record(event_type='Invoice'),
        ]
        stats = calculate_statistics(records)
        assert sorted(stats['event_types']) == ['Invoice', 'PO', 'Working Time']

    def test_skips_empty_event_types(self):
        records = [
            _make_record(event_type='PO'),
            _make_record(event_type=''),
        ]
        stats = calculate_statistics(records)
        assert stats['event_types'] == ['PO']

    def test_empty_records(self):
        stats = calculate_statistics([])
        assert stats['event_types'] == []


# ── calculate_date_range ──────────────────────────────────────────────────

class TestCalculateDateRange:
    def test_basic_range(self):
        records = [
            _make_record(date='2026-03-01'),
            _make_record(date='2026-01-15'),
            _make_record(date='2026-02-20'),
        ]
        dr = calculate_date_range(records)
        assert dr['date_from'] == '2026-01-15'
        assert dr['date_to'] == '2026-03-01'

    def test_single_date(self):
        records = [_make_record(date='2026-06-15')]
        dr = calculate_date_range(records)
        assert dr['date_from'] == '2026-06-15'
        assert dr['date_to'] == '2026-06-15'

    def test_skips_empty_dates(self):
        records = [
            _make_record(date=''),
            _make_record(date='2026-05-01'),
            _make_record(date=''),
        ]
        dr = calculate_date_range(records)
        assert dr['date_from'] == '2026-05-01'
        assert dr['date_to'] == '2026-05-01'

    def test_all_empty_dates(self):
        records = [_make_record(date=''), _make_record(date='')]
        dr = calculate_date_range(records)
        assert dr['date_from'] == ''
        assert dr['date_to'] == ''

    def test_empty_records(self):
        dr = calculate_date_range([])
        assert dr['date_from'] == ''
        assert dr['date_to'] == ''


# ── prepare_json_data ─────────────────────────────────────────────────────

class TestPrepareJsonData:
    def test_returns_valid_json(self):
        records = [_make_record(), _make_record(project='Other')]
        result = prepare_json_data(records)
        parsed = json.loads(result)
        assert isinstance(parsed, list)
        assert len(parsed) == 2

    def test_preserves_fields(self):
        records = [_make_record(project='Alpha', hours=42.5)]
        parsed = json.loads(prepare_json_data(records))
        assert parsed[0]['project'] == 'Alpha'
        assert parsed[0]['hours'] == 42.5

    def test_empty_records(self):
        parsed = json.loads(prepare_json_data([]))
        assert parsed == []
