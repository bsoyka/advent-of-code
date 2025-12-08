from part1 import calculate_distance, pair_junctions_by_distance
from pytest import approx

EXAMPLE_INPUT = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""


def test_calculate_distance():
    assert calculate_distance("162,817,812", "425,690,689") == approx(316.902)


def test_pair_junctions_by_distance():
    junction_pairs = pair_junctions_by_distance(EXAMPLE_INPUT.splitlines(), 4)
    junction_pairs_no_distances = [(p[1], p[2]) for p in junction_pairs]

    expected_pairs = [
        ("162,817,812", "425,690,689"),
        ("162,817,812", "431,825,988"),
        ("906,360,560", "805,96,715"),
        ("431,825,988", "425,690,689"),
    ]

    assert junction_pairs_no_distances == expected_pairs
