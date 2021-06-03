import json
import logging
from pathlib import Path

from model import EquipmentSet

# variable simulating in memory DB
database: dict[str, EquipmentSet] = {}


def setup_database(main_path: Path) -> None:
    """
    Setup the data from JSON file

    :param main_path:
    :return:
    """
    api_file_path = main_path.parent / 'dist/api-response.json'
    logging.info(f"Loading API data from: {api_file_path}")
    try:
        with open(api_file_path) as f:
            json_data = json.load(f)
            # Since there is no database, I'll duplicate de ID for indexing purposes
            for id, value in json_data.items():
                database[id] = EquipmentSet.json_load(id, value)
    except FileNotFoundError:
        logging.error(f"No file found at {api_file_path}")
        return
    logging.info(f"API data loaded")
