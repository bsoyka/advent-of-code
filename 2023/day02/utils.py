AVAILABLE_CUBES = {"red": 12, "green": 13, "blue": 14}


class CubeGame:
    game_id: int
    cube_reveals: list[dict[str, int]]

    def __init__(self, input_string: str):
        # input_string format example:
        # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green

        # Strip "Game "
        input_string = input_string[5:]

        game_id_string, cube_reveals_string = input_string.split(": ")

        self.game_id = int(game_id_string)

        self.cube_reveals = []
        for cube_reveal_string in cube_reveals_string.split("; "):
            cube_reveal: dict[str, int] = {}
            for cube_item in cube_reveal_string.split(", "):
                count_string, color_string = cube_item.split()
                cube_reveal[color_string] = int(count_string)
            self.cube_reveals.append(cube_reveal)

    @property
    def is_possible(self) -> bool:
        for cube_reveal in self.cube_reveals:
            for available_color, available_count in AVAILABLE_CUBES.items():
                shown_count = cube_reveal.get(available_color, 0)
                if shown_count > available_count:
                    return False

        return True

    @property
    def minimum_cubes_by_color(self) -> dict[str, int]:
        minimum_cubes: dict[str, int] = {}

        for cube_reveal in self.cube_reveals:
            for color, count in cube_reveal.items():
                if count > minimum_cubes.get(color, 0):
                    minimum_cubes[color] = count

        return minimum_cubes
