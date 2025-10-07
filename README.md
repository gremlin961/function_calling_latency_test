# Gemini Function Calling Latency Test

This repository contains a Python script to measure and compare the function calling latency of different Google Gemini models available through Vertex AI.

## Description

The `model_latency.py` script sends a prompt to a specified Gemini model and measures the time it takes for the model to respond with a request to call a predefined function. This is useful for evaluating the performance of different model versions for applications that rely on tool use and function calling.

The script currently tests the following models:
- `gemini-2.5-flash`
- `gemini-2.0-flash-001`

You can easily modify the `MODEL_VERSIONS` list in the script to test other models.

## Getting Started

### Prerequisites

- Python 3.x
- Google Cloud SDK installed and authenticated.
- A Google Cloud project with the Vertex AI API enabled.

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/gremlin961/function_calling_latency_test.git
    cd function_calling_latency_test
    ```

2.  Install the required Python libraries:
    ```bash
    pip install google-genai
    ```

## Configuration

Before running the script, you need to configure your Google Cloud project details.

Open `model_latency.py` and replace the placeholder values for `PROJECT_ID` and `LOCATION` with your own:

```python
# --- Configuration ---
# Replace with your Google Cloud project ID and location
PROJECT_ID = "your-gcp-project-id"  # <-- REPLACE THIS
LOCATION = "us-central1"          # <-- REPLACE THIS (if needed)
```

## Usage

Once the configuration is set, run the script from your terminal:

```bash
python model_latency.py
```

The script will iterate through the models defined in the `MODEL_VERSIONS` list and print the function calling latency for each one in milliseconds.

### Example Output

```
--- Testing model: gemini-2.5-flash ---
Function call requested successfully.
Latency: 150.25 ms
-----------------------------------

--- Testing model: gemini-2.0-flash-001 ---
Function call requested successfully.
Latency: 250.75 ms
-----------------------------------------
