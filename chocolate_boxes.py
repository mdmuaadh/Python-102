# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Jose Mina Velasco
#               Mayreli Campos 
#               Herman Ptacnik
#               Muaadh Mohideen
# Section:      535
# Assignment:   TEAM LAB 10  
# Date:         10/26/2025

import random

def make_boxes(chocolates):
    """Return 25 boxes of 4 truffles each that meet all conditions."""
    
    def is_valid_box(box, chocolates):
        """Check if a box meets all requirements."""
        if len(box) != 4:
            return False
        
        truffles = [chocolates[tid] for tid in box]
        
        # Check for duplicate truffles (same attributes)
        if len(truffles) != len(set(tuple(t) for t in truffles)):
            return False
        
        types = [t[0] for t in truffles]
        shapes = [t[1] for t in truffles]
        fills = [t[2] for t in truffles]
        tops = [t[3] for t in truffles]
        
        # No caramel + vanilla
        if "caramel" in fills and "vanilla" in fills:
            return False
        
        # No nuts + sprinkles
        if "nuts" in tops and "sprinkles" in tops:
            return False
        
        # No rectangle + square
        if "rectangle" in shapes and "square" in shapes:
            return False
        
        # Dark chocolate: 0, 2, or 3 only
        dark_count = types.count("dark")
        if dark_count == 1 or dark_count > 3:
            return False
        
        return True
    
    def can_add_truffle(box, tid, chocolates):
        """Check if adding a truffle to box keeps it valid."""
        if tid in box:
            return False
        
        test_box = box + [tid]
        truffles = [chocolates[t] for t in test_box]
        
        # Check for duplicate truffle attributes
        if len(set(tuple(t) for t in truffles)) != len(truffles):
            return False
        
        types = [t[0] for t in truffles]
        shapes = [t[1] for t in truffles]
        fills = [t[2] for t in truffles]
        tops = [t[3] for t in truffles]
        
        # No caramel + vanilla
        if "caramel" in fills and "vanilla" in fills:
            return False
        
        # No nuts + sprinkles
        if "nuts" in tops and "sprinkles" in tops:
            return False
        
        # No rectangle + square
        if "rectangle" in shapes and "square" in shapes:
            return False
        
        # Dark chocolate constraint (can't be 1, max 3)
        dark_count = types.count("dark")
        if dark_count > 3:
            return False
        if len(test_box) == 4 and dark_count == 1:
            return False
        
        return True
    
    # Try multiple times with different random orderings
    for attempt in range(100):
        truffle_ids = list(chocolates.keys())
        random.shuffle(truffle_ids)
        
        boxes = [[] for _ in range(25)]
        used = set()
        
        # Greedy assignment
        for tid in truffle_ids:
            for box in boxes:
                if len(box) < 4 and can_add_truffle(box, tid, chocolates):
                    box.append(tid)
                    used.add(tid)
                    break
        
        # Check if we got a valid solution
        if all(len(box) == 4 for box in boxes) and all(is_valid_box(box, chocolates) for box in boxes):
            return boxes
        
    # If we couldn't find a solution, return empty list
    return []

