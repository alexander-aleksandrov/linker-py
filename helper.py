
def main():
    sort_exclutions()

def sort_exclutions():
    with open("files/exclutions.txt", "r", encoding="utf-8") as f:
        exclutions = [line.strip() for line in f]
    sorted_exclutions = sorted(exclutions, key=len, reverse=True)
    #remove duplicates
    sorted_exclutions = list(dict.fromkeys(sorted_exclutions))
    with open("files/exclutions.txt", "w", encoding="utf-8") as f:
        for word in sorted_exclutions:
            f.write(word + "\n")

if __name__ == "__main__":
    main()