import pandas as pd
import streamlit as st


def load_data(file_path: str) -> pd.DataFrame:
    """
    Load AMD data-center dataset from CSV.
    """

    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        st.error(f"Dataset not found: {file_path}")
        st.stop()
    except Exception as e:
        st.error(f"Error loading dataset: {e}")
        st.stop()

    # Clean column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )

    # Remove completely empty columns
    df = df.dropna(axis=1, how="all")

    # Remove duplicate rows
    df = df.drop_duplicates()

    return df


def get_numeric_columns(df: pd.DataFrame):
    return df.select_dtypes(include="number").columns.tolist()


def get_categorical_columns(df: pd.DataFrame):
    return df.select_dtypes(include=["object", "category"]).columns.tolist()


def find_column(df: pd.DataFrame, possible_names):
    """
    Find the first matching column from a list of possible names.
    """

    for name in possible_names:
        if name in df.columns:
            return name

    return None