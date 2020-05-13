import os

def createIfnotExist(folder):
    if not os.path.exist(folder):
        os.makedirs(folder)

def move(foldername, files):
    for file in files:
        os.replace(file, f'{foldername}/{file}')
    
if __name__ == "__main__":
    
    files = os.listdir()
    files.remove('main.py')

    createIfnotExist('Images')
    createIfnotExist('Media')
    createIfnotExist('Docs')

    imgExts = ['.png', '.jpg', '.jpeg']
    images = [file for file in files if os.path.splitext(file)[1] in imgExts]

    docExts = ['.txt', '.docs', '.doc', '.pdf']
    docs = [file for file in files if os.path.splitext(file)[1] in docExts]

    mediaExts = ['.mp4', '.mp3', '.flv']
    media = [file for file in files if os.path.splitext(file)[1] in mediaExts]

    others = []
    for file in files:
        ext = os.path.splitext(file)[1]
        if (ext not in imgExts) and (ext not in docExts) and (ext not in mediaExts) and os.path.isfile(file):
            other.append(file)
            
    move('Images', images)
    move('Docs', docs)
    move('Media', media)
    move('Others', others)

