# Usability Analysis (SUS and UEQ)

This repository contains the analysis code from my Master's thesis. The thesis was about the human-centered design of two serious game prototypes for cognitive resilience in healthcare workers. I evaluated both prototypes with the System Usability Scale (SUS) and the User Experience Questionnaire (UEQ-26).

## Study design

- 34 healthcare workers took part.
- Each participant used both prototypes (within-subjects design).
- SUS has 10 items rated from 1 to 5.
- UEQ-26 has 26 items rated from -3 to +3, grouped into six scales: Attractiveness, Perspicuity (Clarity), Efficiency, Dependability, Stimulation, and Novelty.

## What the code does

- Calculates the SUS score (0 to 100) for each participant and prototype.
- Calculates the six UEQ scale scores for each participant.
- Reports the mean, standard deviation and median for each prototype.
- Checks normality of the paired differences with the Shapiro-Wilk test.
- Compares the two prototypes with a paired t-test when the differences are normal, and with the Wilcoxon signed-rank test when they are not.
- Reports an effect size for each comparison.
- Applies Holm correction to the six UEQ scale comparisons.
- Saves figures to the `figures/` folder.

## Data

The real data are not included in this repository, to protect participant privacy. The data folder contains only a description of the file format. To run the code, create four CSV files in `data/` as described in `data/README.md`. You can use your own data in the same format, or create random dummy files with `make_dummy_data.py` to test that the code runs. Results from dummy data have no meaning.

## How to run

```bash
pip install -r requirements.txt
python make_dummy_data.py     # optional, only to test the code
python src/analysis.py
```
