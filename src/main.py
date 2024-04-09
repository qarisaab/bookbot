def main():
    with open('books/frankenstein.txt') as f:
        book = 'books/frankenstein.txt'
        text = get_book_text(book)
        print(f"--- Begin report of the {book} --- ")
        count = count_word(text)
        print(f"{count} words found in the document")
        print()
        each_letter = count_letters(text)
        sorted_list = list_of_d(each_letter)
        for item in sorted_list:
            if not item["char"].isalpha():
                continue
            print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")
        


def get_book_text(path):
    with open(path) as f:
        file_content = f.read()
        return file_content

def count_word(text):
    c = text.split()
    return len(c)


def count_letters(text): 
    dic = {}
    for t in text:
        low = t.lower()
        if low in dic:
            dic[low] += 1
        else:
            dic[low] = 1
    return dic
  

def sort_num(dic): 
    return dic['num']

def list_of_d(d):
    li = []
    for ch in  d:
        li.append({'char': ch, 'num': d[ch]})
    li.sort(reverse=True,   key=sort_num)
    return li



main()