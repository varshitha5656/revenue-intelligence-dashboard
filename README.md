# revenue-intelligence-dashboard
Revenue Intelligence Dashboard: Sales pattern analysis &amp; business insights using Python and Streamlit.

## Day 1 Progress
- Added dataset (sales.csv) to the data folder.
- Loaded data in eda.ipynb and confirmed structure.
- Converted OrderDate to datetime and created Month, Profit, and ProfitMargin columns.
- Generated Monthly Revenue Trend chart.
- Exported chart to images/monthly_revenue.png.
## Day 2 Progress
	•	Added new calculated column: Profit (Sales - Cost)
	•	Added Category-wise Revenue chart
	•	Added Region-wise Profit chart
	•	Added Profit Margin calculations
	•	Exported charts to images/ folder
	•	Updated EDA notebook with additional insights
## Day 3 Progress
	•	Created a basic Streamlit app (app.py) to display analysis results.
	•	Loaded sales dataset inside Streamlit using pandas.
	•	Displayed Monthly Revenue Trend chart in the app.
	•	Added product/category-level revenue insights.
	•	Calculated Profit and Profit Margin for better business understanding.
	•	Shown dataset preview inside the dashboard for clarity.
	•	Ran the Streamlit app locally and verified output in browser.
## Day 4 Progress
- Built initial Streamlit dashboard using app.py
- Added category-based filtering using sidebar
- Connected Pandas data processing with Streamlit UI
- Displayed interactive Monthly Revenue Trend
- Added live dataset preview for validation
## Day 5 Progress
- Added metric toggle (Sales / Profit)
- Implemented KPI cards for total metric and total orders
- Enabled category and region-based filtering
- Made monthly trend chart reactive to selected metric
- Improved dashboard interactivity using Streamlit components
## Day 6 Progress
- Added dynamic category and region filters
- Implemented metric toggle (Sales / Profit)
- Fixed filtering logic for "All" selections
- Stabilized monthly aggregation logic
- Debugged runtime NameError and state issues
