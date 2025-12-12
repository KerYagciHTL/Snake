from src.entities.grid import Grid
from src.utils.config import MAX_CELL_SIZE


class TestGrid:
    def test_grid_initialization(self):
        grid = Grid(800, 600)
        assert grid.width == 800
        assert grid.height == 600

    def test_grid_cell_size(self):
        assert MAX_CELL_SIZE == 32

    def test_grid_dimensions(self):
        width, height = 800, 600
        Grid(width, height)
        expected_cols = width // MAX_CELL_SIZE
        expected_rows = height // MAX_CELL_SIZE
        assert expected_cols == 25
        assert expected_rows == 18
