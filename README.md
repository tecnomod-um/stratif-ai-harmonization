Overview

This application is designed to read and harmonize medical observation data, generating individual JSON files for each observation and a comprehensive patient panel that includes all the observations.

How It Works

The application reads data from a CSV file (sample_data.csv), processes the content, and creates structured JSON outputs that conform to the FHIR (Fast Healthcare Interoperability Resources) standard. For each observation in the CSV, the application generates an individual JSON file. In addition, it creates a patient panel JSON that aggregates all the individual observations for a given patient.

Running the Application

To run the application, execute the main.py script:

python main.py

This script will:

Read Input Data: Load the data from sample_data.csv.

Harmonize Observations: Process each row of data to generate individual observation JSON files.

Generate Patient Panel: Create a comprehensive patient panel JSON that includes references to all generated observation JSON files.

Output

Observation JSON Files: Each observation from sample_data.csv is processed and saved as an individual JSON file in the specified output directory.

Patient Panel JSON: A comprehensive patient panel that references all the individual observations is also generated and saved.

Configuration

The application uses a configuration file (config.py) to specify paths, such as:

PATIENT_PANEL_PATH: Directory where the patient panel JSON file will be saved.

Make sure to update the configuration with the correct paths before running the application.

Requirements

Python 3.6 or higher

Required Python packages are listed in requirements.txt. You can install them using:

pip install -r requirements.txt

Example Files

sample_data.csv: The CSV file containing sample patient data used for generating observations.

Usage Notes

Ensure that sample_data.csv is properly formatted with all necessary columns.

The generated JSON files conform to the FHIR standard, making them suitable for integration with healthcare systems.

License

This project is licensed under the MIT License. See the LICENSE file for more details.

