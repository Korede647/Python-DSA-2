# Rank students by average score, breaking ties alphabetically. Sample Input  
# {'Alice':[90,85,88], 'Bob':[90,85,88], 'Charlie':[95,80,85]}  
# Expected Output [('Alice', 87.67), ('Bob', 87.67), ('Charlie', 86.67)] 
# Hint: Compute averages with sum()/len(). Sort with a lambda key (-average, name


from collections import defaultdict

def rank_students(scores):
    averages = []

    for student, marks in scores.items():
        average = sum(marks) / len(marks)
        averages.append((student, round(average, 2)))

    # Sort by average score (descending) and then by name (ascending)
    averages.sort(key=lambda x: (-x[1], x[0]))

    return averages

# Example usage
scores = {
    'Alice': [90, 85, 88],
    'Bob': [90, 85, 88],
    'Charlie': [95, 80, 85]
}
result = rank_students(scores)
print(result)  # Output: [('Alice', 87.67), ('Bob', 87.67), ('Charlie', 86.67)]