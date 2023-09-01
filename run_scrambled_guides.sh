#!/bin/bash

# Function to check if input is a valid DNA sequence
is_valid_sequence() {
    sequence="$1"
    if [[ "$sequence" =~ ^[ACGTacgt]+$ ]]; then
        return 0
    else
        return 1
    fi
}

# Prompt user for input
read -p "Enter the working guide sequence (A, C, G, T only): " working_guide
while ! is_valid_sequence "$working_guide"; do
    read -p "Invalid input. Enter a valid working guide sequence (A, C, G, T only): " working_guide
done

read -p "Enter the number of output guide sequences: " num_guides
while ! [[ "$num_guides" =~ ^[0-9]+$ ]]; do
    read -p "Invalid input. Enter a valid number: " num_guides
done

# Call the Python script with the input
python3 scrambled_guides_given_seq.py "$working_guide" "$num_guides"
