# Health360: Comprehensive Healthcare Risk & Disease Analysis

A Tableau Public project (9 visualizations, 1 dashboard, 1 story) embedded in a small Flask web app.

- Dashboard: https://public.tableau.com/app/profile/shivam.singh2218/viz/Health360_17932068115940/Health360Dashboard
- Story: https://public.tableau.com/app/profile/shivam.singh2218/viz/Health360_17932068115940/Health360Story
- Demo Video : https://drive.google.com/file/d/1N740-avsLLOra_YkecqcoesfHuzYYbzS/view


## Dataset
`smart_healthcare_dataset.csv`: 5,000 patient records, 16 columns (age, gender, BMI, exercise level, smoking,
alcohol, blood pressure, cholesterol, glucose, fatigue, chest pain, dizziness, heart disease, diabetes, stroke,
health_risk_score). There are no missing values. `health_risk_score` is 100 in every row, so it carries no
information. A custom `Risk Points` field replaces it.

## Project procedure

### 1. Data collection and extraction
1. Loaded the CSV into Tableau Public (Connect, Text file).
2. Confirmed 5,000 rows and checked field types in the Data pane.

### 2. Data preparation (6 calculated fields)
| Field | Purpose |
|---|---|
| Age Group | Buckets age into 18-29, 30-44, 45-59, 60-79 |
| BMI Category | Underweight (<18.5), Normal (<25), Overweight (<30), Obese |
| Risk Points | Counts risk factors: BP >= 140, cholesterol >= 240, glucose >= 126, BMI >= 30, smoking, alcohol |
| Risk Level | Low (0-1), Medium (2-3), High (4+) points |
| Any Disease | "Has Disease" if heart disease, diabetes or stroke is 1 |
| High Risk Flag | 1 if Risk Level is High, else 0 (used for the KPI percentage) |

### 3. Data visualizations (9 sheets)
| # | Sheet | Type | What it shows |
|---|---|---|---|
| 1 | KPI Total Patients | KPI card | Number of patients |
| 2 | KPI Heart Disease | KPI card | Heart disease rate |
| 3 | KPI High Risk | KPI card | Share of high-risk patients |
| 4 | Line Disease by Age | Line chart | Heart disease rate by age and gender |
| 5 | Bar Heart Disease by Age Group | Horizontal bar | Heart disease rate by age group |
| 6 | Bar Diabetes by BMI | Horizontal bar | Diabetes rate by BMI category |
| 7 | Donut Risk Level | Donut | Share of Low / Medium / High risk |
| 8 | Pie Any Disease | Pie | Patients with at least one disease |
| 9 | Heatmap Age vs BMI | Heatmap | Average risk points by age group and BMI category |

### 4. Dashboard
`Health360 Dashboard` combines all 9 sheets (KPI row, line + donut + pie, two bars, heatmap) with a fixed
1200 x 1500 layout and a phone layout. The donut, both bar charts and the pie act as filters for the other sheets.

### 5. Story
`Health360 Story` has 5 scenes: (1) 22% of patients are high risk, (2) heart disease rises sharply after about
age 50, (3) nearly 88% of patients aged 60-79 have heart disease, (4) obese patients have the highest risk
scores in every age group, (5) about 36% of patients have at least one disease.

### 6. Performance testing
| Check | Result |
|---|---|
| Amount of data loaded | 5,000 rows x 16 columns (about 0.4 MB CSV), live connection to the CSV |
| Data filters used | 4 dashboard "Use as Filter" actions (donut, 2 bar charts, pie) |
| Calculated fields | 6 |
| Visualizations / graphs | 9 sheets on 1 dashboard |

### 7. Web integration (Flask)
1. Published the workbook with File, Save to Tableau Public (workbook name `Health360`).
2. Copied the embed code for the dashboard and for the story from the Share button.
3. Pasted each embed code into its own Flask template (`templates/dashboard.html`, `templates/story.html`).

## Run the Flask app
```bash
python -m venv venv
venv\Scripts\activate        # Windows  (use: source venv/bin/activate on Mac/Linux)
pip install -r requirements.txt
python app.py
```
Open http://127.0.0.1:5000

| Route | Page |
|---|---|
| `/` | Home |
| `/dashboard` | Embedded Tableau dashboard |
| `/story` | Embedded Tableau story |

## Structure
```
health360_flask/
  app.py
  requirements.txt
  templates/  base.html  index.html  dashboard.html  story.html
  static/     style.css
```
