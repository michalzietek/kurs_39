# class LedLamp:
#     def __init__(self):
#         self.turned_on = False
#         self.color = "White"
#
#     def turn_on(self):
#         self.turned_on = True
#
#     def turn_off(self):
#         self.turned_on = False
#
#     def change_color(self, new_color):
#         self.color = new_color
#
# class KsenonLamp:
#     def __init__(self):
#         self.turned_on = False
#
#     def turn_on(self):
#         self.turned_on = True
#
#     def turn_off(self):
#         self.turned_on = False
#
# class LedLampSwitch:
#     def __init__(self):
#         self.led_lamp = LedLamp()
#
#     def turn_on(self):
#         self.led_lamp.turn_on()
#
#     def turn_off(self):
#         self.led_lamp.turn_off()
#
# class KsenonLampSwitch:
#     def __init__(self):
#         self.led_lamp = LedLamp()
#
#     def turn_on(self):
#         self.led_lamp.turn_on()
#
#     def turn_off(self):
#         self.led_lamp.turn_off()

from abc import ABC

class LightSource(ABC):
    def __init__(self):
        self.turned_on = False

    def turn_on(self):
        self.turned_on = True

    def turn_off(self):
        self.turned_on = False

class LedLamp(LightSource):
    def __init__(self):
        super.__init__()
        self.color = "white"

    def change_color(self, new_color):
        self.color = new_color

class KsenonLamp(LightSource):
    pass


class Switch:
    def __init__(self, light_source: LightSource):
        self.light_source = light_source

    def turn_on(self):
        self.light_source.turn_on()

    def turn_off(self):
        self.light_source.turn_off()


led_lamp = LedLamp()
ksenon_lamp = KsenonLamp()

switch_1 = Switch(led_lamp)
switch_2 = Switch(ksenon_lamp)

