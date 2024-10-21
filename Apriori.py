from itertools import combinations

# Function to calculate support for an itemset
def calculate_support(dataset, itemset):
    count = 0
    for transaction in dataset:
        if itemset.issubset(transaction):
            count += 1
    return count

# Function to generate candidate itemsets
def generate_candidates(prev_freq_itemsets, length):
    candidates = set()
    prev_freq_itemsets = list(prev_freq_itemsets)
    for i in range(len(prev_freq_itemsets)):
        for j in range(i + 1, len(prev_freq_itemsets)):
            # Generate combinations of frequent itemsets
            union_set = prev_freq_itemsets[i].union(prev_freq_itemsets[j])
            if len(union_set) == length:
                candidates.add(frozenset(union_set))
    return candidates

# Apriori Algorithm
def apriori_algorithm(dataset, min_support):
    dataset = list(map(set, dataset))  # Convert each transaction into a set
    items = {frozenset([item]) for transaction in dataset for item in transaction}
    
    # Step 1: Generate frequent 1-itemsets
    freq_itemsets = {item for item in items if calculate_support(dataset, item) >= min_support}
    all_freq_itemsets = [freq_itemsets]  # To store all levels of frequent itemsets
    supports = {}  # To store the support of each itemset

    # Store the support of 1-itemsets
    for itemset in freq_itemsets:
        supports[itemset] = calculate_support(dataset, itemset)
    
    # Step 2: Generate larger itemsets until no more frequent itemsets can be generated
    k = 2  # Length of itemsets to generate
    while freq_itemsets:
        candidates = generate_candidates(freq_itemsets, k)
        freq_itemsets = {itemset for itemset in candidates if calculate_support(dataset, itemset) >= min_support}
        
        # Store the support of k-itemsets
        for itemset in freq_itemsets:
            supports[itemset] = calculate_support(dataset, itemset)
        
        if freq_itemsets:
            all_freq_itemsets.append(freq_itemsets)
        k += 1
    
    return all_freq_itemsets, supports

# Function to generate association rules from the last frequent itemset
def generate_association_rules_from_last(freq_itemsets, dataset, supports, min_confidence):
    rules = []
    last_level = freq_itemsets[-1]  # Get the last frequent itemset level
    for itemset in last_level:
        for i in range(1, len(itemset)):
            subsets = map(frozenset, combinations(itemset, i))
            for subset in subsets:
                confidence = supports[itemset] / supports[subset]
                if confidence >= min_confidence:
                    rules.append((subset, itemset - subset, supports[itemset], confidence))
    return rules

# Example Usage
if __name__ == "__main__":
    # Dataset
    dataset = [
         {1, 2, 4},
        {2, 3, 5},
        {1, 2, 3, 5},
        {2, 5}

    ]
    
    # Get user input for min_support and min_confidence in percentage
    total_transactions = len(dataset)
    min_support_percentage = float(input("Enter minimum support percentage (e.g., 50 for 50%): "))
    min_confidence_percentage = float(input("Enter minimum confidence percentage (e.g., 50 for 50%): "))
    
    # Calculate min_support and min_confidence based on user input
    min_support = (min_support_percentage / 100) * total_transactions
    min_confidence = min_confidence_percentage / 100  # Convert to decimal

    # Run Apriori Algorithm
    freq_itemsets, supports = apriori_algorithm(dataset, min_support)
    
    # Output frequent itemsets with their support
    print("Frequent Itemsets with Support:")
    for i, level in enumerate(freq_itemsets, start=1):
        print(f"\nIteration {i}:")
        for itemset in level:
            print(f"{set(itemset)}: Support = {supports[itemset]}")
    
    # Generate association rules only from the last frequent itemset
    rules = generate_association_rules_from_last(freq_itemsets, dataset, supports, min_confidence)

    # Output association rules
    if rules:
        print("\nAssociation Rules from Last Frequent Itemset:")
        for rule in rules:
            antecedent, consequent, support, confidence = rule
            confidence_percentage = confidence * 100
            print(f"{set(antecedent)} => {set(consequent)}: Support = {support}, Confidence = {confidence:.2f} ({confidence_percentage:.2f}%)")
    else:
        print("\nNo association rules to be generated.")
