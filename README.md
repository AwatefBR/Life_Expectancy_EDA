# Life Expectancy

### Welcome to the Life Expectancy EDA! In this repository, you'll find various datasets and a notebook. The notebook comprehensively explores the datasets through data visualization techniques, providing insightful exploratory data analysis (EDA) visualizations. Additionally, it includes the training of predictive models for life expectancy based on the analyzed data.

#### Features in the datasets
- Country: The country for which the prediction is made.
- Year: The year of observation.
- Status: Whether the country is developed or developing.
- Life Expectancy: The target variable to predict.
- Adult Mortality Rates: Probability of dying between 15 and 60 years per 1000 population for both sexes.
- Number of Infant Deaths: Number of infant deaths per 1000 population.
- Alcohol Consumption: Recorded per capita (15+) alcohol consumption in liters of pure alcohol.
- Percentage Expenditure: Expenditure on health as a percentage of GDP per capita.
- Hepatitis B Immunization: Coverage among 1-year-olds in percentage.
- Measles Cases: Number of reported cases per 1000 population.
- Average Body Mass Index: Average BMI of the entire population.
- Number of Under-Five Deaths: Number of under-five deaths per 1000 population.
- Polio Immunization: Pol3 immunization coverage among 1-year-olds in percentage.
- Government Health Expenditure: General government expenditure on health as a percentage of total government expenditure.
- Diphtheria, Tetanus, Pertussis Immunization: DTP3 immunization coverage among 1-year-olds in percentage.
- Deaths due to HIV/AIDS: Deaths per 1000 live births (0-4 years).
- Gross Domestic Product per Capita: GDP per capita in USD.
- Population: Population of the country.
- Prevalence of Thinness among Children and Adolescents: For age 1 to 19 in percentage.
- Prevalence of Thinness among Children: For age 5 to 9 in percentage.
- Human Development Index (HDI): In terms of income composition of resources (index ranging from 0 to 1).
- Years of Schooling: Number of years of schooling.

### Various algorithms have been tested and evaluated, and a Random Forest Regressor was selected based on the Mean Absolute Error (MAE) metric. 

#### Why use MAE as our metric?
- MAE is chosen for its robustness and sensitivity to prediction errors.
- MAE is suitable for regression tasks where the goal is to predict continuous numerical values.
- It measures the average absolute difference between predicted and actual values, providing a robust measure of average prediction error. 

#### Its advantages include:

- Less sensitivity to outliers compared to Mean Squared Error (MSE).
- Reports errors in the same scale as the target variable.

## Additional Information:
- The trained model is saved as a pickle file in the 'model' folder.
- For details on Exploratory Data Analysis (EDA) and data preprocessing, refer to the notebook: LifeExpectancyEDA+Models.ipynb.
- Cleaned and preprocessed data is stored in the CSV file: data_train_preprocessed.csv.

