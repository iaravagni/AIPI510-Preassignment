import pytest
import pandas as pd
from preassignment import avg_male_age,avg_female_age, df_youngest_female, df_youngest_male

def test_avg_age_calculation():
    expected_female_avg_age = 55.18
    expected_male_avg_age = 53.54    

    # Check if the calculated averages are not NaN
    assert not pd.isna(avg_female_age), f"Female age average shouldn't be a NaN"
    assert not pd.isna(avg_male_age), f"Female age average shouldn't be a NaN"

    # Check if the calculated averages match the expected values
    assert avg_female_age == expected_female_avg_age, f"Expected {expected_female_avg_age}, but got {avg_female_age}"
    assert avg_male_age == expected_male_avg_age, f"Expected {expected_male_avg_age}, but got {avg_male_age}"

def test_youngest_stroke_patients():
    # Check number of rows
    assert df_youngest_female.shape[0] == 10, f"Expected 10 rows for youngest female dataframe, but got {df_youngest_female.shape[0]}"
    assert df_youngest_male.shape[0] == 10, f"Expected 10 rows for youngest male dataframe, but got {df_youngest_male.shape[0]}"

    # Check if gender is correct
    assert df_youngest_female['Gender'].eq('Female').all(), "Some rows in the youngest female DataFrame do not correspond to women."
    assert df_youngest_male['Gender'].eq('Male').all(), "Some rows in the youngest  male DataFrame do not correspond to men."

    # Check df_youngest_female is sorted by age in ascending order
    assert df_youngest_female['age'].is_monotonic_increasing, "The DataFrame for youngest females is not sorted in ascending order by age."
    assert df_youngest_male['age'].is_monotonic_increasing, "The DataFrame for youngest males is not sorted in ascending order by age."
    