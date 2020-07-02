import os


def main():

    renameFilesToParentDir(r'C:\path\to\directory', '.txt')


def renameFilesToParentDir(dir, ext='all'):
    """
    Renames all files inside the given directory and it's subdirectory to the name of the respective parent directory.

    Arguments:
    dir = directory to loop through
    ext (optional) = specify if only specific extensions shall be considered (e.g. '.txt')
    """

    for subdir, dirs, files in os.walk(dir):

        count = 1

        for file in files:

            # Filepath
            path = os.path.join(subdir, file)
            print("OLD: " + path)

            # Name of parent folder
            parentFolder = os.path.basename(
                os.path.normpath(os.path.dirname(path)))

            # File extension
            fileExt = os.path.splitext(path)[1]

            considerFile = True

            if ext != 'all' and not path.lower().endswith((ext)):
                considerFile = False

            if considerFile:
                newFileName = parentFolder + " " + str(count) + fileExt
                newPath = os.path.join(subdir, newFileName)

                os.rename(path, newPath)

                print("NEW: " + newPath)

                count = count + 1

            else:
                print("Not renamed.")

            print("---")


if __name__ == "__main__":
    main()
