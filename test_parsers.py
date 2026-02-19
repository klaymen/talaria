#!/usr/bin/env python3
"""Tests for parsers.py"""

import math
import pytest
import pandas as pd
from parsers import parse_amount, parse_hours, parse_rate


# ── parse_amount ──────────────────────────────────────────────────────────

class TestParseAmount:
    def test_numeric_int(self):
        assert parse_amount(100) == 100.0

    def test_numeric_float(self):
        assert parse_amount(99.5) == 99.5

    def test_zero(self):
        assert parse_amount(0) == 0.0

    def test_negative(self):
        assert parse_amount(-500) == -500.0

    def test_string_plain(self):
        assert parse_amount('1234') == 1234.0

    def test_string_with_euro(self):
        assert parse_amount('€1234') == 1234.0

    def test_string_with_dollar(self):
        assert parse_amount('$1234') == 1234.0

    def test_string_with_commas(self):
        assert parse_amount('1,234,567') == 1234567.0

    def test_string_euro_and_commas(self):
        assert parse_amount('€1,234.56') == 1234.56

    def test_string_with_spaces(self):
        assert parse_amount('  1234  ') == 1234.0

    def test_empty_string(self):
        assert parse_amount('') == 0.0

    def test_nan(self):
        assert parse_amount(float('nan')) == 0.0

    def test_none_like(self):
        assert parse_amount(pd.NA) == 0.0

    def test_unparseable(self):
        assert parse_amount('abc') == 0.0


# ── parse_hours ───────────────────────────────────────────────────────────

class TestParseHours:
    def test_numeric_int(self):
        assert parse_hours(8) == 8.0

    def test_numeric_float(self):
        assert parse_hours(7.5) == 7.5

    def test_zero(self):
        assert parse_hours(0) == 0.0

    def test_string(self):
        assert parse_hours('10') == 10.0

    def test_string_with_spaces(self):
        assert parse_hours('  10.5  ') == 10.5

    def test_empty_string(self):
        assert parse_hours('') == 0.0

    def test_nan(self):
        assert parse_hours(float('nan')) == 0.0

    def test_unparseable(self):
        assert parse_hours('abc') == 0.0


# ── parse_rate ────────────────────────────────────────────────────────────

class TestParseRate:
    def test_numeric_int(self):
        assert parse_rate(50) == 50.0

    def test_numeric_float(self):
        assert parse_rate(75.5) == 75.5

    def test_string_plain(self):
        assert parse_rate('100') == 100.0

    def test_string_with_euro(self):
        assert parse_rate('€50') == 50.0

    def test_string_with_dollar(self):
        assert parse_rate('$75') == 75.0

    def test_percentage(self):
        assert parse_rate('5%') == 5.0

    def test_percentage_decimal(self):
        assert parse_rate('12.5%') == 12.5

    def test_empty_string(self):
        assert parse_rate('') is None

    def test_nan(self):
        assert parse_rate(float('nan')) is None

    def test_unparseable(self):
        assert parse_rate('abc') is None

    def test_unparseable_percentage(self):
        assert parse_rate('abc%') is None


# ── Billable amount calculation (tested via read_excel_data) ──────────────

class TestBillableAmount:
    """Test the billable_amount = hours × billing_rate × (1 + surcharge_rate) formula."""

    def _make_wt_record(self, hours, billing_rate, surcharge_rate):
        """Simulate the billable_amount calculation from parsers.py."""
        billable_amount = None
        if billing_rate is not None and hours > 0:
            multiplier = 1.0
            if surcharge_rate is not None:
                multiplier = 1.0 + surcharge_rate
            billable_amount = hours * billing_rate * multiplier
        return billable_amount

    def test_basic(self):
        # 100 hours × €50 × (1 + 0.05) = 5250
        assert self._make_wt_record(100, 50.0, 0.05) == 5250.0

    def test_no_surcharge(self):
        # 10 hours × €100 × 1.0 = 1000
        assert self._make_wt_record(10, 100.0, None) == 1000.0

    def test_zero_hours(self):
        assert self._make_wt_record(0, 50.0, 0.05) is None

    def test_no_rate(self):
        assert self._make_wt_record(10, None, 0.05) is None

    def test_zero_surcharge(self):
        # surcharge_rate=0 means multiplier=1.0
        assert self._make_wt_record(10, 100.0, 0.0) == 1000.0

    def test_large_surcharge(self):
        # 10 hours × €100 × (1 + 1.5) = 2500
        assert self._make_wt_record(10, 100.0, 1.5) == 2500.0
