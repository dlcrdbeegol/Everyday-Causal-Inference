"""DGP-06 — Weak Instrument (Intermediate, IV), adapted narrative.

Reference: everyday-causal-skills / references/dgp-library.md
DO NOT open this file until the debrief — it reveals the true effect and method.
"""

import numpy as np
import pandas as pd

np.random.seed(606)
n = 3000

# Instrument: generic mass email nudging members toward the wellness program
Z = np.random.binomial(1, 0.5, n)

# Unobserved health motivation (confounder): drives both enrollment and spending
U = np.random.normal(0, 1, n)


def logistic(x):
    return 1 / (1 + np.exp(-x))


# Weak instrument: the generic email barely moves enrollment (F ~ 5)
p_enroll = logistic(-1.0 + 0.3 * Z + 1.0 * U)
D = np.random.binomial(1, p_enroll)

# Outcome: annual medical spending (thousands of dollars)
Y = 50 - 10 * D - 8 * U + np.random.normal(0, 10, n)

df = pd.DataFrame(
    {
        "member_id": np.arange(1, n + 1),
        "received_email": Z,
        "enrolled_program": D,
        "annual_spending": np.round(Y, 2),
    }
)
df.to_csv("data.csv", index=False)
print("Wrote data.csv:", df.shape)
