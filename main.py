def count_batteries_by_health(present_capacities):
    
    # Classifies batteries based on their state-of-health (SoH).
    
    # Initialize counters for different health categories
    healthy_count = 0
    exchange_count = 0
    failed_count = 0
    
    # Constants
    rated_capacity = 120  # Rated capacity of a new battery
    
    # Classify batteries by SoH
    for capacity in present_capacities:
        # Calculate SoH
        soh = (capacity / rated_capacity) * 100
        
        # Classify based on SoH ranges
        if soh > 80:
            healthy_count += 1
        elif 62 <= soh <= 80:
            exchange_count += 1
        else:
            failed_count += 1
    
    # Return counts as a dictionary
    return {
        "healthy": healthy_count,
        "exchange": exchange_count,
        "failed": failed_count
    }


def test_bucketing_by_health():
    # Tests the battery health classification function.
  
    print("Counting batteries by SoH...\n")
    
    # Test data
    present_capacities = [113, 116, 80, 95, 92, 70]
    
    # Run classification
    counts = count_batteries_by_health(present_capacities)
    
    # Print the counts obtained for initial test data
    print("Counts for initial test data:")
    print(counts)
    
    # Assertions
    assert counts["healthy"] == 2
    assert counts["exchange"] == 3
    assert counts["failed"] == 1
    
    
    ## Additional tests for edge cases
    additional_test_data = [120, 62, 61]
    additional_counts = count_batteries_by_health(additional_test_data)
    
    # Print counts for additional test data
    print("\nCounts for additional test data:")
    print(additional_counts)
    
    # Assertions for additional test data
    assert additional_counts["healthy"] == 1
    assert additional_counts["exchange"] == 0
    assert additional_counts["failed"] == 2
    
    print("Classification test passed! :)")



if __name__ == '__main__':
  test_bucketing_by_health()
