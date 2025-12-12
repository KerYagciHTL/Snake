from src.entities.player import Player
from src.utils.config import WIDTH, HEIGHT, MAX_CELL_SIZE


class TestPlayer:
    def test_player_initialization(self):
        player = Player(5, 5)
        assert player.grid_x == 5
        assert player.grid_y == 5
        assert player.direction == (1, 0)
        assert player.alive is True

    def test_set_direction(self):
        player = Player(5, 5)
        player.set_direction(0, -1)
        assert player.direction == (0, -1)

    def test_prevent_reverse_direction(self):
        player = Player(5, 5)
        player.direction = (1, 0)
        player.set_direction(-1, 0)
        assert player.direction == (1, 0)

    def test_movement_after_delay(self):
        player = Player(5, 5)
        player.direction = (1, 0)
        player.update(150)
        assert player.grid_x == 6
        assert player.grid_y == 5

    def test_no_movement_before_delay(self):
        player = Player(5, 5)
        player.direction = (1, 0)
        player.update(100)
        assert player.grid_x == 5
        assert player.grid_y == 5

    def test_out_of_bounds_right(self):
        max_grid_x = WIDTH // MAX_CELL_SIZE
        player = Player(max_grid_x - 1, 5)
        player.direction = (1, 0)
        player.update(150)
        assert not player.alive

    def test_out_of_bounds_left(self):
        player = Player(0, 5)
        player.direction = (-1, 0)
        player.update(150)
        assert not player.alive

    def test_out_of_bounds_bottom(self):
        max_grid_y = HEIGHT // MAX_CELL_SIZE
        player = Player(5, max_grid_y - 1)
        player.direction = (0, 1)
        player.update(150)
        assert not player.alive

    def test_out_of_bounds_top(self):
        player = Player(5, 0)
        player.direction = (0, -1)
        player.update(150)
        assert not player.alive

    def test_dead_player_cannot_move(self):
        player = Player(5, 5)
        player.alive = False
        player.direction = (1, 0)
        player.update(150)
        assert player.grid_x == 5
        assert player.grid_y == 5