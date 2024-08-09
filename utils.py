def clean_number(value: str) -> float:
    return float(value.replace(",", ""))


def clean_int(value: str) -> int:
    return int(value.replace(",", ""))
