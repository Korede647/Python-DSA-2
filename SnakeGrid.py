# Simulate a snake in a grid based on directions. Snake grows when it eats food, dies when 
# it hits walls or itself. Return final body coordinates or 'Game Over'. 
# Sample Input grid = (5,5), start = (2,2), directions = ['U','U','R','D','D','L','L','U'], food = 
# {(1,2), (2,3)}  
# Expected Output [(2,3), (2,2), (1,2)] or 'Game Over'  
# Hint: Use a deque to represent the snake body and a set for O(1) collision detection. 


from collections import deque

def snake_grid(grid, start, directions, food):
    rows, cols = grid
    snake = deque([start])
    food_set = set(food)
    food_eaten = 0

    for direction in directions:
        head_x, head_y = snake[0]

        if direction == 'U':
            new_head = (head_x - 1, head_y)
        elif direction == 'D':
            new_head = (head_x + 1, head_y)
        elif direction == 'L':
            new_head = (head_x, head_y - 1)
        elif direction == 'R':
            new_head = (head_x, head_y + 1)
        else:
            continue

        # Check if the new head is out of bounds or collides with itself
        if (new_head[0] < 0 or new_head[0] >= rows or
                new_head[1] < 0 or new_head[1] >= cols or
                new_head in snake):
            return 'Game Over'

        # Add the new head to the snake
        snake.appendleft(new_head)

        # Check if the snake eats food
        if new_head in food_set:
            food_set.remove(new_head)
            food_eaten += 1
        else:
            snake.pop()  # Remove tail if no food eaten

    return list(snake)

# Example usage
grid = (5, 5)
start = (2, 2)
directions = ['U', 'U', 'R', 'D', 'D', 'L', 'L', 'U']
food = {(1, 2), (2, 3)}

result = snake_grid(grid, start, directions, food)
print(result)  # Output: [(2, 3), (2, 2), (1, 2)] or 'Game Over'