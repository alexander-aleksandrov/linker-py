from stemmer import normalize
import os
import re

def main():
    folder = "testVault" 
    file_names = get_file_names(folder)
    file_dict = normalize_file_names(file_names)
    
    #For each file in the directory normalize it's text and link with posible file names
    for file_name in file_dict:
        path = folder + "/" + file_name
        link_all(file_dict, path)
    print("Done")

#Get all files in the directory
def get_file_names(path):
    file_names = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    file_names = sorted(file_names, key=len, reverse=True)
    return file_names

#Normalize file names by stemming words in them returning a dictionary
def normalize_file_names(file_names): 
    norm_names = {}
    for name in file_names:
        if is_valid(name):
            clean_name = name.replace("-", " ").lower()[:-3]
            word_list = clean_name.split()            
            for i in range(len(word_list)):
                word_list[i] = normalize(word_list[i])
            norm_names[name] = word_list
        else:
            continue
    return norm_names

def link_all(file_dict, path):
    orig_text = open(path, "r", encoding="utf-8").read()
    for file_name in file_dict:
        pattern = ""
        for word in file_dict[file_name]:
            pattern += fr"{word}[а-я]*\s+"      
        matches = re.findall(pattern, orig_text)
        matches = list(dict.fromkeys(matches))
        for match in matches:
            match = match.strip()
            file_name = file_name[:-3]
            orig_text = replace_outside_brackets(orig_text, match, f"[[{file_name}|{match}]]")
    with open(path, "w", encoding="utf-8") as f:
        f.write(orig_text)
        print(f"Linked - {path}")
                
def replace_outside_brackets(text, match, replacement):
    brackets_pattern = r"\[\[.*?\]\]"
    inside_brackets = re.findall(brackets_pattern, text)
    for i in range(len(inside_brackets)):
        text = text.replace(inside_brackets[i], f"__MARKER{i}__")
    text = text.replace(match, replacement)
    for i in range(len(inside_brackets)):
        text = text.replace(f"__MARKER{i}__", inside_brackets[i])
    return text


def is_valid(file_name):
    if file_name.endswith(".md"):
        return True
    
if __name__ == "__main__":
    main()
