# 🏗 Sales Data Warehouse & Analytics System

## 📌 Overview

A Star Schema-based Sales Data Warehouse built using **Python, Pandas, NumPy, and PostgreSQL**.

This project implements a complete ETL pipeline that extracts raw CSV sales data, transforms it using Pandas, loads it into PostgreSQL, and generates business KPIs using advanced SQL analytics.

---

## 🚀 Tech Stack

* Python 3.x
* Pandas
* NumPy
* PostgreSQL
* psycopg2

---

## 🏛 Architecture

```text
Raw CSV Files
      ↓
Python ETL (Pandas)
      ↓
PostgreSQL Data Warehouse
      ↓
SQL Analytics (KPIs)
      ↓
CLI Reporting
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/sales_data_warehouse.git
cd sales_data_warehouse
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available:

```bash
pip install pandas numpy psycopg2 python-dotenv
```

---

### 4️⃣ Database Setup (PostgreSQL)

Create database:

```sql
CREATE DATABASE sales_dw;
```

Update your `.env` file:

```env
DB_NAME=sales_dw
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

---

## ▶️ Running the Project

Run the CLI application:

```bash
python app.py
```

Main Menu:

```text
1. Run ETL Process
2. Revenue Analytics
3. Product Analytics
4. Customer Analytics
5. Time-Based Analytics
6. Exit
```

---

## 📊 Features

* Complete ETL Pipeline
* Star Schema Data Modeling
* Revenue, Product, Customer & Time Analytics
* Advanced SQL (Window Functions, Growth %, Running Totals)
* Indexed fact table for performance optimization
* Modular CLI-based system

---

## 🏆 Resume Highlight

> Designed and implemented a modular Sales Data Warehouse with ETL pipelines and advanced KPI reporting using Python, Pandas, NumPy, and PostgreSQL.

---

## 👨‍💻 Author

Aman Kumar
Aspiring Data Engineer

---

🔗 GitHub Repository:
(Add your repository link here after pushing)