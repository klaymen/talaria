#!/usr/bin/env python3
"""
Excel file parsing functions for the dashboard generator.
"""

import pandas as pd
import sys
from datetime import datetime


def parse_amount(value):
    """Parse amount values that may contain currency symbols and formatting."""
    if pd.isna(value) or value == '':
        return 0.0
    
    # Convert to string and clean
    if isinstance(value, (int, float)):
        return float(value)
    
    value_str = str(value).strip()
    
    # Remove currency symbols and spaces
    value_str = value_str.replace('€', '').replace('$', '').replace(',', '').strip()
    
    try:
        return float(value_str)
    except ValueError:
        return 0.0


def parse_hours(value):
    """Parse hours values."""
    if pd.isna(value) or value == '':
        return 0.0
    
    if isinstance(value, (int, float)):
        return float(value)
    
    try:
        return float(str(value).strip())
    except ValueError:
        return 0.0


def parse_rate(value):
    """Parse rate values (hourly rate or percentage)."""
    if pd.isna(value) or value == '':
        return None
    
    value_str = str(value).strip()
    
    # Remove currency symbols
    value_str = value_str.replace('€', '').replace('$', '').replace(',', '').strip()
    
    # Check if it's a percentage
    if '%' in value_str:
        try:
            return float(value_str.replace('%', ''))
        except ValueError:
            return None
    
    try:
        return float(value_str)
    except ValueError:
        return None


def read_excel_data(file_path):
    """Read and parse Excel file."""
    try:
        df = pd.read_excel(file_path)
        
        # Clean column names
        df.columns = df.columns.str.strip()
        
        # Ensure we have the expected columns
        expected_cols = ['Date', 'Event Type', 'Project', 'Hourly Rate', 'Additional Rate', 'Hours', 'Amount']
        missing_cols = [col for col in expected_cols if col not in df.columns]
        
        if missing_cols:
            print(f"Warning: Missing columns: {missing_cols}")
            print(f"Available columns: {list(df.columns)}")
        
        # Parse data
        records = []
        for idx, row in df.iterrows():
            # Skip empty rows
            if pd.isna(row.get('Project', '')) or str(row.get('Project', '')).strip() == '':
                continue
            
            hourly_rate = parse_rate(row.get('Hourly Rate'))
            additional_rate = parse_rate(row.get('Additional Rate'))
            hours = parse_hours(row.get('Hours'))
            amount = parse_amount(row.get('Amount'))
            event_type = str(row.get('Event Type', '')).strip() if pd.notna(row.get('Event Type')) else ''
            
            # Calculate cost for Working Time: hours × hourly_rate × (1 + additional_rate)
            # Note: additional_rate is already in decimal format in Excel (e.g., 0.20 means 20%)
            # So we use it directly without dividing by 100
            calculated_cost = None
            if event_type == 'Working Time' and hourly_rate is not None and hours > 0:
                multiplier = 1.0
                if additional_rate is not None:
                    # additional_rate is already in decimal format (e.g., 0.20 = 20%), use directly
                    multiplier = 1.0 + additional_rate
                calculated_cost = hours * hourly_rate * multiplier
            
            record = {
                'index': int(row.get('#', idx + 1)) if pd.notna(row.get('#')) else idx + 1,
                'date': str(row.get('Date', '')) if pd.notna(row.get('Date')) else '',
                'event_type': event_type,
                'project': str(row.get('Project', '')).strip() if pd.notna(row.get('Project')) else '',
                'hourly_rate': hourly_rate,
                'additional_rate': additional_rate,
                'hours': hours,
                'amount': amount,
                'calculated_cost': calculated_cost  # For Working Time events
            }
            
            # Parse date
            if record['date']:
                try:
                    # Handle pandas Timestamp objects
                    if hasattr(record['date'], 'strftime'):
                        record['date'] = record['date'].strftime('%Y-%m-%d')
                    elif isinstance(record['date'], datetime):
                        record['date'] = record['date'].strftime('%Y-%m-%d')
                    elif isinstance(record['date'], str):
                        date_str = record['date'].strip()
                        # Remove time component if present (e.g., "2026-01-01 00:00:00" -> "2026-01-01")
                        if ' ' in date_str:
                            date_str = date_str.split(' ')[0]
                        # Try to parse various date formats
                        for fmt in ['%Y-%m-%d', '%d/%m/%Y', '%m/%d/%Y', '%Y/%m/%d']:
                            try:
                                dt = datetime.strptime(date_str, fmt)
                                record['date'] = dt.strftime('%Y-%m-%d')
                                break
                            except ValueError:
                                continue
                        # If parsing failed but we have YYYY-MM-DD format, use it directly
                        if len(date_str) == 10 and date_str[4] == '-' and date_str[7] == '-':
                            try:
                                # Validate it's a valid date
                                datetime.strptime(date_str, '%Y-%m-%d')
                                record['date'] = date_str
                            except ValueError:
                                pass
                except Exception:
                    pass
            
            # Extract year-month for monthly summaries
            if record['date']:
                try:
                    record['year_month'] = record['date'][:7]  # YYYY-MM format
                except:
                    record['year_month'] = ''
            else:
                record['year_month'] = ''
            
            records.append(record)
        
        return records
    
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        sys.exit(1)
