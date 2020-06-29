# designer.py
designer.py is a Python script for designing factorial completely randomzed design and randomized complete block design trials.

# Introduction
Designing an experiment requires the experimenter to randomize the assignment of treatments to experimental units. In some cases, it is useful to block treatments to reduce variability among experimental units. The latter is especially true for experiments in environments where there is sufficient heterogeneity that can influence a measured response. 

The purpose of this script is to take user-supplied input (see below) and output a 'plot plan' and a data recording sheet. 

# Dependencies
Written in Python3.

Python libraries:
- numpy  (1.18.5)
- pandas (1.0.5)

# Usage
Once the script is in your directory of choice, run the script with the following command in a terminal emulator (terminal on MacOS or Linux):

```{bash}
python designer.py
```
# Expected output
Two files:
- *prefix*\_plot\_map.csv: Plot map with a randomization for each treatment combination.
- *prefix*\_manual\_input\_sheet.csv: Each experimental unit is arranged in a tidy format (long). This should be useful for recording data manually and for inputting data on the computer.

**NOTE:** This script, as of now, creates the above files with these prefixes **without** checking for the presence of a preexisting file. Therefore, the output of this file will overwrite any files with matching names in the same directory.

# The script will prompt the user with a series of questions:

## Prefix
Requests a prefix (no spaces) for the files. An example prefix would be 'experiment1', or '2020.06.25_trial'. This prefix will be appended at the beginning of the output file names.

## CRD vs. RCBD
This script will *only* perform randomizations for completely random designs (CRDs) and randomized complete block designs (RCBD). This question expects a string.

## Number of replicates
Requests the number of replicates (positive integers only) in the design.

## Number of factors
Requests the number of factors that (positive integer only).

## Number of levels within factor *n*
Requests the number of levels (or treatments) within the *nth* factor. 

## Name of the levels in factor *n*
Requests the name of each level of the *nth* factor.

# Contributing
This is my first repo. I'm still becoming acquainted with GitHub, feel free to provide suggestions if you are interested in doing so. 

# License
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
