#!/usr/bin/env python3
"""
GitHub Traffic 数据抓取脚本
每日运行，将 clones 和 views 数据追加到 CSV 文件。
"""
import os
import csv
import requests
from datetime import datetime, timezone

REPO = os.environ.get("GITHUB_REPOSITORY")
TOKEN = os.environ["TRAFFIC_PAT"]
DATA_DIR = "traffic-data"

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
}

def fetch(endpoint):
    url = f"https://api.github.com/repos/{REPO}/traffic/{endpoint}"
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    return resp.json()

def append_csv(filepath, rows, fieldnames):
    existing_dates = set()
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                existing_dates.add(row["date"])
    file_exists = os.path.exists(filepath)
    with open(filepath, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        for row in rows:
            if row["date"] not in existing_dates:
                writer.writerow(row)

def main():
    os.makedirs(DATA_DIR, exist_ok=True)

    data = fetch("clones")
    rows = [
        {"date": item["timestamp"][:10], "count": item["count"], "uniques": item["uniques"]}
        for item in data.get("clones", [])
    ]
    append_csv(os.path.join(DATA_DIR, "clones.csv"), rows, ["date", "count", "uniques"])

    data = fetch("views")
    rows = [
        {"date": item["timestamp"][:10], "count": item["count"], "uniques": item["uniques"]}
        for item in data.get("views", [])
    ]
    append_csv(os.path.join(DATA_DIR, "views.csv"), rows, ["date", "count", "uniques"])

    print(f"Traffic data updated at {datetime.now(timezone.utc).isoformat()}")

if __name__ == "__main__":
    main()
