import sys
from collections import defaultdict

def processGame(events, H):
    """
    events: list of tuples (player, frame, attack_value)
        player: 1 or 2
        frame: non-negative integer
        attack_value: positive integer
    H: starting HP for both players

    Returns: [hp1, hp2] with each clamped to min 0
    """
    # TODO: Implement the corrected game logic
    # Hint: Group events by frame, process each frame atomically

    
    sorted_events = sorted(events, key=lambda event: event[1])
    
    player1_hp = H 
    player2_hp = H
    
    i = 0 

    while i < len(sorted_events):
        current_frame = sorted_events[i][1]

        while i < len(sorted_events) and sorted_events[i][1] == current_frame:
            if current_frame[0] == 1:
                player2_hp -= current_frame[2]
            else: 
                player1_hp -= current_frame[2]

        i += 1 

        if player1_hp <= 0 or player2_hp <= 0: 
            break 

    return [player1_hp, player2_hp]


# --- Main execution block. DO NOT MODIFY ---
if __name__ == "__main__":
    try:
        H = int(input().strip())
        n = int(input().strip())
        events = []
        for _ in range(n):
            parts = input().strip().split()
            events.append((int(parts[0]), int(parts[1]), int(parts[2])))

        result = processGame(events, H)
        print(f"{result[0]} {result[1]}")

    except ValueError as e:
        print(f"Input Error: {e}", file=sys.stderr)
        sys.exit(1)
    except EOFError:
        print("Error: Not enough input lines provided.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)
