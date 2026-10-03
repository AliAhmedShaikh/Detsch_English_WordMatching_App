# Deutsch Match — Android vocabulary game

A simple Duolingo-style German vocabulary matching game built with Python + Kivy.

## Features
- Match German words with English meanings
- 5 pairs per round
- Score (+10 for correct matches)
- 3 lives
- Streak counter
- Progress bar
- Randomized word order
- New Game button
- Works offline

## Run on a computer

Install Python 3.10+ and then:

    pip install -r requirements.txt
    python main.py

## Build an Android APK

The easiest route is Buildozer on Linux (Ubuntu) or WSL.

    pip install buildozer
    buildozer init

Replace the generated buildozer.spec with the included one, then:

    buildozer android debug

The APK will be placed in the `bin/` directory.

For a release build, configure signing and use:

    buildozer android release

## Customize vocabulary

Open `main.py` and edit the WORDS list:

    WORDS = [
        ("der Apfel", "the apple"),
        ("das Haus", "the house"),
    ]

You can expand this to hundreds or thousands of A1/B1 words.

## Next upgrades

Possible improvements for a fuller language-learning app:
- A1/A2/B1 vocabulary levels
- German audio/pronunciation
- Multiple game types
- Daily XP and streaks
- Hearts/lives regeneration
- Mistake review
- Progress tracking with SQLite
- User accounts
- German → English and English → German modes
- Sentence matching
- Spaced repetition
- Achievements/badges
- Dark mode
