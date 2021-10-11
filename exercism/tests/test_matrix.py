from ..matrix import Matrix


def test_extract_row_from_one_number_matrix():
    matrix = Matrix('1')
    assert matrix.row(1) == [1]


def test_can_extract_row():
    matrix = Matrix('1 2\n3 4')
    assert matrix.row(2) == [3, 4]


def test_extract_row_where_numbers_have_different_widths():
    matrix = Matrix('1 2\n10 20')
    assert matrix.row(2) == [10, 20]


def test_can_extract_row_from_non_square_matrix_with_no_corresponding_column():
    matrix = Matrix('1 2 3\n4 5 6\n7 8 9\n8 7 6')
    assert matrix.row(4) == [8, 7, 6]


def test_extract_column_from_one_number_matrix():
    matrix = Matrix('1')
    assert matrix.column(1) == [1]


def test_can_extract_column():
    matrix = Matrix('1 2 3\n4 5 6\n7 8 9')
    assert matrix.column(3) == [3, 6, 9]


def test_can_extract_column_from_non_square_matrix_with_no_corresponding_row():
    matrix = Matrix('1 2 3 4\n5 6 7 8\n9 8 7 6')
    assert matrix.column(4) == [4, 8, 6]


def test_extract_column_where_numbers_have_different_widths():
    matrix = Matrix('89 1903 3\n18 3 1\n9 4 800')
    assert matrix.column(2) == [1903, 3, 4]
