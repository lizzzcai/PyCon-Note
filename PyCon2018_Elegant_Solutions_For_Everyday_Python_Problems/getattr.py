

class Dog:
    sound = 'Bark'
    def speak(self):
        print(self.sound + '!', self.sound + '!')


if __name__ == "__main__":
    my_dog = Dog()
    my_dog.speak()

    print(getattr(my_dog, 'speak'))

    speak_method = getattr(my_dog, 'speak')
    speak_method()