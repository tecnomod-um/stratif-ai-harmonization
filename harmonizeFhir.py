from observation import Observation
import json


def harmonize_blood_pressure(resource_id, patient_reference, patient_display, value, unit="mmHg",
                             system="http://unitsofmeasure.org", code="mm[Hg]"):

    blood_pressure_observation = Observation(
        id=resource_id,
        coding_system="http://snomed.info/sct",
        coding_code="75367002",
        coding_display="Blood pressure",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )

    return blood_pressure_observation.to_json()


def harmonize_length(resource_id, patient_reference, patient_display, value, unit="cm", system="http://unitsofmeasure.org", code="cm"):
    length_observation = Observation(
        id=resource_id,
        coding_system="http://snomed.info/sct",
        coding_code="1153637007",
        coding_display="Body height",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return length_observation.to_json()


def harmonize_weight(resource_id, patient_reference, patient_display, value, unit="kg", system="http://unitsofmeasure.org", code="kg"):
    weight_observation = Observation(
        id=resource_id,
        coding_system="http://snomed.info/sct",
        coding_code="27113001",
        coding_display="Body weight",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return weight_observation.to_json()


def harmonize_belly_circumference(resource_id, patient_reference, patient_display, value, unit="cm", system="http://unitsofmeasure.org", code="cm"):
    belly_circumference_observation = Observation(
        id=resource_id,
        coding_system="http://snomed.info/sct",
        coding_code="276361009",
        coding_display="Waist circumference",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return belly_circumference_observation.to_json()


def harmonize_heart_rate(resource_id, patient_reference, patient_display, value, unit="beats/minute", system="http://unitsofmeasure.org", code="/min"):
    heart_rate_observation = Observation(
        id=resource_id,
        coding_system="http://snomed.info/sct",
        coding_code="364075005",
        coding_display="Heart rate",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return heart_rate_observation.to_json()


def harmonize_body_temperature(resource_id, patient_reference, patient_display, value, unit="C", system="http://unitsofmeasure.org", code="Cel"):
    body_temperature_observation = Observation(
        id=resource_id,
        coding_system="http://snomed.info/sct",
        coding_code="386725007",
        coding_display="Body temperature",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return body_temperature_observation.to_json()


# TODO Not enough context
def harmonize_ketones(resource_id, patient_reference, patient_display, value, unit="mmol/L",
                               system="http://unitsofmeasure.org", code="mmol/L"):
    arterial_ketones_observation = Observation(
        id=resource_id,
        coding_system="http://snomed.info/sct",
        coding_code="NONE",
        coding_display="NONE",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return arterial_ketones_observation.to_json()


def harmonize_cortisol(resource_id, patient_reference, patient_display, value, unit="mmol/L",
                                system="http://unitsofmeasure.org", code="mmol/L"):
    salivary_cortisol_observation = Observation(
        id=resource_id,
        coding_system="http://snomed.info/sct",
        coding_code="62037009",
        coding_display="Cortisol measurement",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return salivary_cortisol_observation.to_json()


def harmonize_hemoglobin(resource_id, patient_reference, patient_display, value, unit="g/L", system="http://unitsofmeasure.org", code="g/L"):
    hemoglobin_observation = Observation(
        id=resource_id,
        coding_system="http://snomed.info/sct",
        coding_code="271026005",
        coding_display="Hemoglobin level estimation",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return hemoglobin_observation.to_json()


def harmonize_leukocytes(resource_id, patient_reference, patient_display, value, unit="10^9/L", system="http://unitsofmeasure.org", code="10*9/L"):
    leukocytes_observation = Observation(
        id=resource_id,
        coding_system="http://snomed.info/sct",
        coding_code="275741008",
        coding_display="Leukocytes in urine",  # TODO Check concept
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return leukocytes_observation.to_json()


def harmonize_glucose(resource_id, patient_reference, patient_display, value, unit="mmol/L", system="http://unitsofmeasure.org", code="mmol/L"):
    glucose_observation = Observation(
        id=resource_id,
        coding_system="http://snomed.info/sct",
        coding_code="36048009",
        coding_display="Glucose measurement",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return glucose_observation.to_json()


def harmonize_insulin(resource_id, patient_reference, patient_display, value, unit="mmol/L", system="http://unitsofmeasure.org", code="mmol/L"):
    insulin_observation = Observation(
        id=resource_id,
        coding_system="http://snomed.info/sct",
        coding_code="16890009",  # LOINC code for Insulin
        coding_display="Insulin measurement",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return insulin_observation.to_json()


def harmonize_glucagon(resource_id, patient_reference, patient_display, value, unit="mmol/L", system="http://unitsofmeasure.org", code="mmol/L"):
    glucagon_observation = Observation(
        id=resource_id,
        coding_system="http://snomed.info/sct",
        coding_code="70451005",  # LOINC code for Glucagon
        coding_display="Glucagon measurement",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return glucagon_observation.to_json()


def harmonize_triglyceride(resource_id, patient_reference, patient_display, value, unit="mmol/L", system="http://unitsofmeasure.org", code="mmol/L"):
    triglyceride_observation = Observation(
        id=resource_id,
        coding_system="http://snomed.info/sct",
        coding_code="14740000",
        coding_display="Triglycerides measurement",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return triglyceride_observation.to_json()


def harmonize_ldl(resource_id, patient_reference, patient_display, value, unit="mmol/L", system="http://unitsofmeasure.org", code="mmol/L"):
    ldl_observation = Observation(
        id=resource_id,
        coding_system="http://snomed.info/sct",
        coding_code="22644003",
        coding_display="Low density lipoprotein measurement",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return ldl_observation.to_json()


def harmonize_vldl(resource_id, patient_reference, patient_display, value, unit="mmol/L", system="http://unitsofmeasure.org", code="mmol/L"):
    vldl_observation = Observation(
        id=resource_id,
        coding_system="http://snomed.info/sct",
        coding_code="104585005",
        coding_display="VLDL Cholesterol measurement",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return vldl_observation.to_json()


def harmonize_non_hdl_cholesterol(resource_id, patient_reference, patient_display, value, unit="mmol/L", system="http://unitsofmeasure.org", code="mmol/L"):
    non_hdl_cholesterol_observation = Observation(
        id=resource_id,
        coding_system="http://snomed.info/sct",
        coding_code="NONE", #TODO No corresponding code
        coding_display="NONE",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return non_hdl_cholesterol_observation.to_json()


def harmonize_hdl(resource_id, patient_reference, patient_display, value, unit="mmol/L", system="http://unitsofmeasure.org", code="mmol/L"):
    hdl_observation = Observation(
        id=resource_id,
        coding_system="http://snomed.info/sct",
        coding_code="17888004",
        coding_display="High density lipoprotein measurement",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return hdl_observation.to_json()


def harmonize_cholesterol(resource_id, patient_reference, patient_display, value, unit="mmol/L", system="http://unitsofmeasure.org", code="mmol/L"):
    cholesterol_observation = Observation(
        id=resource_id,
        coding_system="http://snomed.info/sct",
        coding_code="77068002",
        coding_display="Cholesterol measurement",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return cholesterol_observation.to_json()


def harmonize_crp(resource_id, patient_reference, patient_display, value, unit="mg/L", system="http://unitsofmeasure.org", code="mg/L"):
    crp_observation = Observation(
        id=resource_id,
        coding_system="http://snomed.info/sct",
        coding_code="55235003",
        coding_display="C-Reactive Protein measurement",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return crp_observation.to_json()


def harmonize_steps(resource_id, patient_reference, patient_display, value, unit="Number/day", system="http://unitsofmeasure.org", code="{#}/d"):
    steps_observation = Observation(
        id=resource_id,
        coding_system="http://loinc.org",
        coding_code="41950-7",
        coding_display="Number of steps in 24 hour Measured",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return steps_observation.to_json()


def harmonize_total_sleep_time(resource_id, patient_reference, patient_display, value, unit="h", system="http://unitsofmeasure.org", code="h"):
    total_sleep_time_observation = Observation(
        id=resource_id,
        coding_system="http://loinc.org",
        coding_code="93832-4",
        coding_display="Sleep duration",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return total_sleep_time_observation.to_json()


def harmonize_real_sleep_time(resource_id, patient_reference, patient_display, value, unit="h", system="http://unitsofmeasure.org", code="h"):
    real_sleep_time_observation = Observation(
        id=resource_id,
        coding_system="http://loinc.org",
        coding_code="93832-4",
        coding_display="Sleep duration",  # TODO Same code as last observation, check
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return real_sleep_time_observation.to_json()


def harmonize_rem_sleep_time(resource_id, patient_reference, patient_display, value, unit="h", system="http://unitsofmeasure.org", code="h"):
    rem_sleep_time_observation = Observation(
        id=resource_id,
        coding_system="http://loinc.org",
        coding_code="93829-0",
        coding_display="REM sleep duration",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return rem_sleep_time_observation.to_json()


def harmonize_superficial_sleep_time(resource_id, patient_reference, patient_display, value, unit="h", system="http://unitsofmeasure.org", code="h"):
    superficial_sleep_time_observation = Observation(
        id=resource_id,
        coding_system="http://loinc.org",
        coding_code="93830-8",
        coding_display="Light sleep time",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return superficial_sleep_time_observation.to_json()


def harmonize_deep_sleep_time(resource_id, patient_reference, patient_display, value, unit="h", system="http://unitsofmeasure.org", code="h"):
    deep_sleep_time_observation = Observation(
        id=resource_id,
        coding_system="http://loinc.org",
        coding_code="93831-6",
        coding_display="Deep sleep duration",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return deep_sleep_time_observation.to_json()


def harmonize_sleep_efficiency(resource_id, patient_reference, patient_display, value, unit="%", system="http://unitsofmeasure.org", code="%"):
    sleep_efficiency_observation = Observation(
        id=resource_id,
        coding_system="http://snomed.info/sct",
        coding_code="NONE",  # TODO No corresponding code
        coding_display="NONE",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return sleep_efficiency_observation.to_json()


def harmonize_stress(resource_id, patient_reference, patient_display, value, unit="???", system="http://unitsofmeasure.org", code="???"):
    stress_observation = Observation(
        id=resource_id,
        coding_system="http://snomed.info/sct",
        coding_code="405052004",
        coding_display="Level of stress",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return stress_observation.to_json()


def harmonize_mean_heart_rate(resource_id, patient_reference, patient_display, value, unit="beats/minute", system="http://unitsofmeasure.org", code="/min"):
    mean_heart_rate_observation = Observation(
        id=resource_id,
        coding_system="http://loinc.org",
        coding_code="103205-1",
        coding_display="Mean heart rate",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return mean_heart_rate_observation.to_json()


def harmonize_maximum_heart_rate(resource_id, patient_reference, patient_display, value, unit="beats/minute", system="http://unitsofmeasure.org", code="/min"):
    maximum_heart_rate_observation = Observation(
        id=resource_id,
        coding_system="http://loinc.org",
        coding_code="101692-2",  # TODO Exists in SNOMED but seems too specific
        coding_display="Maximum heart rate",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return maximum_heart_rate_observation.to_json()


def harmonize_active_minutes(resource_id, patient_reference, patient_display, value, unit="min", system="http://unitsofmeasure.org", code="min"):
    active_minutes_observation = Observation(
        id=resource_id,
        coding_system="http://snomed.info/sct",
        coding_code="99999-1",  # TODO Not enough context
        coding_display="Active minutes",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return active_minutes_observation.to_json()


def harmonize_burned_calories(resource_id, patient_reference, patient_display, value, unit="kcal", system="http://unitsofmeasure.org", code="kcal"):
    burned_calories_observation = Observation(
        id=resource_id,
        coding_system="http://loinc.org",
        coding_code="41981-2",
        coding_display="Calories burned",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return burned_calories_observation.to_json()


def harmonize_subcutaneous_glucose(resource_id, patient_reference, patient_display, value, unit="mmol/L", system="http://unitsofmeasure.org", code="mmol/L"):
    subcutaneous_glucose_observation = Observation(
        id=resource_id,
        coding_system="http://snomed.info/sct",
        coding_code="NONE",  # TODO No code for this concept
        coding_display="NONE",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return subcutaneous_glucose_observation.to_json()


def harmonize_arterial_ketones(resource_id, patient_reference, patient_display, value, unit="mmol/L", system="http://unitsofmeasure.org", code="mmol/L"):
    arterial_ketones_observation = Observation(
        id=resource_id,
        coding_system="http://snomed.info/sct",
        coding_code="NONE",  # TODO No code for this concept
        coding_display="NONE",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return arterial_ketones_observation.to_json()


def harmonize_salivary_cortisol(resource_id, patient_reference, patient_display, value, unit="nmol/L", system="http://unitsofmeasure.org", code="nmol/L"):
    salivary_cortisol_observation = Observation(
        id=resource_id,
        coding_system="https://loinc.org/",
        coding_code="51844-9",
        coding_display="Cortisol [Moles/volume] in Saliva (oral fluid)",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return salivary_cortisol_observation.to_json()


def save_json_to_file(json_data, filename):
    with open(filename, 'w') as json_file:
        json.dump(json.loads(json_data), json_file, indent=2)
