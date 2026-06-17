"""
file_stream_3.py
----------------
HANDLERS for absolute beginners: FileHandler vs StreamHandler.

Remember from before:
  - A LOGGER creates the message.
  - A HANDLER decides WHERE the message goes.

The two handlers you'll use most:
  - StreamHandler  -> sends messages to the CONSOLE (your screen).
  - FileHandler    -> sends messages to a FILE on disk.

A single logger can have BOTH handlers at the same time, so the same
message can appear on the screen AND be saved to a file. That is what
this example does.
"""

import logging


# ---------------------------------------------------------------------------
# Step 1: make a logger.
# (We give it a name so the output clearly shows where it came from.)
# ---------------------------------------------------------------------------
logger = logging.getLogger("my_app")
logger.setLevel(logging.DEBUG)   # let the logger accept DEBUG and above


# ---------------------------------------------------------------------------
# Step 2: make a FORMATTER.
# This just decides how each line LOOKS. We can reuse it for both handlers.
# ---------------------------------------------------------------------------
formatter = logging.Formatter(
    fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


# ---------------------------------------------------------------------------
# Step 3: make a StreamHandler -> this prints to the console.
# We tell it to only show WARNING and above on the screen.
# ---------------------------------------------------------------------------
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)
console_handler.setFormatter(formatter)


# ---------------------------------------------------------------------------
# Step 4: make a FileHandler -> this writes to a file called "app.log".
#   mode="w"  -> start a fresh file every run (use "a" to keep appending)
# We tell it to save EVERYTHING (DEBUG and above) to the file.
# ---------------------------------------------------------------------------
file_handler = logging.FileHandler("app.log", mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)


# ---------------------------------------------------------------------------
# Step 5: attach BOTH handlers to the logger.
# Now every message is offered to both handlers; each one keeps only the
# levels it was told to keep.
# ---------------------------------------------------------------------------
logger.addHandler(console_handler)
logger.addHandler(file_handler)


# ---------------------------------------------------------------------------
# Step 6: log some messages and see what happens.
# ---------------------------------------------------------------------------
logger.debug("this is a debug message")        # file only
logger.info("this is an info message")          # file only
logger.warning("this is a warning message")     # file AND console
logger.error("this is an error message")        # file AND console
logger.critical("this is a critical message")   # file AND console

print("\nDone! Open 'app.log' to see ALL messages.")
print("On the console above you only saw WARNING and higher.")
