#!/usr/bin/env python3
"""
`subway` testing

@authors: Roman Yasinovskyy
@version: 2021.10
"""

import importlib
import pathlib
import sys
from typing import Generator

import pytest
import tomllib

try:
    importlib.util.find_spec(".".join(pathlib.Path(__file__).parts[-3:-1]), "src")
except ModuleNotFoundError:
    sys.path.append(f"{pathlib.Path(__file__).parents[3]}/")
finally:
    from src.projects.subway import find_routes, read_file


DATA_DIR = pathlib.Path("data/projects/subway/")
TIME_LIMIT = 1


def get_cases(category: str, *attribs: str) -> Generator:
    """Get test cases from the TOML file"""
    with open(pathlib.Path(__file__).with_suffix(".toml"), "rb") as file:
        all_cases = tomllib.load(file)
        for case in all_cases[category]:
            yield tuple(case.get(a) for a in attribs)


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "filename, expected", get_cases("test_case", "filename", "expected")
)
def test_subway(filename: str, expected: str):
    """Testing the path finding"""
    g, src, dst = read_file(DATA_DIR / pathlib.Path(filename))
    assert find_routes(g, src, dst) == expected


if __name__ == "__main__":
    pytest.main(["-v", __file__])
