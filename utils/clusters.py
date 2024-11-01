from typing import List, Tuple, Union
from itertools import combinations
import random
from uuid import uuid4
from utils.points import Point
import numpy as np


class Cluster:
    def __init__(self, all_points: List[Point]):
        self.id: str = str(uuid4())
        self.points: List[Point] = []
        self.centroid: Point = random.choice(all_points)
        self.color = f"#{random.randint(0, 0xFFFFFF):06x}"

    def reset_points(self):
        """Reset the points in the cluster"""

        self.points = []

    def add_point(self, point: Point):
        """Add a point to the cluster"""

        point.cluster_id = self.id
        point.color = self.color
        self.points.append(point)

    def update_centroid(self):
        """Update the centroid of the cluster with the new point average"""

        if len(self.points) == 0:
            return

        points = [point.vector for point in self.points]
        avaerage = np.mean(points, axis=0)

        self.centroid = Point(avaerage.tolist())

    def diameter(self) -> Tuple[float, Union[Point, None], Union[Point, None]]:
        """Calculate the diameter of the cluster, return the diameter and the two points that are the furthest apart"""

        max_distance = 0
        point1 = None
        point2 = None

        if len(self.points) == 0:
            return max_distance, point1, point2

        elif len(self.points) == 1:
            point1 = self.points[0]
            return max_distance, point1, point1

        coint = 0
        for p1, p2 in combinations(self.points, 2):
            coint += 1
            print(f"{coint}")
            current_distance = p1.distance(p2)

            if current_distance > max_distance:
                max_distance = current_distance
                point1 = p1
                point2 = p2

        return max_distance, point1, point2
