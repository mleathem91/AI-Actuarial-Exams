import codecs
with codecs.open('results/gemini-3.1-pro-high/CM2B/September_2025/q2_out.txt', 'r', encoding='utf-16le') as f:
    for line in f:
        print(line.strip())
