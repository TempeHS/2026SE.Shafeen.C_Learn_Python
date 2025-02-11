file = (input("what file?: ")).strip()

if file.endswith(".jpg") or (".jpeg"):
    print("image/jpg") 
elif file.endswith(".png"):
    print("image/png")
elif file.endswith(".pdf"):
    print("application/pdf")
elif file.endswith(".gif"):
    print("image/gif")
elif file.endswith(".txt"):
    print("file/txt")
elif file.endswith(".zip"):
    print("file/zip.")   
else:
    print("application/octet-stream")
       