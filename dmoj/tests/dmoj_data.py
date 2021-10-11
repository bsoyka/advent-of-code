from typing import Dict, List, Tuple

from pytest import approx

problems: Dict[str, List[Tuple]] = {
    'a1': [
        (
            [4, '4 MISSPELL', '1 PROGRAMMING', '7 CONTEST', '3 BALLOON'],
            ['1 MISPELL', '2 ROGRAMMING', '3 CONTES', '4 BALOON'],
        )
    ],
    'a2': [
        (
            ['Fr', 'qp', 'HH', 'db', '  ', 'pq'],
            [
                'Ready',
                'Ordinary pair',
                'Mirrored pair',
                'Ordinary pair',
                'Mirrored pair',
            ],
        )
    ],
    'a3': [([1, 1], 192)],
    'a4b1': [([4, 4, 3, 2, 1], [1, 2, 3, 4])],
    'acmtryouts0a': [([2, 4, 2, 5, 3, 5, 1, 1], [5, 1])],
    'acmtryouts0b': [([2, 1, 'A', 'B', 3, 'ZEO', 'NXF'], ['BA', 'FOXENZ'])],
    'acmtryouts1a': [
        (
            [5, 'Scissors', 'Fox', 'Rock', 'Foxen', 'Paper'],
            ['Rock', 'Foxen', 'Paper'],
        )
    ],
    'alphabetscore': [(['python'], [98]), (['qwertytown'], [180])],
    'aplusb': [([2, '1 1', '-1 0'], [2, -1])],
    'art0': [
        (
            [2, 'astrocat879', 'skyflaren'],
            ['Hi! Follow me! Hi! Yes! Yes! Yes!', 'Hi! Bye!'],
        )
    ],
    'avatarearth': [(['4 6', '3 5 5 7'], 'Yes')],
    'avatarwater': [([12, 17, 12], 5)],
    'bf1': [([3, 5, 8, 2], [2, 5, 8])],
    'bfs17p1': [
        ([5, 'Piano Programming Pottery Protesting Pen-spinning'], 3),
        ([3, 'Photography Photography Photography'], 0),
        (
            [
                8,
                'Paintball Parkour Poker Philately Poker Puzzles Puzzles Photography',
            ],
            7,
        ),
    ],
    'boolean': [('not not True', [True]), ('not not not False', [True])],
    'catlove': [
        ([4, 'cats', 'cats', 'dogs', 'cats'], 'cats'),
        ([6, 'cats', 'cats', 'dogs', 'cats', 'dogs', 'dogs'], 'equal'),
    ],
    'ccc04j1': [
        (9, 'The largest square has side length 3.'),
        (8, 'The largest square has side length 2.'),
        (7535, 'The largest square has side length 86.'),
    ],
    'ccc04j3': [
        (
            [3, 2, 'Easy', 'Smart', 'Soft', 'pie', 'rock'],
            [
                'Easy as pie',
                'Easy as rock',
                'Smart as pie',
                'Smart as rock',
                'Soft as pie',
                'Soft as rock',
            ],
        )
    ],
    'ccc06j1': [([2, 1, 3, 4], 'Your total Calorie count is 649.')],
    'ccc07j1': [([10, 5, 8], 8)],
    'ccc07j3': [
        ([2, 3, 8, 198000], 'no deal'),
        ([8, 10, 9, 8, 7, 6, 5, 4, 3, 400], 'deal'),
    ],
    'ccc08j1': [
        ([69, 1.73], 'Normal weight'),
        ([84.5, 1.8], 'Overweight'),
    ],
    'ccc11j1': [
        ([4, 5], ['VladSaturnian']),
        ([2, 3], ['VladSaturnian', 'GraemeMercurian']),
        ([8, 6], []),
    ],
    'ccc12j1': [
        ([40, 39], 'Congratulations, you are within the speed limit!'),
        ([100, 131], 'You are speeding and your fine is $500.'),
        ([100, 120], 'You are speeding and your fine is $100.'),
    ],
    'ccc12j2': [
        ([30, 10, 20, 20], 'No Fish'),
        ([1, 10, 12, 13], 'Fish Rising'),
    ],
    'ccc13j1': [([12, 15], [18]), ([10, 10], [10])],
    'ccc13j2': [('SHINS', 'YES'), ('NOISE', 'NO')],
    'ccc14j1': [([60, 70, 50], 'Scalene'), ([60, 75, 55], 'Error')],
    'ccc14j2': [([6, 'ABBABB'], 'B'), ([6, 'ABBABA'], 'Tie')],
    'ccc15j1': [([1, 7], 'Before'), ([8, 31], 'After'), ([2, 18], 'Special')],
    'ccc15j2': [
        ('How are you :-) doing :-( today :-)?', 'happy'),
        (':)', 'none'),
        ('This :-(is str :-(:-a(nge te:-)xt.', 'sad'),
    ],
    'ccc16j1': [
        (['W', 'L', 'W', 'W', 'L', 'W'], 2),
        (
            [
                'L',
                'L',
                'L',
                'L',
                'L',
                'L',
            ],
            -1,
        ),
    ],
    'ccc17j1': [([12, 5], 1), ([9, -13], 4)],
    'coci06c2p1': [('11 15', 19), ('4 3', 2)],
    'coci07c2p1': [
        ('0 1 2 2 2 7', '1 0 0 0 0 1'),
        ('2 1 2 1 2 1', '-1 0 0 1 0 7'),
    ],
    'coci09c4p1': [
        ('Knuth-Morris-Pratt', 'KMP'),
        ('Mirko-Slavko', 'MS'),
        ('Pasko-Patak', 'PP'),
    ],
    'dmopc14c5p1': [([3, 5], lambda r: float(r[0]) == approx(47.12, 0.01))],
    'dmopc14c5p2': [([3, '1 8', '9 150', '0 81'], 141)],
    'dmopc15c7p2': [('problem one is really long', 5)],
    'dmopc17c3p1': [([5, '98 -20 96 100 96'], -20), ([4, '3 3 1 1'], 1)],
    'dmopc19c5p0': [
        (
            [
                '5 55',
                'georgechen 24',
                'kevinwan 42',
                'tankibuds 56',
                'richardzhang 1',
                'tzak 99',
            ],
            [
                'georgechen will not advance',
                'kevinwan will not advance',
                'tankibuds will advance',
                'richardzhang will not advance',
                'tzak will advance',
            ],
        )
    ],
    'dmopc19c6p0': [('1 2 3', 'no'), ('1 2 2', 'yes')],
    'dmopc20c1p1': [
        (
            [4, 'MXACY', 'CZBNP', 'PQRST', 'PQRMS'],
            ['NEGATIVE MARKS', 'FAIL', 'PASS', 'FAIL'],
        )
    ],
    'dwite09c4p1': [([150, 1, 9000, 500, 501], [60, 9000, 1, 18, 18])],
    'gfssoc1j1': [([5, 3, 1, 7, 5], 2)],
    'helloworld': [([], 'Hello, World!')],
    'p154ex8': [(6, lambda r: sorted(r) == ['1', '2', '3', '6'])],
    'p184ex8': [([5, 'A', 'B', 'C', 'B', '%'], [1, 2, 1, 0, 0, 0, 1])],
    'pib20p1': [([5, '-1 -5 3 2 0'], 2)],
    'set': [([2, 1, 2], 2), ([4, 1, 2, 2, 5], 3)],
    'si17c1p10': [
        ([4, '1 2 3 4', '3 5 3 1', 3, '10 4 60', '3 20 1'], '26 170')
    ],
    'towers': [([5, '1 3 4 2 5'], 1)],
    'tss17a': [
        (
            [
                4,
                'JOIN JOIN JOI',
                'COMP CMP COMP',
                'CLAB CLUB CLUB',
                'TODAY TWODAY TOODAY',
            ],
            ['JOIN', 'COMP', 'CLUB', '???'],
        ),
        (
            [
                3,
                'DELSYS32 DELSYS33 DELSYS33',
                'SHOTDOWN SHUTDOWN SHUTOFF',
                'RESTART RESTART RESTART',
            ],
            ['DELSYS33', '???', 'RESTART'],
        ),
    ],
    'ucc20p1': [([10, '0101110101', '1101010011'], 2)],
    'ucc20p2': [([3, '1 10', '3 3 5 3', '2 1 8'], 9)],
    'valentines19j2': [
        (
            [
                5,
                '0 0 0',
                '240 200 220',
                '243 12 120',
                '12 3 10',
                '241 100 221',
            ],
            2,
        )
    ],
    'vmss7wc16c5p1': [('5 3', 10), ('1 3', 2)],
    'vpex1p0': [('5 2', '2 1'), ('9 3', '3 0')],
    'waterloow2017a': [(1, 0), (2, 2), (5, 20)],
    'wc16c1j1': [(5, 'spoooooky')],
    'wc17c1j1': [('Snow', 'Snow, eh')],
    'wc17c2j1': [('3 7 9', 20)],
    'wc17c4j1': [(['Run', 'Run'], 'Run'), (['Fight', 'Run'], 'Undecided')],
    'wc18c1j1': [([2, 3, 9], 'Y'), ([4, 3, 11], 'N')],
    'wc18c1j2': [
        (['bob', 'alice', 'bob', 'christine', 'david', 'erika'], 'Y'),
        (['alice', 'frank', 'georgia', 'hans', 'ilia', 'james'], 'N'),
    ],
    'wc18c2j2': [('2:07', 127)],
    'wc18c3j1': [([14, 3, 10], 42)],
}
