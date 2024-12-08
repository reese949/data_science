# SQL Sales Analysis for Northwind Traders

**Created By:** Reese Oliver  
**Date:** December 4, 2024

## Introduction

Welcome to the SQL Data Analysis project for **Northwind Traders**, an international gourmet food distributor. In this project, we delve into Northwind’s sales data to uncover key insights that will help the company's management make data-driven decisions. By examining sales patterns, performance trends, and operational metrics, we aim to provide actionable insights that will accelerate business growth and sharpen the company's competitive edge.

### Core Business Questions

This analysis aims to answer several key business questions, including:

- **Profit Margin Analysis:** Identifying the most profitable products and uncovering pricing inefficiencies.
- **Product Lifecycle Analysis:** Recognizing products that are reaching the end of their lifecycle or discovering emerging products.
- **Employee Performance Evaluation:** Assessing employee productivity to optimize team effectiveness.
- **Product and Category Performance Analysis:** Enhancing inventory management and refining marketing strategies.
- **Customer Purchase Behavior Analysis:** Targeting high-value customers with personalized promotions to boost sales.

To address these questions, we will be using SQL to calculate running totals, compute averages, rank items, and analyze growth rates, all of which are essential techniques for extracting valuable business insights.

## Getting Started

### 1. Installing PostgreSQL and Downloading the Northwind Database

To get started with this project, you will need to install **PostgreSQL** and download the Northwind Traders database. Follow the steps below:

- **Installing PostgreSQL:**  
  [Click here for the installation guide](#) to install PostgreSQL on your computer.

- **Downloading the Northwind Database:**  
  After installing PostgreSQL, you can download the Northwind Traders database from [this GitHub repository](https://github.com/pthom/northwind_psql/tree/master). This guide will walk you through connecting to the database in PostgreSQL.

### 2. Connecting Jupyter Notebook to PostgreSQL

To run SQL queries in a Jupyter Notebook, we use the **ipython-sql** package. Follow these steps:

1. Open a terminal or Jupyter notebook.
2. Install the `ipython-sql` package by running the following command:
   ```bash
   !pip install ipython-sql
3. This will enable you to execute SQL queries directly in your Jupyter Notebook and view the results interactively.

### 3. Running the Magic Command

Once you have ipython installed, you can execute SQL queries with the magic `%sql` command. By loading this extension, you can use the SQL magic commands, such as `%sql` and `%%sql`, to run SQL queries directly in the Jupyter Notebook cells. <br>

**Keep in mind:**
1. For **single line queries**, use `%sql`
2. For **multiple-line queries**, use `%%sql`