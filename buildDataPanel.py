import pandas as pd
from datetime import datetime
import json
import os
import config

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

# Mapping of columns to snake_case keys and function names
COLUMNS_MAPPING = {
    "Steps": "steps",
    "Total sleep time": "total_sleep_time",
    "Real sleep time": "real_sleep_time",
    "REM sleep time": "rem_sleep_time",
    "Superficial sleep time": "superficial_sleep_time",
    "Deep sleep time": "deep_sleep_time",
    "Sleep efficiency": "sleep_efficiency",
    "Stress": "stress",
    "Mean heart rate": "mean_heart_rate",
    "Maximum heart rate": "maximum_heart_rate",
    "Active minutes": "active_minutes",
    "Burned calories": "burned_calories",
    "Blood pressure": "blood_pressure",
    "Length": "length",
    "Weight": "weight",
    "Belly circumference": "belly_circumference",
    "Heart rate": "heart_rate",
    "Body temperature": "body_temperature",
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
    "Non-HDL-cholesterol": "non_hdl_cholesterol",
    "HDL": "hdl",
    "Cholesterol": "cholesterol",
    "CRP": "crp",
    "Subcutanious glucose": "subcutaneous_glucose",
    "Arterial ketones": "arterial_ketones",
    "Salivary cortisol": "salivary_cortisol"
}


def csv_to_dataframe(csv_path):
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
    # Use DataFrame.apply to improve performance and simplify iteration
    panel_results = df.apply(
        lambda row: build_panel(
            patient_reference, patient_display,
            process_observations(row.to_frame().T, patient_reference, patient_display)
        ), axis=1
    ).tolist()

    return panel_results


def process_observations(df, patient_reference, patient_display):
    """
    Processes the DataFrame to generate observations for each available column.

    Args:
        df (DataFrame): DataFrame containing observation data (single row).
        patient_reference (str): Reference to the patient for observations.
        patient_display (str): Display name of the patient.

    Returns:
        dict: Dictionary with observation IDs mapped to column names in camelCase.
    """
    observation_ids = {}

    for column, func_name in COLUMNS_MAPPING.items():
        if column in df.columns:
            value = df[column].iloc[0]

            try:
                func = globals()[f"harmonize_{func_name}"]
                current_resource_id = f"{func_name}-observation-{patient_reference}-{datetime.now().strftime('%Y%m%d%H%M%S')}"
                observation_json = func(
                    resource_id=current_resource_id,
                    patient_reference=patient_reference,
                    patient_display=patient_display,
                    value=value
                )

                observation_ids[COLUMNS_MAPPING[column]] = current_resource_id
                save_observation_to_file(json_string=observation_json, filename=current_resource_id)

            except KeyError:
                print(f"Function for {func_name} not found.")
            except Exception as e:
                print(f"Error processing {column}: {e}")

    return observation_ids


def build_panel(patient_reference, patient_display, observation_ids):
    """
    Constructs a panel using the given observation IDs, using a custom CodeSystem for the observation categories.

    Args:
        patient_reference (str): Reference to the patient for observations.
        patient_display (str): Display name of the patient.
        observation_ids (dict): Dictionary of observation IDs for a single row.

    Returns:
        dict: A formatted panel containing observation IDs.
    """
    # Build a unique panel ID based on patient_reference and a unique value (e.g., timestamp)
    patient_id = patient_reference.split("/")[-1]  # Extract patient ID from reference
    panel_id = f"comprehensive-health-panel-{patient_id}"

    # Build the formatted panel with the required structure
    panel = {
        "resourceType": "Observation",
        "id": panel_id,
        "meta": {
            "profile": "http://example.com/fhir/StructureDefinition/comprehensive-panel"
        },
        "status": "final",
        "category": [
            {
                "coding": [
                    {
                        "system": "http://example.com/fhir/CodeSystem/comprehensive-observation-codes",
                        "code": "comprehensive-panel",
                        "display": "Comprehensive Health Panel"
                    }
                ]
            }
        ],
        "code": {
            "coding": [
                {
                    "system": "http://loinc.org",
                    "code": "96500-0",  # Example LOINC code
                    "display": "Comprehensive health observation panel"
                }
            ]
        },
        "subject": {
            "reference": patient_reference,
            "display": patient_display
        },
        "effectiveDateTime": datetime.now().isoformat(),
        "hasMember": [
            {"reference": f"Observation/{obs_id}"} for obs_id in observation_ids.values()
        ]
    }

    return panel


def save_observation_to_file(json_string, filename):
    """
    Saves a JSON string to a file in the harmonization output directory.

    Args:
        json_string (str): The JSON data as a string.
        filename (str): The name of the file to save the JSON data, without extension.

    Returns:
        str: The path to the saved JSON file.
    """
    try:
        # Convertir el JSON string a un diccionario
        json_data = json.loads(json_string)

        # Construir la ruta completa del archivo usando el directorio de salida de configuración
        output_path = os.path.join(config.HARMONIZATION_OUTPUT_DIR, f"{filename}.json")

        # Guardar el JSON en el archivo
        with open(output_path, 'w') as json_file:
            json.dump(json_data, json_file, indent=4)

        print(f"JSON saved successfully to: {output_path}")
        return output_path

    except json.JSONDecodeError as e:
        print(f"Error: The provided string is not valid JSON. Details: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while saving the JSON. Details: {e}")


def save_panel_to_json(panel):
    """
    Saves the given panel to a JSON file in the location specified by config.PATIENT_PANEL_PATH.

    Args:
        panel (dict): The panel data to save.
    """
    # Generate the file path using the panel ID
    file_path = os.path.join(config.PATIENT_PANEL_OUTPUT_DIR, f"{panel['id']}.json")

    # Write the panel data to a JSON file
    with open(file_path, 'w') as json_file:
        json.dump(panel, json_file, indent=4)

    print(f"Panel saved successfully to: {file_path}")
