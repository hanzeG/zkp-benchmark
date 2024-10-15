# save this as a file, e.g., `process_data.py`
import json
import os

def noir_parser(file_path, phase, metrix):
    # Initialize variables to hold input_length and prove_times for each algorithm
    mimc_input_length = []
    mimc_prove_times = []
    griffin_input_length = []
    griffin_prove_times = []
    poseidon_input_length = []
    poseidon_prove_times = []
    poseidon2_input_length = []
    poseidon2_prove_times = []

    # Load the JSON data
    data = {}
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
    else:
        print(f"File not found: {file_path}")
        # Return empty lists if file not found
        return [], [], [], [], [], [], [], []

    # List of algorithms to process
    algorithms = ['mimc', 'griffin', 'poseidon', 'poseidon2']

    for algo in algorithms:
        # Get the h keys under the algorithm
        h_data = data.get(algo, {})
        h_keys = list(h_data.keys())

        # Extract the numbers from h keys and sort them
        h_numbers = []
        for h in h_keys:
            if h.startswith('h'):
                try:
                    number = int(h[1:])
                    h_numbers.append(number)
                except ValueError:
                    pass  # Skip keys that don't have a number after 'h'

        h_numbers.sort()

        # Initialize the prove_times list for this algorithm
        times = []

        # Iterate over the sorted h_numbers and extract the prove times
        for number in h_numbers:
            h_key = f'h{number}'
            time = data.get(algo, {}).get(h_key, {}).get(phase, {}).get(metrix, None)
            times.append(time)

        # Store the input_length and prove_times for each algorithm
        if algo == 'mimc':
            mimc_input_length = h_numbers
            mimc_prove_times = times
        elif algo == 'griffin':
            griffin_input_length = h_numbers
            griffin_prove_times = times
        elif algo == 'poseidon':
            poseidon_input_length = h_numbers
            poseidon_prove_times = times
        elif algo == 'poseidon2':
            poseidon2_input_length = h_numbers
            poseidon2_prove_times = times

    # Return the input_length and prove_times lists for each algorithm
    return (mimc_input_length, mimc_prove_times,
            griffin_input_length, griffin_prove_times,
            poseidon_input_length, poseidon_prove_times,
            poseidon2_input_length, poseidon2_prove_times)