import json # to read and store user data in a JSON file
import os # to handle file paths and create the data folder if it doesn't exist


def load_data(file_name):
    """
    Load data from a JSON file.

    JSON → Python

    """

    try:

        with open(
            file_name,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    except FileNotFoundError:

        # Return an empty list if the file doesn't exist
        return []

    except json.JSONDecodeError:

        print(
            f"Warning: {file_name} "
            "contains invalid JSON."
        )

        return []


def save_data(
    file_name,
    data
):
    """
    Save Python data into a JSON file.

    Python → JSON
    
    """

    # Get the folder name
    folder = os.path.dirname(file_name)

    # Create the folder if it doesn't exist
    if folder:

        os.makedirs(
            folder,
            exist_ok=True
        )

    # Open the file in write mode
    with open(
        file_name,
        "w",
        encoding="utf-8"
    ) as file:

        # Convert Python data to JSON
        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )