import pytest
import pandas as pd
from preassignment import df_raw,df

def test_df():
    assert not df_raw.empty, "df variable seems to be empty."
    assert list(df_raw.columns) == ['Gender','age','education','currentSmoker','cigsPerDay','BPMeds','prevalentStroke','prevalentHyp','diabetes','totChol','sysBP','diaBP','BMI','heartRate','glucose','Heart_stroke'], "df columns don't match the expected ones."
    assert df_raw.shape[0] == 4238, f"df expected to have 4238 rows, but got {df.shape[0]}"

def test_df_nan():
    assert not df.isnull().values.any(), "df has NaN values."