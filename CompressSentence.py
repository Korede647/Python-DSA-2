# Compress a sentence by replacing each unique word with an integer ID.  
# Sample Input 'the cat sat on the mat'  
# Expected Output encoded = [1,2,3,4,1,5], mapping = {1:'the',2:'cat',3:'sat',4:'on',5:'mat'} 
# Hint: Use a dictionary to map words to IDs, assign IDs on first occurrence.

from collections import defaultdict

def compress_sentence(sentence):
    words = sentence.split()
    word_to_id = {}
    encoded = []
    next_id = 1

    for word in words:
        if word not in word_to_id:
            word_to_id[word] = next_id
            next_id += 1
        encoded.append(word_to_id[word])

    return encoded, word_to_id

# Example usage
sentence = 'the cat sat on the mat'
encoded, mapping = compress_sentence(sentence)
print('Encoded:', encoded)  # Output: [1, 2, 3, 4, 1, 5]
print('Mapping:', mapping)  # Output: {1: 'the', 2: 'cat', 3: 'sat', 4: 'on', 5: 'mat'}