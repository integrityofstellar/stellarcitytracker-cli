import os
import json
import argparse
from pydantic import BaseModel


class Statistic(BaseModel):
    instagram: int
    youtube: int
    day: int


if not os.path.exists("data.json"):
    print("Data file not found, creating new one...")
    with open("data.json", "w") as f:
        json.dump({"statistics": []}, f)


def auto_increment() -> int:
    with open("data.json", "r") as f:
        data = json.load(f)
    if data["statistics"]:
        return data["statistics"][-1]["day"] + 1
    return 1


def save_statistic(statistic: Statistic) -> None:
    with open("data.json", "r") as f:
        data = json.load(f)

    data["statistics"].append(statistic.model_dump())

    with open("data.json", "w") as f:
        json.dump(data, f)

    print(f"Statistic for day {statistic.day} saved successfully")


def main() -> None:
    parser = argparse.ArgumentParser(description="StellarCity Habitats calculator")

    parser.add_argument("instagram", type=str, help="Amount of Instagram followers")
    parser.add_argument("youtube", type=str, help="Amount of Youtube subscribers")

    args = parser.parse_args()

    instagram_count = args.instagram
    youtube_count = args.youtube

    try:
        instagram_count = int(instagram_count)
        youtube_count = int(youtube_count)
    except ValueError:
        print("Please provide integers as input")
        return

    day = auto_increment()

    statistic = Statistic(instagram=instagram_count, youtube=youtube_count, day=day)

    save_statistic(statistic)

    with open("data.json", "r") as f:
        data = json.load(f)

    if len(data["statistics"]) <= 1:
        print(
            f"\nTotal: {instagram_count + youtube_count}\n\nInstagram: {instagram_count}\nYoutube: {youtube_count}",
        )
        return

    previous_day = data["statistics"][-2]

    prev_total = previous_day["instagram"] + previous_day["youtube"]
    today_total = instagram_count + youtube_count
    total_diff = today_total - prev_total

    instagram_diff = instagram_count - previous_day["instagram"]
    youtube_diff = youtube_count - previous_day["youtube"]

    print(
        f"\nTotal: {today_total} ({total_diff:+})\n\nInstagram: {instagram_count} ({instagram_diff:+})\nYoutube: {youtube_count} ({youtube_diff:+})",
    )


if __name__ == "__main__":
    main()
