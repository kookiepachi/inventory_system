

import json
import logging
from datetime import datetime
from typing import Dict, List, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

# Global inventory dictionary
stock_data: Dict[str, int] = {}


def add_item(item: str, qty: int = 0, logs: Optional[List[str]] = None) -> None:
    """Add a given quantity of an item to inventory."""
    if logs is None:
        logs = []

    if not isinstance(item, str) or not item.strip():
        raise ValueError("Item name must be a non-empty string.")
    if not isinstance(qty, int) or qty < 0:
        raise ValueError("Quantity must be a non-negative integer.")

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")
    logging.info("Added %d of %s. New total = %d", qty, item, stock_data[item])


def remove_item(item: str, qty: int) -> None:
    """Remove a specified quantity of an item from inventory."""
    if not isinstance(item, str) or not item.strip():
        raise ValueError("Item name must be a non-empty string.")
    if not isinstance(qty, int) or qty <= 0:
        raise ValueError("Quantity must be a positive integer.")

    try:
        current = stock_data[item]
        new_qty = current - qty
        if new_qty > 0:
            stock_data[item] = new_qty
        else:
            del stock_data[item]
        logging.info("Removed %d of %s. Remaining = %s", qty, item, stock_data.get(item))
    except KeyError:
        logging.warning("Tried to remove non-existing item: %s", item)


def get_qty(item: str) -> int:
    """Return quantity of an item; 0 if item not found."""
    if not isinstance(item, str):
        raise TypeError("Item name must be a string.")
    return stock_data.get(item, 0)


def load_data(filename: str = "inventory.json") -> None:
    """Load inventory data safely from a JSON file."""
    global stock_data
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, dict):
            raise ValueError("Invalid file format. Expected dictionary structure.")

        # Ensure all values are integers
        stock_data = {k: int(v) for k, v in data.items()}
        logging.info("Loaded inventory data from %s", filename)

    except FileNotFoundError:
        logging.warning("File %s not found. Starting with empty inventory.", filename)
        stock_data = {}
    except (json.JSONDecodeError, ValueError) as err:
        logging.error("Error reading %s: %s", filename, err)
        stock_data = {}


def save_data(filename: str = "inventory.json") -> None:
    """Save inventory data to a JSON file safely."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(stock_data, file, indent=2)
    logging.info("Saved inventory data to %s", filename)


def print_data() -> None:
    """Print all items and their quantities in sorted order."""
    print("\n=== Inventory Report ===")
    if not stock_data:
        print("No items available in stock.")
    else:
        for item, qty in sorted(stock_data.items()):
            print(f"{item} → {qty}")


def check_low_items(threshold: int = 5) -> List[str]:
    """Return a list of items with quantity below a given threshold."""
    if not isinstance(threshold, int) or threshold < 0:
        raise ValueError("Threshold must be a non-negative integer.")
    low_items = [item for item, qty in stock_data.items() if qty < threshold]
    logging.info("Items below threshold (%d): %s", threshold, low_items)
    return low_items


def demo() -> None:
    """Demo function to test inventory operations safely."""
    add_item("apple", 10)
    add_item("banana", 2)
    add_item("orange", 8)
    remove_item("apple", 3)
    remove_item("grape", 2)  

    print("Apple stock:", get_qty("apple"))
    print("Low stock items:", check_low_items())

    save_data()
    load_data()
    print_data()


if __name__ == "__main__":
    demo()
