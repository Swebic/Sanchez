def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "set_3_sample_data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if from_member follows to_member,
        "followed by" if from_member is followed by to_member,
        "friends" if from_member and to_member follow each other,
        "no relationship" if neither from_member nor to_member follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    fromfollows = social_graph[from_member]["following"]
    tofollows = social_graph[to_member]["following"]

    if to_member in fromfollows and from_member in tofollows:
        return "friends"
    elif to_member in fromfollows:
        return "follower"
    elif from_member in tofollows: 
        return "followed by"
    else:
        return "no relationship"


def tic_tac_toe(board):
    '''Tic Tac Toe.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "set_3_sample_data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    size = len(board)
    #Checks Rows
    for row in board:
        if row.count(row[0]) == size and row[0] !='':
            return row[0]
    #Checks Columns
    for col in range(size):
        column = [board[row][col] for row in range(size)]
        if column.count(column[0]) == size and column [0] != '':
            return column [0]
    #Checks from top-left to bottom-right
    diagonal1 = [board[i][i] for i in range(size)]
    if diagonal1.count(diagonal1[0])== size and diagonal1[0] != '':
        return diagonal1[0]
    #Checks from from top-right to bottom-left
    diagonal2 = [board[i][size - 1 - i] for i in range(size)]
    if diagonal2.count(diagonal2[0])== size and diagonal2[0] != '':
        return diagonal2[0]
    return "NO WINNER"

def eta(first_stop, second_stop, route_map):
    '''ETA.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "set_3_sample_data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    total_travel_time = 0
    current_stop = first_stop

    # Loop until we reach the second_stop
    while current_stop != second_stop:
        found_next_leg = False #Finds if there's a next leg in the loop
        for (from_stop, to_stop), leg_info in route_map.items(): #Accessing dictionary items
            if from_stop == current_stop:
                total_travel_time += leg_info["travel_time_mins"]
                current_stop = to_stop
                found_next_leg = True
                break  # Move to the next leg
        
        # This would only happen if the route is not fully connected
        if not found_next_leg:
            # If for some reason the next leg isn't found, it breaks to prevent infinite loop
            break 

    return total_travel_time
