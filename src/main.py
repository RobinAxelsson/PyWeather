def main():
    
    print("Hello World")
    with open("data.json", 'r', encoding="utf-8") as datafile:
        print(datafile.read())
    return

if __name__ == '__main__':
    main()