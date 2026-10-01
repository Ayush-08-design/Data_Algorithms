# The Rabin-Karp algorithm is a highly efficient string-searching algorithm developed 
# by Richard M. Karp and Michael O. Rabin in 1987. It is designed to find all occurrences 
# of a pattern string within a given text string


# 1. Calculate the Pattern Hash: 
    # Compute the hash value of the pattern string.
# 2. Compute the Initial Window Hash: 
    # Compute the hash value of the first substring in the text that matches the length 
    # of the pattern.

# 3. Slide the Window & Compare:
    # • If the current substring's hash matches the pattern's hash, perform a 
    # character-by-character check to confirm the match. This step handles hash 
    # collisions (spurious hits), where different text yields the same hash value.
    
    # • If the hashes do not match, slide the window right by one character.
    
# 4. Rolling Hash Update: 
    # Instead of recalculating the hash from scratch for the next window, 
    # compute the new hash value in O(1) constant time by mathematically subtracting 
    # the old leftmost character and adding the new rightmost character.
    
    
    
def rabin_karp_search(pattern: str, text: str) -> list:
    
    m = len(pattern)
    n = len(text)
    
    # Base number of characters in the input alphabet (ASCII)
    d = 256 
    # A prime number used for the modulus to prevent overflow and minimize collisions
    q = 101 
    
    pattern_hash = 0    # Hash value for the pattern
    window_hash = 0     # Hash value for the current window of text
    h = 1               # The multiplier value for the highest place value: (d^(m-1)) % q
    
    matches = []

    # Edge case: If pattern is longer than the text or empty
    if m > n or m == 0:
        return matches

    # Calculate the value of h = pow(d, m-1) % q
    for i in range(m - 1):
        h = (h * d) % q

    # 1. Calculate the initial hash value of the pattern and first window of text
    for i in range(m):
        pattern_hash = (d * pattern_hash + ord(pattern[i])) % q
        window_hash = (d * window_hash + ord(text[i])) % q

    # 2. Slide the pattern over the text step by step
    for i in range(n - m + 1):
        
        # If the hash values match, check the characters one by one
        if pattern_hash == window_hash:
            match_found = True
            for j in range(m):
                if text[i + j] != pattern[j]:
                    match_found = False  # Spurious hit / Hash collision
                    break
            
            if match_found:
                matches.append(i)

        # 3. Calculate hash value for the next window of text
        # Remove the leading character, add the trailing character
        if i < n - m:
            window_hash = (d * (window_hash - ord(text[i]) * h) + ord(text[i + m])) % q
            
            # Ensure the window hash value is positive
            if window_hash < 0:
                window_hash = window_hash + q

    return matches


# --- Example Execution ---
if __name__ == "__main__":
    text_corpus = "ABCCDDAEFGBCBABCD"
    search_pattern = "BCD"
    
    results = rabin_karp_search(search_pattern, text_corpus)
    
    print(f"Text:    '{text_corpus}'")
    print(f"Pattern: '{search_pattern}'")
    print(f"Pattern found at starting index/indices: {results}")
