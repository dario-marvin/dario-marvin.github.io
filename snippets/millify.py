import math
import re
from typing import Union


def millify(n: Union[float, int]) -> str:
    """
    Returns the simplified string using the final letter as an indicator of the power of 3

    :param n: *float*, the input number to be converted
    :return: *str*, the suitably converted input into string format, with 0, 1, or 2 decimals
    """

    if n < 0:
        return '-' + millify(-n)

    if n < 1000:
        if isinstance(n, int):
            return str(n)
        else:
            if n.is_integer():
                return str(int(n))
            else:
                return f'{n:.2f}'.rstrip('0').rstrip('.')

    else:
        millnames = ['', 'k', 'm', 'b', 't', 'qa', 'qi', 'sx', 'sp', 'oc', 'no', 'dc', 'ud', 'dd', 'td', 'qad', 'qid']
        n = float(n)

        max_index = len(millnames) - 1
        thousands = int(math.floor(math.log10(n) / 3))

        millidx = max(0, min(max_index, thousands))

        formatted_number = f'{(n / 10 ** (3 * millidx)):.2f}'
        if formatted_number.endswith('.00'):
            formatted_number = formatted_number[:-1]

        return f'{formatted_number}{millnames[millidx]}'


def demillify(n: Union[str, int, float]) -> float:
    """
    Takes the simplified number format, e.g. 3.75m, and returns the equivalent float

    :param n: *str*, the number in simplified string format
    :return: *float* the equivalent number
    """

    if isinstance(n, int) or isinstance(n, float):
        return n

    if not re.search('[a-zA-Z]', n):
        if '.' in n:
            return float(n)
        else:
            return int(n)

    if n.endswith(('k', 'K')):
        return int(float(n[:-1]) * 1e3)
    elif n.endswith(('m', 'M')):
        return int(float(n[:-1]) * 1e6)
    elif n.endswith(('b', 'B')):
        return int(float(n[:-1]) * 1e9)
    elif n.endswith(('t', 'T')):
        return int(float(n[:-1]) * 1e12)
    elif n.endswith(('qa', 'QA')):
        return int(float(n[:-2]) * 1e15)
    elif n.endswith(('qi', 'QI')):
        return int(float(n[:-2]) * 1e18)
    elif n.endswith(('sx', 'SX')):
        return int(float(n[:-2]) * 1e21)
    elif n.endswith(('sp', 'SP')):
        return int(float(n[:-2]) * 1e24)
    else:
        raise Exception(f'Number format {n} not recognized')
