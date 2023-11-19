# Runing the code

I expect the code to run without installing any addtional libraries (it was written using Python `3.11.6`)

You can run the game with a pre-set deck by setting a value for the `--i` argument
```bash
python3 .\main.py --i .\deck.txt
```

The game will run with a random deck if `--i` isn't set
```bash
python3 .\main.py
```

You can also specify an `--o` value to save the deck that was used in the last game in a file
```bash
python3 .\main.py --o .\new_deck.txt
```

# Running the tests

The tests use [unittest](https://docs.python.org/3/library/unittest.html) and tests can be run from the terminal
```bash
python3 .\test.py -v
```