# 🏗 Sales Data Warehouse & Analytics System

## 📌 Overview

This project is a **Star Schema-based Sales Data Warehouse** built using:

* Python
* Pandas
* NumPy
* PostgreSQL

It simulates a real-world Data Engineering workflow where raw sales data is extracted from CSV files, transformed using Pandas, loaded into PostgreSQL, and analyzed using advanced SQL queries.

---

## 🎯 Objective

To design and implement a complete ETL pipeline and analytics system capable of answering business questions such as:

* Total revenue
* Top-selling products
* Best customers
* Sales by region
* Monthly growth trends
* Profit margins
* Customer retention insights

---

## 🏛 Architecture

```text
Raw CSV Files
      ↓
Python ETL (Pandas + NumPy)
      ↓
PostgreSQL Data Warehouse
      ↓
SQL Analytics Queries
      ↓
Business Insights (CLI Reporting)
```

---

## 🔄 ETL Process

**Extract**

* Read CSV files using Pandas

**Transform**

* Remove nulls and duplicates
* Standardize date formats
* Calculate revenue and profit

**Load**

* Insert cleaned data into PostgreSQL
* Map foreign keys
* Populate fact table

---

## 📊 Analytics Implemented

* Revenue Analytics (Total, Monthly, Regional, Category-wise)
* Product Analytics (Top Products, Profit Margin, Category Performance)
* Customer Analytics (Top Customers, Repeat Customers, Revenue per Customer)
* Time-Based Analytics (Monthly Growth %, Running Total, Moving Average)
* Advanced SQL with Window Functions (`LAG()`, `SUM() OVER()`)

---

## 🖥 CLI Features

```text
1. Run ETL Process
2. Revenue Analytics
3. Product Analytics
4. Customer Analytics
5. Time-Based Analytics
6. Exit
```

---

## 🚀 Key Skills Demonstrated

* Star Schema Data Modeling
* ETL Pipeline Development
* SQL Aggregations & Window Functions
* Foreign Keys & Indexing
* Modular Python Project Structure

---

## 🏆 Resume Highlight

> Designed and implemented a modular Sales Data Warehouse with ETL pipelines and advanced KPI reporting using Python, Pandas, NumPy, and PostgreSQL.

---

## 👨‍💻 Author

Aman Kumar
Aspiring Data Engineer