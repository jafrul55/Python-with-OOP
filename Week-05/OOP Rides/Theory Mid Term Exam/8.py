FileName = 'File.txt'
with open(FileName,'r') as file:
    book_concept = file.read()
    pages = book_concept.split("--")
    Len = len(pages)
    current_page = 0

    while current_page < Len:
        print(pages[current_page].strip())
        user_input = input("[enter - read more,positive integer -skiped forward, press q to quit]: ")
        if user_input.lower() == 'q':
            break
        elif user_input.isdigit():
            current_page += int(user_input)
        else:
            current_page += 1
