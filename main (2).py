from kivymd.app import MDApp
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
import matplotlib.pyplot as plt


class ProjectApp(MDApp):

    def graph(self, instance):
        x = self.text3.text
        y = []
        y1 = self.texxt1.text
        y2 = self.texxt2.text
        y3 = self.texxt3.text
        x = int(x)
        list_x = list(range(x))
        y1 = float(y1)
        y2 = float(y2)
        y3 = float(y3)
        y.append(y1)
        y.append(y2)
        y.append(y3)
        Y = []
        Y1 = (y1+y2+y3)/x
        Y.append(Y1)
        Y.append(Y1)
        Y.append(Y1)
        plt.title('Правильное питание')
        plt.xlabel('Приемы пищи:')
        plt.ylabel('Количество Ккал:')
        plt.plot(list_x, y, label="Сейчас", marker='o', color='green')
        plt.plot(list_x, Y, label='надо', marker='>')
        self.fl.add_widget(plt.show())

    def boo2(self, instance):
        x = self.text3.text
        x = int(x)
        self.fl.clear_widgets(children=None)
        self.grid = GridLayout(cols=2, rows=2)
        self.texxt1 = TextInput(multiline=False, font_size=28, size_hint=(.25, .15), background_color=(0, 1, 1, 1), text='1')
        self.texxt2 = TextInput(multiline=False, font_size=28, size_hint=(.25, .15), background_color=(0, 1, 1, 1), text='2')
        self.texxt3 = TextInput(multiline=False, font_size=28, size_hint=(.25, .15), background_color=(0, 1, 1, 1), text='3')
        self.grid.add_widget(self.texxt1)
        self.grid.add_widget(self.texxt2)
        self.grid.add_widget(self.texxt3)
        self.grid.add_widget(Button(text='Начертить график', font_size=28, size_hint=(.25, .15), background_color=(0, 1, 1, 1),
                                    on_press=self.graph))
        self.fl.add_widget(self.grid)

    def boo1(self, instance):
        m = self.text1.text
        h = self.text2.text
        if m != '' and h != '':
            m = float(m)
            h = float(h)
            self.fl.clear_widgets(children=None)
            a = str(round(m/((h/100)**2), 1))
            self.fl.add_widget(Label(text=('Ваш индекс массы тела =' + a),
                                     font_size=28, size_hint=(.25, .15),
                                     pos=(300, 500), color='black'))
            self.fl.add_widget(Label(text='ИМТ<16 - значительный дефицит массы тела\n'
                                          '16-18.5 - дефицит массы тела\n'
                                          '18.5-25 - норма\n'
                                          '25-30 - лишний вес\n'
                                          '30-35 - ожирение 1 степени\n'
                                          '35-40 - ожирение 2 степени\n'
                                          'ИМТ>40 - ожирение 3 степени', font_size=28,
                                     size_hint=(.25, .15), pos=(300, 250), color='black'))
            self.fl.add_widget(Button(text='Назад', font_size=28,
                                      background_color=(0, 1, 1, 1),
                                      size_hint=(.25, .15), pos=(0, 0),
                                      on_press=self.cvc))

    def click(self, instance):
        self.fl.clear_widgets(children=None)
        self.fl.add_widget(Label(text='Работу выполнил Хузун Иван', font_size=28,
                                 size_hint=(.5, .25), pos=(300, 300), color='black'))
        self.fl.add_widget(Button(text='Назад', font_size=28,
                                  background_color=(0, 1, 1, 1),
                                  size_hint=(.25, .15), pos=(0, 0)))

    def comeback(self, instance):
        self.fl.clear_widgets(children=None)
        self.fl.add_widget(Button(text='ИМТ', size_hint=(.5, .25),
                                  pos=(0, 300), on_press=self.cvc,
                                  background_color=(0, 1, 1, 1)))
        self.fl.add_widget(Button(text='Питание', size_hint=(.5, .25),
                                  pos=(300, 300),on_press=self.food,
                                  background_color=(0, 1, 1, 1)))
        self.fl.add_widget(Button(text='Назад', size_hint=(.25, .15),
                                  background_color=(0, 1, 1, 1)
                                  ))

#   ЕДА
    def food(self, instance):
        self.fl.clear_widgets(children=None)
        grid = GridLayout(cols=2, rows=2)
        self.text3 = TextInput(multiline=False, font_size=28, size_hint=(.25, .15),
                               background_color=(0, 1, 1, 1))
        self.text4 = TextInput(font_size=28, size_hint=(.25, .15), background_color=(0, 1, 1, 1))
        grid.add_widget(Label(text='Введите количество приёмов\n'
                                   'пищи в день:\n'
                                   'в формате(число раз)',
                              font_size=28, size_hint=(.5, .25), color='black'))
        grid.add_widget(self.text3)
        self.fl.add_widget(grid)
        self.fl.add_widget(Button(text='Далее', font_size=28,
                                  background_color=(0, 1, 1, 1),
                                  size_hint=(0.25, 0.15), pos=(50, 500),
                                  on_press=self.boo2))

#   ИМТ
    def cvc(self, instance):
        grid = GridLayout(cols=2, rows=2)
        la1 = Label(text='Введите ваш вес(кг):', color='black')
        la2 = Label(text='Введите ваш рост(см):', color='black')
        self.text1 = TextInput(text='', multiline=False, font_size=36,
                               size_hint=(.5, .15), pos=(0, 300))
        self.text2 = TextInput(text='', multiline=False, font_size=36,
                               size_hint=(.5, .15), pos=(300, 300))

        self.fl.clear_widgets(children=None)
        grid.add_widget(la1)
        grid.add_widget(self.text1)
        grid.add_widget(la2)
        grid.add_widget(self.text2)
        self.fl.add_widget(grid)
        self.fl.add_widget(Button(text='Назад', font_size=28,
                                  background_color=(0, 1, 1, 1),
                                  size_hint=(0.25, 0.15), pos=(0, 0),
                                  on_press=self.comeback))
        self.fl.add_widget(Button(text='Найти индекс\n'
                                       'массы тела', font_size=28,
                                  background_color=(0, 1, 1, 1),
                                  size_hint=(0.25, 0.15), pos=(50, 500),
                                  on_press=self.boo1))

#   начальный экран
    def build(self):

        self.fl = FloatLayout()

        self.Butt1 = Button(text='Начать работу', font_size=28,
                            background_color=(0, 1, 1, 1),
                            on_press=self.comeback,
                            size_hint=(.25, .25),
                            pos=(0, 0))

        self.Butt2 = Button(text='Авторы:', font_size=28,
                            background_color=(0, 1, 1, 1),
                            on_press=self.click,
                            size_hint=(.25, .25),
                            pos=(600, 0))

        self.fl.add_widget(self.Butt1)
        self.fl.add_widget(self.Butt2)

        return self.fl


if __name__ == '__main__':
    ProjectApp().run()
