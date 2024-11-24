def read_file():
    try:
        with open("data.txt","r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("File not found")
    except PermissionError:
        print("You don not have permission to read the file")
    except Exception as e:
        print(f"An error occurred: {e}")
read_file()