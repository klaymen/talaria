#!/usr/bin/env python3
"""Integration tests using test_input.xlsx"""

import os
import json
import pytest
from pathlib import Path

from parsers import read_excel_data
from calculations import calculate_statistics, calculate_date_range, prepare_json_data
from generate_dashboard import generate_html


TEST_FILE = Path(__file__).parent / 'test_input.xlsx'

pytestmark = pytest.mark.skipif(
    not TEST_FILE.exists(),
    reason='test_input.xlsx not found'
)


@pytest.fixture(scope='module')
def records():
    return read_excel_data(str(TEST_FILE))


# ── Excel parsing ─────────────────────────────────────────────────────────

class TestReadExcelData:
    def test_returns_list(self, records):
        assert isinstance(records, list)
        assert len(records) > 0

    def test_record_has_required_fields(self, records):
        required = {
            'index', 'date', 'event_type', 'project', 'billing_rate',
            'surcharge_rate', 'hours', 'amount', 'billable_amount',
            'comment', 'sheet', 'year_month'
        }
        for record in records:
            assert required.issubset(record.keys()), \
                f"Missing fields: {required - record.keys()}"

    def test_indexes_are_sequential(self, records):
        indexes = [r['index'] for r in records]
        assert indexes == list(range(1, len(records) + 1))

    def test_dates_are_formatted(self, records):
        """All non-empty dates should be YYYY-MM-DD format."""
        for r in records:
            if r['date']:
                assert len(r['date']) == 10, f"Bad date: {r['date']}"
                assert r['date'][4] == '-' and r['date'][7] == '-'

    def test_year_month_matches_date(self, records):
        for r in records:
            if r['date'] and r['year_month']:
                assert r['year_month'] == r['date'][:7]

    def test_multi_sheet_support(self, records):
        """Should have records from multiple sheets."""
        sheets = set(r['sheet'] for r in records)
        assert len(sheets) >= 2

    def test_working_time_has_billable_amount(self, records):
        """All Working Time records with rate and hours should have billable_amount."""
        for r in records:
            if r['event_type'] == 'Working Time' and r['billing_rate'] and r['hours'] > 0:
                assert r['billable_amount'] is not None
                assert r['billable_amount'] > 0

    def test_billable_amount_formula(self, records):
        """Verify billable_amount = hours × billing_rate × (1 + surcharge_rate)."""
        for r in records:
            if r['billable_amount'] is not None:
                multiplier = 1.0
                if r['surcharge_rate'] is not None:
                    multiplier = 1.0 + r['surcharge_rate']
                expected = r['hours'] * r['billing_rate'] * multiplier
                assert abs(r['billable_amount'] - expected) < 0.01, \
                    f"Record {r['index']}: {r['billable_amount']} != {expected}"

    def test_non_working_time_has_no_billable_amount(self, records):
        """Non-Working Time events should not have billable_amount."""
        for r in records:
            if r['event_type'] != 'Working Time':
                assert r['billable_amount'] is None

    def test_known_event_types(self, records):
        """All event types should be from the known set."""
        known = {'Working Time', 'PO', 'Invoice', 'Purchase', 'T&L',
                 'Deferment', 'Financial Record', 'Closure'}
        for r in records:
            if r['event_type']:
                assert r['event_type'] in known, \
                    f"Unknown event type: {r['event_type']}"


# ── Calculations on parsed data ───────────────────────────────────────────

class TestCalculationsIntegration:
    def test_statistics_finds_all_event_types(self, records):
        stats = calculate_statistics(records)
        et = set(stats['event_types'])
        assert 'Working Time' in et
        assert 'PO' in et
        assert 'Invoice' in et

    def test_date_range_is_valid(self, records):
        dr = calculate_date_range(records)
        assert dr['date_from'] <= dr['date_to']
        assert dr['date_from'] != ''

    def test_json_round_trip(self, records):
        data_json = prepare_json_data(records)
        parsed = json.loads(data_json)
        assert len(parsed) == len(records)
        # Verify a known field survives the round trip
        for orig, rt in zip(records, parsed):
            assert orig['project'] == rt['project']
            assert orig['event_type'] == rt['event_type']


# ── Full HTML generation ──────────────────────────────────────────────────

class TestHTMLGeneration:
    @pytest.fixture(scope='class')
    def html(self, records):
        return generate_html(records)

    def test_generates_html(self, html):
        assert html.startswith('<!DOCTYPE html>')
        assert '</html>' in html

    def test_contains_alldata_json(self, html):
        assert 'const allData =' in html

    def test_no_stale_pre_computed_json(self, html):
        """The cleaned-up version should NOT embed projectFinancials or monthlyWorkingTime."""
        assert 'const projectFinancials' not in html
        assert 'const monthlyWorkingTime' not in html

    def test_summary_cards_have_placeholders(self, html):
        """Summary values should be placeholders (JS fills them in)."""
        assert 'id="totalPOCoverage">-</div>' in html
        assert 'id="totalCharges">-</div>' in html
        assert 'id="totalInvoices">-</div>' in html

    def test_event_type_dropdown_populated(self, html):
        """The event type filter dropdown should have options from Python."""
        assert '<option value="Working Time">' in html
        assert '<option value="PO">' in html

    def test_contains_charts(self, html):
        assert 'projectAmountChart' in html
        assert 'forecastChart' in html

    def test_contains_css(self, html):
        assert '<style>' in html
        assert '--color-primary' in html

    def test_no_python_fstring_artifacts(self, html):
        """No unresolved f-string placeholders should remain."""
        # These would indicate a broken f-string
        import re
        # Look for {variable_name} patterns that aren't JS template literals
        # (JS uses ${...} inside backtick strings, which is fine)
        # We specifically check for Python variable names that were removed
        assert '{total_po_coverage' not in html
        assert '{total_charges' not in html
        assert '{total_invoices' not in html
        assert '{total_hours' not in html
        assert '{financials_json}' not in html
        assert '{monthly_summary_json}' not in html
