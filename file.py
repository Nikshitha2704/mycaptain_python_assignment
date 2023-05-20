filename = input("enter a filename: ")
parts = filename.split('.')
if len(parts) > 1:
    print("extension:", parts[-1])
else:
    print("the file name does not have any extension")
    