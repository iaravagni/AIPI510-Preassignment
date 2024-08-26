import pandas as pd

def calculate_avg_age(data):
    avg_age = data["age"].mean()
    return avg_age

def df_processing(data,gender):

    # Get the filtered df for people who had a heart stroke
    stroke_patients = data.query("Heart_stroke == 'yes' and Gender == @gender")

    # Calculate the average age by gender
    avg_gender_age = stroke_patients["age"].mean().__round__(2)

    return avg_gender_age

#Get path and open the file
path = 'heart_disease.csv'
df_raw = pd.read_csv(path) 

#Delete NaN values
df = df_raw.dropna()

#Process csv file
avg_female_age = df_processing(df,'Female')
avg_male_age = df_processing(df,'Male')

#Print the output
print(f"Average Female Age having a heart stroke: {avg_female_age}")
print(f"Average Male Age having a heart stroke: {avg_male_age}")

df_youngest_female= df.query("Heart_stroke == 'yes' and Gender=='Female'").sort_values(by='age',ascending=True).head(10)
df_youngest_male= df.query("Heart_stroke == 'yes' and Gender=='Male'").sort_values(by='age',ascending=True).head(10)

print(f'List of youngest women who had a stroke\n: {df_youngest_female}')
print(f'List of youngest men who had a stroke\n: {df_youngest_male}')
