from typing import List
from utils.points import Point


def load_benchmark(file: str) -> List[Point]:
    points = []

    with open(f"../benchmark/{file}") as f:
        for line in f:
            position = line.strip().split(" ")
            position = list(filter(lambda x: x != "", position))

            x = int(position[0])
            y = int(position[1])

            points.append(Point(x, y))

    return points
