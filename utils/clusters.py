from typing import List
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

    def update_centroid(self):
        """Update the centroid of the cluster with the new point average"""

        if len(self.points) == 0:
            return

        points = [point.vector for point in self.points]
        avaerage = np.mean(points, axis=0)

        self.centroid = Point(avaerage.tolist())
