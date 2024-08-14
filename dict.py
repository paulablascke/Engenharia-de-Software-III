sells = {"Tecnology": "iPhone", "Book": "Spider Man", "Computer": "Samsung Galaxy Book2"}
sells_tecnology = {"iPhone": 1500, "Samsung Galaxy Book2": 1000, "PS5": 500, "iPad": 580}

# Show by private words
book = sells["Book"]
cellphone = sells["Tecnology"]

# Show by sells 
samsumg_galaxy = sells_tecnology["Samsung Galaxy Book2"]
video_game = sells_tecnology["PS5"]

print("Product:")
print(f"Cellphone: {cellphone}")
print(f"Book: {book}")

print("------" * 5)

print("Sells:")
print(f"Computer: {samsumg_galaxy}")
print(f"Video Game: {video_game}")