import json
import os

DB_FILE = "inventory_db.json"

def load_inventory():
    if not os.path.exists(DB_FILE):
        default_inventory = {
            "101": {"name": "Burgers", "stock": 50, "reorder_level": 10},
            "102": {"name": "Chips", "stock": 80, "reorder_level": 15},
            "103": {"name": "Soft Drinks", "stock": 8, "reorder_level": 12}
        }
        save_inventory(default_inventory)
        return default_inventory
    with open(DB_FILE, "r") as file:
        return json.load(file)

def save_inventory(data):
    with open(DB_FILE, "w") as file:
        json.dump(data, file, indent=4)

def check_low_stock(current_inventory):
    low_stock_items = []
    for item_id, details in current_inventory.items():
        if details["stock"] <= details["reorder_level"]:
            low_stock_items.append(f"{details['name']} (Stock: {details['stock']})")
    if low_stock_items:
        print("⚠️ LOW STOCK ALERT:")
        for alert in low_stock_items:
            print(f" - {alert}")
    else:
        print("✅ All stock levels are sufficient.")

def process_sale(item_id, quantity_sold):
    inventory = load_inventory()
    if item_id in inventory:
        if inventory[item_id]["stock"] >= quantity_sold:
            inventory[item_id]["stock"] -= quantity_sold
            save_inventory(inventory)
            print(f"✅ Sold {quantity_sold} {inventory[item_id]['name']}. Stock updated!")
            check_low_stock(inventory)
        else:
            print(f"❌ Not enough stock to sell {quantity_sold} {inventory[item_id]['name']}.")
    else:
        print("❌ Item ID not found in system.")

if __name__ == "__main__":
    print("--- Running Tech-Tasty Automation Engine ---")
    user_item = input("Enter Item ID: ")
    user_qty_string = input("Enter quantity sold: ")
    user_qty_integer = int(user_qty_string)
    process_sale(user_item, user_qty_integer)
