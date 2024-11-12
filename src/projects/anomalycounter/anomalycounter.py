#!/usr/bin/env python3
"""
`anomalycounter` implementation and driver

@authors:
@version: 2024.10
"""

import argparse
from pathlib import Path


def count(filename: Path, sides: int) -> int:
    """Count number of anomalies/blobs in an image

    :param filename: name of the file to process
    :return: number of anomalies/blobs in the file
    """
    # entry to the file parsing alg
    parsed = parse_file(filename)
    return comb(parsed, sides)


def parse_file(filename: Path) -> list[list[str]]:
    """
    python implementation of pseudocode: test 
    """
    outer_list = []
    inner_list = []
    file = open(filename, "r")
    lines = file.readlines()
    for line in lines:
        inner_list = []
        for char in line:
            if char != "\n":
                inner_list.append(char)
        outer_list.append(inner_list)
    return outer_list


def flood(bitmap: list[list[str]], row, col, sides: int) -> None:
    """
    flood fill alg, fill in area of each blob, two fns: one for 8 and one for 4
    """
    class Scan:
        ANOMALY = "*"

        def __init__(self, bitmap, row, col):
            self.bitmap = bitmap
            self.row = row
            self.col = col
            self.borders = (
                # upper border
                row - 1 >= 0,
                # left border
                col - 1 >= 0,
                # right border
                col + 1 < len(bitmap[0]),
                # bottom border
                row + 1 < len(bitmap)
            )
            self.edges = {
                "upper": self.borders[0],
                "left": self.borders[1],
                "right": self.borders[2],
                "lower": self.borders[3],
                "upper-left": self.borders[0] and self.borders[1],
                "upper-right": self.borders[0] and self.borders[2],
                "lower-left": self.borders[3] and self.borders[1],
                "lower-right": self.borders[3] and self.borders[2]
            }

        def get_tile(self,row ,col):
            return self.bitmap[row][col]

        def is_safe(self, direction: str) -> bool:
            return self.edges[direction]

        def upper(self) -> bool:
            if self.is_safe("upper"):
                return self.get_tile(self.row - 1, self.col) == self.ANOMALY

        def left(self) -> bool:
            if self.is_safe("left"):
                return self.get_tile(self.row, self.col - 1) == self.ANOMALY

        def right(self) -> bool:
            if self.is_safe("right"):
                return self.get_tile(self.row, self.col + 1) == self.ANOMALY

        def lower(self) -> bool:
            if self.is_safe("lower"):
                return self.get_tile(self.row + 1, self.col) == self.ANOMALY

        def upper_left(self) -> bool:
            if self.is_safe("upper-left"):
                return self.get_tile(self.row - 1, self.col - 1) == self.ANOMALY

        def upper_right(self) -> bool:
            if self.is_safe("upper-right"):
                return self.get_tile(self.row - 1, self.col + 1) == self.ANOMALY

        def lower_left(self) -> bool:
            if self.is_safe("lower-left"):
                return self.get_tile(self.row + 1, self.col - 1) == self.ANOMALY

        def lower_right(self) -> bool:
            if self.is_safe("lower-right"):
                return self.get_tile(self.row + 1, self.col + 1) == self.ANOMALY

    # mark current tile as blank !!! using . here, I think space would also work
    blank = "."
    bitmap[row][col] = blank
    # begin recursion, cardinal directions(for both 4 and 8 parsings)
    scan = Scan(bitmap, row, col)
    if sides == 4:
        """
         0
      1     2
         3
        """
        tiles = scan.upper(), scan.left(), scan.right(), scan.lower()
        if tiles[0]:
            flood(bitmap, row - 1, col, sides)
        if tiles[1]:
            flood(bitmap, row, col - 1, sides)
        if tiles[2]:
            flood(bitmap, row, col + 1, sides)
        if tiles[3]:
            flood(bitmap, row + 1, col, sides)

    else:  # sides == 8
        assert sides == 8
        """
        0 1 2
        3   4
        5 6 7
        """
        tiles = (
                scan.upper_left(), scan.upper(), scan.upper_right(),
                scan.left(), scan.right(),
                scan.lower_left(), scan.lower(), scan.lower_right()
            )
        if tiles[0]:
            flood(bitmap, row - 1, col - 1, sides)
        if tiles[1]:
            flood(bitmap, row - 1, col, sides)
        if tiles[2]:
            flood(bitmap, row - 1, col + 1, sides)
        if tiles[3]:
            flood(bitmap, row, col - 1, sides)
        if tiles[4]:
            flood(bitmap, row, col + 1, sides)
        if tiles[5]:
            flood(bitmap, row + 1, col - 1, sides)
        if tiles[6]:
            flood(bitmap, row + 1, col, sides)
        if tiles[7]:
            flood(bitmap, row + 1, col + 1, sides)


def comb(bitmap: list[list[str]], sides: int) -> int:
    """
    search for next blob, when found call flood and increment counter
    """
    anomaly_counter = 0
    for row in range(len(bitmap)):
        for col in range(len(bitmap[row])):
            if bitmap[row][col] == "*":
                # if anomaly found, call flood
                flood(bitmap, row, col, sides)
                anomaly_counter += 1

    return anomaly_counter


def main():
    """Entry point"""

    parser = argparse.ArgumentParser(
        description="Specify adjacency rule (4 or 8 sides)"
    )
    parser.add_argument("--sides", type=int, choices=[4, 8], required=True)

    args = parser.parse_args()
    
    data_dir = "data/projects/anomalycounter/"
    for file in sorted(Path(data_dir).glob("*.in")):
        print(f"{file.name}: {count(file, args.sides)}")


if __name__ == "__main__":
    main()
