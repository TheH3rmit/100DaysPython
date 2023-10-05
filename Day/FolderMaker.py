#Tool for making folders
import os
for n in range(8, 100):
    path = f"E:\Programming\Python\Day{n}"

    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created folder '{path}'.")
    else:
        print(f"Folder '{path}' already exists.")
