#ThorPy minigame tutorial. Guess the number : play game
import thorpy, thorpy_game_full_code_part_1_game_code #note that mygame.py must be in the same folder

application = thorpy.Application(size=(600, 400), caption="Guess the number max val 100 min val 0")
mygame = thorpy_game_full_code_part_1_game_code.MyGame(player_name="Jack", min_val=0, max_val=100, trials=101)
mygame.launch_game()
application.quit()
