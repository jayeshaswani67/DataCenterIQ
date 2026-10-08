# DataCenterIQ — AMD Data Center GPU Analysis

DataCenterIQ is a data analytics and visualization project focused on analyzing **AMD data-center GPUs** and understanding how accelerator hardware evolves across architecture, memory, compute performance, power consumption, and semiconductor process technology.

The project combines **Python-based exploratory data analysis (EDA)** with an interactive **Streamlit dashboard** to turn GPU specifications into useful data-center infrastructure insights.

---

## 🚀 Project Overview

Modern AI and high-performance computing infrastructure depends heavily on accelerator hardware.

DataCenterIQ analyzes AMD data-center GPU specifications to answer questions such as:

- How are AMD GPU architectures evolving?
- Which GPUs provide the highest memory capacity?
- How does memory bandwidth change across generations?
- How does GPU power consumption vary?
- Which GPUs provide better performance per watt?
- How are semiconductor process nodes changing over time?
- What hardware characteristics matter for data-center infrastructure?

The goal is not simply to display GPU specifications, but to use data to understand **compute infrastructure trends and efficiency**.

---

## 🎯 Objectives

The main objectives of DataCenterIQ are:

1. Analyze AMD data-center GPU specifications.
2. Clean and standardize technical hardware data.
3. Compare GPU architectures and product series.
4. Analyze memory capacity and memory bandwidth.
5. Study GPU power/TDP characteristics.
6. Calculate relative performance-per-watt where supported by the dataset.
7. Study process-node evolution.
8. Build an interactive Streamlit dashboard.
9. Create a foundation for future AI infrastructure analysis.

---

## 📊 Analysis Areas

### GPU Portfolio

Analyze the distribution of AMD data-center GPUs across:

- GPU models
- Product series
- Architectures
- Launch years

### Architecture Evolution

Analyze how AMD GPU architectures change over time and compare technical characteristics between generations.

### Semiconductor Process Technology

Analyze process-node changes across GPU generations.

Example:

```text
Launch Year → Process Node
```

This helps visualize the relationship between GPU generations and semiconductor manufacturing technology.

### Memory

Analyze:

- Memory capacity
- Memory bandwidth
- Memory characteristics by architecture
- Memory trends across GPU generations

Memory is especially important for AI workloads where model size and memory bandwidth can become major bottlenecks.

### Power & Efficiency

Analyze:

- GPU TDP
- Power consumption
- Compute performance
- Performance per watt

A simple relative efficiency metric is calculated when both compute performance and TDP are available:

```text
Performance per Watt = Compute Performance / TDP
```

The metric is intended for relative comparison within the dataset and should not be treated as a universal benchmark.

---

## 🧠 Key Infrastructure Questions

DataCenterIQ is designed around several data-center infrastructure questions:

### Compute

- Which GPUs provide the strongest compute characteristics?
- How does compute capability change across generations?

### Memory

- Which GPUs provide the largest memory capacity?
- Which GPUs provide the highest memory bandwidth?
- Is memory capability increasing with newer architectures?

### Efficiency

- Which GPUs provide the strongest performance-per-watt according to the dataset?
- Does higher power consumption correspond to higher compute performance?

### Semiconductor Technology

- How has process technology changed over time?
- Which architectures use smaller process nodes?

### Infrastructure

- How can accelerator power affect data-center cooling?
- How can increasing GPU power affect rack density?
- Which hardware characteristics could become infrastructure bottlenecks?

---

## 🛠️ Tech Stack

### Programming

- Python 3.12

### Data Analysis

- Pandas
- NumPy

### Visualization

- Matplotlib
- Seaborn
- Plotly

### Interactive Dashboard

- Streamlit

### Development

- Jupyter Notebook
- VS Code
- Python virtual environment

---

## 📁 Project Structure

```text
DataCenterIQ/
│
├── .venv/
│
├── data/
│   ├── amd_datacenter_gpus.csv
│   └── amd_datacenter_gpus_clean.csv
│
├── notebooks/
│   └── DataCenterIQ_Analysis.ipynb
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── analysis.py
│   └── charts.py
│
├── assets/
│   └── dashboard_preview.png
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🔬 Exploratory Data Analysis

The main notebook is:

```text
notebooks/DataCenterIQ_Analysis.ipynb
```

The notebook performs:

```text
Load Dataset
      ↓
Inspect Dataset
      ↓
Clean & Normalize Data
      ↓
Detect GPU Fields
      ↓
Portfolio Analysis
      ↓
Architecture Analysis
      ↓
Process Node Analysis
      ↓
Memory Analysis
      ↓
Bandwidth Analysis
      ↓
Power Analysis
      ↓
Performance/Watt
      ↓
Correlation Analysis
      ↓
Infrastructure Insights
```

---

## 📈 Streamlit Dashboard

The Streamlit application provides an interactive interface for exploring the dataset.

Planned dashboard sections include:

### Overview

High-level metrics such as:

- Total GPU models
- GPU series
- Architectures
- Launch years
- Memory
- Power
- Compute characteristics

### GPU Comparison

Compare individual GPUs using technical specifications.

### Architecture

Explore:

- Architecture distribution
- Architecture evolution
- Launch timeline
- Technical characteristics

### Efficiency

Analyze:

- TDP
- Compute performance
- Performance per watt
- Power vs performance

### Dataset

Explore the underlying dataset and filtered records.

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/jayeshaswani67/DataCenterIQ.git
```

Move into the project:

```bash
cd DataCenterIQ
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows CMD:

```cmd
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🧪 Jupyter Kernel

The project uses a dedicated kernel:

```text
Python (DataCenterIQ)
```

Install the kernel with:

```bash
python -m ipykernel install --user --name DataCenterIQ --display-name "Python (DataCenterIQ)"
```

Open the notebook:

```text
notebooks/DataCenterIQ_Analysis.ipynb
```

Select:

```text
Python (DataCenterIQ)
```

Then run the notebook from top to bottom.

---

## 📂 Dataset

Place the AMD dataset at:

```text
data/amd_datacenter_gpus.csv
```

The notebook automatically looks for the dataset in the project structure.

After cleaning and standardization, the notebook can generate:

```text
data/amd_datacenter_gpus_clean.csv
```

---

## ▶️ Run the Streamlit Dashboard

From the project root:

```bash
streamlit run app.py
```

Streamlit will start the local dashboard.

Typically it will be available at:

```text
http://localhost:8501
```

---

## 🔎 Example Analysis

The project can investigate relationships such as:

```text
GPU Architecture
        │
        ├── Compute Performance
        │
        ├── Memory Capacity
        │
        ├── Memory Bandwidth
        │
        ├── Power Consumption
        │
        └── Process Node
                 │
                 ↓
        Data Center Efficiency
```

This provides a foundation for thinking about GPU infrastructure beyond individual benchmark numbers.

---

## 💡 Future Development

DataCenterIQ can be expanded into a broader **AI Infrastructure Intelligence Platform**.

Potential future features:

### Infrastructure Cost Modeling

Estimate:

```text
GPU Cost
+ Electricity
+ Cooling
+ Rack Infrastructure
+ Utilization
= Estimated Infrastructure Cost
```

### GPU TCO Analysis

Build a total-cost-of-ownership model for accelerator deployments.

### Energy Efficiency

Estimate:

```text
Performance / Watt
Performance / Dollar
Performance / Rack
```

### AI Workload Modeling

Compare GPUs for workloads such as:

- LLM inference
- LLM training
- Computer vision
- HPC
- Scientific computing

### Infrastructure Optimization

Explore:

- GPU utilization
- Rack density
- Cooling requirements
- Power constraints
- Accelerator selection

### Future AI Infrastructure

Potential extensions include:

- GPU cluster analysis
- AI data-center cost optimization
- Accelerator utilization monitoring
- Carbon/energy analysis
- GPU fleet optimization
- AI infrastructure forecasting

---

## 🧭 Project Direction

DataCenterIQ is intended to evolve from a GPU specification analysis project into a broader exploration of:

> **How can data and AI be used to design more efficient computing infrastructure?**

The long-term direction is to study the relationship between:

```text
Hardware
   ↓
Compute
   ↓
Memory
   ↓
Power
   ↓
Cooling
   ↓
Infrastructure
   ↓
Cost
   ↓
AI Workloads
```

---

## ⚠️ Limitations

The analysis is dependent on the quality and completeness of the source dataset.

Performance-per-watt calculations are only performed when the dataset contains both an appropriate compute-performance field and power/TDP field.

The analysis should therefore be interpreted as **dataset-based comparative analysis**, not as an independent hardware benchmark.

---

## 📌 Status

```text
🟡 Project in Development
```

### Current

- [x] Python environment
- [x] Project structure
- [x] EDA notebook
- [x] Data cleaning workflow
- [x] GPU analysis
- [x] Architecture analysis
- [x] Memory analysis
- [x] Power analysis
- [x] Efficiency analysis
- [ ] Final Streamlit dashboard
- [ ] Dashboard deployment
- [ ] GitHub release

---

## 👨‍💻 Author

**Jayesh Aswani**

Full Stack Developer Intern | AI & Data Infrastructure Enthusiast

Interested in:

- AI infrastructure
- Data engineering
- GPU computing
- AI/ML
- Full-stack engineering
- Future computing technologies

---

## ⭐ Future Vision

DataCenterIQ starts with AMD GPU data, but the larger goal is to build tools that help answer a bigger question:

> **How do we build more efficient computing infrastructure for the next generation of AI?**

---

## 📄 License

This project is intended for educational, research, and portfolio purposes.

Check the original dataset's licensing and usage terms before redistributing the dataset.