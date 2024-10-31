from typing import List
from utils.points import Point


def load_benchmark(file: str) -> List[Point]:
    points = []

    with open(f"../benchmark/{file}.txt") as f:
        for line in f:
            position = line.strip().split(" ")
            position = list(filter(lambda x: x != "", position))
            position = list(map(float, position))

            points.append(Point(position))

    return points
