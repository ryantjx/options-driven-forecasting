import sys
import os

def set_project_root(root_dir):
    """
    Set the project root directory for imports and change the current working directory.

    Args:
        root_dir (str): The path to the project's root directory.
    """
    # Make sure the provided path is an absolute path
    root_dir = os.path.abspath(root_dir)

    # Set the project root directory for imports
    if root_dir not in sys.path:
        sys.path.append(root_dir)

    # Change the current working directory to the project root
    os.chdir(root_dir)