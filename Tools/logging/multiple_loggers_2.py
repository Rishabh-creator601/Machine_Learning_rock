"""
multiple_loggers.py
-------------------
A beginner-friendly look at MULTIPLE loggers.

In logging_1.ipynb we used logging.debug(), logging.warning(), etc.
Those all use ONE built-in logger called the "root" logger.

But in a real program you often want SEPARATE loggers so you can tell
which part of the code a message came from, and control each one on its own.

You create a named logger with:
        logging.getLogger("some_name")

Calling getLogger with the same name always gives you back the SAME logger,
so you can grab it from anywhere in your code.
"""

import logging


# ---------------------------------------------------------------------------
# Step 1: configure the basics (just like logging_1.ipynb)
# This controls the root logger and acts as the default for everyone.
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.DEBUG,
    filename="log2.txt",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    force=True,
)


# ---------------------------------------------------------------------------
# Step 2: create two DIFFERENT loggers, each with its own name.
# The name shows up in the output (the %(name)s part of the format),
# so you can instantly see which logger produced each line.
# ---------------------------------------------------------------------------
logger1 = logging.getLogger("module_one")
logger2 = logging.getLogger("module_two")


# ---------------------------------------------------------------------------
# Step 3: each logger can have its OWN level.
# logger1 will show everything (DEBUG and up).
# logger2 will only show WARNING and up, so its debug/info lines are hidden.
# ---------------------------------------------------------------------------
logger1.setLevel(logging.DEBUG)
logger2.setLevel(logging.WARNING)


# ---------------------------------------------------------------------------
# Step 4: use them and compare the output.
# ---------------------------------------------------------------------------
logger1.debug("logger1: this is a debug message")
logger1.info("logger1: this is an info message")
logger1.warning("logger1: this is a warning message")

logger2.debug("logger2: this debug is HIDDEN (level is WARNING)")
logger2.info("logger2: this info is HIDDEN (level is WARNING)")
logger2.warning("logger2: this warning IS shown")
logger2.error("logger2: this error IS shown")
