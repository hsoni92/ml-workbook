"""Date defaults and validation for itinerary planner."""

from datetime import date, timedelta


def _parse_yyyy_mm_dd(s: str) -> date | None:
    """Parse YYYY-MM-DD string to date, or return None if invalid."""
    s = (s or "").strip()
    if not s:
        return None
    try:
        return date.fromisoformat(s)
    except ValueError:
        return None


def compute_default_dates(
    start_date: str,
    end_date: str,
    num_destinations: int,
    *,
    trip_duration_days: int | None = None,
    today: date | None = None,
) -> tuple[str, str]:
    """Compute start and end dates, filling defaults when missing.

    When trip_duration_days is set (e.g. user said "15 days"), the span is forced to that many
    calendar days (inclusive). Otherwise:
    - If both start and end are given and valid (start <= end), return them as YYYY-MM-DD.
    - If only start_date is set: end = start + default_days.
    - If only end_date is set: start = end - default_days, or today if that would be in the past.
    - If neither is set: start = today, end = today + default_days.
    - num_destinations is used only for default_days when trip_duration_days is not set.
    """
    if today is None:
        today = date.today()
    default_days = (
        trip_duration_days
        if trip_duration_days is not None and trip_duration_days > 0
        else (max(15, num_destinations) if num_destinations else 15)
    )
    # Span in calendar days inclusive = (end - start).days + 1, so end = start + (N - 1)
    span_days = default_days - 1  # timedelta to add to start to get end

    start_d = _parse_yyyy_mm_dd(start_date)
    end_d = _parse_yyyy_mm_dd(end_date)

    # When trip_duration_days is set, prefer it over LLM end_date for length
    if trip_duration_days is not None and trip_duration_days > 0:
        if start_d is not None:
            end_d = start_d + timedelta(days=span_days)
            return start_d.isoformat(), end_d.isoformat()
        if end_d is not None:
            start_d = end_d - timedelta(days=span_days)
            if start_d < today:
                start_d = today
                end_d = today + timedelta(days=span_days)
            return start_d.isoformat(), end_d.isoformat()
        start_d = today
        end_d = today + timedelta(days=span_days)
        return start_d.isoformat(), end_d.isoformat()

    if start_d is not None and end_d is not None:
        if start_d <= end_d:
            return start_d.isoformat(), end_d.isoformat()
        start_d = None
        end_d = None

    if start_d is not None and end_d is None:
        end_d = start_d + timedelta(days=default_days - 1)
        return start_d.isoformat(), end_d.isoformat()

    if start_d is None and end_d is not None:
        start_d = end_d - timedelta(days=default_days - 1)
        if start_d < today:
            start_d = today
            end_d = today + timedelta(days=default_days - 1)
        return start_d.isoformat(), end_d.isoformat()

    start_d = today
    end_d = today + timedelta(days=default_days - 1)
    return start_d.isoformat(), end_d.isoformat()
