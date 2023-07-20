# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. 
# Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к языку

text = "She sells sea shells on the sea shore," \
       " The shells that she sells are sea shells," \
       " I'm sure. So if she, sells sea shells, on the" \
       " sea shore I'm sure, that the shells, are sea shore, shells"

text_list = text.lower().split()

text_dict = {}

for i in text_list:
    cl = i.strip(".,!:;")
    if cl not in text_dict:
        text_dict[cl] = 1
    else:
        text_dict[cl] += 1

print(text_dict)

result = dict(sorted(text_dict.items(), key=lambda x: x[1], reverse=True))
print(result)