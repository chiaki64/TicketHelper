#!/usr/bin/env python
# -*- coding: gbk -*
# @auther:Hieda no Chiaki <forblackking@gmail.com>

class Menu:
    def __init__(self):
        pass

    def menu_index(self):
        print("====Menu====")
        print("1.实时查询")
        print("2.刷票")
        print("============")

    def menu_first_index(self):
        pass

    def menu_second_index(self):
        pass

    def choose(self):
        while True:
            try:
                self.choose = input()
                self.choose = int(self.choose)
                break;
            except ValueError as e:
                print("Plesse Input Right Choose! Try Again.")
        return self.choose


if __name__ == '__main__':
    Menu = Menu()
    Menu.menu_index()
    Menu.choose()
