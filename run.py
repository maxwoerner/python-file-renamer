import os


def main():

    extension = '.txt'
    rootdir = r'C:\Users\username\Desktop\test'

    for subdir, dirs, files in os.walk(rootdir):

        count = 1

        for file in files:

            # Filepath
            path = os.path.join(subdir, file)
            print("OLD: " + path)

            # Name of parent folder
            parentFolder = os.path.basename(
                os.path.normpath(os.path.dirname(path)))

            if path.lower().endswith((extension)):
                newFileName = parentFolder + " " + str(count) + extension
                newPath = os.path.join(subdir, newFileName)

                os.rename(path, newPath)

                print("NEW: " + newPath)

                count = count + 1

            else:

                print("Not renamed.")

            print("---")


if __name__ == "__main__":
    main()
