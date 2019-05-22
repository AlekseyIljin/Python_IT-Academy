class FileParser:
    def __init__(self, url, text, for_replace = None):
        self.url = url
        self.text = text
        self.for_replace = for_replace

    def counter(self):
        file = open(self.url, 'r')
        start_data = file.read()
        file.close()
        count = start_data.count(self.text)
        return count

    def replacer(self):
        file = open(self.url, 'r')
        start_data = file.read()
        file.close()

        file = open(self.url, 'w')
        new_data = start_data.replace(self.text, self.for_replace)
        file.write(new_data)
        file.close()

class Main:
    def main():
        mode = input("Which mode would you like to use 1 or 2?\n")
        if mode == "1":
            path = input("Input path where do you want to search:\n")
            searching_string = input("Input which string are you looking for:\n")
            parser = FileParser(path, searching_string)
            print("Total count of that string is: " + str(parser.counter()))
        elif mode == "2":
            path = input("Input path where do you want to search:\n")
            to_change_string = input("Input which string are you want to change:\n")
            for_change = input("And finally to which string you want change:\n")
            parser = FileParser(path, to_change_string, for_change)
            parser.replacer()
            print("Now checkout your file")
        

if __name__ == "__main__":
    Main.main()
