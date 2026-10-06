colorY = "\033[0;93m"
colorR = "\033[0;72m"
resetC = "\033[0m"
myint = 4
char = f"{colorY}☺︎{resetC}"
enm = f"{colorR}%{resetC}"
print('{:02d}'.format(myint))
print(f"↑=-{char}-$-{enm}--&-=↓")
print("+-------------------------------------------------+")
print("| +------------- You leveled up !! -------------+ |")

for i in range(100):
    color = f"\033[0;{i}m"
    print(f"{color}rainbowssss{resetC}" + f" this is color {i}")