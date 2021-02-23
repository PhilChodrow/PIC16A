import unittest

def reverse_lookup(D, val):
    """
    Find all keys in a dictionary D with the specified value. 
    """
    if type(D) != dict:
        raise TypeError("First argument must be a dictionary")

    return [key for key in D.keys() if D[key] == val]

class TestReverseLookup(unittest.TestCase):
    
    def test_type_error(self):
        D = ["cat", "dog", "giraffe"] 
        with self.assertRaises(TypeError):
            reverse_lookup(D, "Picard")
            
    def test_standard_lookup(self):

        D={
            "cat":3,
            "dog":3,
            "platypus":8,
            "cow":3,
            "duck":4
            }

        result = len(reverse_lookup(D, 3))
        
        self.assertEqual(result, 3)
    
    def test_no_matches(self):
        # this test is expected to fail
        
        D={
            "cat":3,
            "dog":3,
            "platypus":8,
            "cow":3,
            "duck":4
            }

        result = len(reverse_lookup(D, 6))
        
        self.assertEqual(result, 0)
    

if __name__ == "__main__":
    unittest.main()