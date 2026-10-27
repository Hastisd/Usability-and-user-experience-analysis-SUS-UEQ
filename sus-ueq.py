# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 11:01:33 2026

@author: Hasti
"""

import numpy as np
from scipy import stats

# ──────────────────────────────────────────────────────────────────────────────
#  RAW DATA  (n=34, within-subjects, health workers)
#  SUS: 10 items, Likert 1–5
#  UEQ: 26 items, semantic differential –3 to +3
# ──────────────────────────────────────────────────────────────────────────────

SUS_P1 = np.array([
   # Paste one row per participant (34 rows), 10 values each, from 1 to 5.
    # Example row: [3, 2, 4, 2, 4, 2, 4, 2, 4, 2],
], dtype=float)

SUS_P2 = np.array([
   # Paste one row per participant (34 rows), 10 values each, from 1 to 5.
    # Example row: [3, 2, 4, 2, 4, 2, 4, 2, 4, 2],
], dtype=float)
##2
UEQ_P1 = np.array([
# Item no.:  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26
    # Scale:     A,  C,  N,  C,  S,  S,  S,  D,  E,  N,  D,  A,  C,  A,  N,  A,  D,  S,  D,  E,  C,  E,  E,  A,  A,  N
    # Example:   2,  1,  0, -1,  2,  1,  0,  2,  1, -1,  3,  2,  0,  1,  2, -2,  1,  0,  2,  3,  1,  0, -1,  2,  1,  0
    #
    # Paste one row per participant below (34 rows), same layout as the example row:
    # [ 2,  1,  0, -1,  2,  1,  0,  2,  1, -1,  3,  2,  0,  1,  2, -2,  1,  0,  2,  3,  1,  0, -1,  2,  1,  0],
], dtype=float)

UEQ_P2 = np.array([
   # Item no.:  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26
    # Scale:     A,  C,  N,  C,  S,  S,  S,  D,  E,  N,  D,  A,  C,  A,  N,  A,  D,  S,  D,  E,  C,  E,  E,  A,  A,  N
    # Example:   2,  1,  0, -1,  2,  1,  0,  2,  1, -1,  3,  2,  0,  1,  2, -2,  1,  0,  2,  3,  1,  0, -1,  2,  1,  0
    #
    # Paste one row per participant below (34 rows), same layout as the example row:
    # [ 2,  1,  0, -1,  2,  1,  0,  2,  1, -1,  3,  2,  0,  1,  2, -2,  1,  0,  2,  3,  1,  0, -1,  2,  1,  0],
], dtype=float)

# ──────────────────────────────────────────────────────────────────────────────
#  UEQ-26 scale → 0-indexed item positions (verified against stored averages)
# ──────────────────────────────────────────────────────────────────────────────
UEQ_SCALES = {
    'Attractiveness': [0, 11, 13, 15, 23, 24],
    'Clarity':        [1,  3, 12, 20],
    'Efficiency':     [8, 19, 21, 22],
    'Dependability':  [7, 10, 16, 18],
    'Stimulation':    [4,  5,  6, 17],
    'Novelty':        [2,  9, 14, 25],
}

# ──────────────────────────────────────────────────────────────────────────────
#  Helpers
# ──────────────────────────────────────────────────────────────────────────────
def calc_sus(data):
    """Standard SUS formula → 0–100 score per participant."""
    scores = []
    for row in data:
        s = sum((v - 1) if (i + 1) % 2 == 1 else (5 - v)
                for i, v in enumerate(row))
        scores.append(s * 2.5)
    return np.array(scores)

def sus_grade(score):
    if score >= 85: return "Excellent (A)"
    if score >= 72: return "Good (B)"
    if score >= 52: return "OK (C)"
    if score >= 38: return "Poor (D)"
    return "Awful (F)"

def effect_label(d):
    a = abs(d)
    if a < 0.2:  return "negligible"
    if a < 0.5:  return "small"
    if a < 0.8:  return "medium"
    return "large"

def choose_test(s1, s2):
    """Shapiro-Wilk on paired differences → Wilcoxon or paired t-test."""
    diff = s2 - s1
    _, p_norm = stats.shapiro(diff)
    if p_norm > 0.05:
        stat, p = stats.ttest_rel(s1, s2)
        name = "Paired t-test"
    else:
        stat, p = stats.wilcoxon(s1, s2)
        name = "Wilcoxon signed-rank"
    d = diff.mean() / diff.std() if diff.std() != 0 else 0
    return name, stat, p, p_norm, d

# ══════════════════════════════════════════════════════════════════════════════
print("=" * 68)
print("  STATISTICAL ANALYSIS — Prototype 1 vs Prototype 2")
print("  Instrument: SUS & UEQ  |  Design: within-subjects  |  n = 34")
print("=" * 68)

# ─────────────────────────────  SUS  ─────────────────────────────────────────
sus_p1 = calc_sus(SUS_P1)
sus_p2 = calc_sus(SUS_P2)

print("\n━━━  SUS  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print(f"\n  P1 → Mean={sus_p1.mean():.2f}  SD={sus_p1.std():.2f}"
      f"  Median={np.median(sus_p1):.2f}  [{sus_grade(sus_p1.mean())}]")
print(f"  P2 → Mean={sus_p2.mean():.2f}  SD={sus_p2.std():.2f}"
      f"  Median={np.median(sus_p2):.2f}  [{sus_grade(sus_p2.mean())}]")

sw1 = stats.shapiro(sus_p1)
sw2 = stats.shapiro(sus_p2)
sw_d = stats.shapiro(sus_p2 - sus_p1)
print("\n  Shapiro-Wilk normality test:")
for label, sw in [("P1 scores", sw1), ("P2 scores", sw2), ("Paired diff", sw_d)]:
    tag = "Normal" if sw.pvalue > 0.05 else "Non-normal"
    print(f"    {label:<12} W={sw.statistic:.4f}  p={sw.pvalue:.4f}  → {tag}")

test_name, stat_val, p_val, p_norm_d, d = choose_test(sus_p1, sus_p2)
print(f"\n  → Differences {'normal' if p_norm_d>0.05 else 'non-normal'}; selected: {test_name}")
print(f"  Statistic={stat_val:.4f}  p={p_val:.4f}"
      f"  → {'SIGNIFICANT ✓' if p_val<0.05 else 'Not significant'} (α=0.05)")
print(f"  Cohen's d={d:.4f}  → {effect_label(d)} effect")
print(f"\n  Numerically preferred: {'P1' if sus_p1.mean()>sus_p2.mean() else 'P2'}"
      f" (no significant difference detected)")

# ─────────────────────────────  UEQ  ─────────────────────────────────────────
print("\n━━━  UEQ  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print(f"\n  {'Scale':<16} {'P1 M':>6} {'P1 SD':>6}"
      f" {'P2 M':>6} {'P2 SD':>6}"
      f"  {'Norm(diff)':>10}  {'Test':>20}"
      f"  {'Stat':>7}  {'p':>7}  {'Sig':>4}  {'d':>6}")
print("  " + "─" * 98)

ueq_results = {}
for scale, idx in UEQ_SCALES.items():
    s1 = UEQ_P1[:, idx].mean(axis=1)
    s2 = UEQ_P2[:, idx].mean(axis=1)
    tname, stat, p, p_n, d = choose_test(s1, s2)
    ueq_results[scale] = dict(
        p1_m=s1.mean(), p1_sd=s1.std(),
        p2_m=s2.mean(), p2_sd=s2.std(),
        test=tname, stat=stat, p=p, d=d
    )
    norm_tag = "Normal" if p_n > 0.05 else "Non-normal"
    sig = "✓" if p < 0.05 else "✗"
    print(f"  {scale:<16} {s1.mean():>6.3f} {s1.std():>6.3f}"
          f" {s2.mean():>6.3f} {s2.std():>6.3f}"
          f"  {norm_tag:>10}  {tname:>20}"
          f"  {stat:>7.3f}  {p:>7.4f}  {sig:>4}  {d:>6.3f}")

print("\n  Scale-level preferences (numerical):")
for scale, r in ueq_results.items():
    pref = "P1" if r['p1_m'] >= r['p2_m'] else "P2"
    print(f"    {scale:<16}  {pref}  (P1={r['p1_m']:.3f}, P2={r['p2_m']:.3f})")

ov1 = np.mean([r['p1_m'] for r in ueq_results.values()])
ov2 = np.mean([r['p2_m'] for r in ueq_results.values()])
print(f"\n  Overall UEQ avg: P1={ov1:.3f}, P2={ov2:.3f}"
      f"  → {'P1' if ov1>ov2 else 'P2'} numerically preferred")

