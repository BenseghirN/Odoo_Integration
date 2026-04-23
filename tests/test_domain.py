import pytest
from mygamecollection.domain.entities.game import Game
from mygamecollection.domain.enums.game_status import GameStatus
from mygamecollection.domain.entities.genre import Genre
from mygamecollection.domain.entities.user import User
from mygamecollection.domain.entities.user_game import UserGame


class TestGameCreate:
    def test_create_valid_game(self):
        game = Game.create(igdb_id=1, name="Elden Ring")
        assert game.igdb_id == 1
        assert game.name == "Elden Ring"
        assert game.summary is None
        assert game.release_date is None
        assert game.cover_url is None
        assert game.id is None

    def test_create_game_with_all_fields(self):
        game = Game.create(
            igdb_id=1,
            name="Elden Ring",
            summary="An open world RPG",
            release_date="2022-02-25",
            cover_url="https://example.com/cover.jpg",
        )
        assert game.summary == "An open world RPG"
        assert game.release_date == "2022-02-25"
        assert game.cover_url == "https://example.com/cover.jpg"

    def test_create_game_empty_name_raises(self):
        with pytest.raises(ValueError, match="Game name cannot be empty"):
            Game.create(igdb_id=1, name="")

    def test_create_game_whitespace_name_raises(self):
        with pytest.raises(ValueError, match="Game name cannot be empty"):
            Game.create(igdb_id=1, name="   ")

    def test_create_game_has_empty_genres(self):
        game = Game.create(igdb_id=1, name="Elden Ring")
        assert game.genres == []

    def test_create_game_has_empty_user_games(self):
        game = Game.create(igdb_id=1, name="Elden Ring")
        assert game.user_games == []


class TestUserCreate:
    def test_create_valid_user(self):
        user = User.create(login="noris", first_name="Noris", last_name="Dev")
        assert user.login == "noris"
        assert user.first_name == "Noris"
        assert user.last_name == "Dev"
        assert user.id is None

    def test_create_user_empty_login_raises(self):
        with pytest.raises(ValueError, match="Login cannot be empty"):
            User.create(login="", first_name="Noris", last_name="Dev")

    def test_create_user_whitespace_login_raises(self):
        with pytest.raises(ValueError, match="Login cannot be empty"):
            User.create(login="   ", first_name="Noris", last_name="Dev")

    def test_create_user_empty_first_name_raises(self):
        with pytest.raises(ValueError, match="First name cannot be empty"):
            User.create(login="noris", first_name="", last_name="Dev")

    def test_create_user_empty_last_name_raises(self):
        with pytest.raises(ValueError, match="Last name cannot be empty"):
            User.create(login="noris", first_name="Noris", last_name="")

    def test_create_user_has_empty_user_games(self):
        user = User.create(login="noris", first_name="Noris", last_name="Dev")
        assert user.user_games == []


class TestGenreCreate:
    def test_create_valid_genre(self):
        genre = Genre.create(igdb_id=12, name="RPG")
        assert genre.igdb_id == 12
        assert genre.name == "RPG"
        assert genre.id is None

    def test_create_genre_empty_name_raises(self):
        with pytest.raises(ValueError, match="Genre name cannot be empty"):
            Genre.create(igdb_id=12, name="")

    def test_create_genre_whitespace_name_raises(self):
        with pytest.raises(ValueError, match="Genre name cannot be empty"):
            Genre.create(igdb_id=12, name="   ")

    def test_create_genre_has_empty_games(self):
        genre = Genre.create(igdb_id=12, name="RPG")
        assert genre.games == []


class TestUserGameCreate:
    def test_create_valid_user_game(self):
        user_game = UserGame.create(user_id=1, game_id=42)
        assert user_game.user_id == 1
        assert user_game.game_id == 42

    def test_create_user_game_default_status_is_todo(self):
        user_game = UserGame.create(user_id=1, game_id=42)
        assert user_game.status == GameStatus.TO_DO