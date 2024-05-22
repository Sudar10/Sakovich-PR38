from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import random

# Словарь с вопросами
questions = {
    "Какой цвет тебе больше нравится?": ["Красный", "Оранжевый", "Желтый", "Зеленый", "Голубой", "Синий", "Фиолетовый"],
    "Какой цвет привлекает тебя больше всего?": ["Красный", "Оранжевый", "Желтый", "Зеленый", "Голубой", "Синий", "Фиолетовый"],
    "Какой цвет ты ассоциируешь с счастьем?": ["Красный", "Оранжевый", "Желтый", "Зеленый", "Голубой", "Синий", "Фиолетовый"],
    "Какой цвет ты чаще всего выбираешь для одежды?": ["Красный", "Оранжевый", "Желтый", "Зеленый", "Голубой", "Синий", "Фиолетовый"],
    "Какой цвет ты видишь в своих мечтах?": ["Красный", "Оранжевый", "Желтый", "Зеленый", "Голубой", "Синий", "Фиолетовый"],
    "Какой цвет ты предпочитаешь в интерьере?": ["Красный", "Оранжевый", "Желтый", "Зеленый", "Голубой", "Синий", "Фиолетовый"],
    "Какой цвет ты ассоциируешь с покоем и спокойствием?": ["Красный", "Оранжевый", "Желтый", "Зеленый", "Голубой", "Синий", "Фиолетовый"],
    "Какой цвет ты ассоциируешь с энергией и активностью?": ["Красный", "Оранжевый", "Желтый", "Зеленый", "Голубой", "Синий", "Фиолетовый"],
    "Какой цвет ты выберешь для своей машины?": ["Красный", "Оранжевый", "Желтый", "Зеленый", "Голубой", "Синий", "Фиолетовый"],
    "Какой цвет ты бы выбрал для путешествия во времени?": ["Красный", "Оранжевый", "Желтый", "Зеленый", "Голубой", "Синий", "Фиолетовый"],
}

class ColorTestApp(App):
    def build(self):
        self.question_label = Label(text="Начнем тест!")
        self.answer_label = Label(text="")
        self.next_button = Button(text="Следующий вопрос", on_press=self.next_question)
        self.layout = BoxLayout(orientation='vertical')
        self.layout.add_widget(self.question_label)
        self.layout.add_widget(self.answer_label)
        self.layout.add_widget(self.next_button)
        return self.layout

    def next_question(self, instance):
        question = random.choice(list(questions.keys()))
        answers = questions[question]
        self.question_label.text = question
        self.answer_label.text = "\n".join(answers)

if __name__ == '__main__':
    ColorTestApp().run()
