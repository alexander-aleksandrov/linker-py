from word import normalize

def main():
    path = input("Enter the path to the folder: ")
    files = normalize_file_names(path)
    link_all(files)   



def normalize_file_names(path):
    ...
    #create folder backup

    #make list of files in folder
    #for each file in list
        #validate file as md
        #if valid, add to list
    #for each file in list
        #create new filename
        #rename file

    #delete folder backup

def create_new_filename(file_name):
     ...
     #create new filename using normalize function
     #return new filename

def link_all(files):
    ...
    #search for filename in all files
    #if found, replace with link


if __name__ == "__main__":
    main()
