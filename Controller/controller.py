import UI.typeOfOutput as ui
import Controller.commands as com

def start():
    while True:
        ui.menu_console()
        user_input = input()
        if user_input == '1':
            com.show("all")
        elif user_input == '2':
            com.show("id")
        elif user_input == '3':
            com.show("date")
        elif user_input == '4':
            com.show("all")
            com.change_note()
        elif user_input == '5':
            com.add_note()
        elif user_input == '6':
            com.show("all")
            com.del_notes()
        else:
            print("Работа завершена")
            break