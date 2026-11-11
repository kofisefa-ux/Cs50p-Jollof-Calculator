def main():
    guests = int(input("Enter the number of guests: "))
    rice_cups = guests * 0.35
    tomato_liters = guests * 0.15
    onions = guests * 1.2
    meat_kg = guests * 0.25
    
    rice_bags = rice_cups / 5
    tomato_cans = tomato_liters / 0.5
    meat_packs = meat_kg / 1.0
    
    price_per_rice_bag = 25.00   
    price_per_tomato_can = 3.50  
    price_per_onion = 0.75       
    price_per_meat_pack = 12.00  
    
    total_rice_cost = rice_bags * price_per_rice_bag
    total_tomato_cost = tomato_cans * price_per_tomato_can
    total_onion_cost = onions * price_per_onion
    total_meat_cost = meat_packs * price_per_meat_pack
    
    grand_total = total_rice_cost + total_tomato_cost + total_onion_cost + total_meat_cost
    
    print("\n--- JOLLOF PARTY SHOPPING LIST & BUDGET ---")
    print(f"Total Rice: {rice_cups:.2f} cups ({rice_bags:.2f} 5-cup bags) - ${total_rice_cost:.2f}")
    print(f"Total Tomato Puree: {tomato_liters:.2f} L ({tomato_cans:.2f} 0.5L cans) - ${total_tomato_cost:.2f}")
    print(f"Total Onions: {onions:.1f} onions - ${total_onion_cost:.2f}")
    print(f"Total Meat: {meat_kg:.2f} kg ({meat_packs:.2f} 1kg packs) - ${total_meat_cost:.2f}")
    print("----------------------------------------")
    print(f"Estimated Total Budget: ${grand_total:.2f}")

main()