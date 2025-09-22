import re

def isNumber(s: str) -> bool:
    sign = r"[+-]?"  # zero or one sign
    decimal = r"\."  # decimal dot
    exponential = r"[eE]"  # exponential

    pattern = f'^{sign}(?:\d(?:{decimal}\d*)?|{decimal}\d+)({exponential}{sign}\d+)?$'
    return bool(re.fullmatch(pattern, s))
    
