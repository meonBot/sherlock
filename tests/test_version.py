import os
from sherlock_interactives import Interactives
import sherlock

def test_versioning() -> None:
    # Ensure __version__ matches version presented to the user
    assert sherlock.__version__ in Interactives.run_cli("--version")
    # Ensure __init__ is single source of truth for __version__ in package
    # Temporarily allows sherlock.py so as to not trigger early upgrades
    found:list = Interactives.walk_sherlock_for_files_with(r'__version__ *= *')
    expected:list = [
        # Normalization is REQUIRED for Windows ( / vs \ )
        os.path.normpath("sherlock/__init__.py"),
        os.path.normpath("sherlock/sherlock.py"),
    ]
    # Sorting is REQUIRED for Mac
    assert sorted(found) == sorted(expected)
