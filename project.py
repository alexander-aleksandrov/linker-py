from stemmer import normalize
import os

def main():
    folder = "testVault" 
    file_names = get_file_names(folder)
    change_file_names(file_names, folder)


def get_file_names(path):
    file_names = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    return file_names
    
def change_file_names(file_names, folder):
    for file_name in file_names:
        if validate(file_name):
            new_name = file_name.replace("-", " ").lower()[:-3]
            new_name = new_name.split()
            
            for i in range(len(new_name)):
                new_name[i] = normalize(new_name[i])

            new_name = " ".join(new_name) + ".md"
            old_file_path = os.path.join(folder, file_name)
            new_file_path = os.path.join(folder, new_name)
            os.rename(old_file_path, new_file_path)
        else:
            continue

def normalize_file_names(path):
    ...
    #create folder backup

    #make list of files in folder
    #for each file in list
        #validate file as md
        #if valid, clean name from dashes and add to list
    #for each file in list
        #create list of words from filename
        #if all words are valid
            #create new filename
            #rename file
    #delete folder backup

def link_all(files):
    ...
    #search for filename in all files
    #if found, replace with link


def validate(file_name):
    if file_name.endswith(".md"):
        return True
    
if __name__ == "__main__":
    main()
