import random

def daily_sales(available_items, inventory_records, current_day):
    '''
***********COMPLETE THIS FUNCTION***********
This function is responsible for updating the sales for a given day.
---------------
Function Input:
---------------
available_items: (integer) Available Tshirts from the previous day.
inventory_records: (List) A list of inventory records until the previous day. Each row contains (day, sales, restocked items, available items)
current_day: (integer) Day number which you want to add as the current day. 

----------------
Function Output:
----------------
available_items:(integer) This function returns this integer which updates the available items at the current day.

The function will also update the inventory_records (For restocking) for a  given current day. 

    '''
    # Only allows sales day every day except restock days (every 7th day)
    if current_day % 7 == 0:
        return available_items
    
    # Simulate daily sales
    items_sold = random.randint(0, 200)  # Random sales between 0 or less than 200
    available_items -= items_sold

    # Update inventory records
    inventory_records.append((current_day, items_sold, 0, available_items))

    # Return updated available items
    return available_items