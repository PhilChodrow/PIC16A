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
        D = ["Riker", "Picard", "Sisko"] 
        with self.assertRaises(TypeError):
            reverse_lookup(D, "Picard")
            
    def test_standard_lookup(self):

        D = {
            "Riker"   : "TNG",
            "Picard"  : "TNG",
            "Sisko"   : "DS9",
            "Kira"    : "DS9",
            "Janeway" : "VOY"
            }

        result = len(reverse_lookup(D, "TNG"))
        
        self.assertEqual(result, 2)
    
    def test_no_matches(self):
        # this test is expected to fail
        
        D = {
            "Riker"   : "TNG",
            "Picard"  : "TNG",
            "Sisko"   : "DS9",
            "Kira"    : "DS9",
            "Janeway" : "VOY"
            }
        
        result = len(reverse_lookup(D, "TOS"))
        
        self.assertEqual(result, 1)

if __name__ == "__main__":
    unittest.main()