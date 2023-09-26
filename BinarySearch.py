from typing import List, Optional, Any

def binary_search(values: List, target: Any) -> Optional[int]:
    """
    Perform a binary search to find a target value in a values.
    
    Return the index of the target if found
    
    Return None if target is not found

    Runtime: O(log(n))

    Arguments:
        values {values[any]} 
        target {any} 
    """
    
    # Sets the upper bound
    upperBound = len(values) - 1  
    # Sets the lower bound
    lowerBound = 0                
    
    # Slice the list of values between the upper and lower bounds
    while lowerBound <= upperBound:
        
        # Sets the value in the middle
        midValue = (upperBound + lowerBound) // 2
        
        if values[midValue] == target:
            # Return the value if found
            return midValue 
        elif values[midValue] > target:
            # Update the upper bound if the target is smaller than the mid value
            upperBound = midValue - 1 
        elif values[midValue] < target:
            # Update the lower bound if the target is larger than the mid value
            lowerBound = midValue + 1           
            
    # Target not found -> return None
    return None


# Test cases

def test_binary_search():
    # Test empty list
    assert binary_search([], 1) is None
    
    # Test list with one element (target present)
    assert binary_search([1], 1) == 0
    
    # Test list with one element (target not present)
    assert binary_search([1], 2) is None
    
    # Test multiple elements (target at beginning)
    assert binary_search([1, 2, 3, 4, 5], 1) == 0
    
    # Test multiple elements (target in middle)
    assert binary_search([1, 2, 3, 4, 5], 3) == 2
    
    # Test multiple elements (target at end)
    assert binary_search([1, 2, 3, 4, 5], 5) == 4
    
    # Test multiple elements (target not present)
    assert binary_search([1, 2, 3, 4, 5], 6) is None
    
    # Test list with duplicate elements (target present)
    assert binary_search([1, 2, 2, 4, 5], 2) in [1, 2]
    
    # Test list with all identical elements (target present)
    assert binary_search([2, 2, 2, 2, 2], 2) in [0, 1, 2, 3, 4]
    
    # Test list with all identical elements (target not present)
    assert binary_search([2, 2, 2, 2, 2], 3) is None
    
    print("All tests passed!")

# Run the test function
test_binary_search()