from observation import Observation


# Function to harmonize Blood Pressure Observation
def harmonize_blood_pressure(resource_id, patient_reference, patient_display, value, unit="mmHg",
                             system="http://unitsofmeasure.org", code="mm[Hg]"):
    # Create an Observation object for Blood Pressure
    blood_pressure_observation = Observation(
        id=resource_id,
        coding_system="http://loinc.org",
        coding_code="85354-9",  # LOINC code for Blood Pressure panel
        coding_display="Blood pressure panel",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )

    # Return the JSON representation of the observation
    return blood_pressure_observation.to_json()


# Function to harmonize Length (Height) Observation
def harmonize_length(resource_id, patient_reference, patient_display, value, unit="cm", system="http://unitsofmeasure.org", code="cm"):
    length_observation = Observation(
        id=resource_id,
        coding_system="http://loinc.org",
        coding_code="8302-2",  # LOINC code for Body height
        coding_display="Body height",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return length_observation.to_json()


# Function to harmonize Weight Observation
def harmonize_weight(resource_id, patient_reference, patient_display, value, unit="kg", system="http://unitsofmeasure.org", code="kg"):
    weight_observation = Observation(
        id=resource_id,
        coding_system="http://loinc.org",
        coding_code="29463-7",  # LOINC code for Body weight
        coding_display="Body weight",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return weight_observation.to_json()


# Function to harmonize Belly Circumference Observation
def harmonize_belly_circumference(resource_id, patient_reference, patient_display, value, unit="cm", system="http://unitsofmeasure.org", code="cm"):
    belly_circumference_observation = Observation(
        id=resource_id,
        coding_system="http://loinc.org",
        coding_code="56086-2",  # LOINC code for Belly circumference
        coding_display="Belly circumference",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return belly_circumference_observation.to_json()


# Function to harmonize Heart Rate Observation
def harmonize_heart_rate(resource_id, patient_reference, patient_display, value, unit="beats/minute", system="http://unitsofmeasure.org", code="/min"):
    heart_rate_observation = Observation(
        id=resource_id,
        coding_system="http://loinc.org",
        coding_code="8867-4",  # LOINC code for Heart rate
        coding_display="Heart rate",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return heart_rate_observation.to_json()


def harmonize_body_temperature(resource_id, patient_reference, patient_display, value, unit="°C", system="http://unitsofmeasure.org", code="Cel"):
    body_temperature_observation = Observation(
        id=resource_id,
        coding_system="http://loinc.org",
        coding_code="8310-5",  # LOINC code for Body temperature
        coding_display="Body temperature",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return body_temperature_observation.to_json()


# Function to harmonize Subcutaneous Glucose Observation
def harmonize_subcutaneous_glucose(resource_id, patient_reference, patient_display, value, unit="mmol/L",
                                   system="http://unitsofmeasure.org", code="mmol/L"):
    subcutaneous_glucose_observation = Observation(
        id=resource_id,
        coding_system="http://loinc.org",
        coding_code="14743-9",  # LOINC code for Subcutaneous glucose
        coding_display="Glucose [Moles/volume] in Subcutaneous tissue",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return subcutaneous_glucose_observation.to_json()


# Function to harmonize Arterial Ketones Observation
def harmonize_arterial_ketones(resource_id, patient_reference, patient_display, value, unit="mmol/L",
                               system="http://unitsofmeasure.org", code="mmol/L"):
    arterial_ketones_observation = Observation(
        id=resource_id,
        coding_system="http://loinc.org",
        coding_code="2500-7",  # LOINC code for Arterial ketones
        coding_display="Ketones [Moles/volume] in Arterial blood",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return arterial_ketones_observation.to_json()


# Function to harmonize Salivary Cortisol Observation
def harmonize_salivary_cortisol(resource_id, patient_reference, patient_display, value, unit="nmol/L",
                                system="http://unitsofmeasure.org", code="nmol/L"):
    salivary_cortisol_observation = Observation(
        id=resource_id,
        coding_system="http://loinc.org",
        coding_code="2142-8",  # LOINC code for Salivary cortisol
        coding_display="Cortisol [Moles/volume] in Saliva",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return salivary_cortisol_observation.to_json()


# Function to harmonize Hemoglobin Observation
def harmonize_hemoglobin(resource_id, patient_reference, patient_display, value, unit="g/L", system="http://unitsofmeasure.org", code="g/L"):
    hemoglobin_observation = Observation(
        id=resource_id,
        coding_system="http://loinc.org",
        coding_code="718-7",  # LOINC code for Hemoglobin
        coding_display="Hemoglobin [Mass/volume] in Blood",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return hemoglobin_observation.to_json()


# Function to harmonize Leukocytes Observation
def harmonize_leukocytes(resource_id, patient_reference, patient_display, value, unit="10^9/L", system="http://unitsofmeasure.org", code="10*9/L"):
    leukocytes_observation = Observation(
        id=resource_id,
        coding_system="http://loinc.org",
        coding_code="6690-2",  # LOINC code for Leukocytes
        coding_display="Leukocytes [#/volume] in Blood",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return leukocytes_observation.to_json()


# Function to harmonize Glucose Observation
def harmonize_glucose(resource_id, patient_reference, patient_display, value, unit="mmol/L", system="http://unitsofmeasure.org", code="mmol/L"):
    glucose_observation = Observation(
        id=resource_id,
        coding_system="http://loinc.org",
        coding_code="2339-0",  # LOINC code for Glucose
        coding_display="Glucose [Moles/volume] in Blood",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return glucose_observation.to_json()


# Function to harmonize Insulin Observation
def harmonize_insulin(resource_id, patient_reference, patient_display, value, unit="mmol/L", system="http://unitsofmeasure.org", code="mmol/L"):
    insulin_observation = Observation(
        id=resource_id,
        coding_system="http://loinc.org",
        coding_code="27895-6",  # LOINC code for Insulin
        coding_display="Insulin [Moles/volume] in Serum or Plasma",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return insulin_observation.to_json()


# Function to harmonize Ketones Observation
def harmonize_ketones(resource_id, patient_reference, patient_display, value, unit="mmol/L", system="http://unitsofmeasure.org", code="mmol/L"):
    ketones_observation = Observation(
        id=resource_id,
        coding_system="http://loinc.org",
        coding_code="29539-4",  # LOINC code for Ketones
        coding_display="Ketones [Moles/volume] in Serum or Plasma",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return ketones_observation.to_json()


# Function to harmonize Cortisol Observation
def harmonize_cortisol(resource_id, patient_reference, patient_display, value, unit="mmol/L", system="http://unitsofmeasure.org", code="mmol/L"):
    cortisol_observation = Observation(
        id=resource_id,
        coding_system="http://loinc.org",
        coding_code="2143-6",  # LOINC code for Cortisol
        coding_display="Cortisol [Moles/volume] in Serum or Plasma",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return cortisol_observation.to_json()


# Function to harmonize Glucagon Observation
def harmonize_glucagon(resource_id, patient_reference, patient_display, value, unit="mmol/L", system="http://unitsofmeasure.org", code="mmol/L"):
    glucagon_observation = Observation(
        id=resource_id,
        coding_system="http://loinc.org",
        coding_code="1659-1",  # LOINC code for Glucagon
        coding_display="Glucagon [Moles/volume] in Serum or Plasma",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return glucagon_observation.to_json()


# Function to harmonize Triglyceride Observation
def harmonize_triglyceride(resource_id, patient_reference, patient_display, value, unit="mmol/L", system="http://unitsofmeasure.org", code="mmol/L"):
    triglyceride_observation = Observation(
        id=resource_id,
        coding_system="http://loinc.org",
        coding_code="2571-8",  # LOINC code for Triglyceride
        coding_display="Triglyceride [Moles/volume] in Serum or Plasma",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return triglyceride_observation.to_json()


# Function to harmonize LDL Observation
def harmonize_ldl(resource_id, patient_reference, patient_display, value, unit="mmol/L", system="http://unitsofmeasure.org", code="mmol/L"):
    ldl_observation = Observation(
        id=resource_id,
        coding_system="http://loinc.org",
        coding_code="39469-2",  # LOINC code for LDL cholesterol
        coding_display="LDL Cholesterol [Moles/volume] in Serum or Plasma",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return ldl_observation.to_json()


# Function to harmonize VLDL Observation
def harmonize_vldl(resource_id, patient_reference, patient_display, value, unit="mmol/L", system="http://unitsofmeasure.org", code="mmol/L"):
    vldl_observation = Observation(
        id=resource_id,
        coding_system="http://loinc.org",
        coding_code="55838-7",  # LOINC code for VLDL cholesterol
        coding_display="VLDL Cholesterol [Moles/volume] in Serum or Plasma",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return vldl_observation.to_json()


# Function to harmonize Non-HDL Cholesterol Observation
def harmonize_non_hdl_cholesterol(resource_id, patient_reference, patient_display, value, unit="mmol/L", system="http://unitsofmeasure.org", code="mmol/L"):
    non_hdl_cholesterol_observation = Observation(
        id=resource_id,
        coding_system="http://loinc.org",
        coding_code="96625-3",  # LOINC code for Non-HDL cholesterol
        coding_display="Non-HDL Cholesterol [Moles/volume] in Serum or Plasma",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return non_hdl_cholesterol_observation.to_json()


# Function to harmonize HDL Observation
def harmonize_hdl(resource_id, patient_reference, patient_display, value, unit="mmol/L", system="http://unitsofmeasure.org", code="mmol/L"):
    hdl_observation = Observation(
        id=resource_id,
        coding_system="http://loinc.org",
        coding_code="2085-9",  # LOINC code for HDL cholesterol
        coding_display="HDL Cholesterol [Moles/volume] in Serum or Plasma",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return hdl_observation.to_json()


# Function to harmonize Cholesterol Observation
def harmonize_cholesterol(resource_id, patient_reference, patient_display, value, unit="mmol/L", system="http://unitsofmeasure.org", code="mmol/L"):
    cholesterol_observation = Observation(
        id=resource_id,
        coding_system="http://loinc.org",
        coding_code="2093-3",  # LOINC code for Cholesterol
        coding_display="Cholesterol [Moles/volume] in Serum or Plasma",
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
        coding_system="http://loinc.org",
        coding_code="1988-5",  # LOINC code for C-Reactive Protein (CRP)
        coding_display="C-Reactive Protein [Mass/volume] in Serum or Plasma",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return crp_observation.to_json()


def harmonize_steps(resource_id, patient_reference, patient_display, value, unit="Number/day", system="http://unitsofmeasure.org", code="number/day"):
    steps_observation = Observation(
        id=resource_id,
        coding_system="http://loinc.org",
        coding_code="55423-8",  # LOINC code for Number of steps
        coding_display="Number of steps in a day",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return steps_observation.to_json()


# Function to harmonize Steps Observation
def harmonize_steps(resource_id, patient_reference, patient_display, value, unit="Number/day", system="http://unitsofmeasure.org", code="number/day"):
    steps_observation = Observation(
        id=resource_id,
        coding_system="http://loinc.org",
        coding_code="55423-8",  # LOINC code for Number of steps
        coding_display="Number of steps in a day",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return steps_observation.to_json()


# Function to harmonize Total Sleep Time Observation
def harmonize_total_sleep_time(resource_id, patient_reference, patient_display, value, unit="hours, minutes", system="http://unitsofmeasure.org", code="h,min"):
    total_sleep_time_observation = Observation(
        id=resource_id,
        coding_system="http://loinc.org",
        coding_code="3150-0",  # LOINC code for Sleep duration
        coding_display="Total sleep time",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return total_sleep_time_observation.to_json()


# Function to harmonize Real Sleep Time Observation
def harmonize_real_sleep_time(resource_id, patient_reference, patient_display, value, unit="hours, minutes", system="http://unitsofmeasure.org", code="h,min"):
    real_sleep_time_observation = Observation(
        id=resource_id,
        coding_system="http://loinc.org",
        coding_code="3151-8",  # Custom LOINC code for Real sleep time
        coding_display="Real sleep time",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return real_sleep_time_observation.to_json()


# Function to harmonize REM Sleep Time Observation
def harmonize_rem_sleep_time(resource_id, patient_reference, patient_display, value, unit="hours, minutes", system="http://unitsofmeasure.org", code="h,min"):
    rem_sleep_time_observation = Observation(
        id=resource_id,
        coding_system="http://loinc.org",
        coding_code="3152-6",  # Custom LOINC code for REM sleep time
        coding_display="REM sleep time",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return rem_sleep_time_observation.to_json()


# Function to harmonize Superficial Sleep Time Observation
def harmonize_superficial_sleep_time(resource_id, patient_reference, patient_display, value, unit="hours, minutes", system="http://unitsofmeasure.org", code="h,min"):
    superficial_sleep_time_observation = Observation(
        id=resource_id,
        coding_system="http://loinc.org",
        coding_code="3153-4",  # Custom LOINC code for Superficial sleep time
        coding_display="Superficial sleep time",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return superficial_sleep_time_observation.to_json()


# Function to harmonize Deep Sleep Time Observation
def harmonize_deep_sleep_time(resource_id, patient_reference, patient_display, value, unit="hours, minutes", system="http://unitsofmeasure.org", code="h,min"):
    deep_sleep_time_observation = Observation(
        id=resource_id,
        coding_system="http://loinc.org",
        coding_code="3154-2",  # Custom LOINC code for Deep sleep time
        coding_display="Deep sleep time",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return deep_sleep_time_observation.to_json()


# Function to harmonize Sleep Efficiency Observation
def harmonize_sleep_efficiency(resource_id, patient_reference, patient_display, value, unit="%", system="http://unitsofmeasure.org", code="%"):
    sleep_efficiency_observation = Observation(
        id=resource_id,
        coding_system="http://loinc.org",
        coding_code="248272009",  # SNOMED CT code for Sleep efficiency
        coding_display="Sleep efficiency",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return sleep_efficiency_observation.to_json()


# Function to harmonize Stress Observation
def harmonize_stress(resource_id, patient_reference, patient_display, value, unit="Low to high", system="http://unitsofmeasure.org", code="low-high"):
    stress_observation = Observation(
        id=resource_id,
        coding_system="http://loinc.org",
        coding_code="93085-8",  # LOINC code for Stress level
        coding_display="Stress level",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return stress_observation.to_json()


# Function to harmonize Mean Heart Rate Observation
def harmonize_mean_heart_rate(resource_id, patient_reference, patient_display, value, unit="beats/minute", system="http://unitsofmeasure.org", code="/min"):
    mean_heart_rate_observation = Observation(
        id=resource_id,
        coding_system="http://loinc.org",
        coding_code="8893-0",  # LOINC code for Heart rate
        coding_display="Mean heart rate",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return mean_heart_rate_observation.to_json()


# Function to harmonize Maximum Heart Rate Observation
def harmonize_maximum_heart_rate(resource_id, patient_reference, patient_display, value, unit="beats/minute", system="http://unitsofmeasure.org", code="/min"):
    maximum_heart_rate_observation = Observation(
        id=resource_id,
        coding_system="http://loinc.org",
        coding_code="2081-4",  # LOINC code for Maximum heart rate
        coding_display="Maximum heart rate",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return maximum_heart_rate_observation.to_json()


# Function to harmonize Active Minutes Observation
def harmonize_active_minutes(resource_id, patient_reference, patient_display, value, unit="minutes", system="http://unitsofmeasure.org", code="min"):
    active_minutes_observation = Observation(
        id=resource_id,
        coding_system="http://loinc.org",
        coding_code="99999-1",  # Custom LOINC code for Active minutes
        coding_display="Active minutes",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return active_minutes_observation.to_json()


# Function to harmonize Burned Calories Observation
def harmonize_burned_calories(resource_id, patient_reference, patient_display, value, unit="kcal", system="http://unitsofmeasure.org", code="kcal"):
    burned_calories_observation = Observation(
        id=resource_id,
        coding_system="http://loinc.org",
        coding_code="99999-2",  # Custom LOINC code for Burned calories
        coding_display="Burned calories",
        subject_reference=patient_reference,
        subject_display=patient_display,
        value=value,
        value_unit=unit,
        value_system=system,
        value_code=code
    )
    return burned_calories_observation.to_json()



# Example usage:
if __name__ == "__main__":
    # Generating a Blood Pressure Observation JSON
    bp_json = harmonize_blood_pressure(
        resource_id="bp-observation-1234",
        patient_reference="Patient/1234",
        patient_display="John Doe",
        value=120
    )

    length_json = harmonize_length(resource_id="length-1234", patient_reference="Patient/1234", patient_display="John Doe", value=175)
    weight_json = harmonize_weight(resource_id="weight-5678", patient_reference="Patient/1234", patient_display="John Doe", value=70)
    belly_circ_json = harmonize_belly_circumference(resource_id="belly-circ-9101", patient_reference="Patient/1234", patient_display="John Doe", value=90)
    heart_rate_json = harmonize_heart_rate(resource_id="heart-rate-2345", patient_reference="Patient/1234", patient_display="John Doe", value=72)
    body_temp_json = harmonize_body_temperature(resource_id="body-temp-6789", patient_reference="Patient/1234", patient_display="John Doe", value=37.5)
    sub_glucose_json = harmonize_subcutaneous_glucose(resource_id="sub-glucose-1234", patient_reference="Patient/1234",
                                                      patient_display="John Doe", value=5.5)
    arterial_ketones_json = harmonize_arterial_ketones(resource_id="arterial-ketones-5678",
                                                       patient_reference="Patient/1234", patient_display="John Doe",
                                                       value=0.5)
    salivary_cortisol_json = harmonize_salivary_cortisol(resource_id="salivary-cortisol-9101",
                                                         patient_reference="Patient/1234", patient_display="John Doe",
                                                         value=250)

    hemoglobin_json = harmonize_hemoglobin(resource_id="hemoglobin-1234", patient_reference="Patient/1234",
                                           patient_display="John Doe", value=150)
    leukocytes_json = harmonize_leukocytes(resource_id="leukocytes-5678", patient_reference="Patient/1234",
                                           patient_display="John Doe", value=6.5)
    glucose_json = harmonize_glucose(resource_id="glucose-9101", patient_reference="Patient/1234", patient_display="John Doe",
                                     value=5.2)
    insulin_json = harmonize_insulin(resource_id="insulin-1122", patient_reference="Patient/1234", patient_display="John Doe",
                                     value=0.025)
    ketones_json = harmonize_ketones(resource_id="ketones-3344", patient_reference="Patient/1234", patient_display="John Doe",
                                     value=0.1)
    cortisol_json = harmonize_cortisol(resource_id="cortisol-5566", patient_reference="Patient/1234", patient_display="John Doe",
                                       value=0.4)
    glucagon_json = harmonize_glucagon(resource_id="glucagon-7788", patient_reference="Patient/1234", patient_display="John Doe",
                                       value=0.015)
    triglyceride_json = harmonize_triglyceride(resource_id="triglyceride-9900", patient_reference="Patient/1234",
                                               patient_display="John Doe", value=1.5)
    ldl_json = harmonize_ldl(resource_id="ldl-2345", patient_reference="Patient/1234", patient_display="John Doe", value=2.3)
    vldl_json = harmonize_vldl(resource_id="vldl-6789", patient_reference="Patient/1234", patient_display="John Doe", value=0.5)
    non_hdl_json = harmonize_non_hdl_cholesterol(resource_id="non-hdl-5432", patient_reference="Patient/1234",
                                                 patient_display="John Doe", value=3.0)
    hdl_json = harmonize_hdl(resource_id="hdl-9876", patient_reference="Patient/1234", patient_display="John Doe", value=1.2)
    cholesterol_json = harmonize_cholesterol(resource_id="cholesterol-4321", patient_reference="Patient/1234",
                                             patient_display="John Doe", value=4.5)
    crp_json = harmonize_crp(resource_id="crp-1212", patient_reference="Patient/1234", patient_display="John Doe", value=3.0)

    patient_reference = "Patient/12345"
    patient_display = "John Doe"

    # Test Steps
    steps_json = harmonize_steps(resource_id="steps-001", patient_reference=patient_reference,
                                 patient_display=patient_display, value=10000)
    print("Steps JSON:", steps_json)

    # Test Total Sleep Time
    total_sleep_time_json = harmonize_total_sleep_time(resource_id="sleep-001", patient_reference=patient_reference,
                                                       patient_display=patient_display, value="7h 30min")
    print("Total Sleep Time JSON:", total_sleep_time_json)

    # Test Real Sleep Time
    real_sleep_time_json = harmonize_real_sleep_time(resource_id="realsleep-001", patient_reference=patient_reference,
                                                     patient_display=patient_display, value="6h 50min")
    print("Real Sleep Time JSON:", real_sleep_time_json)

    # Test REM Sleep Time
    rem_sleep_time_json = harmonize_rem_sleep_time(resource_id="remsleep-001", patient_reference=patient_reference,
                                                   patient_display=patient_display, value="1h 20min")
    print("REM Sleep Time JSON:", rem_sleep_time_json)

    # Test Superficial Sleep Time
    superficial_sleep_time_json = harmonize_superficial_sleep_time(resource_id="superficial-001",
                                                                   patient_reference=patient_reference,
                                                                   patient_display=patient_display, value="5h 00min")
    print("Superficial Sleep Time JSON:", superficial_sleep_time_json)

    # Test Deep Sleep Time
    deep_sleep_time_json = harmonize_deep_sleep_time(resource_id="deep-001", patient_reference=patient_reference,
                                                     patient_display=patient_display, value="1h 00min")
    print("Deep Sleep Time JSON:", deep_sleep_time_json)

    # Test Sleep Efficiency
    sleep_efficiency_json = harmonize_sleep_efficiency(resource_id="efficiency-001",
                                                       patient_reference=patient_reference,
                                                       patient_display=patient_display, value=85)
    print("Sleep Efficiency JSON:", sleep_efficiency_json)

    # Test Stress
    stress_json = harmonize_stress(resource_id="stress-001", patient_reference=patient_reference,
                                   patient_display=patient_display, value="Moderate")
    print("Stress JSON:", stress_json)

    # Test Mean Heart Rate
    mean_heart_rate_json = harmonize_mean_heart_rate(resource_id="meanhr-001", patient_reference=patient_reference,
                                                     patient_display=patient_display, value=70)
    print("Mean Heart Rate JSON:", mean_heart_rate_json)

    # Test Maximum Heart Rate
    maximum_heart_rate_json = harmonize_maximum_heart_rate(resource_id="maxhr-001", patient_reference=patient_reference,
                                                           patient_display=patient_display, value=120)
    print("Maximum Heart Rate JSON:", maximum_heart_rate_json)

    # Test Active Minutes
    active_minutes_json = harmonize_active_minutes(resource_id="active-001", patient_reference=patient_reference,
                                                   patient_display=patient_display, value=45)
    print("Active Minutes JSON:", active_minutes_json)

    # Test Burned Calories
    burned_calories_json = harmonize_burned_calories(resource_id="calories-001", patient_reference=patient_reference,
                                                     patient_display=patient_display, value=500)
    print("Burned Calories JSON:", burned_calories_json)

    # Print outputs for each observation
    print(hemoglobin_json)
    print(leukocytes_json)
    print(glucose_json)
    print(insulin_json)
    print(ketones_json)
    print(cortisol_json)
    print(glucagon_json)
    print(triglyceride_json)
    print(ldl_json)
    print(vldl_json)
    print(non_hdl_json)
    print(hdl_json)
    print(cholesterol_json)
    print(crp_json)
    print(sub_glucose_json)
    print(arterial_ketones_json)
    print(salivary_cortisol_json)
    print(length_json)
    print(weight_json)
    print(belly_circ_json)
    print(heart_rate_json)
    print(body_temp_json)
    print(bp_json)
