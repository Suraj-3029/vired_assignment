import sys

if (len(sys.argv) != 3):
    print("Please give the Source and destination")
    exit()
source_dir = sys.argv[1]
destination_dir = sys.argv[2]
print(source_dir, destination_dir)
