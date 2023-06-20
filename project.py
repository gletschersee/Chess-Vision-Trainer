"""
Chess Vision Trainer v.1.0 by Gletschersee
--------------------------------------------------------------------------
This code creates a "Chess Vision Trainer" with a GUI per use of pygame.
The resulting app allows users to train their knowledge of chess square names
per modern/ standard/ algebraic notation in a gamified way.
"""
import pygame as g
import random as r
import csv


def main():
    """
    Opens, runs, and closes the GUI, calling all the required functions while doing so.
    """
    # The GUI is initialized and variables are introduced with their default value.
    g.init()
    g.display.set_icon(g.image.load("graphics/cvt_classical70x70.png"))
    g.display.set_caption("Chess Vision Trainer v.1.0 - Gletschersee")
    screen = g.display.set_mode((500, 700))
    clock = g.time.Clock()
    screen.fill(g.Color("white"))
    draw_board(screen)
    run = True
    menu = "home"
    user = "guest_session"
    feedback = welcome(user)
    to_find = get_to_find()
    score = 0
    highscore = 0
    lives = 3
    old_seconds_value = 0
    seconds_displayed = 5
    records = []
    mode = "classical"
    # The app will run as long as it is not closed.
    while run:
        # This part creates a countdown for the timed mode.
        # It is outside of the following for loop, to update the countdown also without user interaction.
        if menu == "home" and mode == "timed":
            # The counter is introduced.
            seconds = (g.time.get_ticks() - tick_counter) / 1000
            # If necessary, the counter is displayed or is being reset.
            if int(seconds) != old_seconds_value:
                # Update the countdown to the new value.
                if int(seconds) == 0:
                    seconds_displayed = 5
                elif int(seconds) > 0:
                    seconds_displayed -= 1
                old_seconds_value = int(seconds)
                if seconds_displayed == 0:
                    # If the time is up, treat the "round" as over.
                    tick_counter = g.time.get_ticks()
                    old_seconds_value = 0
                    seconds_displayed = 5
                    if user != "guest_session":
                        # The score is saved.
                        if score > 0:
                            with open("record_logbook.csv", "a", newline="") as file:
                                writer = csv.DictWriter(
                                    file, fieldnames=["user", "score", "mode"]
                                )
                                writer.writerow(
                                    {"user": user, "score": score, "mode": mode}
                                )
                                records.append(
                                    {"user": user, "score": score, "mode": mode}
                                )
                    feedback = get_feedback(None, "Time's up!", score, highscore)
                    score = 0
            # The countdown timer is updated on the screen.
            menu_home(
                screen, to_find, score, highscore, user, menu, mode, seconds_displayed
            )
            write_feedback(screen, feedback)
            g.display.flip()
        # Every time the app experiences user interaction, the app reacts, if necessary.
        for event in g.event.get():
            # The app closes if desired.
            if event.type == g.QUIT:
                run = False
            # The records from the CSV file are gathered.
            with open("record_logbook.csv") as file:
                reader = csv.DictReader(file)
                records = []
                for i in list(reader):
                    records.append(
                        {
                            "user": i.get("user"),
                            "score": i.get("score"),
                            "mode": i.get("mode"),
                        }
                    )
            # The screen is updated according to the current menu.
            if menu == "home":
                menu_home(
                    screen,
                    to_find,
                    score,
                    highscore,
                    user,
                    menu,
                    mode,
                    seconds_displayed,
                )
            elif menu == "user":
                menu_user(screen, to_find, score, highscore, user, menu, records, menu)
                write_records(screen, records, user, mode)
            show_mode(screen, mode)
            # The maximum FPS of the app.
            clock.tick(80)
            if event.type == g.MOUSEBUTTONDOWN:
                # For every mouse click, check...
                if g.mouse.get_pressed()[0]:
                    # For every left click, check...
                    # Call the click_handler function to understand what the user clicked on.
                    click = click_handler(g.mouse.get_pos(), menu, mode)
                    if click == "User button":
                        # "User button" is not only leading to the user menu,
                        # but also from the user menu back to the home menu.
                        if menu == "home":
                            menu = "user"
                            menu_user(
                                screen,
                                to_find,
                                score,
                                highscore,
                                user,
                                menu,
                                records,
                                mode,
                            )
                            feedback = None
                        elif menu == "user":
                            menu = "home"
                            menu_home(
                                screen,
                                to_find,
                                score,
                                highscore,
                                user,
                                menu,
                                mode,
                                seconds_displayed,
                            )
                            feedback = welcome(user)
                    elif click == "Switch button":
                        # The switch button is in the user menu.
                        # It is pressed to switch the user.
                        new_user = switch_user(screen)
                        if new_user == False:
                            run = False
                        elif new_user != None:
                            # If the user is being switched, update the scores.
                            user = new_user.lower()
                            if user != "guest_session":
                                user_scores = []
                                for i in records:
                                    if i.get("user") == user and i.get("mode") == mode:
                                        user_scores.append(i.get("score"))
                                if len(user_scores) > 0:
                                    highscore = int(max(user_scores))
                                else:
                                    highscore = 0
                            else:
                                score = 0
                                highscore = 0
                    elif click in ["classical", "lives", "timed"]:
                        # These clicks are the result of clicking on the mode icon in the top left corner.
                        if user != "guest_session":
                            # The score is saved.
                            if score > 0:
                                with open(
                                    "record_logbook.csv", "a", newline=""
                                ) as file:
                                    writer = csv.DictWriter(
                                        file, fieldnames=["user", "score", "mode"]
                                    )
                                    writer.writerow(
                                        {"user": user, "score": score, "mode": mode}
                                    )
                                    records.append(
                                        {"user": user, "score": score, "mode": mode}
                                    )
                        # The mode is changed.
                        mode = click
                        if user != "guest_session":
                            # The scores are updated.
                            user_scores = []
                            for i in records:
                                if i.get("user") == user and i.get("mode") == mode:
                                    user_scores.append(i.get("score"))
                                if len(user_scores) > 0:
                                    highscore = int(max(user_scores))
                                else:
                                    highscore = 0
                        else:
                            highscore = 0
                        # Mode-specific and -nonspecific values are reset.
                        lives = 3
                        if mode == "timed":
                            tick_counter = g.time.get_ticks()
                            old_seconds_value = 0
                            seconds_displayed = 5
                        score = 0
                        # Update the feedback value at the bottom of the screen.
                        feedback = get_feedback(click, None, None, None)
                    elif click != None:
                        # If a square on the chessboard is clicked, validate the guess.
                        validation_result = validate_guess(click, to_find, mode, lives)
                        if validation_result[0] != "Correct!" and mode == "lives":
                            highlight_square(screen, to_find, False)
                        elif validation_result[0] != "Correct!" and mode != "lives":
                            highlight_square(screen, click, False)
                        if validation_result[0] == "Correct!":
                            highlight_square(screen, click, True)
                            score += 1
                            if score > highscore:
                                highscore = score
                            feedback = get_feedback(
                                click, validation_result[0], score, highscore
                            )
                            if mode == "timed":
                                tick_counter = g.time.get_ticks()
                                old_seconds_value = 0
                                seconds_displayed = 5
                        elif validation_result[0] == "Try again!":
                            # Reset game variables and save the score if logged in.
                            lives = 3
                            if mode == "timed":
                                tick_counter = g.time.get_ticks()
                                old_seconds_value = 0
                                seconds_displayed = 5
                            if user != "guest_session":
                                if score > 0:
                                    with open(
                                        "record_logbook.csv", "a", newline=""
                                    ) as file:
                                        writer = csv.DictWriter(
                                            file, fieldnames=["user", "score", "mode"]
                                        )
                                        writer.writerow(
                                            {"user": user, "score": score, "mode": mode}
                                        )
                                        records.append(
                                            {"user": user, "score": score, "mode": mode}
                                        )
                            # Update the feedback value at the bottom of the screen.
                            feedback = get_feedback(
                                click, validation_result[0], score, highscore
                            )
                            score = 0
                        elif validation_result[0] == "Two lives remaining.":
                            lives = 2
                            feedback = get_feedback(
                                click, validation_result[0], score, highscore
                            )
                        elif validation_result[0] == "One life remaining.":
                            lives = 1
                            feedback = get_feedback(
                                click, validation_result[0], score, highscore
                            )
                        if validation_result[0] == "Nope. Tick Tock...":
                            feedback = get_feedback(
                                click, validation_result[0], score, highscore
                            )
                        if validation_result[1]:
                            # Generate a new square that the user shall find.
                            to_find = get_to_find()
            # Update the screen and write the feedback.
            write_feedback(screen, feedback)
            g.display.flip()


def show_mode(screen, mode):
    """Displaying the logo of each mode in the top left corner.

    Args:
        screen (g.display.set_mode): The pygame call for creating a window.
        mode (str): One of the three modes of the Chess Vision Trainer.
    """
    classical_logo = g.image.load("graphics/cvt_classical70x70.png")
    lives_logo = g.image.load("graphics/cvt_lives70x70.png")
    timed_logo = g.image.load("graphics/cvt_timed70x70.png")
    if mode == "classical":
        screen.blit(classical_logo, (410, 15))
    elif mode == "lives":
        screen.blit(lives_logo, (410, 15))
    elif mode == "timed":
        screen.blit(timed_logo, (410, 15))


def menu_home(screen, to_find, score, highscore, user, menu, mode, seconds_displayed):
    """Calling all the functions required to handle the home menu.

    Args:
        screen (g.display.set_mode): The pygame call for creating a window.
        to_find (str): String of the notation for the square that the user should find.
        score (int): Score of that particular user in that particular mode.
        highscore (int): Highscore of that particular user in that particular mode.
        user (str): Name of the user.
        menu (str): "home", one of the two menus of Chess Vision Trainer.
        mode (str): One of the three modes of the Chess Vision Trainer.
        seconds_displayed (int): Seconds that shall be used for the countdown in the timed mode.
    """
    draw_background_home(screen, mode)
    draw_board(screen)
    write_info(screen, to_find, score, highscore, user, menu)
    show_mode(screen, mode)
    if mode == "timed":
        draw_timer(screen, seconds_displayed)


def draw_background_home(screen, mode):
    """Draws the background for the home menu on the screen.

    Args:
        screen (g.display.set_mode): The pygame call for creating a window.
        mode (str): One of the three modes of the Chess Vision Trainer.
    """
    # Draw complete background.
    g.draw.rect(screen, "dark green", g.Rect(0, 0, 500, 700))
    # Draw frame.
    screen.blit(g.image.load(f"graphics/{mode}_frame500x700.png"), (0, 0))
    # Draw logo and info frame.
    g.draw.rect(screen, "lightpink4", g.Rect(40, 40, 420, 160))
    # Draw logo frame and write logo text.
    g.draw.rect(screen, "peachpuff4", g.Rect(50, 50, 400, 50))
    font = g.font.SysFont("bahnschrift", 35)
    logo = font.render("Chess Vision Trainer", 1, ("cornsilk"))
    screen.blit(logo, (85, 60))
    # Draw info frame.
    g.draw.rect(screen, "cornsilk", g.Rect(50, 100, 400, 90))
    # Draw the user button and write the user button text.
    g.draw.rect(screen, "peachpuff4", g.Rect(260, 110, 180, 35))
    font = g.font.SysFont("bahnschrift", 35)
    user_button = font.render("User", 1, ("cornsilk"))
    screen.blit(user_button, (312, 112))
    # Draw chessboard frame.
    g.draw.rect(screen, "lightpink4", g.Rect(40, 240, 420, 420))


def draw_board(screen):
    """Draws the chessboard on the screen.

    Args:
        screen (g.display.set_mode): The pygame call for creating a window.
    """
    x = 100
    y = 250
    s = 50
    # Draw the background for the chessboard.
    g.draw.rect(screen, "cornsilk", g.Rect(50, 250, 400, 400))
    # Draw the chessboard itself.
    odd_row = True
    while y < 610:
        while x < 410:
            g.draw.rect(screen, "peachpuff4", g.Rect(x, y, s, s))
            x += 100
        if odd_row:
            x = 50
        else:
            x = 100
        odd_row = not odd_row
        y += 50


def highlight_square(screen, to_highlight, correct_boolean):
    """Highlights a square as correct (green) or incorrect (red).

    Args:
        screen (g.display.set_mode): The pygame call for creating a window.
        to_highlight (str): String of the notation for the square that shall be highlighted.
        correct_boolean (boolean): Hint on whether the square shall be treated as correct or incorrect.
    """
    x, y = square_to_position_translator(to_highlight)
    if correct_boolean:
        color = "dark green"
    else:
        color = "indianred4"
    g.draw.rect(screen, color, g.Rect(x, y, 50, 50))


def menu_user(screen, to_find, score, highscore, user, menu, records, mode):
    """Calling all the functions required to handle the home user.

    Args:
        screen (g.display.set_mode): The pygame call for creating a window.
        to_find (str): String of the notation for the square that the user should find.
        score (int): Score of that particular user in that particular mode.
        highscore (int): Highscore of that particular user in that particular mode.
        user (str): Name of the user.
        menu (str): "user", one of the two menus of Chess Vision Trainer.
        records (lst): List of all the entries in record_logbook.csv.
        mode (str): One of the three modes of the Chess Vision Trainer.
    """
    draw_background_user(screen)
    write_info(screen, to_find, score, highscore, user, menu)
    show_mode(screen, mode)
    write_records(screen, records, user, mode)


def draw_background_user(screen):
    """Draws the background for the user menu on the screen.

    Args:
        screen (g.display.set_mode): The pygame call for creating a window.
    """
    # Draw complete background.
    g.draw.rect(screen, "dark green", g.Rect(0, 0, 500, 700))
    # Draw frame.
    g.draw.rect(screen, "lightpink4", g.Rect(40, 40, 420, 620))
    # Draw logo frame and write logo text.
    g.draw.rect(screen, "peachpuff4", g.Rect(50, 50, 400, 50))
    font = g.font.SysFont("bahnschrift", 35)
    logo = font.render("Chess Vision Trainer", 1, ("cornsilk"))
    screen.blit(logo, (85, 60))
    # Draw top frame.
    g.draw.rect(screen, "cornsilk", g.Rect(50, 100, 400, 90))
    # Draw the home button and write the home button text.
    g.draw.rect(screen, "peachpuff4", g.Rect(260, 110, 180, 35))
    font = g.font.SysFont("bahnschrift", 35)
    home_button = font.render("Home", 1, ("cornsilk"))
    screen.blit(home_button, (302, 112))
    # Draw change user button and write change user button text.
    font = g.font.SysFont("bahnschrift", 35)
    g.draw.rect(screen, "peachpuff4", g.Rect(60, 110, 180, 35))
    change_user_button = font.render(f"Switch", 1, ("cornsilk"))
    screen.blit(change_user_button, (95, 112))
    # Draw the bottom frame.
    g.draw.rect(screen, "cornsilk", g.Rect(50, 200, 400, 450))


def write_records(screen, records, user, mode):
    """Writes the scoreboard in the user menu on the screen.

    Args:
        screen (g.display.set_mode): The pygame call for creating a window.
        records (lst): List of all the entries in record_logbook.csv.
        user (str): Name of the user.
        mode (str): One of the three modes of the Chess Vision Trainer.
    """
    # Introduce a set of users so that every user will only be displayed once,
    # with their high score for that mode, on the scoreboard.
    users = set()
    for i in records:
        users.add(i.get("user"))
    # Sort the information from the CSV file based on the score.
    sorted_records = []
    for i in reversed(sorted(records, key=lambda i: int(i["score"]))):
        # Filter the information based on the selected mode.
        if i["mode"] == mode:
            sorted_records.append(i)
    # Write the scoreboard.
    font = g.font.SysFont("bahnschrift", 30)
    y = 210
    n = 1
    for i in sorted_records:
        user_info = i.get("user")
        score_info = i.get("score")
        if user_info in users:
            # Check so that only the high score and no other scores are displayed for each user.
            color = "peachpuff4"
            # Highlight any potential entry of the user that is currently logged in.
            if user_info == user:
                color = "indianred4"
            # Write the scoreboard.
            count_record = font.render(f"{n}", 1, color)
            single_record = font.render(f"| {user_info} scored {score_info}", 1, color)
            screen.blit(count_record, (70, y))
            screen.blit(single_record, (90, y))
            users.remove(i.get("user"))
            y += 50
            n += 1
            # Do not allow the scoreboard to print more entries than fit in the designated scoreboard size.
            if n == 10:
                break
        else:
            continue


def get_to_find():
    """Generate the notation of a random square on the chessboard.

    Returns:
        str: Notation of a chess square that the user shall find.
    """
    file = r.choice(["a", "b", "c", "d", "e", "f", "g", "h"])
    rank = str(r.randint(1, 8))
    to_find = file + rank
    return to_find


def write_info(screen, to_find, score, highscore, user, menu):
    """Writing varying data and text on the screen.

    Args:
        screen (g.display.set_mode): The pygame call for creating a window.
        to_find (str): String of the notation for the square that the user should find.
        score (int): Score of that particular user in that particular mode.
        highscore (int): Highscore of that particular user in that particular mode.
        user (str): Name of the user.
        menu (str): One of the two menus of Chess Vision Trainer.
    """
    font = g.font.SysFont("bahnschrift", 30)
    if menu == "home":
        # Write all the information for the home menu in the top frame.
        play_info = font.render(f"Play      !", 1, ("peachpuff4"))
        find_info = font.render(to_find, 1, ("indianred4"))
        score_info = font.render(
            f"Score: {score}            Highscore: {highscore}", 1, ("peachpuff4")
        )
        screen.blit(play_info, (60, 110))
        screen.blit(find_info, (130, 110))
        screen.blit(score_info, (60, 150))
    if menu == "user":
        # Write all the information for the user menu in the bottom frame.
        you_info = font.render(f"You:", 1, ("peachpuff4"))
        user_info = font.render(user, 1, ("indianred4"))
        screen.blit(you_info, (60, 150))
        screen.blit(user_info, (120, 150))


def welcome(user):
    """Generating an individual welcoming message.

    Args:
        user (str): Name of the user.

    Returns:
        str: Welcoming message that can be displayed on the screen.
    """
    if user == "guest_session":
        return "Welcome, stranger! :)"
    else:
        return f"Welcome back, {user}!"


def click_handler(position, menu, mode):
    """Handling all the left clicks during the run of the app.

    Args:
        position (lst): X and y coordinates of the position on the screen.
        menu (str): One of the two menus of Chess Vision Trainer.
        mode (str): One of the three modes of the Chess Vision Trainer.

    Returns:
        str or None: An indication of how that click shall be handled.
    """
    x, y = position
    # Changing modes.
    if 410 < x < 480 and 15 < y < 85:
        if mode == "classical":
            mode = "lives"
        elif mode == "lives":
            mode = "timed"
        elif mode == "timed":
            mode = "classical"
        return mode
    if menu == "home":
        # If left mouse click in board range, convert position to square notation.
        if 50 < x < 450 and 250 < y < 650:
            square_entered = click_square_translator(x, y)
            return square_entered
        # Switch to user menu.
        elif 260 < x < 440 and 110 < y < 145:
            return "User button"
        # Else, ignore click.
        return None
    elif menu == "user":
        # Switch to home menu.
        if 260 < x < 440 and 110 < y < 145:
            return "User button"
        # User wants to log in with a different "account".
        elif 60 < x < 240 and 110 < y < 145:
            return "Switch button"
        # Else, ignore click.
        return None


def switch_user(screen):
    """Capturing input for a name that the user wants to use.

    Args:
        screen (g.display.set_mode): The pygame call for creating a window.

    Returns:
        str or None or False: An indication of how the input shall be handled.
    """
    text = ""
    while True:
        # Briefly show a circle to indicate the end of input capturing.
        g.draw.circle(screen, "cornsilk", (78, 128), 5)
        for event in g.event.get():
            # Quit the app instantly, if the user wants to.
            if event.type == g.QUIT:
                return False
            if event.type == g.KEYDOWN:
                # Finalize the new user name.
                if event.key == g.K_RETURN:
                    new_user = text
                    text = ""
                    return new_user
                # Delete one character from the new user name.
                elif event.key == g.K_BACKSPACE:
                    text = text[:-1]
                # Write to the new user name.
                else:
                    text += event.unicode
            # Stop the input capturing but continue to run the app.
            if event.type == g.MOUSEBUTTONDOWN:
                text = ""
                return None


def click_square_translator(x, y):
    """Translating a position on the displayed chessboard to its corresponding square notation.

    Args:
        x (int): X coordinate of the position on the chessboard.
        y (int): Y coordinate of the position on the chessboard.

    Returns:
        str: Notation of the square on that position.
    """
    if x < 100:
        x = "a"
    elif x < 150:
        x = "b"
    elif x < 200:
        x = "c"
    elif x < 250:
        x = "d"
    elif x < 300:
        x = "e"
    elif x < 350:
        x = "f"
    elif x < 400:
        x = "g"
    else:
        x = "h"
    if y < 300:
        y = "8"
    elif y < 350:
        y = "7"
    elif y < 400:
        y = "6"
    elif y < 450:
        y = "5"
    elif y < 500:
        y = "4"
    elif y < 550:
        y = "3"
    elif y < 600:
        y = "2"
    else:
        y = "1"
    return str(x) + str(y)


def square_to_position_translator(square):
    """Translating a square notation to its corresponding position on the displayed chessboard.

    Args:
        square (str): Notation of the square.

    Returns:
        Pair of int and int: X and y coordinate for the position on the chessboard.
    """
    file, rank = list(square)
    x = 0
    y = 0
    if file == "a":
        x = 50
    elif file == "b":
        x = 100
    elif file == "c":
        x = 150
    elif file == "d":
        x = 200
    elif file == "e":
        x = 250
    elif file == "f":
        x = 300
    elif file == "g":
        x = 350
    elif file == "h":
        x = 400
    if rank == "8":
        y = 250
    elif rank == "7":
        y = 300
    elif rank == "6":
        y = 350
    elif rank == "5":
        y = 400
    elif rank == "4":
        y = 450
    elif rank == "3":
        y = 500
    elif rank == "2":
        y = 550
    elif rank == "1":
        y = 600
    return x, y


def validate_guess(square, to_find, mode, lives):
    """Reacting based on whether the guessed square is the square that was searched for.

    Args:
        square (str): Notation of the chess square that the user guessed.
        to_find (str): Notation of the chess square that the user shall find.
        mode (str): One of the three modes of the Chess Vision Trainer.
        lives (int): The guesses the user has left in the "lives" mode.

    Returns:
        Pair of str and boolean: An indication of how the guess shall be handled.
    """
    # Handle correct guess.
    if square == to_find:
        return ("Correct!", True)
    # Handle incorrect guess. Reaction varies per mode.
    elif mode == "classical":
        return ("Try again!", False)
    elif mode == "lives":
        if lives == 1:
            return ("Try again!", True)
        elif lives == 2:
            return ("One life remaining.", True)
        elif lives == 3:
            return ("Two lives remaining.", True)
    elif mode == "timed":
        return ("Nope. Tick Tock...", False)


def get_feedback(square, exclamation, score, highscore):
    """Generating feedback according to the user's action.

    Args:
        square (str): Notation of the chess square that the user guessed.
        exclamation (str): First part of the outcome of the validate_guess function.
        score (int): Score of that particular user in that particular mode.
        highscore (int): Highscore of that particular user in that particular mode.

    Returns:
        str: Feedback message that can be displayed on the screen.
    """
    # User changes mode...
    if square in ["classical", "lives", "timed"]:
        return "Mode changed!"
    # User guesses correctly...
    if exclamation == "Correct!":
        return f"You played {square}. {exclamation}"
    # User guesses wrong...
    elif exclamation == "Try again!":
        if score == 0:
            return f"You played {square}. Try again! :)"
        elif score < (highscore / 2):
            return "We both know, you can do better!"
        elif score < highscore:
            return "Not bad. Now break your highscore!"
        else:
            return "Congratulations! :)"
    elif exclamation in [
        "Two lives remaining.",
        "One life remaining.",
        "Nope. Tick Tock...",
    ]:
        return exclamation
    # Countdown ended in timed mode.
    elif exclamation == "Time's up!":
        if score == 0:
            return "No thinking allowed! :)"
        elif score < (highscore / 2):
            return "Every sloth would be faster."
        elif score < highscore:
            return "Zzz... Did something happen?"
        else:
            return "At lightning speed! :)"


def draw_timer(screen, seconds_to_display):
    """Drawing the countdown for the "lives" mode in the "home" menu on the screen.

    Args:
        screen (g.display.set_mode): The pygame call for creating a window.
        seconds_displayed (int): Seconds that shall be used for the countdown in the timed mode.
    """
    font = g.font.SysFont("bahnschrift", 30)
    timer = font.render(str(seconds_to_display), 1, ("cornsilk"))
    screen.blit(timer, (240, 205))


def write_feedback(screen, text):
    """Writing a message, either from the welcome or the get_feedback function, on the screen.

    Args:
        screen (g.display.set_mode): The pygame call for creating a window.
        text (str): The message that shall be displayed on the screen.
    """
    font = g.font.SysFont("bahnschrift", 20)
    feedback = font.render(text, 1, ("cornsilk"))
    screen.blit(feedback, (130, 670))


if __name__ == "__main__":
    main()
