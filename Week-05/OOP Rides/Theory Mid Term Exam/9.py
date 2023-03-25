FileName = 'File.txt'
with open(FileName,'r') as file:
    book_concept = file.read()
    pages = book_concept.split("--")
    Len = len(pages)
    current_page = 0

    while current_page >= 0 and current_page < Len:
        print(pages[current_page].strip())
        user_input = input("[enter - read more,press positive integer -skiped forward,press -1 to go back page, press q to quit]: ")
        if user_input.lower() == 'q':
            break
        elif user_input.isdigit():
            current_page += int(user_input)
        elif user_input.startswith("-") and user_input[1:].isdigit():
            current_page += int(user_input)
        else:
            current_page += 1
