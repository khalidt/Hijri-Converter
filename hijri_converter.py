"""
Hijri <-> Gregorian date converter.

Uses the tabular (arithmetic) Islamic calendar, going through the
Julian Day Number (JDN) as a calendar-neutral bridge:

    Hijri  <-->  JDN  <-->  Gregorian
"""

# ----------------------------------------------------------------------
# Hijri  <-->  JDN
# ----------------------------------------------------------------------

def hijri_to_jdn(y, m, d):
    """Tabular Islamic (Hijri) date -> Julian Day Number."""
    return (
        (11 * y + 3) // 30
        + 354 * y
        + 30 * m
        - (m - 1) // 2
        + d
        + 1948440 - 385
    )


def jdn_to_hijri(jdn):
    """Julian Day Number -> tabular Islamic (Hijri) date (y, m, d)."""
    jd = jdn - 1948440 + 10632
    n = (jd - 1) // 10631
    jd = jd - 10631 * n + 354
    j = (((10985 - jd) // 5316) * ((50 * jd) // 17719)
         + (jd // 5670) * ((43 * jd) // 15238))
    jd = (jd - ((30 - j) // 15) * ((17719 * j) // 50)
          - (j // 16) * ((15238 * j) // 43) + 29)
    m = (24 * jd) // 709
    d = jd - (709 * m) // 24
    y = 30 * n + j - 30
    return y, m, d


# ----------------------------------------------------------------------
# Gregorian  <-->  JDN
# ----------------------------------------------------------------------

def gregorian_to_jdn(y, m, d):
    """Proleptic Gregorian date -> Julian Day Number."""
    a = (14 - m) // 12
    yy = y + 4800 - a
    mm = m + 12 * a - 3
    return (d + (153 * mm + 2) // 5 + 365 * yy
            + yy // 4 - yy // 100 + yy // 400 - 32045)


def jdn_to_gregorian(jdn):
    """Julian Day Number -> proleptic Gregorian date (y, m, d)."""
    a = jdn + 32044
    b = (4 * a + 3) // 146097
    c = a - (146097 * b) // 4
    dd = (4 * c + 3) // 1461
    e = c - (1461 * dd) // 4
    m = (5 * e + 2) // 153
    day = e - (153 * m + 2) // 5 + 1
    month = m + 3 - 12 * (m // 10)
    year = 100 * b + dd - 4800 + (m // 10)
    return year, month, day


# ----------------------------------------------------------------------
# Public convenience functions
# ----------------------------------------------------------------------

WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturday", "Sunday"]


def weekday(jdn):
    # JDN 0 was a Monday; (jdn mod 7) == 0 -> Monday
    return WEEKDAYS[jdn % 7]


def hijri_to_gregorian(y, m, d):
    jdn = hijri_to_jdn(y, m, d)
    gy, gm, gd = jdn_to_gregorian(jdn)
    return gy, gm, gd, weekday(jdn)


def gregorian_to_hijri(y, m, d):
    jdn = gregorian_to_jdn(y, m, d)
    hy, hm, hd = jdn_to_hijri(jdn)
    return hy, hm, hd, weekday(jdn)


# ----------------------------------------------------------------------
# Command-line interface
# ----------------------------------------------------------------------

def _parse(date_str):
    parts = date_str.replace("-", "/").split("/")
    if len(parts) != 3:
        raise ValueError("Date must be in DD/MM/YYYY format")
    d, m, y = (int(p) for p in parts)
    return y, m, d


def main():
    print("Hijri <-> Gregorian converter (tabular Islamic calendar)")
    print("-" * 56)
    print("  1) Hijri (AH)   -> Gregorian")
    print("  2) Gregorian    -> Hijri (AH)")
    choice = input("Choose 1 or 2: ").strip()
    date_str = input("Enter date as DD/MM/YYYY: ").strip()

    y, m, d = _parse(date_str)

    if choice == "1":
        gy, gm, gd, wd = hijri_to_gregorian(y, m, d)
        print(f"\n{d:02d}/{m:02d}/{y} AH  =  {wd}, "
              f"{gd:02d}/{gm:02d}/{gy} (Gregorian)")
    elif choice == "2":
        hy, hm, hd, wd = gregorian_to_hijri(y, m, d)
        print(f"\n{d:02d}/{m:02d}/{y} (Gregorian)  =  {wd}, "
              f"{hd:02d}/{hm:02d}/{hy} AH")
    else:
        print("Invalid choice.")
        return

    print("\nNote: tabular/arithmetic calendar. Saudi Umm al-Qura "
          "(observation-based) may differ by +/-1 day.")


if __name__ == "__main__":
    main()
