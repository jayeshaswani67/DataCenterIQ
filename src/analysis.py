import pandas as pd


def dataset_summary(df: pd.DataFrame) -> dict:
    """
    Generate high-level dataset statistics.
    """

    return {
        "rows": len(df),
        "columns": len(df.columns),
        "missing_values": int(df.isna().sum().sum()),
        "duplicate_rows": int(df.duplicated().sum()),
    }


def numeric_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generate descriptive statistics for numeric columns.
    """

    numeric_df = df.select_dtypes(include="number")

    if numeric_df.empty:
        return pd.DataFrame()

    return numeric_df.describe().T


def architecture_summary(df: pd.DataFrame, column: str):
    """
    Count products by architecture.
    """

    if column not in df.columns:
        return pd.DataFrame()

    return (
        df[column]
        .value_counts(dropna=False)
        .reset_index()
        .rename(columns={
            column: "architecture",
            "count": "gpu_count"
        })
    )


def calculate_efficiency(
    df: pd.DataFrame,
    performance_column: str,
    power_column: str
):
    """
    Calculate performance per watt.

    Only use when both performance and power columns exist.
    """

    result = df.copy()

    result["performance_per_watt"] = (
        result[performance_column] / result[power_column]
    )

    return result


def calculate_memory_per_watt(
    df: pd.DataFrame,
    memory_column: str,
    power_column: str
):
    """
    Calculate memory capacity per watt.
    """

    result = df.copy()

    result["memory_per_watt"] = (
        result[memory_column] / result[power_column]
    )

    return result


def yearly_trend(
    df: pd.DataFrame,
    year_column: str,
    metric_column: str
):
    """
    Aggregate a metric by launch year.
    """

    if year_column not in df.columns:
        return pd.DataFrame()

    if metric_column not in df.columns:
        return pd.DataFrame()

    result = (
        df.groupby(year_column)[metric_column]
        .mean()
        .reset_index()
        .sort_values(year_column)
    )

    return result