from core.inventory import Inventory
from core.models import Electronics, Grocery, Item
from core.exceptions import InventoryException
from core.utils import sort_items, most_expensive, below_quantity_threshold

def print_menu():
    print("\n" + "="*35)
    print("    INVENTORY MANAGEMENT SYSTEM")
    print("="*35)
    print("1. Add Electronics")
    print("2. Add Grocery")
    print("3. Remove Item")
    print("4. Update Quantity")
    print("5. Display Inventory")
    print("6. Read from File")
    print("7. Write to File")
    print("8. Find Most Expensive Item")
    print("9. Find Items Below Quantity Threshold")
    print("10. Sort by Price")
    print("11. Exit")
    print("-" * 35)

def run_cli():
    inventory = Inventory()

    while True:
        print_menu()
        choice = input("Enter your choice (1-11): ").strip()

        try:
            match choice:
                case "1":
                    item_id = input("Enter Item ID: ").strip()
                    name = input("Enter Name: ").strip()
                    quantity = int(input("Enter Quantity: ").strip())
                    price = float(input("Enter Price: ").strip())
                    warranty = int(input("Enter Warranty (months): ").strip())
                    item: Item = Electronics(item_id, name, quantity, price, warranty)
                    inventory.add_item(item)
                    print(f"Success: Added '{name}' to inventory.")

                case "2":
                    item_id = input("Enter Item ID: ").strip()
                    name = input("Enter Name: ").strip()
                    quantity = int(input("Enter Quantity: ").strip())
                    price = float(input("Enter Price: ").strip())
                    expiry = input("Enter Expiration Date (YYYY-MM-DD): ").strip()
                    item = Grocery(item_id, name, quantity, price, expiry)
                    inventory.add_item(item)
                    print(f"Success: Added '{name}' to inventory.")

                case "3":
                    item_id = input("Enter Item ID to remove: ").strip()
                    inventory.remove_item(item_id)
                    print(f"Success: Item '{item_id}' removed.")

                case "4":
                    item_id = input("Enter Item ID to update: ").strip()
                    quantity = int(input("Enter new Quantity: ").strip())
                    inventory.update_quantity(item_id, quantity)
                    print(f"Success: Item '{item_id}' quantity updated to {quantity}.")

                case "5":
                    print("\n--- Current Inventory ---")
                    if len(inventory) == 0:
                        print("Inventory is empty.")
                    else:
                        inventory.display_inventory()

                case "6":
                    filename = input("Enter filename to read (default: assets/inventory.csv): ").strip() or "assets/inventory.csv"
                    inventory.read_from_file(filename)
                    print(f"Success: Inventory loaded from '{filename}'.")

                case "7":
                    filename = input("Enter filename to write (default: assets/export.csv): ").strip() or "assets/export.csv"
                    inventory.write_to_file(filename)
                    print(f"Success: Inventory saved to '{filename}'.")

                case "8":
                    if len(inventory) == 0:
                        print("Inventory is empty.")
                    else:
                        expensive: Item = most_expensive(inventory)
                        print(f"\nMost Expensive Item:\n{expensive.display()}")

                case "9":
                    threshold = int(input("Enter quantity threshold: ").strip())
                    low: list[Item] = below_quantity_threshold(inventory, threshold)
                    print(f"\n--- Items below {threshold} quantity ---")
                    if not low:
                        print("No items found below this threshold.")
                    else:
                        for i in low:
                            print(i.display())

                case "10":
                    if len(inventory) == 0:
                        print("Inventory is empty.")
                    else:
                        sorted_list: list[Item] = sort_items(inventory, key_fn=lambda x: x.price)
                        print("\n--- Inventory Sorted by Price ---")
                        for i in sorted_list:
                            print(i.display())

                case "11":
                    print("Exiting application")
                    break

                case _:
                    print("Invalid choice. Please enter a number between 1 and 11")

        except InventoryException as e:
            print(f"\nError: {e}")
        except ValueError:
            # Catches casting errors (e.g. user types "ten" instead of "10" for quantity)
            print("\nError: Expected a number but received text. Please try again.")
        except Exception as e:
            # Prevent crashing of cli
            print(f"\nError: An unexpected error occurred: {e}")