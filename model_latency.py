import time
#import vertexai
#from vertexai.generative_models import FunctionDeclaration, Tool, GenerativeModel
from google import genai
from google.genai import types


# --- Configuration ---
# Replace with your Google Cloud project ID and location
PROJECT_ID = "your-gcp-project-id"
LOCATION = "us-central1"

# Models to test
MODEL_VERSIONS = ["gemini-2.5-flash", "gemini-2.0-flash-001"] # Example model versions
PROMPT = "What is the weather like in Boston?" # Example prompt to send to the models


# Initialize Vertex AI
client = genai.Client(
    vertexai=True, project=PROJECT_ID, location=LOCATION
)

# --- Define the Function and Tool ---

def get_current_weather(location: str, unit: str = "fahrenheit"):
    """
    Get the current weather in a given location.

    Args:
        location: The city and state, e.g. San Francisco, CA.
        unit: The unit to use, either "celsius" or "fahrenheit".
    """
    # This is a dummy function. In a real scenario, this would make an API call.
    return {"weather": f"sunny and 75 {unit} in {location}"}

# Define the function declaration for the model
get_weather_func = {
    "name": "get_current_weather",
    "description": "Get the current weather in a given location.",
    "parameters":{
        "type": "object",
        "properties": {
            "location": {"type": "string", "description": "The city and state, e.g. San Francisco, CA"},
            "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}
        },
        "required": ["location"]
    },
}


# Configure the Tools and Configs
tools = types.Tool(function_declarations=[get_weather_func])
config = types.GenerateContentConfig(tools=[tools])

# --- Latency Measurement ---

def measure_function_calling_latency(model_name: str):
    """
    Measures the latency of a function call for a given model.
    """
    print(f"--- Testing model: {model_name} ---")
    try:

        # Start the timer
        start_time = time.perf_counter()

        # Send the function
        response = client.models.generate_content(
            model=model_name,
            contents=PROMPT,
            config=config,
        )

        # End the timer
        end_time = time.perf_counter()

        # Calculate the latency
        latency = (end_time - start_time) * 1000  # in milliseconds

        # Check if the model requested a function call
        if response.candidates[0].content.parts[0].function_call:
            print(f"Function call requested successfully.")
            print(f"Latency: {latency:.2f} ms")
        else:
            print("The model did not request a function call.")

    except Exception as e:
        print(f"An error occurred: {e}")
    print("-" * (len(model_name) + 18))
    print()


if __name__ == "__main__":
    if PROJECT_ID == "your-gcp-project-id":
        print("Please replace 'your-gcp-project-id' with your actual Google Cloud project ID.")
    else:
        for model_version in MODEL_VERSIONS:
            measure_function_calling_latency(model_version)