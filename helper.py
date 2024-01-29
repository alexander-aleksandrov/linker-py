import re

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

def convert_text(path):
    converted_text = []
    new_text = ""
    with open(path, "r", encoding="utf-8") as f:
        text = f.read().split()
    for word in text:
        if re.fullmatch(r"[а-я]+", word.strip().lower()):
            converted_text.append(word)
    for word in converted_text:
        new_text += word + "\n"
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
           
        

    

if __name__ == "__main__":
    main()