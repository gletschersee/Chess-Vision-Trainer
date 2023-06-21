<a name="top"></a>

<div align="center">

# **Chess Vision Trainer**
v.1.0 - *Gletschersee*

![Chess Vision Trainer Logo](https://raw.githubusercontent.com/gletschersee/Chess-Vision-Trainer/main/graphics/cvt_classical70x70.png)

[![Video](https://img.shields.io/badge/Video%20Demo%20-%20Chess%20Vision%20Trainer%20-%20black?logo=youtube&labelColor=red)](https://www.youtube.com/watch?v=a2HBwKvbtOo)

<div align="left">


## Description

Chess Vision Trainer is an app that allows users to train their knowledge of chess square names
per modern/ standard/ algebraic notation in a gamified way.


### Tutorial

Required:
You need to have Python and pip installed.
Steps before you can use the app:
1. Load this repository into your coding environment.
2. Use pip to install pygame.
3. Run chess_vision_trainer.py.
Now you should be able to see the GUI and use the app.

#### How to use the app

At the top left, a notation of a square is shown. Select that square on the chessboard.
Your score and high score are displayed at the top, and the records per mode under the user menu.
To reach the user menu, click on the button on the right side of the top half of the app.
Please note, that when you start the app, your username is set to "guest_session."
Any stats for that particular username are **NOT** saved.

<p align="right">(<a href="#top">Back to top</a>)</p>

#### Changing user

You can change your username by clicking on user on the right side of the top half of the app.
When you click on change, your input will be registered and after you press enter, it will be set as your name.
If you want to switch your user/ username again, just click the switch button again.

When you click while your input is captured, you stop/ exit the changing of the user/ username.

On the left of the switch button, a small circle will appear briefly once the app stops capturing your input.

Every keyboard input is accepted.
By pressing directly ↩, you will get "" as your username.
And, by typing a very long username, your username cannot be fully displayed.


#### The modes

You can play three different modes.
Select the mode by clicking through the icons in the top left corner.
The three modes are:
- Classic
    - Icon: ♞, Knight chess piece
    - You have one guess per round
    - The square you have to find will **NOT** be renewed when your guess is wrong
- Lives:
    - Icon: ❤️, Heart
    - You have three guesses per round
    - The square you have to find will be renewed when your guess is wrong
- Timed
    - Icon: ⚡, Lightning bolt
    - You have 5 seconds and infinite guesses per move
    - The square you have to find will be renewed when your guess is wrong

<p align="right">(<a href="#top">Back to top</a>)</p>


### Ideas for future versions

*Please note that it is unlikely that I will implement all of these changes.
Most likely, I am not going to continue this project at all.
In the unlikely case that there are people interested in my project, I might continue.*

- [ ] Improve code
    - [ ] Add classes
    - [ ] Reduce code repetitions and increase code clarity
        - [ ] Restructure
        - [ ] Make use of map, list comprehension, unpacking, type hints, global, yield, enumerate
- [ ] Settings menu
    - [ ] On and off button for notation at the side of the board
    - [ ] On and off button for notation on the board for each square
    - [ ] Switch to the descriptive/ old notation system
- [ ] Improve user switch
    - [ ] Show input
    - [ ] Make requirements, such as length and only word characters
    - [ ] Add a password system
- [ ] Implement a web API instance of Chess Vision Trainer
    - [ ] log in with passwords
    - [ ] global leaderboard
- [ ] Option to switch sides from white to black


<p align="right">(<a href="#top">Back to top</a>)</p>


### Side note

This project is my first Python project with a GUI.
It is my final project for the CS50 course "Introduction to Python."
I am aware that it is not optimized, missing many improvements, such as adding object-oriented programming
or importing other modules that already provide features, e.g., buttons.
I coded this in 48 hours and am, as it should be obvious, still a complete beginner.
Thus, do not expect well-written code or a program that has no flaws.
Some inconveniences I am aware of are, for instance:
    Names do not have a maximum length and, thus, can go over the border.
    The input of what you are typing is not visible.
    The position of text displayed on the screen varies depending on the length of the text.
As stated, I am aware of that.
I just had limited time available and am new to Python and, especially, GUIs.
Thus, it is what it is.

Greetings from Germany
Gletschersee

### Fun fact

I did not start chess when I was 4. I started when I was an adult and am still bad at chess.

## File descriptions

- `README.md` This file. It contains the documentation for and other information on the project.
- `chess_vision_trainer.py` The main file. It runs the entire app.
- `record_logbook.csv` Records file. All the game statistics from logged-in users are saved here. 
- `requirements.txt` Requirements file. This file contains all the tools I have worked with. Normally, it should be enough to pip install pygame.
- `test_chess_vision_trainer.py` The testing file. This file can be run with pytest to ensure chess_vision_trainer.py is working as intended. It does **NOT** catch everything.
- `graphics/...` The folder for all the graphics used for this project.
    - `additional ressources/...` The subfolder for higher-resolution images, that are not directly used in the code.



## Licensing

Everyone is welcome to continue with my project and add features from the list below or
whatever they might see fit to add.
If you continue my project, leave my name as the original author in all files.
You may, if you want, add yours to mine.
For instance, assuming your name/ GitHub username is "GenericName," then the title should be:
    Chess Vision Trainer [version] by Gletschersee and GenericName
This project is not to be commercialized.

<p align="right">(<a href="#top">Back to top</a>)</p>


## Version Log

| Version               | Changes                                                       |
|:---------------------:|---------------------------------------------------------------|
| **v.1.0**             | The original version of the Chess Vision Trainer.             |
| *No further versions* | *None*                                                        |

Past versions are not highlighted.
Current version is **bolt**.
Planned versions are in *Italic*.




## References

### Code

All the code is written by me, Gletschersee.

<p align="right">(<a href="#top">Back to top</a>)</p>

### Graphics

The graphics used are partly based on/ inspired by images that are not from me.
All of them have licenses that allow me to use them in the way I used them.

[Classical logo](https://pixabay.com/de/vectors/ritter-pferd-schach-spiel-bewegung-33015/)

[Classical frame](https://blog.starsunflowerstudio.com/free-laurel-frames-arrows-clip-art/)

[Heart logo](https://commons.wikimedia.org/wiki/File:Heart_font_awesome.svg)

[Hearts frame](https://thenounproject.com/icon/row-of-hearts-1773997/)

[Bolt logo](https://commons.wikimedia.org/wiki/File:Bolt_font_awesome.svg)

[Bolt frame](https://svgsilh.com/de/image/2031288.html)


## Contact Information

My name is Maxim. You may contact me at maximsamuel@icloud.com
