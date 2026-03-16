import urllib.request
import urllib.parse
import json

chart_config = {
    "type": "line",
    "data": {
        "labels": ["0", "1", "2", "3", "4", "5"],
        "datasets": [
            {
                "label": "Path 1",
                "data": [0.03, 0.04, 0.05, 0.06, 0.05, 0.04],
                "borderColor": "blue",
                "fill": False
            }
        ]
    },
    "options": {
        "title": {
            "display": True,
            "text": "Simulated CIR Paths"
        }
    }
}

encoded_config = urllib.parse.quote(json.dumps(chart_config))
url = f"https://quickchart.io/chart?c={encoded_config}"

try:
    urllib.request.urlretrieve(url, "results/gemini-3.1-pro-high/CM2B/September_2025/test_plot.png")
    print("Success")
except Exception as e:
    print(e)
