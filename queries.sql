CREATE VIEW todays_currencies as
SELECT *
FROM currency
WHERE currency_date = CURRENT_DATE;

-- Only aplicable to sqlite
SELECT 
	min(currency_rate), 
	max(currency_rate), 
	avg(currency_rate), 
	strftime('%Y-%m', currency_date) AS year_month
FROM currency
group by year_month
ORDER by year_month