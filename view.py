import datetime
import controller as c

def start():
    print('Введите /all для просмотра всех заметок,\n /add для добавления заметки, /edit для изменения заметки, /delete для удаления заметки и /exit для выхода')
    c.load()
    while True:     
        response = input('Введите команду ')
        if(response=='/all'):
            c.showAll()
        elif(response=='/add'):
            print("Введите новую заметку")
            note = input('Заметка: ')
            id = int(input('Введите id заметки '))
            date = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))        
            c.addNote(id, note, date)                     
        elif(response=="/edit"):
            id = int(input('Введите id записи '))
            noteEdit = input("Введите измененную заметку: ")
            c.edit(id, noteEdit)

        elif(response=="/delete"):
            id = int(input('Введите id записи '))
            c.deleteNote(id)
        elif(response=="/exit"):
                print('Выходим, будем рады видеть вас снова!')
                exit()
        else:
            print('Введена неверная комманда, попробуйте еще раз!')