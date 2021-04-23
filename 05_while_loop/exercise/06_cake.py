width = int(input())
height = int(input())
piece = input()
size = width * height
while size > 0 and piece != "STOP":
    piece_size = int(piece)
    size -= piece_size
    if size < 0:
        print(f"No more cake left! You need {abs(size)} pieces more.")
        break
    piece = (input())
if size >= 0:
    print(f"{size} pieces are left.")
