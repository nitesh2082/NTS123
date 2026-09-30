#list example
# Sequential order of product IDs added to the cart
cart_item_ids = ["PROD-101", "PROD-205", "PROD-101", "PROD-884"]

# Common operations
cart_item_ids.append("PROD-330")      # Add newly clicked item to the end
recent_item = cart_item_ids.pop()     # Remove the most recently added item
first_item = cart_item_ids[0]         # Inspect the first item added ("PROD-101")

print("Cart item IDs:", cart_item_ids)

#dictionary example

# Detailed specifications of a single product
product = {
    "sku": "PROD-101",
    "name": "Wireless Noise-Canceling Headphones",
    "price_usd": 149.99,
    "in_stock": True,
    "rating": 4.8,
}

# Common operations
current_price = product["price_usd"]             # Direct lookup by attribute name
product["price_usd"] = 129.99                    # Apply a discount
product["brand"] = "AudioTech"                   # Insert a new key-value field
is_available = product.get("in_stock", False)    # Safe retrieval with a fallback

a=[1,2]
b=[3,4]
#b.extend(a)
#print(b)

concatenated_list = a + b
print(concatenated_list)
pop_list = concatenated_list.pop()
print(concatenated_list)
removed_item = concatenated_list.pop(0)  # Remove the first item
print("Removed item:", removed_item)
cleared_list = concatenated_list.clear()  # Clear all items from the list
print(concatenated_list)

x=[1,3,5,8,2]
count_of_3 = x.count(3)  # Count occurrences of the value 3
print("Count of 3 in the list:", count_of_3)
y=[1,3,5,8,2,[1,2,3]]

print("Count of 1 in the list:", y.count(1))  # Count occurrences of the value 1

#List comprehension example
list1=[1,2,3,4,5]
list2=[6,7,8,9,10]

#nested list comprehension
newlist=[1,2,3,4,[5,6,7,8,9]]

print("New list:", newlist)
print(newlist[4][3])
