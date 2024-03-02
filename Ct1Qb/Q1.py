# A dart board of radius 10 units & the wall it is hanging on are represented as using a 2D co-ordinate (0,0) . Variables x & y store the x coordinate and y coordinate of the dart that hits the dart  board . write a python expression using variables x & y that evaluates to true if the dart hits ( is within) the dart board .

def is_dart_on_board(x, y):
    # Check if the distance from the origin is less than or equal to the radius of the dart board
    dart_hits_board = (x**2 + y**2) <= 10**2

    # Display the result
    if dart_hits_board:
        print("The dart hits the dart board!")
    else:
        print("The dart misses the dart board.")


# Input x and y coordinates of the dart
x = float(input("Enter the x coordinate of the dart: "))
y = float(input("Enter the y coordinate of the dart: "))

# Check if the dart hits the dart board
is_dart_on_board(x, y)



# a( 0, 0)  => The dart hits the dart board!
# b( 10, 10) => The dart misses the dart board.
# c( 6, 6) => The dart hits the dart board!
# d( 7, 8) => The dart misses the dart board.
