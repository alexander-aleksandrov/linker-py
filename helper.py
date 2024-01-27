
def main():
    endings = "ивш,ывш,ующ".split(",")
    sorted_endings = sorted(endings, key=len, reverse=True)
    print(sorted_endings)

if __name__ == "__main__":
    main()