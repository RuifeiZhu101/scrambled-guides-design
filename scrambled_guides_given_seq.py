#!/usr/bin/env python3

import sys
import random
#pip install python-Levenshtein
import Levenshtein
from math import factorial
from collections import Counter

def scramble_sequence(sequence):
    """
    Scramble the order of nucleotides in a DNA sequence.
    
    Args:
        sequence (str): The DNA sequence.
    
    Returns:
        str: The scrambled DNA sequence.
    """
    sequence_list = list(sequence)
    random.shuffle(sequence_list)
    scrambled_sequence = ''.join(sequence_list)
    return scrambled_sequence

def calculate_pairwise_distance(seq1, seq2):
    """
    Calculate the Levenshtein distance (pairwise distance) between two sequences.
    
    Args:
        seq1 (str): The first sequence.
        seq2 (str): The second sequence.
    
    Returns:
        int: The Levenshtein distance between the two sequences.
    """
    return Levenshtein.distance(seq1, seq2)

def generate_scrambled_guides(working_guide, num_guides):
    """
    Generate scrambled guide sequences with the same length and maximum pairwise distance.
    
    Args:
        working_guide (str): The working guide sequence.
        num_guides (int): The number of scrambled guide sequences to generate.
    
    Returns:
        list: List of scrambled guide sequences.
    """
    guide_length = len(working_guide)
    nucleotide_counts = Counter(working_guide) # counts A,C,G,T in the given working guide
    
    # Calculate the number of possible permutations
    # the number of distinct permutations of a DNA sequence can be calculated using
    # formula (total number of nucleotides)! / (count(A)! * count(C)! * count(G)! * count(T)!)
    total_possible_permutations = factorial(guide_length)
    for count in nucleotide_counts.values():
        total_possible_permutations //= factorial(count)
    
    # Set the maximum attempts as the number of possible permutations 
    max_attempts = min(total_possible_permutations,1000)
    attempts = 0
    scrambled_guides = [] # temperary list to store generated scrambled guides

    
    while attempts < max_attempts:
        guide = scramble_sequence(working_guide)
        scrambled_guides.append(guide)
        attempts += 1
    
    # Sort the scrambled guides based on the Levenshtein distance to the working guide
    scrambled_guides.sort(key=lambda x: calculate_pairwise_distance(x, working_guide), reverse=True)
    
    # Select the top num_guides guides with maximum pairwise distance
    final_guides = scrambled_guides[:num_guides]

    return final_guides


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 scrambled_guides_given_seq.py <working_guide> <num_guides>")
        return
    
    working_guide = sys.argv[1]
    num_guides = int(sys.argv[2])
    
    if not all(nucleotide in "ACGTacgt" for nucleotide in working_guide):
        print("Working guide sequence should only contain A, C, G, or T.")
        return
    
    nucleotide_counts = Counter(working_guide)
    total_possible_permutations = factorial(len(working_guide))
    for count in nucleotide_counts.values():
        total_possible_permutations //= factorial(count)
    
    max_attempts = min(total_possible_permutations, 1000)
    scrambled_guides = generate_scrambled_guides(working_guide, max_attempts)
    
    scrambled_guides.sort(key=lambda x: calculate_pairwise_distance(x, working_guide), reverse=True)
    
    final_guides = scrambled_guides[:num_guides]

    print("Scrambled Guide Sequences:")
    for i, guide in enumerate(final_guides, 1):
        print(f"Guide {i}: {guide}")

if __name__ == "__main__":
    main()

