import openpyxl

wb = openpyxl.load_workbook("exams/CM1B/September_2025/Answer-Booklet.xlsx", data_only=True)
ws = wb["Q3 Base"]

with open("results/gemini-3.1-pro-high/CM1B/September_2025/q3_csv.csv", "w", encoding="utf-8") as f:
    for r in range(1, 100):
        row = [ws.cell(row=r, column=c).value for c in range(1, 15)]
        row_str = ",".join([str(x).replace(",", "") if x is not None else "" for x in row])
        f.write(row_str + "\n")
