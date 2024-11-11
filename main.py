from buildDataPanel import csv_to_dataframe, process_batch, save_panel_to_json

# Example patient
patient_reference = "12345"
patient_display = "John Doe"

# Loads sample datasheet
csv_path = "sample_data.csv"
df = csv_to_dataframe(csv_path)

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
