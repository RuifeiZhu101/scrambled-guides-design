# scrambled_guides_design + CasOFFinder Filtering

## Project Overview
This project aims to provide a in-house tool for scrambled guide design.

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
(base) ubuntu@ip-172-31-22-126:~/scrambled_guides_design$ ./run_scrambled_guides.sh 
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
Add the feature to assess the scrambled guides regarding to thier off-target nomination result, and output the scrambled guides with the less off-target nominations.


## Authors and acknowledgment
Ruifei Zhu
