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
        coding_display="Leukocytes in urine",  # TODO ¿Es este el concepto correcto?
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
        coding_code="NONE", #TODO No encuentro codigo correspondiente
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
        coding_code="41950-7",  # TODO No encontré equivalente de SNOMED CT
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
        coding_display="Sleep duration",  # TODO ¿Podemos usar el mismo código que el anterior?
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
        coding_code="NONE",  # TODO No hay codigo para esto
        coding_display="NONE",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return sleep_efficiency_observation.to_json()


# TODO Unidad de medida?
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
        coding_code="101692-2",  # TODO Esta sí está en SNOMED pero con un nombre más específico
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
        coding_code="99999-1",  # TODO Falta contexto
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
        coding_code="NONE",  # TODO No hay codigo relacionado con este concepto especifico
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
        coding_code="NONE",  # TODO No hay codigo relacionado con este concepto especifico
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


if __name__ == "__main__":

    patient_reference = "Patient/12345"
    patient_display = "John Doe"

    bp_json = harmonize_blood_pressure(resource_id="bp-observation-1234", patient_reference="Patient/1234", patient_display="John Doe", value=120)
    save_json_to_file(bp_json, "armonized_jsons/bp-observation-1234.json")

    length_json = harmonize_length(resource_id="length-1234", patient_reference="Patient/1234", patient_display="John Doe", value=175)
    save_json_to_file(length_json, "armonized_jsons/length-observation-1234.json")

    weight_json = harmonize_weight(resource_id="weight-5678", patient_reference="Patient/1234", patient_display="John Doe", value=70)
    save_json_to_file(weight_json, "armonized_jsons/weight-observation-5678.json")

    belly_circ_json = harmonize_belly_circumference(resource_id="belly-circ-9101", patient_reference="Patient/1234", patient_display="John Doe", value=90)
    save_json_to_file(belly_circ_json, "armonized_jsons/belly-cinc-observation-1234.json")

    heart_rate_json = harmonize_heart_rate(resource_id="heart-rate-2345", patient_reference="Patient/1234", patient_display="John Doe", value=72)
    save_json_to_file(heart_rate_json, "armonized_jsons/heart-rate-observation-2345.json")

    body_temp_json = harmonize_body_temperature(resource_id="body-temp-6789", patient_reference="Patient/1234", patient_display="John Doe", value=37.5)
    save_json_to_file(body_temp_json, "armonized_jsons/body-temp-observation-6789.json")

    sub_glucose_json = harmonize_subcutaneous_glucose(resource_id="sub-glucose-1234", patient_reference="Patient/1234",
                                                      patient_display="John Doe", value=5.5)
    save_json_to_file(sub_glucose_json, "armonized_jsons/sub-glucose-observation-1234.json")

    arterial_ketones_json = harmonize_arterial_ketones(resource_id="arterial-ketones-5678",
                                                       patient_reference="Patient/1234", patient_display="John Doe",
                                                       value=0.5)
    save_json_to_file(arterial_ketones_json, "armonized_jsons/arterial-ketones-observation-5678.json")

    salivary_cortisol_json = harmonize_salivary_cortisol(resource_id="salivary-cortisol-9101",
                                                         patient_reference="Patient/1234", patient_display="John Doe",
                                                         value=250)
    save_json_to_file(salivary_cortisol_json, "armonized_jsons/salivary-cortisol-observation-9101.json")

    hemoglobin_json = harmonize_hemoglobin(resource_id="hemoglobin-1234", patient_reference="Patient/1234",
                                           patient_display="John Doe", value=150)
    save_json_to_file(hemoglobin_json, "armonized_jsons/hemoglobin-observation-1234.json")

    leukocytes_json = harmonize_leukocytes(resource_id="leukocytes-5678", patient_reference="Patient/1234",
                                           patient_display="John Doe", value=6.5)
    save_json_to_file(leukocytes_json, "armonized_jsons/leukocytes-observation-1234.json")

    glucose_json = harmonize_glucose(resource_id="glucose-9101", patient_reference="Patient/1234", patient_display="John Doe",
                                     value=5.2)
    save_json_to_file(glucose_json, "armonized_jsons/glucose-observation-9101.json")

    insulin_json = harmonize_insulin(resource_id="insulin-1122", patient_reference="Patient/1234", patient_display="John Doe",
                                     value=0.025)
    save_json_to_file(insulin_json, "armonized_jsons/insulin-observation-1122.json")

    ketones_json = harmonize_ketones(resource_id="ketones-3344", patient_reference="Patient/1234", patient_display="John Doe",
                                     value=0.1)
    save_json_to_file(ketones_json, "armonized_jsons/ketones-observation-3344.json")

    cortisol_json = harmonize_cortisol(resource_id="cortisol-5566", patient_reference="Patient/1234", patient_display="John Doe",
                                       value=0.4)
    save_json_to_file(cortisol_json, "armonized_jsons/cortisol-observation-5566.json")

    glucagon_json = harmonize_glucagon(resource_id="glucagon-7788", patient_reference="Patient/1234", patient_display="John Doe",
                                       value=0.015)
    save_json_to_file(glucagon_json, "armonized_jsons/glucagon-observation-1234.json")

    triglyceride_json = harmonize_triglyceride(resource_id="triglyceride-9900", patient_reference="Patient/1234",
                                               patient_display="John Doe", value=1.5)
    save_json_to_file(triglyceride_json, "armonized_jsons/trygliceride-observation-1234.json")

    ldl_json = harmonize_ldl(resource_id="ldl-2345", patient_reference="Patient/1234", patient_display="John Doe", value=2.3)
    save_json_to_file(ldl_json, "armonized_jsons/ldl-observation-1234.json")

    vldl_json = harmonize_vldl(resource_id="vldl-6789", patient_reference="Patient/1234", patient_display="John Doe", value=0.5)
    save_json_to_file(vldl_json, "armonized_jsons/vldl-observation-1234.json")

    non_hdl_json = harmonize_non_hdl_cholesterol(resource_id="non-hdl-5432", patient_reference="Patient/1234",
                                                 patient_display="John Doe", value=3.0)
    save_json_to_file(non_hdl_json, "armonized_jsons/non-hdl-observation-1234.json")

    hdl_json = harmonize_hdl(resource_id="hdl-9876", patient_reference="Patient/1234", patient_display="John Doe", value=1.2)
    save_json_to_file(hdl_json, "armonized_jsons/hdl-observation-1234.json")

    cholesterol_json = harmonize_cholesterol(resource_id="cholesterol-4321", patient_reference="Patient/1234",
                                             patient_display="John Doe", value=4.5)
    save_json_to_file(cholesterol_json, "armonized_jsons/cholesterol-observation-1234.json")

    crp_json = harmonize_crp(resource_id="crp-1212", patient_reference="Patient/1234", patient_display="John Doe", value=3.0)
    save_json_to_file(crp_json, "armonized_jsons/crp-observation-1234.json")

    steps_json = harmonize_steps(resource_id="steps-001", patient_reference=patient_reference,
                                 patient_display=patient_display, value=10000)
    save_json_to_file(steps_json, "armonized_jsons/steps-observation-1234.json")

    total_sleep_time_json = harmonize_total_sleep_time(resource_id="sleep-001", patient_reference=patient_reference,
                                                       patient_display=patient_display, value="7h 30min")
    save_json_to_file(total_sleep_time_json, "armonized_jsons/total-sleep-time-observation-1234.json")

    real_sleep_time_json = harmonize_real_sleep_time(resource_id="realsleep-001", patient_reference=patient_reference,
                                                     patient_display=patient_display, value="6h 50min")
    save_json_to_file(real_sleep_time_json, "armonized_jsons/real-sleep-time-observation-1234.json")

    rem_sleep_time_json = harmonize_rem_sleep_time(resource_id="remsleep-001", patient_reference=patient_reference,
                                                   patient_display=patient_display, value="1h 20min")
    save_json_to_file(rem_sleep_time_json, "armonized_jsons/rem-sleep-time-observation-1234.json")

    superficial_sleep_time_json = harmonize_superficial_sleep_time(resource_id="superficial-001",
                                                                   patient_reference=patient_reference,
                                                                   patient_display=patient_display, value="5h 00min")
    save_json_to_file(superficial_sleep_time_json, "armonized_jsons/superficial-sleep-time-observation-1234.json")

    deep_sleep_time_json = harmonize_deep_sleep_time(resource_id="deep-001", patient_reference=patient_reference,
                                                     patient_display=patient_display, value="1h 00min")
    save_json_to_file(deep_sleep_time_json, "armonized_jsons/deep-sleep-time-observation-1234.json")

    sleep_efficiency_json = harmonize_sleep_efficiency(resource_id="efficiency-001",
                                                       patient_reference=patient_reference,
                                                       patient_display=patient_display, value=85)
    save_json_to_file(sleep_efficiency_json, "armonized_jsons/sleep-efficiency-observation-1234.json")

    stress_json = harmonize_stress(resource_id="stress-001", patient_reference=patient_reference,
                                   patient_display=patient_display, value="Moderate")
    save_json_to_file(stress_json, "armonized_jsons/stress-observation-1234.json")

    mean_heart_rate_json = harmonize_mean_heart_rate(resource_id="meanhr-001", patient_reference=patient_reference,
                                                     patient_display=patient_display, value=70)
    save_json_to_file(mean_heart_rate_json, "armonized_jsons/mean-heart-rate-observation-1234.json")

    maximum_heart_rate_json = harmonize_maximum_heart_rate(resource_id="maxhr-001", patient_reference=patient_reference,
                                                           patient_display=patient_display, value=120)
    save_json_to_file(maximum_heart_rate_json, "armonized_jsons/maximum-heart-rate-observation-1234.json")

    active_minutes_json = harmonize_active_minutes(resource_id="active-001", patient_reference=patient_reference,
                                                   patient_display=patient_display, value=45)
    save_json_to_file(active_minutes_json, "armonized_jsons/active-minutes-observation-1234.json")

    burned_calories_json = harmonize_burned_calories(resource_id="calories-001", patient_reference=patient_reference,
                                                     patient_display=patient_display, value=500)
    save_json_to_file(burned_calories_json, "armonized_jsons/burned-calories-observation-1234.json")

