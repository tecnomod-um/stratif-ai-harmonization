import pandas as pd

from harmonizeFhir import (
    harmonize_steps,
    harmonize_total_sleep_time,
    harmonize_real_sleep_time,
    harmonize_rem_sleep_time,
    harmonize_superficial_sleep_time,
    harmonize_deep_sleep_time,
    harmonize_sleep_efficiency,
    harmonize_stress,
    harmonize_mean_heart_rate,
    harmonize_maximum_heart_rate,
    harmonize_active_minutes,
    harmonize_burned_calories,
    harmonize_blood_pressure,
    harmonize_length,
    harmonize_weight,
    harmonize_belly_circumference,
    harmonize_heart_rate,
    harmonize_body_temperature,
    harmonize_hemoglobin,
    harmonize_leukocytes,
    harmonize_glucose,
    harmonize_insulin,
    harmonize_ketones,
    harmonize_cortisol,
    harmonize_glucagon,
    harmonize_triglyceride,
    harmonize_ldl,
    harmonize_vldl,
    harmonize_non_hdl_cholesterol,
    harmonize_hdl,
    harmonize_cholesterol,
    harmonize_crp,
    harmonize_subcutaneous_glucose,
    harmonize_arterial_ketones,
    harmonize_salivary_cortisol
)

# Mapping of columns to camelCase keys and function names
COLUMNS_MAPPING = {
    "Steps": "steps",
    "Total sleep time": "totalSleepTime",
    "Real sleep time": "realSleepTime",
    "REM sleep time": "remSleepTime",
    "Superficial sleep time": "superficialSleepTime",
    "Deep sleep time": "deepSleepTime",
    "Sleep efficiency": "sleepEfficiency",
    "Stress": "stress",
    "Mean heart rate": "meanHeartRate",
    "Maximum heart rate": "maximumHeartRate",
    "Active minutes": "activeMinutes",
    "Burned calories": "burnedCalories",
    "Blood pressure": "bloodPressure",
    "Length": "length",
    "Weight": "weight",
    "Belly circumference": "bellyCircumference",
    "Heart rate": "heartRate",
    "Body temperature": "bodyTemperature",
    "Hemoglobin": "hemoglobin",
    "Leukocytes": "leukocytes",
    "Glucose": "glucose",
    "Insulin": "insulin",
    "Ketones": "ketones",
    "Cortisol": "cortisol",
    "Glucagon": "glucagon",
    "Triglyceride": "triglyceride",
    "LDL": "ldl",
    "VLDL": "vldl",
    "Non-HDL-cholesterol": "nonHdlCholesterol",
    "HDL": "hdl",
    "Cholesterol": "cholesterol",
    "CRP": "crp",
    "Subcutanious glucose": "subcutaneousGlucose",
    "Arterial ketones": "arterialKetones",
    "Salivary cortisol": "salivaryCortisol"
}


def csv_to_dataframe(csv_path):
    """
    Reads a CSV file from the given path and converts it to a DataFrame.

    Args:
        csv_path (str): Path to the CSV file.

    Returns:
        DataFrame: The CSV data converted into a pandas DataFrame.
    """
    try:
        df = pd.read_csv(csv_path)
        return df
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None


def process_batch(df, patient_reference, patient_display):
    """
    Processes each row of the DataFrame and sends the resulting observations to build_panel.

    Args:
        df (DataFrame): DataFrame containing multiple rows of observation data.
        patient_reference (str): Reference to the patient for observations.
        patient_display (str): Display name of the patient.

    Returns:
        list: A list of results from build_panel for each row.
    """
    # List to store the results from build_panel for each row
    panel_results = []

    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():
        # Process the current row using process_observations
        observation_ids = process_observations(row.to_frame().T, patient_reference, patient_display)

        # Pass the observation IDs to build_panel and store the result
        panel_result = build_panel(patient_reference, patient_display, observation_ids)
        panel_results.append(panel_result)

    return panel_results


def process_observations(df, patient_reference, patient_display):
    """
    Processes the DataFrame to generate observations for each available column.

    Args:
        df (DataFrame): DataFrame containing observation data.
        patient_reference (str): Reference to the patient for observations.
        patient_display (str): Display name of the patient.

    Returns:
        dict: Dictionary with observation IDs mapped to column names in camelCase.
    """
    # Dictionary to store observation IDs
    observation_ids = {}

    # Loop through each column, checking for relevant observations
    for column, func_name in COLUMNS_MAPPING.items():
        if column in df.columns:
            # Retrieve the value from the first row (assumes single-row data)
            value = df[column].iloc[0]

            # Call the appropriate harmonization function and store the result
            try:
                func = globals()[f"harmonize_{func_name}"]
                observation_json = func(
                    resource_id=f"{func_name}-observation",
                    patient_reference=patient_reference,
                    patient_display=patient_display,
                    value=value
                )

                # Extract the ID from the JSON and store it in the dictionary
                observation_ids[COLUMNS_MAPPING[column]] = observation_json["id"]

            except KeyError:
                print(f"Function for {func_name} not found.")
            except Exception as e:
                print(f"Error processing {column}: {e}")

    return observation_ids


def build_panel(patiend_reference, patient_display, observation_ids):
    return None
