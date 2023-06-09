# oop worksheet

class: comp sci

### circle question worksheet

<aside>
⭐ Create a circle class
Attributes: radius, diameter
Methods: get_radius, get_diameter, get circumference, get area

</aside>

```python
from math import pi as PI

class Circle:
    def __init__(self):
        ''' This initializes our four attributes. '''
        self.__radius = self.set_radius()
        self.__diameter = self.__radius * 2
        self.__circumference = self.set_circumference()
        self.__area = self.set_area()

    def set_radius(self):
        ''' This sets a numeric radius to our object '''
        user_input = ''
        while not user_input or not(user_input.isdigit()):
            user_input = input('Enter the radius: ')
        return float(user_input)
    # end of set_radius()

    def set_circumference(self):
        return 2 * PI * self.__radius

    def set_area(self):
        return PI * (self.__radius ** 2)

    def get_radius(self):
        return self.__radius

    def get_diameter(self):
        return self.__diameter

    def get_circumference(self):
        return self.__circumference

    def get_area(self):
        return self.__area

    # Base Overrides
    def __str__(self):
        ''' This creates a string version of Circle '''
        return f'A circle object with a radius of {self.__radius}.'

    def __repr__(self):
        return self.__str__()
```

to access on main:

```python
from circle import Circle

test = Circle()
print('Area:', test.get_area())
```
