# 📊 Order Channel Performance & Market Share Analytics

### SkyCity Auckland Restaurants & Bars

## 🚀 Project Overview

This project analyzes multi-channel ordering performance across restaurants in **SkyCity Auckland**, focusing on how different order channels contribute to revenue, volume, and strategic positioning.

With the rise of delivery aggregators like Uber Eats and DoorDash, restaurants must optimize their channel mix to balance **profitability, reach, and operational risk**.

---

## 🎯 Objectives

### 🔹 Primary Objectives

- Quantify total order volume by channel
- Measure channel market share
- Identify dominant channels across Auckland subregions

### 🔹 Secondary Objectives

- Analyze channel mix by cuisine and segment
- Identify aggregator dependency risks
- Evaluate channel diversification strategies

---

## 📂 Dataset Description

The dataset includes:

- Restaurant details (Name, Cuisine, Segment, Subregion)
- Order volume across channels:
  - In-Store
  - Uber Eats
  - DoorDash
  - Self-Delivery

- Revenue & Profit metrics per channel
- Operational metrics:
  - AOV (Average Order Value)
  - Growth Factor
  - COGS, OPEX, Commission Rates
  - Delivery Cost & Radius

---

## 🔍 Exploratory Data Analysis (EDA)

Key analysis performed:

- ✅ Data validation & consistency checks
- ✅ Channel-wise order aggregation
- ✅ Market share computation
- ✅ Subregion-based channel comparison
- ✅ Cuisine & segment-level analysis
- ✅ Dependency risk identification
- ✅ Channel diversification scoring

---

## 📊 Key Insights

- 📌 Delivery aggregators dominate overall order volume
- 📌 Central Auckland shows strong in-store presence
- 📌 Fast-food cuisines rely heavily on aggregators
- 📌 Many restaurants show **>70% dependency** on third-party platforms
- 📌 Balanced channel mix improves operational resilience

---

## 📈 Visualizations

The project includes:

- Channel market share (Pie Chart)
- Orders by channel (Bar Chart)
- Subregion channel distribution (Stacked Bar)
- Cuisine vs channel mix
- Aggregator dependency distribution
- AOV vs Orders (Scatter Plot)
- Profit by channel

---

## ⚠️ Risk Analysis

Restaurants are flagged as **high-risk** if:

- Aggregator Dependence > 70%

Risks include:

- High commission costs
- Reduced profit margins
- Platform dependency

---

## 📊 KPIs Used

- Channel Order Share (%)
- Aggregator Dependence Index
- In-Store Reliance Ratio
- Channel Diversification Score
- Subregion Channel Dominance

---

## 🖥️ Streamlit Dashboard

An interactive dashboard is built using **Streamlit** with:

### 🔹 Features

- Subregion filter
- Cuisine & segment selection
- Channel-wise performance visualization
- Dependency risk indicators
- KPI summary panel

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/channel-analytics.git
cd channel-analytics
```

### 2️⃣ Install Dependencies

```bash
pip install pandas matplotlib plotly streamlit
```

### 3️⃣ Run the Dashboard

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
├── data/
│   └── SkyCity Auckland Restaurants & Bars.csv
├── notebooks/
│   └── EDA.ipynb
├── app.py
├── requirements.txt
└── README.md
```

---

## 🧠 Strategic Recommendations

- ✅ Reduce over-dependence on aggregators
- ✅ Promote self-delivery for better margins
- ✅ Optimize channel mix based on location
- ✅ Leverage in-store strengths for cafes
- ✅ Use data-driven channel allocation

---

## 🌟 Future Enhancements

- 📈 Predictive analytics (channel demand forecasting)
- 🤖 Machine learning for profit optimization
- 🌐 Live dashboard deployment (Streamlit Cloud)
- 📊 Real-time data integration

---

## 👨‍💻 Author

**ANANT SINGH**
Frontend Developer | Data Analytics Enthusiast

---

## 📜 License

This project is for academic and internship purposes.
