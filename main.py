from buildDataPanel import csv_to_dataframe, json_to_dataframe, process_batch, save_panel_to_json

# Loads sample datasheet
# csv_path = "sample_data.csv"
# df = csv_to_dataframe(csv_path)

# TODO Recibir el input de un kafka
json_input = '{"Patient_id": "PruebaJson2", "Patient_display": "John2", "Steps": 78, "Total sleep time": 120, "Real sleep time": 36.5, "REM sleep time": 90}'
df = json_to_dataframe(json_input)
patient_reference = df['Patient_id'].iloc[0]  # TODO Checkear distintos formatos de entrada
patient_display = df['Patient_display'].iloc[0]

# Checks if datasheet has been correctly loaded
if df is not None:
    # Harmonizes the data
    panel_results = process_batch(df, patient_reference, patient_display)

    # Saves the results to a file
    for index, panel in enumerate(panel_results):
        # print(f"Panel result for row {index + 1}:")
        # print(panel)
        save_panel_to_json(panel)
        # print("\n")
else:
    print("Error loading CSV. Please check the path or the file content.")
