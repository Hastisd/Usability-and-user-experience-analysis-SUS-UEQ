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

The real data are not included in this repository, to protect participant privacy. The four data arrays at the top of `analysis.py` are empty, so the script will stop with a message until you add data.

To run the analysis, paste your own data into the four arrays, in this format:

| Array | Shape | Values |
|---|---|---|
| `SUS_P1`, `SUS_P2` | participants x 10 | integers 1 to 5, entered as answered (the script does the reverse scoring) |
| `UEQ_P1`, `UEQ_P2` | participants x 26 | integers -3 to +3, already recoded so that higher is always more positive |

Each row is one participant. The row order must be the same in all four arrays, because the comparison is within-subjects (paired). The UEQ items must be in the standard UEQ-26 order, because the scale mapping in the script uses item positions.

## How to run

```bash
pip install numpy scipy
python analysis.py
```
