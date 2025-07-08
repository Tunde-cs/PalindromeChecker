
#!/usr/bin/env python3

import subprocess
import sys

def run_test_with_debug(test_input):
    """Run a test case and capture both stdout and stderr"""
    print(f"Running test: {test_input.strip()}")
    print("=" * 50)
    
    process = subprocess.Popen(
        ['python3', 'main.py'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    stdout, stderr = process.communicate(input=test_input)
    
    print("STDOUT (Result):")
    print(stdout.strip())
    print("\nSTDERR (Debug Info):")
    print(stderr.strip())
    print("\n" + "=" * 50 + "\n")
    
    return stdout.strip(), stderr.strip()

def main():
    print("DEBUG TEST RUNNER FOR HIDDEN TEST CASES")
    print("=" * 60)
    
    # Test cases that might be failing
    test_cases = [
        # Basic cases
        "1\nzooz\nlzxoo",
        "1\nbac\nbac",
        "1\nabc\ndef",
        
        # Edge cases
        "1\n\n",
        "1\na\n",
        "1\n\nb",
        
        # Single character cases
        "1\na\na",
        "1\na\nb",
        
        # Longer cases
        "1\nabcdefghij\njihgfedcba",
        
        # Multiple test cases in one run
        "3\nzooz\nlzxoo\nbac\nbac\nabc\ndef"
    ]
    
    for i, test_input in enumerate(test_cases):
        print(f"TEST CASE {i + 1}:")
        run_test_with_debug(test_input)

if __name__ == "__main__":
    main()
