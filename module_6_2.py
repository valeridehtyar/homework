class Vehicle:
    _COLOR_VARIANTS = ['red','yellow','orange','green','blue','purple','brown','gray','white','black']
    def get_color_variants(self):
        return self._COLOR_VARIANTS
    def __init__(self,owner,model1,color,engine_power):
        self.owner = owner
        self._model1 = model1
        self._engine_power = engine_power
        self._color = color
    def get_model(self):
        return f'Модель:{self._model1}'
    def get_horsepower(self):
        return f'Мощность двигателя:{self._engine_power}'
    def get_color(self):
        return f'Цвет кузова: {self._color}'
    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')
    def set_color(self,new_color):
        if new_color.lower() in [color.lower() for color in self._COLOR_VARIANTS]:
            self._color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5
    def __init__(self, owner, model, color, engine_power):
        super().__init__(owner, model,color,engine_power)
    def get_passengers_limit(self):
        return self.__PASSENGERS_LIMIT

vehicle1 = Sedan('Fedos','Toyota Mark II','blue',500)
vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

vehicle1.print_info()