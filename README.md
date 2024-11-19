## Overview

This application is designed to read and harmonize medical observation data, generating individual JSON files for each observation and a comprehensive patient panel that includes all the observations.

### How It Works

The application reads data from a CSV file (sample_data.csv), processes the content, and creates structured JSON outputs that conform to the FHIR (Fast Healthcare Interoperability Resources) standard. The application generates an individual JSON file for each observation in the CSV. In addition, it creates a patient panel JSON that aggregates all the individual observations for a given patient.

### Running the Application

To run the application, execute the main.py script:

```
python main.py
```

This script will:

- Read Input Data: Load the data from sample_data.csv.
- Harmonize Observations: Process each row of data to generate individual observation JSON files.
- Generate Patient Panel: Create a comprehensive patient panel JSON that includes references to all generated observation JSON files.

### Output

- Observation JSON Files: Each observation from sample_data.csv is processed and saved as an individual JSON file in the specified output directory.
- Patient Panel JSON: A comprehensive patient panel that references all the individual observations is also generated and saved.

### Configuration

The application uses a configuration file (config.py) to specify paths, such as:

HARMONIZATION_OUTPUT_DIR: Directory where the observation JSON files will be saved.
PATIENT_PANEL_OUTPUT_DIR: Directory where the patient panel will be stored in a json format.

These directories do not need to be modified for the application to work

### Requirements

- Python 3.11 (or higher)
Required Python packages are listed in requirements.txt. You can install them using:

```
pip install -r requirements.txt
```

### Example Files

- sample_data.csv: The CSV file containing sample patient data used for generating observations.
- There are example output files inside the output directories.

