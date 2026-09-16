"""Shared model endpoints; these are not clinical response or grading criteria."""

from bisect import bisect_left

from .toxicity import crs_grade, icans_grade


def at_day(times, values, day):
    """Interpolate an observed day; return None outside the simulated interval."""
    if day > times[-1] or day < times[0]:
        return None
    i = bisect_left(times, day)
    if times[i] == day:
        return values[i]
    weight = (day - times[i - 1]) / (times[i] - times[i - 1])
    return values[i - 1] + weight * (values[i] - values[i - 1])


def summarize(times, series, params, lysis_peak, seed):
    result = {}
    for key in ("E", "M", "IFN", "IL6", "TNF"):
        values = series[key]
        result[f"{key}_peak"] = max(values)
    result["E_peak_day"] = times[series["E"].index(result["E_peak"])]
    for key, label in (("T", "T_min"), ("B", "B_nadir")):
        result[label] = min(series[key])
        result[f"{label}_day"] = times[series[key].index(result[label])]
    for key, days in (("T", (90, 120)), ("M", (90, 120)), ("B", (90,))):
        for day in days:
            result[f"{key}_d{day}"] = at_day(times, series[key], day)
    t90, t120 = result["T_d90"], result["T_d120"]
    m120, b90 = result["M_d120"], result["B_d90"]
    response_min = min(v for t, v in zip(times, series["T"]) if t <= 90)
    if t90 is not None:
        response_min = min(response_min, t90)
    result["responds"] = (
        None if t90 is None else (response_min < 0.1 * params["T0"] and t90 < 0.2 * params["T0"])
    )
    result["CR"] = None if t90 is None else (result["responds"] and t90 < 5e-4 * params["T0"])
    relapse_min = min(v for t, v in zip(times, series["T"]) if t <= 120)
    if t120 is not None:
        relapse_min = min(relapse_min, t120)
    result["relapses"] = (
        None
        if t120 is None
        else (result["responds"] and t120 > max(relapse_min, 1e4) * 3 and t120 > 1e8)
    )
    result["persistent"] = None if m120 is None else m120 > 1.8e7
    result["B_aplasia"] = None if b90 is None else b90 < 1e7
    result["lysis_peak"] = lysis_peak
    result["CRS_grade"] = crs_grade(
        result["IL6_peak"], result["IFN_peak"], result["TNF_peak"], lysis_peak
    )
    result["ICANS_grade"] = icans_grade(result["CRS_grade"], seed)
    return result
