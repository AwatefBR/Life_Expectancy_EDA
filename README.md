# LifeExpectancyProject
In this repository you will find an app able to predict the Life Expectancy acoording to various features:

1.Country : Country
2.Year: Year
3.Status : Developed or Developing
4.Life expectancy in age : this is our goal, what we want to predict
5.Adult Mortality Rates of both sexes (probability of dying between 15 and 60 years per 1000 population)
6.Number of Infant Deaths per 1000 population
7.Alcohol - Recorded per capita (15+) alcohol consumption (in liters of pure alcohol)
8.Percentage expenditure: Expenditure on health as a percentage of Gross Domestic Product per capita(%)
9.Hepatitis B immunization coverage among 1-year-olds (%)
10.Measles - number of reported cases per 1000 population
12.Average Body Mass Index of entire population
12.Number of under-five deaths per 1000 population
13.Polio (Pol3) immunization coverage among 1-year-olds (%)
14.General government expenditure on health as a percentage of total government expenditure (%)
15.Diphtheria tetanus toxoid and pertussis (DTP3) immunization coverage among 1-year-olds (%)
16.Deaths per 1000 live births HIV/AIDS (0-4 years)
17.Gross Domestic Product per capita (in USD)
18.Population of the country
19.Prevalence of thinness among children and adolescents for Age 1 to 19 (%)
20.Prevalence of thinness among children for Age 5 to 9 (%)
21.Human Development Index in terms of income composition of resources (index ranging from 0 to 1)
22.Number of years of Schooling (years)

- Differents algorithms have been tested and evaluated.
- A Random Forest Regressor was selected according to the metrics chosen, the Mean Absolute Error
- Why use the Mean Absolute Error (MAE) as our metric for models evaluation ?

MAE is used for regression tasks where the goal is to predict a continuous numerical value.

For Regression Tasks, MAE measures the average absolute difference between the predicted values and the actual values.

It provides a measure of the average magnitude of errors made by the model.

Main advantages :

It is less sensitive to outliers compared to other regression metrics like Mean Squared Error (MSE).

MAE is reported in the same scale as the target variable.

MAE is less sensitive to outliers and provides a more robust measure of average prediction error.

- The model was saved as a pickle file in the 'model' folder.
- To find more about the EDA and the data preprocessing, check the ipynb file : LifeExpectancyEDA+Models.ipynb
- The cleaned and preprocessed data have been saved in a csv file : data_train_preprocessed.csv

Deploying the app locally, here are the following steps to do on your terminal:
- create a virtual environment after saving this repository in a folder of your choice :
- mkdir life_expectancy
- python -m venv .venv
- install the required libraries : pip install -r requirements.txt
- Once this done, open Docker, buil the image and run it :
- docker build -t my-app .
- docker run -p 5000:5000 my-app
- Finally, make sur you're at the root of the project folder : puthon app/app.py
- Copy paste the URL given by the terminal on your Web Browser
- Play with the app ! 
