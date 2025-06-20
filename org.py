import os
import shutil

directory="D:\VS CODE\Ideas\Folder organization"

file_categories={
    "Images":[".jpg",".jpeg",".png"],
    "Videos":[".mp4",".mod"],
    "Docx":[".pdf",".txt",".xlsx",".txt"],
    "Others":[]
}


for file_name in os.listdir(directory):
    print(file_name)
    file_path=os.path.join(directory,file_name)
    _,file_ext=os.path.splitext(file_path)
    print(file_ext)

    category_to_drop="Others"
    for category,extension in file_categories.items():
        if file_ext in extension:
            category_to_drop=category
            break;
    
    path_to_be_moved=os.path.join(directory,category_to_drop)

    os.makedirs(path_to_be_moved,exist_ok=True)
    shutil.move(file_path,path_to_be_moved)
print(file_categories)