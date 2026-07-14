import sys

def generate_shape(n, shape):
    """
    Generates a geometric pattern on an n x n grid.

    Args:
        n: Grid size (n x n, always odd for diamond)
        shape: Either "checkerboard" or "diamond"

    Returns:
        A 2D list of integers (0 or 1) representing the pattern.
    """
    result = []
    center = n // 2
    if shape == "checkerboard":
        for i in range(5):
            a=[]
            for j in range(5):
                if i % 2 == 0:
                    if j % 2 == 0:
                        a.append(0)
                    else:
                        a.append(1)
                else:
                    if j % 2 == 0:
                        a.append(1)
                    else:
                        a.append(0)
        result.append(a)    

    elif shape == "diamond":
        for i in range(n):
            arr = []
            for j in range(n):
                if abs(i-center) + abs(j-center) <= center:
                    arr.append(1)
                else: 
                    arr.append(0)
            result.append(arr)

    return result 

# --- Main execution block. DO NOT MODIFY ---
if __name__ == "__main__":
    try:
        n = int(input().strip())
        shape = input().strip()

        result = generate_shape(n, shape)
        for row in result:
            print(" ".join(str(x) for x in row))

    except ValueError as e:
        print(f"Input Error: {e}", file=sys.stderr)
        sys.exit(1)
    except EOFError:
        print("Error: Not enough input lines provided.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)
