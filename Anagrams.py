#  Group sentences that are anagrams of each other, ignoring spaces and punctuation.  
# Sample Input ['Listen to me', 'Enlist to me', 'The eyes', 'They see']  
# Expected Output [['Listen to me', 'Enlist to me'], ['The eyes', 'They see']] 
# Hint: Normalize sentences and use sorted characters or frequency counts as keys.

from collections import defaultdict

def group_anagrams(sentences):
    anagram_map = defaultdict(list)

    for sentence in sentences:
        # Normalize the sentence: remove spaces and punctuation, convert to lowercase
        normalized = ''.join(filter(str.isalpha, sentence)).lower()
        # Use sorted characters as the key
        key = ''.join(sorted(normalized))
        anagram_map[key].append(sentence)

    return list(anagram_map.values())

# Example usage
sentences = ['Listen to me', 'Enlist to me', 'The eyes', 'They see']
result = group_anagrams(sentences)
print(result)  # Output: [['Listen to me', 'Enlist to me'], ['The eyes', 'They see']]