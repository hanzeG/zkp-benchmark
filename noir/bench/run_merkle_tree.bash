#!/bin/bash

CIRCUIT_DIRS=(
    "../test-circuit/mimc/m0"
    "../test-circuit/mimc/m1"
    "../test-circuit/mimc/m2"
    "../test-circuit/mimc/m3"
    "../test-circuit/mimc/m4"
    "../test-circuit/mimc/m5"
    "../test-circuit/mimc/m6"
    "../test-circuit/mimc/m7"

    "../test-circuit/griffin/m0"
    "../test-circuit/griffin/m1"
    "../test-circuit/griffin/m2"
    "../test-circuit/griffin/m3"
    "../test-circuit/griffin/m4"
    "../test-circuit/griffin/m5"
    "../test-circuit/griffin/m6"
    "../test-circuit/griffin/m7"

    "../test-circuit/poseidon/m0"
    "../test-circuit/poseidon/m1"
    "../test-circuit/poseidon/m2"
    "../test-circuit/poseidon/m3"
    "../test-circuit/poseidon/m4"
    "../test-circuit/poseidon/m5"
    "../test-circuit/poseidon/m6"
    "../test-circuit/poseidon/m7"

    "../test-circuit/poseidon2/m0"
    "../test-circuit/poseidon2/m1"
    "../test-circuit/poseidon2/m2"
    "../test-circuit/poseidon2/m3"
    "../test-circuit/poseidon2/m4"
    "../test-circuit/poseidon2/m5"
    "../test-circuit/poseidon2/m6"
    "../test-circuit/poseidon2/m7"
)

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

RESULTS_FILE="$SCRIPT_DIR/merkle_tree_results.json"

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