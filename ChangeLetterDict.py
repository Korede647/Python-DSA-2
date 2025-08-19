# Transform a start word into an end word by changing one letter at a time, ensuring each 
# intermediate word exists in a dictionary. Use BFS to find the shortest transformation 
# sequence.  
# Sample Input start = 'hit', end = 'cog', dictionary = {'hot','dot','dog','lot','log','cog'} 
# Expected Output ['hit', 'hot', 'dot', 'dog', 'cog'] 
# Hint: Think of words as nodes and edges between words that differ by 1 letter

from collections import deque
def change_letter_dict(start, end, dictionary):
    if end not in dictionary:
        return []

    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        current_word, path = queue.popleft()

        if current_word == end:
            return path

        for i in range(len(current_word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = current_word[:i] + c + current_word[i+1:]

                if next_word in dictionary and next_word not in visited:
                    visited.add(next_word)
                    queue.append((next_word, path + [next_word]))

    return []

# Example usage
start = 'hit'
end = 'cog'
dictionary = {'hot', 'dot', 'dog', 'lot', 'log', 'cog'}
result = change_letter_dict(start, end, dictionary)
print(result)  # Output: ['hit', 'hot', 'dot', 'dog', 'cog']





