from flask import render_template, request, jsonify
from sklearn.externals import joblib
from app import app

def extract_features(data):
    country = data.get('country')
    year = data.get('year')
    status = data.get('status')
    adultmortality = data.get(adultmortality)
    infantdeaths = infantdeaths,
    alcohol = data.get('alcohol')
    percentageExpenditure=data.get(percentageExpenditure)
    hepatitisB=data.get(hepatitisB)
    measles= data.get(measles)
    bmi=data.get(bmi)
    underFiveDeaths=data.get(underFiveDeaths)
    polio=data.get(polio)
    totalExpenditure=data.get(totalExpenditure)
    diphtheria=data.get(diphtheria)
    hivAids=data.get(hivAids)
    gdp=data.get(gdp)
    population=data.get(population)
    thinness1to19years=data.get(thinness1to19years)
    thinness5to9years=data.get(thinness5to9years)
    incomeComposition=data.get(incomeComposition)
    schooling=data.get(schooling)
    return {
        'country': country,
        'year': year,
        'status': status,
        'adultmortality' : adultmortality,
        'infantdeaths' : infantdeaths,
        'alcohol' : alcohol, 
        'percentageExpenditure' : percentageExpenditure,
        'hepatitisB': hepatitisB, 
        'measles': measles, 
        'bmi' : bmi,
        'underFiveDeaths' : underFiveDeaths,
        'polio' : polio, 
        'totalExpenditure' : totalExpenditure, 
        'diphtheria' : diphtheria,
        'hivAids'  :hivAids, 
        'gdp' : gdp, 
        'population' : population, 
        'thinness1to19years' : thinness1to19years,
        'thinness5to9years' : thinness5to9years, 
        'incomeComposition' : incomeComposition,
        'schooling'  : schooling
    }


model = joblib.load('model/RFRegressor_trained.pkl')

@app.route('/')
def index():
    countries = ['Afghanistan', 'Albania', 'Algeria', 'Angola', 'Antigua and Barbuda', 'Argentina',
       'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh',
       'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan',
       'Bolivia (Plurinational State of)', 'Bosnia and Herzegovina', 'Botswana', 'Brazil',
       'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cambodia',
       'Cameroon', 'Canada', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia',
       'Comoros', 'Congo', 'Cook Islands', 'Costa Rica', 'Croatia', 'Cuba', 'Cyprus',
       'Czechia', "Côte d'Ivoire", "Democratic People's Republic of Korea",
       'Democratic Republic of the Congo', 'Denmark', 'Djibouti', 'Dominica',
       'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea',
       'Eritrea', 'Estonia', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia',
       'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea',
       'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India',
       'Indonesia', 'Iran (Islamic Republic of)', 'Iraq', 'Ireland', 'Israel', 'Italy',
       'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Kuwait',
       'Kyrgyzstan', "Lao People's Democratic Republic", 'Latvia', 'Lebanon', 'Lesotho',
       'Liberia', 'Libya', 'Lithuania', 'Luxembourg', 'Madagascar', 'Malawi', 'Malaysia',
       'Maldives', 'Mali', 'Malta', 'Mauritania', 'Mauritius', 'Mexico',
       'Micronesia (Federated States of)', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco',
       'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand',
       'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama',
       'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar',
       'Republic of Korea', 'Republic of Moldova', 'Romania', 'Russian Federation', 'Rwanda',
       'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'Samoa',
       'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles',
       'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia',
       'South Africa', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland',
       'Sweden', 'Switzerland', 'Syrian Arab Republic', 'Tajikistan', 'Thailand',
       'The former Yugoslav republic of Macedonia', 'Timor-Leste', 'Togo', 'Tonga',
       'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Uganda', 'Ukraine',
       'United Arab Emirates', 'United Kingdom of Great Britain and Northern Ireland',
       'United Republic of Tanzania', 'United States of America', 'Uruguay', 'Uzbekistan',
       'Vanuatu', 'Venezuela (Bolivarian Republic of)', 'Viet Nam', 'Yemen', 'Zambia',
       'Zimbabwe' ]
    years = list(range(2000, 2016))
    status = ['Developed', 'Developing']
    adultmortality = list(range(1, 1000, 50))
    infantdeaths = list(range(0, 2000, 100))
    alcohol = list(range(0, 20, 0.5))
    percentageExpenditure = list(range(0, 20000, 500))
    hepatitisB =list(range(1, 100))
    measles = ''
    bmi =list(range(1,100))
    underFiveDeaths =list(range(0, 2500, 250))
    polio =list(range(1, 100))
    totalExpenditure =list(range(0, 20, 0.5))
    diphtheria =list(range(1, 100))
    hivAids =list(range(1, 60))
    gdp = ''
    population = ''
    thinness1to19years = list(range(0, 30))
    thinness5to9years =list(range(0, 30))
    incomeComposition =list(range(0, 1, 0.5))
    schooling =list(range(1,25,1))
    return render_template('index.html',countries=countries, years=years, status = status, 
                           adultmortality = adultmortality, infantdeaths =infantdeaths,
                           alcohol = alcohol, percentageExpenditure=percentageExpenditure,
                           hepatitisB=hepatitisB, measles= measles, bmi=bmi,underFiveDeaths=underFiveDeaths,
                           polio=polio, totalExpenditure=totalExpenditure, diphtheria=diphtheria,
                           hivAids=hivAids, gdp=gdp, population=population, thinness1to19years=thinness1to19years,
                           thinness5to9years=thinness5to9years, incomeComposition=incomeComposition,
                           schooling=schooling)



@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = extract_features(data) 
    prediction = model.predict([features])[0]
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)