from typing import Callable, Dict, List

aliens: Dict[str, List[Callable]] = {
    'TroyMartian': [lambda d: d['antennae'] >= 3, lambda d: d['eyes'] <= 4],
    'VladSaturnian': [lambda d: d['antennae'] <= 6, lambda d: d['eyes'] >= 2],
    'GraemeMercurian': [
        lambda d: d['antennae'] <= 2,
        lambda d: d['eyes'] <= 3,
    ],
}

description: Dict[str, int] = {'antennae': int(input()), 'eyes': int(input())}

for alien, criteria in aliens.items():
    if all(criterion(description) for criterion in criteria):
        print(alien)
