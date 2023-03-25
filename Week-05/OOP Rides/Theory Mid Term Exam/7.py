FileName = 'File.txt'
with open(FileName,'r') as file:
    book_concept = file.read()
    pages = book_concept.split("--")
    Len = len(pages)

    for i in range(Len):
        print(pages[i].strip())
        if i < Len-1:
            user_input = input("[enter - read more,press q to quit]: ")
            if user_input.lower() == 'q':
                break