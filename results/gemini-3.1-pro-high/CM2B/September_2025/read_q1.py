import json
import codecs

with codecs.open('results/gemini-3.1-pro-high/CM2B/September_2025/q1_results.txt', 'r', encoding='utf-16le') as f:
    # Just print line by line
    for line in f.readlines():
        print(line.strip())
