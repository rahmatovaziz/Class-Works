# 1 задача

# Написать финкцию, к-я будет прнимать 1 параметр - размер ёлки 
# и будет выводить ёлку данного размера

def draw_christmas_tree(size):
    if size < 3:
        print('Error')
    else:        
        for i in range(1, size + 1):
            print('*' * i)

draw_christmas_tree(20)

# 2 задача

# draw_rectangle(5, 3)

# def draw_rectangle(width, height):
#     for i in range(height):
#         print('*' * width)

# draw_rectangle(10, 2)  


def clear_text_from_uppercase(text):
    new_text = ''
    for letter in text:
        if letter. issuper(): pass
        else: new_text = new_text + letter
    return new_text

print(clear_text_from_uppercase('svfnjfnbjnv')) 

# show_devisors(24)