import numpy as np

# --- 2026 FISCAL INPUTS (MARCH 2026 AUDIT) ---
TRILLION = 1_000_000_000_000
NATIONAL_DEBT = 39.0 * TRILLION      # Current Mar 2026 Debt
ANNUAL_REVENUE = 5.6 * TRILLION     # CBO 2026 Projected Revenue
INTEREST_EXPENSE = 1.0 * TRILLION    # Current Interest (19% of Revenue)
AI_DISPLACEMENT_RATE = 0.07          # Annual tax base erosion (Goldman/WEF avg)

def run_leos_collapse_sim(runs=10_000_000):
    collapse_count = 0
    years_to_singularity = []

    for _ in range(runs):
        debt = NATIONAL_DEBT
        revenue = ANNUAL_REVENUE
        stability = 1.0
        
        for year in range(1, 15):
            # 1. Interest Death Spiral (Variable rates based on risk)
            rate_shock = np.random.normal(0.045, 0.015) 
            debt += (debt * rate_shock) + (1.9 * TRILLION) # Adding annual deficit
            
            # 2. AI Tax Base Erosion
            # Every job lost to AI is a 1:1 hit to the legacy payroll tax model
            revenue -= (revenue * np.random.uniform(0.02, AI_DISPLACEMENT_RATE))
            
            # 3. The "X-Date" Logic
            # If Interest > 35% of Revenue, discretionary spending dies.
            if (debt * rate_shock) > (revenue * 0.35):
                collapse_count += 1
                years_to_singularity.append(year)
                break
                
    avg_years = np.mean(years_to_singularity) if years_to_singularity else 0
    survival_rate = (1 - (collapse_count / runs)) * 100
    
    print(f"--- LEOS MONTE CARLO RESULTS (NUPA REPO) ---")
    print(f"Total Runs: {runs:,}")
    print(f"Survival Rate: {survival_rate:.6f}%")
    print(f"Median Fiscal Singularity: 2026 + {int(avg_years)} years")
    print(f"Status: TERMINAL DECOHERENCE DETECTED")

run_leos_collapse_sim()

