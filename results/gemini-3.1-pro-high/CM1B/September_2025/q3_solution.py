import os
from openpyxl import Workbook

# Parameters
premium_0 = 1100
premium_growth = 0.03
term = 20
alloc_rates = {1: 0.75}
for i in range(2, 8): alloc_rates[i] = 1.03
for i in range(8, 21): alloc_rates[i] = 0.95

bos = 0.05
amc = 0.005
i_nu = 0.03
rdr = 0.08
initial_exp = 250
renewal_exp = 50
commission_rate = 0.015
age = 40

# Read tables from Q3 CSV dump
uf_growth = {}
mortality = {} # t -> q_x
with open("results/gemini-3.1-pro-high/CM1B/September_2025/q3_csv.csv", "r", encoding="utf-8") as f:
    for line in f:
        cols = line.strip().split(",")
        if len(cols) > 2 and cols[1].isdigit():
            # Unit fund growth
            t = int(cols[1])
            try:
                uf_growth[t] = float(cols[2])
            except:
                pass
        
        # mortality reading logic. Columns: 4=Age, 5=q[x], 6=q[x-1]+1, 7=qx
        if len(cols) > 7 and cols[4].isdigit():
            x = int(cols[4])
            if x == 40:
                mortality[1] = float(cols[5]) # q[x]
            if x == 41:
                mortality[2] = float(cols[6]) # q[x-1]+1
            if x >= 42:
                mortality[x - 40 + 1] = float(cols[7]) # qx

results = []
profit_vector = []
pif = [1.0] # Probability in force at start of year t

uf_end = 0.0

print("(i) Profit Vector Calculation")
for t in range(1, term + 1):
    q = mortality[t]
    if t < term:
        pif.append(pif[-1] * (1 - q))
        
    prem = premium_0 * (1 + premium_growth) ** (t - 1)
    alloc = prem * alloc_rates[t]
    unalloc = prem - alloc
    bos_income = alloc * bos
    inv = alloc - bos_income
    
    # Unit fund growth
    uf_bef_amc = (uf_end + inv) * (1 + uf_growth[t])
    amc_deduction = uf_bef_amc * amc
    uf_end = uf_bef_amc - amc_deduction
    
    # Non-unit cashflows
    expenses = initial_exp if t == 1 else renewal_exp
    comm = prem * commission_rate
    
    start_cf = unalloc + bos_income - expenses - comm
    interest = start_cf * i_nu
    
    death_benefit = uf_end * 2
    death_strain = death_benefit - uf_end
    exp_death_cost = q * death_strain
    
    profit = start_cf + interest + amc_deduction - exp_death_cost
    profit_vector.append(profit)
    
    results.append({
        "t": t, "prem": prem, "alloc": alloc, "inv": inv,
        "uf_end": uf_end, "start_cf": start_cf, "profit": profit, "q": q, "pif": pif[t-1]
    })
    print(f"Year {t:2d} | UF: {uf_end:8.2f} | Start CF: {start_cf:8.2f} | Profit: {profit:8.2f}")

# (ii) Zeroisation
reserves = [0.0] * (term + 1)
revised_profit = [0.0] * term

# Work backwards
for t in range(term, 0, -1):
    idx = t - 1
    # We need RevisedProfit_t = Profit_t + V_{t-1}(1+i_NU) - V_t p_{x+t-1} >= 0
    # So V_{t-1} = max(0, (V_t * p_{x+t-1} - Profit_t) / (1 + i_NU))
    
    v_t = reserves[t]
    p_x = 1 - mortality[t]
    prof_t = profit_vector[idx]
    
    required_v = (v_t * p_x - prof_t) / (1 + i_nu)
    reserves[t-1] = max(0.0, required_v)
    
    revised_profit[idx] = prof_t + reserves[t-1] * (1 + i_nu) - v_t * p_x

print("\n(ii) Zeroisation (Reserves & Revised Profit)")
for t in range(1, term + 1):
    print(f"Year {t:2d} | Reserve at end: {reserves[t]:8.2f} | Revised Profit: {revised_profit[t-1]:8.2f}")

# (iii) Present value of profits
npv_before = sum(profit_vector[t-1] * pif[t-1] / ((1 + rdr) ** t) for t in range(1, term + 1))
npv_after = sum(revised_profit[t-1] * pif[t-1] / ((1 + rdr) ** t) for t in range(1, term + 1))

print(f"\n(iii) PV of profits before zeroisation: {npv_before:.4f}")
print(f"PV of profits after zeroisation: {npv_after:.4f}")

# Export to Excel
OUT_DIR = "results/gemini-3.1-pro-high/CM1B/September_2025"
os.makedirs(OUT_DIR, exist_ok=True)
wb_out = Workbook()
ws_out = wb_out.active
ws_out.title = "Q3 Solution"

headers = ["Year", "Premium", "Unallocated", "BOS", "Expenses", "Commission", "Start CF", 
           "Interest", "AMC", "Death Cost", "Profit Vector", "Reserve End Yr", "Revised Profit", 
           "PIF", "PV(RevProfit)"]
ws_out.append(headers)

for t in range(1, term + 1):
    idx = t - 1
    r = results[idx]
    unalloc = r["prem"] - r["alloc"]
    bos_val = r["alloc"] * bos
    exp = initial_exp if t == 1 else renewal_exp
    comm = r["prem"] * commission_rate
    interest = r["start_cf"] * i_nu
    amc_val = (r["uf_end"] / (1 - amc)) * amc
    death_cost = r["q"] * r["uf_end"]
    
    pv_rev_prof = revised_profit[idx] * pif[idx] / ((1 + rdr) ** t)
    
    row = [t, r["prem"], unalloc, bos_val, exp, comm, r["start_cf"],
           interest, amc_val, death_cost, profit_vector[idx], reserves[t], revised_profit[idx],
           pif[idx], pv_rev_prof]
    ws_out.append(row)

ws_out.append([])
ws_out.append(["NPV Before:", npv_before])
ws_out.append(["NPV After:", npv_after])

workings_path = os.path.join(OUT_DIR, "workings_q3.xlsx")
wb_out.save(workings_path)

with open(os.path.join(OUT_DIR, "q3_output.txt"), "w", encoding="utf-8") as f:
    f.write(f"(iii) PV of profits before zeroisation: {npv_before:.4f}\n")
    f.write(f"(iii) PV of profits after zeroisation: {npv_after:.4f}\n")
