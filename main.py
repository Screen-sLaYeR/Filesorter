from  tkinter.ttk import *
from tkinter.ttk import Progressbar
import tkinter as tk 
import tkinter.filedialog
import shutil,os,time
main_dir = ""
global res 
res = []
#Image_Xtensions
image_extensions = (".jpg", ".jpeg", ".JPG", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw", ".PNG",
                    ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico")
# ? supported Video types
video_extensions = (".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg", "MOV",
                    ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd")
# ? supported Audio types
audio_extensions = (".m4a", ".flac", "mp3", ".wav", ".wma", ".aac")
# ? supported Document types
document_extensions = (".doc", ".docx", ".odt", ".PDF",
                       ".pdf", ".xls", ".xlsx", ".ppt", ".pptx")

def path_getter():
    tk.directory= tkinter.filedialog.askdirectory()
    main_dir = tk.directory
    return main_dir
#Printing the List Elements
def og_sort(main_dir,res,the_op):
    progress.place(x = 10, y = 130)
    the_op.place(x=80,y = 170)
    img_dest = main_dir +"/Images"
    progress["value"] = 5
    the_op.insert(tk.END,"Created the Image Folder\n")
    time.sleep(1)
    os.mkdir(img_dest)
    vid_dest = main_dir +"/Videos"
    progress["value"] = 10
    time.sleep(1)
    the_op.insert(tk.END,"Created the Video Folder\n")
    os.mkdir(vid_dest)
    aud_dest = main_dir +"/Audios"
    os.mkdir(aud_dest)
    progress["value"] = 15
    time.sleep(1)
    the_op.insert(tk.END,"Created the Audio Folder\n")
    doc_dest = main_dir +"/Documents"
    os.mkdir(doc_dest)
    progress["value"] = 20
    time.sleep(1)
    the_op.insert(tk.END,"Created the Documant Folder\n")
    mix_dest = main_dir +"/Mixed"
    os.mkdir(mix_dest)
    progress["value"] = 25
    time.sleep(1)
    the_op.insert(tk.END,"Created the Mixed Folder\n")
    for file in os.listdir(main_dir):
    # check if current path is a file
        if os.path.isfile(os.path.join(main_dir, file)):
            res.append(file)
    pro_bar = 75/len(res)
    updater = pro_bar
    def message(string):
           for i in string:
            time.sleep(0.2)
            the_op.insert(tk.END,i)
            the_op.yview(tk.END)
    for i in res:
        #for Images
        progress["value"]= 25 + pro_bar
        if i.endswith(image_extensions):
            current_file_dest = main_dir+'/'+i
            shutil.move(current_file_dest,img_dest)
            message(i)
    #For Videos 
        if i.endswith(video_extensions):   
            current_file_dest = main_dir+'/'+i
            shutil.move(current_file_dest,vid_dest)
            message(i)
    #For Audios 
        if i.endswith(audio_extensions):
            current_file_dest = main_dir+'/'+i
            shutil.move(current_file_dest,aud_dest)
            message(i)
    #For Documents
        if i.endswith(document_extensions):
            current_file_dest = main_dir+'/'+i
            shutil.move(current_file_dest,doc_dest)
            message(i)
        else: 
            current_file_dest = main_dir+'/'+i
        try:
            shutil.move(current_file_dest,mix_dest)
            message(i)
        finally:
            pro_bar = pro_bar + updater
            continue
root = tk.Tk()
root.geometry("400x300")
root.title("Super File Manager")
browse_button = Button(root, text = "Browse", command = lambda:path_getter())
progress = Progressbar(root, orient = tk.HORIZONTAL,
          length = 380, mode = 'determinate')
start_button = Button(root, text = "Start", command = lambda:og_sort(main_dir,res,the_op))
the_op = tk.Text(root,height = 5,width =35)
curr_dir = tk.Text(root,height=1,width=35)
def path_getter():
    global main_dir
    tk.directory= tkinter.filedialog.askdirectory()
    main_dir = tk.directory
    curr_dir.insert(tk.END,main_dir)
curr_dir.place(x=10,y=60)
start_button.place(x=170,y=100)
browse_button.place(x=320,y=57)
root.mainloop()