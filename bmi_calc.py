

def get_category_and_risk(bmi):
    category_type = 'Underweight'
    risk = "Malnutrition risk"
    if bmi>=18.5 and bmi<25.0:
        category_type = "Normal weight"
        risk = "Low risk"
    elif bmi>=25.0 and bmi<30.0:
        category_type = "Overweight"
        risk = "Enhanced risk"
    elif bmi>=30.0 and bmi<40.0:
        category_type = "Moderately obese"
        risk = "Medium risk"
    elif bmi>=30.0 and bmi<40.0:
        category_type = "Severely obese"
        risk = "High risk"
    elif bmi>=40:
        category_type = "Very severely obese"
        risk = "Very high risk"
    return category_type, risk


def get_bmi_data(mass, height_cm):
    bmi =  mass/(height_cm/100)
    category, risk = get_category_and_risk(bmi)
    return  bmi, category, risk
