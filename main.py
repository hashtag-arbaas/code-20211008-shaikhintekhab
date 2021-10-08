from bmi_calc import get_bmi_data
from config import DATA, OVERWEIGHT_CATEGORY

if __name__ == "__main__":
    
    bmi_result_data = DATA

    for index, data in enumerate(DATA):
        # calculate bmi, category, health risk
        bmi_result_data[index]["bmi"],bmi_result_data[index]["category"], bmi_result_data[index]["health_risk"] = \
            get_bmi_data(data["WeightKg"], data["HeightCm"])
    
    # count number of overweight
    overweight_count = len([data for data in bmi_result_data if data["category"] in OVERWEIGHT_CATEGORY])
    print(bmi_result_data)
    print(f"Total number of overweight people are: {str(overweight_count)}")

    
