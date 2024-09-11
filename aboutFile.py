def read_file(name_file):
    try:
        with open(name_file + ".txt") as file:
            text = file.readline()
            print(text)
    except FileNotFoundError:
        print("File not found")
    except IOError:
        print("Cant read file")
    except:
        print ("Unknown error")

read_file("file")