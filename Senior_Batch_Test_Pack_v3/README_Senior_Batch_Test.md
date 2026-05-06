# Senior Batch Assessment Pack — Final Version

## 1) Exam overview
- **Batch:** Senior Batch
- **Total duration allowed:** **2 hours 30 minutes**
- **Recommended working time:** around **2 hours**
- **Extra buffer:** around **30 minutes** for testing, saving outputs, and creating the final zip
- **Total questions:** **10**
- **Total marks:** **100**

This assessment is based on material from:
1. Python Foundation
2. pandas
3. Data Visualization with Matplotlib and Seaborn

---

## 2) What students must submit

Create **one folder** using this format:

`seniorbatch_<studentname>_<rollno>`

Inside that folder, keep:

### A. One notebook
`seniorbatch_<studentname>_<rollno>.ipynb`

### B. Output files generated during the test
- `q3_sector_profit_summary.csv`
- `q4_top_companies_efficiency.csv`
- `q5_food_revenue.csv`
- `q6_top_customers.csv`
- `q7_college_salary.csv`
- `q8_team_position_salary.csv`
- `q9_top5_lodging_revenue.png`
- `q10_marketsegment_booking_mix.png`

### C. Important note
Do **not** edit, rename, or overwrite the original dataset files inside the `datasets` folder.

After completing the test:
1. keep only your notebook and required outputs inside your submission folder
2. compress that folder into **one zip file**
3. submit that zip file

---

## 3) Allowed tools
Students may use:
- Python
- pandas
- matplotlib
- seaborn

No external datasets should be used.

---

## 4) General rules
1. Use **Jupyter Notebook (`.ipynb`) only**.
2. In the **first notebook cell**, write:
   - student name
   - roll number
   - batch name
3. Solve the questions in order: **Q1 to Q10**.
4. Every question must contain:
   - the code used
   - visible output in the notebook
5. Save all required CSV and PNG files in the **same folder as the notebook**.
6. Do not hardcode final answers without showing the code used to derive them.
7. Charts must contain:
   - a meaningful title
   - labeled axes
   - readable category names
8. The notebook should run from top to bottom without errors.

---

## 5) Dataset paths to use

### pandas datasets
- `datasets/pandas/fortune1000.csv`
- `datasets/pandas/restaurant_foods.csv`
- `datasets/pandas/restaurant_week_1_sales.csv`
- `datasets/pandas/restaurant_week_2_sales.csv`
- `datasets/pandas/nba.csv`

### visualization dataset
- `datasets/dataviz/HotelCustomersDataset.xlsx`

---

# 6) Question paper

## Q1. Python Function — Next Palindrome (8 marks)
Write a function:

```python
def next_palindrome(num):
    ...
```

Return the **next palindrome strictly greater than** the input number.

Test your function using:
```python
next_palindrome(90)
next_palindrome(123)
next_palindrome(808)
```

---

## Q2. Python Function — Frequency Dictionary (8 marks)
Write a function:

```python
def word_frequency(text):
    ...
```

Rules:
- convert the text to lowercase
- remove commas and full stops
- split into words
- return a dictionary of word counts

Test using:
```python
sample_text = "Python is simple. Python is powerful, and Python is fun."
```

Display the final dictionary clearly.

---

## Q3. Fortune 1000 — Sector Profit Summary (10 marks)
Use: `datasets/pandas/fortune1000.csv`

Tasks:
1. Load the CSV.
2. Keep only rows where:
   - `Profits > 0`
   - `Revenue >= 50000`
3. Group by `Sector`.
4. Create these output columns:
   - `company_count`
   - `avg_revenue`
   - `total_profits`
5. Sort by:
   - `total_profits` descending
   - then `avg_revenue` descending
6. Save the **top 5 rows** to:
   - `q3_sector_profit_summary.csv`

---

## Q4. Fortune 1000 — Company Efficiency Score (10 marks)
Use: `datasets/pandas/fortune1000.csv`

Tasks:
1. Load the CSV.
2. Keep only rows where:
   - `Employees > 0`
   - `Revenue > 0`
3. Create a new column:
   - `revenue_per_employee = Revenue / Employees`
4. Keep these columns:
   - `Company`
   - `Sector`
   - `Revenue`
   - `Employees`
   - `revenue_per_employee`
5. Sort by `revenue_per_employee` descending.
6. Save the **top 10 rows** to:
   - `q4_top_companies_efficiency.csv`

---

## Q5. Restaurant Data — Food Revenue Summary (10 marks)
Use:
- `datasets/pandas/restaurant_foods.csv`
- `datasets/pandas/restaurant_week_1_sales.csv`
- `datasets/pandas/restaurant_week_2_sales.csv`

Tasks:
1. Combine week 1 and week 2 sales.
2. Merge with the food master file.
3. Create a summary by `Food Item` with:
   - `orders`
   - `unit_price`
   - `revenue`
4. Sort by:
   - `orders` descending
   - then `revenue` descending
5. Save the **top 5 rows** to:
   - `q5_food_revenue.csv`

---

## Q6. Restaurant Data — Top Customers by Spend (10 marks)
Use the same 3 restaurant datasets.

Tasks:
1. Combine both weekly sales files.
2. Merge with the food master file.
3. Create a customer-level summary with:
   - `Customer ID`
   - `total_orders`
   - `total_spend`
4. Sort by:
   - `total_spend` descending
   - then `total_orders` descending
5. Save the **top 10 customers** to:
   - `q6_top_customers.csv`

---

## Q7. NBA Data — College Salary Analysis (10 marks)
Use: `datasets/pandas/nba.csv`

Tasks:
1. Remove rows where `Salary` or `College` is null.
2. Group by `College`.
3. Calculate:
   - `players`
   - `avg_salary`
4. Keep only colleges with at least **5 players**.
5. Sort by `avg_salary` descending.
6. Save the **top 5 rows** to:
   - `q7_college_salary.csv`

---

## Q8. NBA Data — Team and Position Salary Matrix (10 marks)
Use: `datasets/pandas/nba.csv`

Tasks:
1. Remove rows where `Salary` is null.
2. Create a pivot table with:
   - `index = Team`
   - `columns = Position`
   - `values = Salary`
   - `aggfunc = mean`
3. Fill missing values with 0.
4. Round values to 2 decimals.
5. Save the full pivot table to:
   - `q8_team_position_salary.csv`

---

## Q9. Hotel Data — Top 5 Nationalities by Lodging Revenue (12 marks)
Use: `datasets/dataviz/HotelCustomersDataset.xlsx`

Tasks:
1. Group by `Nationality`.
2. Compute total `LodgingRevenue`.
3. Select the **top 5 nationalities** by total lodging revenue.
4. Create a bar chart.
5. Save the chart as:
   - `q9_top5_lodging_revenue.png`

Chart rules:
- chart title required
- x-axis must show nationality
- y-axis must show total lodging revenue
- labels should be readable

---

## Q10. Hotel Data — Market Segment Booking Mix (12 marks)
Use: `datasets/dataviz/HotelCustomersDataset.xlsx`

Tasks:
1. Group by `MarketSegment`.
2. Calculate:
   - total `BookingsCheckedIn`
   - total `BookingsCanceled`
   - total `BookingsNoShowed`
3. Create one chart that clearly compares these 3 values for each market segment.
4. Save the chart as:
   - `q10_marketsegment_booking_mix.png`

In the **final markdown cell** of the notebook, write **3 business insights** based on **both Q9 and Q10 together**.

---

## 7) Suggested time split
- Q1–Q2: 20 minutes
- Q3–Q6: 55 minutes
- Q7–Q8: 25 minutes
- Q9–Q10: 35 minutes
- Final testing and packaging: 15 minutes

---

## 8) Final checklist before submission
- notebook file name is correct
- all 8 required output files are present
- notebook runs without errors
- charts are visible and saved
- final zip contains only your work folder

Good luck.
