# scrambled_guides_design

## Project Overview
This tool is designed to assist researchers in the field of CRISPR gene editing by providing a powerful command-line utility for designing scrambled guide RNA sequences.

### Key Objectives:

**Scrambled Guide Design** : Generate scrambled guide RNA sequences based on a given guide sequence.

**Levenshtein Distance**: Calculate the Levenshtein distance between input guide sequences and scrambled guides for assessing their similarity.

**Incorporation with Off-Target Assessment Tool**: (See Future Directions) - Plan to incorporate off-target nomination assessment.

This project serves as a valuable resource for optimizing gRNA design, enhancing the precision of CRISPR-based experiments.

## Authors and acknowledgment
Author: Ruifei Zhu

Project Origin: This project was initiated during my summer internship. While it hasn't reached its full potential yet, it represents a significant step towards efficient gRNA design. I would like to express my gratitude to my mentor, Wenwen H. from Excision, for her invaluable guidance and the original idea behind this project.

## Current Tool Features

Design desired number of scrabled guides given a working guide sequence. Current scrambled guides can fulfill several features:
1. Same length and exactly same nucleotides composation(i.e. same count for each nuleotide) achieved by shuffling the given guide sequence.

2. Calculated the [Levenshtein distance](https://www.cuelogic.com/blog/the-levenshtein-algorithm#:~:text=The%20Levenshtein%20distance%20is%20a,one%20word%20into%20the%20other.) (pairwise distance) between input guide sequence and a scrambled guide. 

3. Output desired number of scrambled guides considering the searching space(currently choose minimum between(all possible result, 1000) to save calculation time), and output desired number of scrambled guides with maximum Levenshtein distance between input guide sequence and the scrambled guide. 

## TooUsage
1. Clone this repository to your working environment.
2. Change the directory to `scrambled_guides_design` with both python and bash script within the same directory.
3. Simply run `run_scrambled_guides.sh` by:
```
./run_scrambled_guides.sh
```
This will prompt a require for the input: 1. a guide sequence(string contains case-insensitive "A,C,G,T"), and 2. a intager(number of scrambled guides you want). For example:

```
(base) ubuntu@ip-123:~/scrambled_guides_design$ ./run_scrambled_guides.sh 
Enter the working guide sequence (A, C, G, T only): AAAACCCTTTGGG
Enter the number of output guide sequences: 5
```


After you giving the input correctly, this should print you disired number of guides out. For example:
```
Scrambled Guide Sequences:
Guide 1: GCTGTGAACAATC
Guide 2: CGGCTTGAAATAC
Guide 3: CTGTTGAGCACAA
Guide 4: TCTGAGACGACAT
```
## Future directions:
Expand the tool's functionality by adding the ability to assess the scrambled guides for off-target nominations. This will allow users to generate scrambled guides with fewer off-target nominations, enhancing the precision of CRISPR gene editing experiments.