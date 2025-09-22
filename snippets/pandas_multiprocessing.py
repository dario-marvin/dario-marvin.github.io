"""
Pandas + multiprocessing examples
- Row-wise operation with Pool.imap over itertuples (fast tuple access)
- Column-wise operation with Pool.imap over items (Series per column)
"""

import multiprocessing as mp
import numpy as np
import pandas as pd
from typing import Tuple


def hypotenuse(row: Tuple[int, int, int]) -> float:
    """Compute sqrt(a^2 + b^2) given a row tuple (index, a, b)."""
    _, a, b = row
    return float((a ** 2 + b ** 2) ** 0.5)


def sum_of_squares(col_tuple: Tuple[str, pd.Series]) -> int:
    """Sum of squares for a column; col_tuple is (name, Series)."""
    name, series = col_tuple
    return int(sum(int(x) ** 2 for x in series))


def demo() -> None:
    # Sample frame with two numeric columns
    df = pd.DataFrame(np.random.randint(3, 10, size=(5, 2)), columns=["a", "b"])
    print("Input DataFrame:\n", df.head(), "\n", sep="")

    # Row-wise parallelism
    with mp.Pool(processes=4) as pool:
        # Efficient row iterator returning tuples (index, a, b)
        rows = df.itertuples(index=True, name=None)
        result_iter = pool.imap(hypotenuse, rows, chunksize=10)
        row_outputs = [round(x, 2) for x in result_iter]
    print("Row-wise hypotenuse results:", row_outputs[: min(len(row_outputs), 10)])

    # Column-wise parallelism
    with mp.Pool(processes=2) as pool:
        # In pandas < 2.0, `items` is `iteritems`
        columns_iter = df.items()
        result_iter = pool.imap(sum_of_squares, columns_iter, chunksize=10)
        col_outputs = list(result_iter)
    print("Column-wise sum of squares results:", col_outputs)


if __name__ == "__main__":
    demo()
