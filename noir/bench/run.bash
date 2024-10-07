#!/bin/bash

CIRCUIT_DIRS=(
    # "../test-circuit/sha256/h2"
    # "../test-circuit/sha256/h4"
    # "../test-circuit/sha256/h8"
    # "../test-circuit/sha256/h16"
    # "../test-circuit/sha256/h32"
    # "../test-circuit/sha256/h64"
    # "../test-circuit/sha256/h128"

    # "../test-circuit/mimc/h2"
    # "../test-circuit/mimc/h3"
    # "../test-circuit/mimc/h4"
    # "../test-circuit/mimc/h5"
    # "../test-circuit/mimc/h6"
    # "../test-circuit/mimc/h7"
    # "../test-circuit/mimc/h8"
    # "../test-circuit/mimc/h9"
    # "../test-circuit/mimc/h10"
    # "../test-circuit/mimc/h11"
    # "../test-circuit/mimc/h12"
    # "../test-circuit/mimc/h13"
    # "../test-circuit/mimc/h14"
    # "../test-circuit/mimc/h15"
    # "../test-circuit/mimc/h16"

    # "../test-circuit/griffin/h3"
    "../test-circuit/griffin/h4"
    # "../test-circuit/griffin/h8"

    # "../test-circuit/poseidon/h2"
    "../test-circuit/poseidon/h3"
    # "../test-circuit/poseidon/h4"
    # "../test-circuit/poseidon/h5"
    # "../test-circuit/poseidon/h6"
    # "../test-circuit/poseidon/h7"
    # "../test-circuit/poseidon/h8"
    # "../test-circuit/poseidon/h9"
    # "../test-circuit/poseidon/h10"
    # "../test-circuit/poseidon/h11"
    # "../test-circuit/poseidon/h12"
    # "../test-circuit/poseidon/h13"
    # "../test-circuit/poseidon/h14"
    # "../test-circuit/poseidon/h15"
    # "../test-circuit/poseidon/h16"

    # "../test-circuit/poseidon2/h2"
    # "../test-circuit/poseidon2/h3"
    # "../test-circuit/poseidon2/h4"
    # "../test-circuit/poseidon2/h8"
    # "../test-circuit/poseidon2/h12"
    # "../test-circuit/poseidon2/h16"
)

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

RESULTS_FILE="$SCRIPT_DIR/results.json"

# Initialize JSON file
echo "{}" > "$RESULTS_FILE"

for CIRCUIT_DIR in "${CIRCUIT_DIRS[@]}"
do
    # Get absolute path
    CIRCUIT_PATH="$(realpath "$SCRIPT_DIR/$CIRCUIT_DIR")"

    # Extract family and h values
    FAMILY="$(basename "$(dirname "$CIRCUIT_DIR")")"
    H="$(basename "$CIRCUIT_DIR")"

    echo ">> ---------- TEST CASE: $FAMILY, $H in Barretenberg ----------"

    # Debug: Print extracted values
    # echo "Debug: FAMILY = $FAMILY, H = $H"

    # Change to circuit directory
    cd "$CIRCUIT_PATH" || { echo "Cannot enter directory $CIRCUIT_PATH"; exit 1; }

    # ******************************************************
    # ************* Witness **************
    # ****************************************************** 
    
    ACIR_OPCODES=$(nargo info --json | jq -r '.programs[].functions[].acir_opcodes')
    
    echo ">> 0.1 ACIR_Ppcodes: $ACIR_OPCODES"
    
    # echo ">> 1.1 Execute Noir Program"

    # Corrected command
    TIME_OUTPUT=$( { NODE_OPTIONS=--max-old-space-size=12000 /usr/bin/time -l nargo execute witness > /dev/null; } 2>&1 )

    # Extract user time and maximum resident set size
    USER_TIME=$(echo "$TIME_OUTPUT" | grep 'user' | awk '{print $1}')
    MAX_RSS=$(echo "$TIME_OUTPUT" | grep 'maximum resident set size' | awk '{print $1}')

    # Build JSON object
    COMMAND_JSON=$(jq -n \
        --arg user_time "$USER_TIME" \
        --arg max_rss "$MAX_RSS" \
        '{user_time: $user_time, max_resident_size: $max_rss}')

    # Update JSON file
    jq --arg family "$FAMILY" --arg h "$H" --argjson data "$COMMAND_JSON" \
       '(.[$family] //= {} ) | .[$family][$h].witness = $data' \
       "$RESULTS_FILE" > tmp.$$.json && mv tmp.$$.json "$RESULTS_FILE"

    echo ">> 1.1 Executed Noir Program, user time: $USER_TIME, max ram: $MAX_RSS"

    # ******************************************************
    # ************* Prove **************
    # ****************************************************** 
    # echo ">> 2.1 Generating Proof by Barretenberg"

    # Corrected command
    TIME_OUTPUT=$( { NODE_OPTIONS=--max-old-space-size=12000 /usr/bin/time -l bb prove -b "./target/${H}.json" -w ./target/witness.gz -o ./target/proof > /dev/null; } 2>&1 )

    # Extract user time and maximum resident set size
    USER_TIME=$(echo "$TIME_OUTPUT" | grep 'user' | awk '{print $1}')
    MAX_RSS=$(echo "$TIME_OUTPUT" | grep 'maximum resident set size' | awk '{print $1}')

    # Build JSON object
    COMMAND_JSON=$(jq -n \
        --arg user_time "$USER_TIME" \
        --arg max_rss "$MAX_RSS" \
        '{user_time: $user_time, max_resident_size: $max_rss}')

    # Update JSON file
    jq --arg family "$FAMILY" --arg h "$H" --argjson data "$COMMAND_JSON" \
       '(.[$family] //= {} ) | .[$family][$h].prove = $data' \
       "$RESULTS_FILE" > tmp.$$.json && mv tmp.$$.json "$RESULTS_FILE"

    echo ">> 2.1 Generated Proof by Barretenberg, user time: $USER_TIME, max ram: $MAX_RSS"

    # ******************************************************
    # ************* Verify **************
    # ******************************************************     
    # echo ">> 3.1 Generating Verification Key"

    # Corrected command
    TIME_OUTPUT=$( { NODE_OPTIONS=--max-old-space-size=12000 /usr/bin/time -l bb write_vk -b "./target/${H}.json" -o ./target/vk > /dev/null; } 2>&1 )

    # Extract user time and maximum resident set size
    USER_TIME=$(echo "$TIME_OUTPUT" | grep 'user' | awk '{print $1}')
    MAX_RSS=$(echo "$TIME_OUTPUT" | grep 'maximum resident set size' | awk '{print $1}')

    # Build JSON object
    COMMAND_JSON=$(jq -n \
        --arg user_time "$USER_TIME" \
        --arg max_rss "$MAX_RSS" \
        '{user_time: $user_time, max_resident_size: $max_rss}')

    # Update JSON file
    jq --arg family "$FAMILY" --arg h "$H" --argjson data "$COMMAND_JSON" \
       '(.[$family] //= {} ) | .[$family][$h].write_vk = $data' \
       "$RESULTS_FILE" > tmp.$$.json && mv tmp.$$.json "$RESULTS_FILE"

    echo ">> 3.1 Generated Verification Key by Barretenberg, user time: $USER_TIME, max ram: $MAX_RSS"

    # echo ">> 3.2 Verifying proof"

    # Corrected command
    TIME_OUTPUT=$( { NODE_OPTIONS=--max-old-space-size=12000 /usr/bin/time -l bb verify -k ./target/vk -p ./target/proof > /dev/null; } 2>&1 )

    # Extract user time and maximum resident set size
    USER_TIME=$(echo "$TIME_OUTPUT" | grep 'user' | awk '{print $1}')
    MAX_RSS=$(echo "$TIME_OUTPUT" | grep 'maximum resident set size' | awk '{print $1}')

    # Build JSON object
    COMMAND_JSON=$(jq -n \
        --arg user_time "$USER_TIME" \
        --arg max_rss "$MAX_RSS" \
        '{user_time: $user_time, max_resident_size: $max_rss}')

    # Update JSON file
    jq --arg family "$FAMILY" --arg h "$H" --argjson data "$COMMAND_JSON" \
       '(.[$family] //= {} ) | .[$family][$h].verify = $data' \
       "$RESULTS_FILE" > tmp.$$.json && mv tmp.$$.json "$RESULTS_FILE"

    echo ">> 3.2 Verified by Barretenberg, user time: $USER_TIME, max ram: $MAX_RSS"

    # Return to script directory
    cd "$SCRIPT_DIR"
done