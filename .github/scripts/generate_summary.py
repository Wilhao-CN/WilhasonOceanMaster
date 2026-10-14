#!/usr/bin/env python3
"""
生成 Shields.io Endpoint 可读取的汇总 JSON。
"""
import csv
import json
import os

def sum_csv(filepath):
    if not os.path.exists(filepath):
        return 0
    with open(filepath, "r", encoding="utf-8") as f:
        return sum(int(row["count"]) for row in csv.DictReader(f))

def main():
    clones = sum_csv("traffic-data/clones.csv")
    views = sum_csv("traffic-data/views.csv")
    summary = {
        "schemaVersion": 1,
        "label": "traffic",
        "message": f"clones {clones} | views {views}",
        "color": "blue",
    }
    os.makedirs("traffic-data", exist_ok=True)
    with open("traffic-data/traffic-summary.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)
    print(f"Summary written: {summary['message']}")

if __name__ == "__main__":
    main()
