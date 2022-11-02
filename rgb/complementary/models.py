from django.db import models
from django.core.validators import MaxValueValidator


def _hexadecimal(default: int = None):
    default = default if default else 0
    validators = [MaxValueValidator(255)]

    return models.PositiveSmallIntegerField(default=default, validators=validators)


class RGB(models.Model):
    r = _hexadecimal()
    g = _hexadecimal()
    b = _hexadecimal()

    def __repr__(self):
        rgb_str = f"{self.r}, {self.g}, {self.b}"

        return rgb_str

    def __str__(self):
        return "rgb(" + self.__repr__() + ")"


class RGBA(RGB):
    a = _hexadecimal(default=255)

    def __repr__(self):
        rgba_str = super().__repr__() + f", {self.a}"

        return rgba_str

    def __str__(self):
        rgba_str = "rgba(" + self.__repr__() + ")"

        return rgba_str
