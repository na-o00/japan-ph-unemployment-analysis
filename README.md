# Japan vs Philippines Unemployment Analysis
This project compares unemployment trends between Japan and the Philippines using historical economic data and Python.
The analysis examines unemployment rates, long-term trends, moving averages, differences between the two countries, year-to-year changes, and the statistical relationship between their unemployment rates.
The goal is to explore differences between the labor markets of two Asia-Pacific economies.

## Research Question
* How have unemployment rates changed in Japan and the Philippines over time?
* Which country generally experienced higher unemployment?
* How did the unemployment gap change over time?
* Did unemployment trends in Japan and the Philippines shift together?
* What does the correlation between the two countries suggest?

## Data
**Source**: World Bank Open Data
**Countries**: Japan, Philippines
**Indicator**: Unemployment, total (% of total labor force)

## Tools Used
* Python
* pandas
* matplotlib
* NumPy

## Analysis
### 1. Unemployment Trend Comparison
Compares annual unemployment rates between Japan and the Philippines.
### 2. Moving Average Analysis
Uses moving averages to smooth short-term fluctuations and highlight long-term labor-market trends.
### 3. Unemployment Gap
Calculates:
**Japan Unemployment - Philippines Unemployment**
This shows the difference in  unemployment rates between the two countries.
### 4. Growth Rate Analysis
Examines year-to-year changes in unemployment.
### 5. Ratio Analysis
Compares the relative unemployment rates of the two countries.
### 6. Correlation Analysis
Uses a scatter plot, the correlation coefficient, and a regression line to examine whether unemployment rates in Japan and the Philippines tend to move together.

## Key Findings
* The Philippines generally experienced higher unemployment rates than Japan throughout much of the observed period.
* The unemployment gap between the two countries varied over time.
* Japan's unemployment rate remained relatively low compared with the Philippines during many periods.
* The correlation between Japanese and Philippine unemployment was approximately **-0.03**, indicating essentially no linear relationship in this dataset.
* The regression slope was approximately **-0.07**, suggesting that there was very little linear association between the two unemployment rates.
* The results suggest that the two countries' labor markets were influenced by different domestic economic conditions rather than consistently moving together.

## Visualization
### Unemployment Trends
![Unemployment Analysis](unemployment_analysis.png)
The visualization includes unemployment trends, moving averages, the unemployment gap, growth rates, ratios, and the relationship between Japan and the Philippines.

## Limitations
Correlation does not imply causation.

The analysis only measures the statistical relationship between the two unemployment rates and does not identify the underlying causes of unemployment.

Growth-rate and ratio calculations can also become unstable when values are close to zero.

Unemployment statistics may also be affected by differences in national definitions, labor-force surveys, and data collection methods.

## Future Improvements
* Compare youth unemployment rates
* Compare labor-force participation rates
* Add ASEAN country comparisons
* Examine the effects of major economic events
* Add GDP growth to investigate Okun's Law
* Build an interactive Power BI dashboard

## What I learned
Through this project, I practiced:
* Working with real-world labor-market data
* Data cleaning and organizing using pandas
* Creating time-series visualizations
* Calculating moving averages
* Comparing economic indicators between countries
* Calculating correlations and regression  relationships
* Interpreting statistical results and their  limitations

## Future Project
This project will eventually be integrated with my other Japan–Philippines economic analyses into a broader economic comparison dashboard.
