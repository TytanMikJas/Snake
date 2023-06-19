# Snake
This is a simple snake game repo, created using python and pygame.

#How to install

## Cloning the project
```bash
git clone https://github.com/TytanMikJas/Snake.git
cd Snake
```

## Running as script

You can run the app as a script

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/main.py
```

# You can install this app on ubuntu

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Building using Pyinstaller
```bash
pyinstaller main.py --onefile --windowed
```

## Building package
```bash
./build-package-structure.sh
```

## Installing package 
```bash
sudo dpkg -i main.deb
```

