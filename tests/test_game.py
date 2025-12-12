import pytest
import pygame
from src.game import Game


class TestGame:
    @pytest.fixture
    def game(self):
        game = Game()
        yield game
        pygame.quit()

    def test_game_initialization(self, game):
        assert game.running is True
        assert game.player is not None
        assert game.grid is not None

    def test_game_stops_when_player_dies(self, game):
        game.player.alive = False
        game.update(0)
        assert game.running is False

    def test_escape_key_stops_game(self, game):
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_ESCAPE)
        pygame.event.post(event)
        game.handle_events()
        assert game.running is False

    def test_quit_event_stops_game(self, game):
        event = pygame.event.Event(pygame.QUIT)
        pygame.event.post(event)
        game.handle_events()
        assert game.running is False
