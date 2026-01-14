# Fishtank Fiasco
A cool fish tank "game" made in pygame. Soon to be in stores worldwide.

## Features
- As of now the fish move

## TODO 

- Animation System
- Better graphics
- Boid logic
- Dynamic Fish logic
- Sound system
- Menu system
- Moar fish
- Interaction!
- Levels + customization
- Every other feature
- Documentation

## Installation

### To run the game:
To run a compiled version of this project, you should only need python
installed to run it.

### To work on the code:
To work on this project, you are going to need a compatible version of
Python and Pygame. Python 3.12.6 will work in this case, as well as the newest
version of Pygame, which at the time of writing is version 2.6.1. You'll need
any dependencies that come with that as well. I would highly recommend
using Vscode for your IDE, but notepad.exe works just fine too.

The simplest way to ensure this works is to use a virtual environment. Below is a short guide for windows. 
If you are on Linux, I trust you can figure it out. If you're on Mac, see if you can pay someone to do it for you :).

1. Clone the Repo (Simply download this from github and open the project in VSCODE)

2. Type these commands to make a virtual enivronment: 

```bash
python -m venv vev

# Wait a moment for it to download. You should see a (venv) in front of 
# your terminal text and a venv folder.

# (In powershell, which should be the default terminal in vscode):
.\venv\Scripts\activate.ps1
# (If you are using cmd do this instead):
venv\Scripts\activate.bat
# If you are Linux/mac do this:
source venv/bin/activate

# Next install the dependencies
pip install -r requirements.txt

# Finally run the game
python main.py
```
Note that on the offchance you are adding a dependency to the project
before uploading your work to github, please add it to
the requirements.txt file. Just type this into the terminal:
```bash
pip freeze > requirements.txt
```

If you know me in real life, feel free to ask me questions. Or use google. Good luck!


## License

All code in this program is licensed under the MIT license (see LICENSE).

All game assets (including but not limited to art, audio, music, story,
and level data) are proprietary unless stated otherwise and are not
covered by the MIT License.

They are (c) 2026 NPNicholls. All rights reserved.


## Credits

// example third party asset attribution:
Some assets are used under license from:

tree.png © 2025 FriendName — used with permission
footsteps.wav CC-BY 4.0 — attribution in credits