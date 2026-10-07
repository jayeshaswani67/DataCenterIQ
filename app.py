import streamlit as st
import pandas as pd

from src.data_loader import (
    load_data,
    find_column,
    get_numeric_columns,
    get_categorical_columns
)

from src.analysis import (
    dataset_summary,
    numeric_summary,
    architecture_summary,
    yearly_trend
)

from src.charts import (
    bar_chart,
    line_chart,
    scatter_chart,
    histogram
)


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="AMD Data Center Intelligence",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown(
    """
    <style>

    .main {
        padding-top: 1rem;
    }

    .metric-card {
        padding: 20px;
        border-radius: 12px;
        border: 1px solid rgba(128,128,128,0.25);
        text-align: center;
    }

    .section-title {
        margin-top: 30px;
        margin-bottom: 15px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

DATA_PATH = "data/amd_datacenter_gpus.csv"

df = load_data(DATA_PATH)


# --------------------------------------------------
# COLUMN DETECTION
# --------------------------------------------------

gpu_column = find_column(
    df,
    [
        "gpu_name",
        "product_name",
        "model",
        "name",
        "gpu"
    ]
)

architecture_column = find_column(
    df,
    [
        "architecture",
        "gpu_architecture",
        "architecture_name"
    ]
)

series_column = find_column(
    df,
    [
        "series",
        "product_series",
        "family"
    ]
)

year_column = find_column(
    df,
    [
        "launch_year",
        "release_year",
        "year"
    ]
)

process_column = find_column(
    df,
    [
        "process_node_nm",
        "process_node",
        "node_nm",
        "process_nm"
    ]
)

memory_column = find_column(
    df,
    [
        "memory_gb",
        "memory",
        "vram_gb",
        "vram"
    ]
)

power_column = find_column(
    df,
    [
        "tdp_w",
        "tdp",
        "power_w",
        "power"
    ]
)

bandwidth_column = find_column(
    df,
    [
        "memory_bandwidth_gbps",
        "memory_bandwidth",
        "bandwidth_gbps",
        "bandwidth"
    ]
)

compute_column = find_column(
    df,
    [
        "compute_performance",
        "performance",
        "fp32",
        "fp16",
        "flops",
        "tflops"
    ]
)


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.title("AMD Data Center")

st.sidebar.markdown(
    """
    **Hardware Intelligence Dashboard**

    Analyze AMD data-center accelerators,
    architecture evolution and infrastructure
    efficiency.
    """
)

st.sidebar.divider()

st.sidebar.subheader("Filters")


# Architecture filter

if architecture_column:

    architectures = sorted(
        df[architecture_column]
        .dropna()
        .astype(str)
        .unique()
        .tolist()
    )

    selected_architectures = st.sidebar.multiselect(
        "Architecture",
        architectures,
        default=architectures
    )

    df_filtered = df[
        df[architecture_column]
        .astype(str)
        .isin(selected_architectures)
    ]

else:

    df_filtered = df.copy()


# Year filter

if year_column:

    years = pd.to_numeric(
        df_filtered[year_column],
        errors="coerce"
    ).dropna()

    if not years.empty:

        min_year = int(years.min())
        max_year = int(years.max())

        selected_years = st.sidebar.slider(
            "Launch Year",
            min_value=min_year,
            max_value=max_year,
            value=(min_year, max_year)
        )

        df_filtered = df_filtered[
            pd.to_numeric(
                df_filtered[year_column],
                errors="coerce"
            ).between(
                selected_years[0],
                selected_years[1]
            )
        ]


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("AMD Data Center Intelligence")

st.markdown(
    """
    Interactive analysis of AMD data-center GPU and
    accelerator hardware, architecture evolution,
    memory, compute characteristics and infrastructure
    efficiency.
    """
)

st.divider()


# --------------------------------------------------
# KPI SECTION
# --------------------------------------------------

summary = dataset_summary(df_filtered)

col1, col2, col3, col4 = st.columns(4)


with col1:
    st.metric(
        "Products",
        summary["rows"]
    )


with col2:
    if architecture_column:
        value = df_filtered[
            architecture_column
        ].nunique()
    else:
        value = "N/A"

    st.metric(
        "Architectures",
        value
    )


with col3:
    if memory_column:
        avg_memory = pd.to_numeric(
            df_filtered[memory_column],
            errors="coerce"
        ).mean()

        if pd.notna(avg_memory):
            st.metric(
                "Avg Memory",
                f"{avg_memory:.1f}"
            )
        else:
            st.metric("Avg Memory", "N/A")
    else:
        st.metric("Avg Memory", "N/A")


with col4:
    if process_column:
        avg_process = pd.to_numeric(
            df_filtered[process_column],
            errors="coerce"
        ).mean()

        if pd.notna(avg_process):
            st.metric(
                "Avg Process Node",
                f"{avg_process:.1f} nm"
            )
        else:
            st.metric("Avg Process Node", "N/A")
    else:
        st.metric("Avg Process Node", "N/A")


# --------------------------------------------------
# TABS
# --------------------------------------------------

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "📊 Overview",
        "🏗️ Architecture",
        "⚡ Efficiency",
        "🔎 Dataset"
    ]
)


# ==================================================
# TAB 1 — OVERVIEW
# ==================================================

with tab1:

    st.subheader("Data Center Hardware Overview")

    col1, col2 = st.columns(2)

    # Architecture distribution

    with col1:

        if architecture_column:

            architecture_data = architecture_summary(
                df_filtered,
                architecture_column
            )

            if not architecture_data.empty:

                fig = bar_chart(
                    architecture_data,
                    "architecture",
                    "gpu_count",
                    "Products by Architecture"
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

        else:

            st.info(
                "Architecture column not detected."
            )


    # Launch year

    with col2:

        if year_column:

            year_counts = (
                df_filtered
                .assign(
                    launch_year_numeric=pd.to_numeric(
                        df_filtered[year_column],
                        errors="coerce"
                    )
                )
                .dropna(
                    subset=["launch_year_numeric"]
                )
                .groupby(
                    "launch_year_numeric"
                )
                .size()
                .reset_index(
                    name="products"
                )
            )

            if not year_counts.empty:

                fig = line_chart(
                    year_counts,
                    "launch_year_numeric",
                    "products",
                    "AMD Data Center Product Evolution"
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )


    # Memory distribution

    if memory_column:

        st.subheader("Memory Distribution")

        numeric_memory = pd.to_numeric(
            df_filtered[memory_column],
            errors="coerce"
        )

        memory_df = pd.DataFrame({
            memory_column: numeric_memory
        }).dropna()

        if not memory_df.empty:

            fig = histogram(
                memory_df,
                memory_column,
                "Memory Capacity Distribution"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )


# ==================================================
# TAB 2 — ARCHITECTURE
# ==================================================

with tab2:

    st.subheader("Architecture Analysis")

    if architecture_column:

        if year_column:

            trend_df = (
                df_filtered
                .copy()
            )

            trend_df["_year"] = pd.to_numeric(
                trend_df[year_column],
                errors="coerce"
            )

            architecture_year = (
                trend_df
                .dropna(subset=["_year"])
                .groupby(
                    ["_year", architecture_column]
                )
                .size()
                .reset_index(
                    name="products"
                )
            )

            if not architecture_year.empty:

                fig = scatter_chart(
                    architecture_year,
                    "_year",
                    "products",
                    "Architecture Evolution",
                    color=architecture_column
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

        # Architecture table

        st.subheader("Architecture Breakdown")

        arch_table = (
            df_filtered[
                [architecture_column]
            ]
            .value_counts()
            .reset_index()
        )

        st.dataframe(
            arch_table,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.warning(
            "No architecture column detected in the dataset."
        )


# ==================================================
# TAB 3 — EFFICIENCY
# ==================================================

with tab3:

    st.subheader("Infrastructure Efficiency")

    st.markdown(
        """
        Efficiency metrics are calculated only when the
        required columns are available in the dataset.
        """
    )

    # Performance / Watt

    if compute_column and power_column:

        efficiency_df = df_filtered.copy()

        efficiency_df["_performance"] = pd.to_numeric(
            efficiency_df[compute_column],
            errors="coerce"
        )

        efficiency_df["_power"] = pd.to_numeric(
            efficiency_df[power_column],
            errors="coerce"
        )

        efficiency_df = efficiency_df[
            (efficiency_df["_power"] > 0)
        ].dropna(
            subset=["_performance", "_power"]
        )

        if not efficiency_df.empty:

            efficiency_df["performance_per_watt"] = (
                efficiency_df["_performance"]
                / efficiency_df["_power"]
            )

            st.subheader(
                "Performance per Watt"
            )

            display_columns = []

            if gpu_column:
                display_columns.append(gpu_column)

            if architecture_column:
                display_columns.append(
                    architecture_column
                )

            display_columns.append(
                "performance_per_watt"
            )

            result = (
                efficiency_df[
                    display_columns
                ]
                .sort_values(
                    "performance_per_watt",
                    ascending=False
                )
            )

            st.dataframe(
                result,
                use_container_width=True,
                hide_index=True
            )

            if gpu_column:

                fig = bar_chart(
                    result.head(10),
                    gpu_column,
                    "performance_per_watt",
                    "Top Products by Performance per Watt"
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

    else:

        st.info(
            "Performance-per-watt analysis requires "
            "both performance and power/TDP columns."
        )


    # Memory / Watt

    if memory_column and power_column:

        st.subheader(
            "Memory Capacity per Watt"
        )

        memory_efficiency = df_filtered.copy()

        memory_efficiency["_memory"] = pd.to_numeric(
            memory_efficiency[memory_column],
            errors="coerce"
        )

        memory_efficiency["_power"] = pd.to_numeric(
            memory_efficiency[power_column],
            errors="coerce"
        )

        memory_efficiency = (
            memory_efficiency[
                memory_efficiency["_power"] > 0
            ]
            .dropna(
                subset=["_memory", "_power"]
            )
        )

        if not memory_efficiency.empty:

            memory_efficiency[
                "memory_per_watt"
            ] = (
                memory_efficiency["_memory"]
                / memory_efficiency["_power"]
            )

            display_columns = []

            if gpu_column:
                display_columns.append(
                    gpu_column
                )

            display_columns.append(
                "memory_per_watt"
            )

            result = (
                memory_efficiency[
                    display_columns
                ]
                .sort_values(
                    "memory_per_watt",
                    ascending=False
                )
            )

            st.dataframe(
                result,
                use_container_width=True,
                hide_index=True
            )


# ==================================================
# TAB 4 — DATASET
# ==================================================

with tab4:

    st.subheader("Dataset Explorer")

    st.write(
        f"Showing {len(df_filtered)} of {len(df)} records."
    )

    st.dataframe(
        df_filtered,
        use_container_width=True,
        height=500
    )

    st.subheader("Dataset Statistics")

    stats = df_filtered.describe(
        include="all"
    ).T

    st.dataframe(
        stats,
        use_container_width=True
    )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "AMD Data Center Intelligence Dashboard • "
    "Built with Python, Pandas, Plotly and Streamlit"
)