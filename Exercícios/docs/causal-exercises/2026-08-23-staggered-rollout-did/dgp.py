"""DGP-04 — Staggered Policy Rollout (Intermediate, DiD).

Reference: everyday-causal-skills / references/dgp-library.md
DO NOT open this file until the debrief — it reveals the true effect.
"""

import numpy as np
import pandas as pd

np.random.seed(404)
n_stores = 200
n_months = 24

cohort_month = np.repeat([7, 13, 19, 0], 50)

store_id = np.repeat(np.arange(1, n_stores + 1), n_months)
month = np.tile(np.arange(1, n_months + 1), n_stores)
g = np.repeat(cohort_month, n_months)

store_fe = np.repeat(np.random.normal(0, 20, n_stores), n_months)
time_fe = np.tile(np.random.normal(0, 5, n_months), n_stores)

treat_effect = np.where(
    (g == 0) | (month < g),
    0,
    np.where(
        g == 7,
        200 + 2 * (month - g),
        np.where(g == 13, 150 + 1.5 * (month - g), 100 + 1 * (month - g)),
    ),
)

orders = 800 + store_fe + time_fe + treat_effect + np.random.normal(0, 30, n_stores * n_months)

df = pd.DataFrame(
    {
        "store_id": store_id,
        "month": month,
        "cohort_month": g,
        "orders": np.round(orders).astype(int),
    }
)
df.to_csv("data.csv", index=False)
print("Wrote data.csv:", df.shape)
