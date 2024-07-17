from configparser import ConfigParser
import os

config = ConfigParser()
file1 = os.path.join(os.path.dirname(__file__), "config.ini")

def save_high_score(score):
    print(score)
    try:
        config.read(file1)
        if not config.has_section("player1"):
            config.add_section("player1")
        config.set("player1", "highscore", str(score))
        with open(file1, "w") as configfile:
            config.write(configfile)
    except Exception as e:
        print(f"Error saving high score: {e}")

def load_high_score():
    try:
        config.read(file1)
        if config.has_section("player1") and config.has_option("player1", "highscore"):
            return int(config.get("player1", "highscore"))
        else:
            return 0
    except Exception as e:
        print(f"Error loading high score: {e}")
        return 0
