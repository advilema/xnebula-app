import os
import shutil


PATH_DATABASE = "instance/database.db"
PATH_IMAGES = "static/images"


def delete_file(file_path):
    try:
        os.remove(file_path)
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def reset():
    print("Deleting the database")
    delete_file(PATH_DATABASE)
    print("Done!")

    print("Deleting all the images")
    shutil.rmtree(PATH_IMAGES)

    # Recreate the empty directory
    os.mkdir(PATH_IMAGES)

    print("App successfully reset!")


if __name__ == "__main__":
    reset()