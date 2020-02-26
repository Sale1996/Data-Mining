import utils
import prediction_algorithms
import pandas as pd
import validation_methods


def prediktuj_data_set(x_train, x_test, y_train, y_test):
    # popunjavamo NaN vrednosti sa srednjom vrednosti dataseta jer algoritam ne dozvoljava NaN vrednosti
    x_train_without_nan = x_train.fillna(x_train.mean())
    x_test_without_nan = x_test.fillna(x_test.mean())
    y_train_without_nan = y_train.fillna(y_train.mean())
    y_test_without_nan = y_test.fillna(y_test.mean())

    # treniranje predikcionog modela
    x_Boost_regression = prediction_algorithms.XGBoost_regression(pd.get_dummies(x_train_without_nan),
                                                                  y_train_without_nan)
    xBoost_prediction = x_Boost_regression.predict(
        pd.get_dummies(x_test_without_nan))  # za predikciju neophono je da prosledimo 2d array, odnosno ceo dataset wtf

    # testiranje na gresku
    MSE = validation_methods.mean_squared_error_metrics(y_test_without_nan, xBoost_prediction)
    r2_error = validation_methods.r2_metrics(y_test_without_nan, xBoost_prediction)
    print("X boost regression errors:")
    print("MSE: ")
    print(MSE)
    print("R2 ERROR: ")
    print(r2_error)

    elastic_regression = prediction_algorithms.elastic_regression(pd.get_dummies(x_train_without_nan),
                                                                  y_train_without_nan, 0.01)
    elastic_regression_prediction = elastic_regression.predict(x_test_without_nan)

    MSE = validation_methods.mean_squared_error_metrics(y_test_without_nan, elastic_regression_prediction)
    r2_error = validation_methods.r2_metrics(y_test, elastic_regression_prediction)
    print("Elastic net regression errors:")
    print("MSE: ")
    print(MSE)
    print("R2 ERROR: ")
    print(r2_error)


'''
AGRICULTURAL METHANE EMISSION DATA SET
'''

agricultural_methane_emission = utils.read_exel(
    "/home/sale/Desktop/GitHubSIAP/Data-Mining/tabele1990-2017/treba_regresija/agricultural_methane_emission.xlsx")
# cist ispis da proverimo da li je tabela dobro ucitana.
print(agricultural_methane_emission.head())
# enkodujemo x_data... sa one hot encodingom, jer sadrzi kolonu year koja je string kategorickog tipa
x_data_encoded_agricultural_methane_emission = pd.get_dummies(agricultural_methane_emission[['Country Code', 'Year']])
x_train_agricultural_methane_emission, x_test_agricultural_methane_emission, y_train_agricultural_methane_emission, y_test_agricultural_methane_emission = utils.train_test_split_data(
    x_data_encoded_agricultural_methane_emission,
    agricultural_methane_emission[
        ['Agricultural methane emissions (% of total)']],
    0.2)

'''
CORRUPTION PERCEPTIONS INDEX DATA SET
'''
corruption_perceptions_index = utils.read_exel(
    "/home/sale/Desktop/GitHubSIAP/Data-Mining/tabele1990-2017/treba_regresija/corruption_perceptions_index.xlsx")
# cist ispis da proverimo da li je tabela dobro ucitana.
print(corruption_perceptions_index.head())
# enkodujemo x_data... sa one hot encodingom, jer sadrzi kolonu year koja je string kategorickog tipa
x_data_encoded_corruption_perceptions_index = pd.get_dummies(corruption_perceptions_index[['Country Code', 'Year']])
x_train_corruption_perceptions_index, x_test_corruption_perceptions_index, y_train_corruption_perceptions_index, y_test_corruption_perceptions_index = utils.train_test_split_data(
    x_data_encoded_corruption_perceptions_index,
    corruption_perceptions_index[
        ['Corruption index']],
    0.2)

'''
CORRUPTION PERCEPTION INDEX 2 DATASET
'''

coruption_perception_index_2 = utils.read_exel(
    "/home/sale/Desktop/GitHubSIAP/Data-Mining/tabele1990-2017/treba_regresija/CoruptionPerceptionIndex_filtered.xlsx")
# cist ispis da proverimo da li je tabela dobro ucitana.
print(coruption_perception_index_2.head())
# enkodujemo x_data... sa one hot encodingom, jer sadrzi kolonu year koja je string kategorickog tipa
x_data_encoded_coruption_perception_index_2 = pd.get_dummies(coruption_perception_index_2[['Country Code', 'Year']])
x_train_coruption_perception_index_2, x_test_coruption_perception_index_2, y_train_coruption_perception_index_2, y_test_coruption_perception_index_2 = utils.train_test_split_data(
    x_data_encoded_coruption_perception_index_2,
    coruption_perception_index_2[
        ['corruption_index']],
    0.2)

'''
DAILY PER CAPITA SUPPLY OF CALORIES DATA SET
'''

daily_per_capita_supply_of_calories = utils.read_exel(
    "/home/sale/Desktop/GitHubSIAP/Data-Mining/tabele1990-2017/treba_regresija/daily-per-capita-supply-of-calories.xlsx")
# cist ispis da proverimo da li je tabela dobro ucitana.
print(daily_per_capita_supply_of_calories.head())
# enkodujemo x_data... sa one hot encodingom, jer sadrzi kolonu year koja je string kategorickog tipa
x_data_encoded_daily_per_capita_supply_of_calories = pd.get_dummies(daily_per_capita_supply_of_calories[['Country Code', 'Year']])
x_train_daily_per_capita_supply_of_calories, x_test_daily_per_capita_supply_of_calories, y_train_daily_per_capita_supply_of_calories, y_test_daily_per_capita_supply_of_calories = utils.train_test_split_data(
    x_data_encoded_daily_per_capita_supply_of_calories,
    daily_per_capita_supply_of_calories[
        ['Daily caloric supply (kcal/person/day)']],
    0.2)


'''
LIFE SATISFACTION DATA SET
'''
life_satisfaction = utils.read_exel(
    "/home/sale/Desktop/GitHubSIAP/Data-Mining/tabele1990-2017/treba_regresija/life_satisfaction.xlsx")
# cist ispis da proverimo da li je tabela dobro ucitana.
print(life_satisfaction.head())
# enkodujemo x_data... sa one hot encodingom, jer sadrzi kolonu year koja je string kategorickog tipa
x_data_encoded_life_satisfaction = pd.get_dummies(life_satisfaction[['Country Code', 'Year']])
x_train_life_satisfaction, x_test_life_satisfaction, y_train_life_satisfaction, y_test_life_satisfaction = utils.train_test_split_data(
    x_data_encoded_life_satisfaction,
    life_satisfaction[
        ['Happines']],
    0.2)

'''
POLITICAL REGIME UPDATED2016 DATA SET
'''
political_regime_updated2016 = utils.read_exel(
    "/home/sale/Desktop/GitHubSIAP/Data-Mining/tabele1990-2017/treba_regresija/political-regime-updated2016.xlsx")
# cist ispis da proverimo da li je tabela dobro ucitana.
print(political_regime_updated2016.head())
# enkodujemo x_data... sa one hot encodingom, jer sadrzi kolonu year koja je string kategorickog tipa
x_data_encoded_political_regime_updated2016 = pd.get_dummies(political_regime_updated2016[['Country Code', 'Year']])
x_train_political_regime_updated2016, x_test_political_regime_updated2016, y_train_political_regime_updated2016, y_test_political_regime_updated2016 = utils.train_test_split_data(
    x_data_encoded_political_regime_updated2016,
    political_regime_updated2016[
        ['Political Regime (OWID based on Polity IV and Wimmer & Min) (Score)']],
    0.2)

'''
SHARE WITH ALCOHOL OR DRUG USE DISORDERS 
'''
share_with_alcohol_or_drug_use_disorders = utils.read_exel(
    "/home/sale/Desktop/GitHubSIAP/Data-Mining/tabele1990-2017/treba_regresija/share-with-alcohol-or-drug-use-disorders.xlsx")
# cist ispis da proverimo da li je tabela dobro ucitana.
print(share_with_alcohol_or_drug_use_disorders.head())
# enkodujemo x_data... sa one hot encodingom, jer sadrzi kolonu year koja je string kategorickog tipa
x_data_encoded_share_with_alcohol_or_drug_use_disorders = pd.get_dummies(share_with_alcohol_or_drug_use_disorders[['Country Code', 'Year']])
x_train_share_with_alcohol_or_drug_use_disorders, x_test_share_with_alcohol_or_drug_use_disorders, y_train_share_with_alcohol_or_drug_use_disorders, y_test_share_with_alcohol_or_drug_use_disorders = utils.train_test_split_data(
    x_data_encoded_share_with_alcohol_or_drug_use_disorders,
    share_with_alcohol_or_drug_use_disorders[
        ['Prevalence - Alcohol and substance use disorders: Both (age-standardized percent) (%)']],
    0.2)

'''
UN MIGRANT STOCK BY ORIGIN AND DESTINATION 2019
'''
UN_MigrantStockByOriginAndDestination_2019 = utils.read_exel(
    "/home/sale/Desktop/GitHubSIAP/Data-Mining/tabele1990-2017/treba_regresija/UN_MigrantStockByOriginAndDestination_2019.xlsx")
# cist ispis da proverimo da li je tabela dobro ucitana.
print(UN_MigrantStockByOriginAndDestination_2019.head())
# enkodujemo x_data... sa one hot encodingom, jer sadrzi kolonu year koja je string kategorickog tipa
x_data_encoded_UN_MigrantStockByOriginAndDestination_2019 = pd.get_dummies(UN_MigrantStockByOriginAndDestination_2019[['Country Code', 'Year']])
x_train_UN_MigrantStockByOriginAndDestination_2019, x_test_UN_MigrantStockByOriginAndDestination_2019, y_train_UN_MigrantStockByOriginAndDestination_2019, y_test_UN_MigrantStockByOriginAndDestination_2019 = utils.train_test_split_data(
    x_data_encoded_UN_MigrantStockByOriginAndDestination_2019,
    UN_MigrantStockByOriginAndDestination_2019[
        ['Total origin']],
    0.2)

'''
WARS FORMATTED
'''
wars_formated = utils.read_exel(
    "/home/sale/Desktop/GitHubSIAP/Data-Mining/tabele1990-2017/treba_regresija/wars_formated.xlsx")
# cist ispis da proverimo da li je tabela dobro ucitana.
print(wars_formated.head())
# enkodujemo x_data... sa one hot encodingom, jer sadrzi kolonu year koja je string kategorickog tipa
x_data_encoded_wars_formated = pd.get_dummies(wars_formated[['Country Code', 'Year']])
x_train_wars_formated, x_test_wars_formated, y_train_wars_formated, y_test_wars_formated = utils.train_test_split_data(
    x_data_encoded_wars_formated,
    wars_formated[
        ['won_war']],
    0.2)