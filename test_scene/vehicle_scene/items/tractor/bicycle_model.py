#!/usr/bin/python3
# -*- coding: utf-8 -*-
from math import sin, cos, tan, pi


class Bicycle():
    def __init__(self,
                 frame_rate,
                 angle_the,
                 angle_fi,
                 angel_fi_limit,
                 velocity,
                 pos_x,
                 pos_y,
                 R_curve,
                 H_base):

        self.rate = frame_rate
        self.the = angle_the
        self.fi = angle_fi
        self.fi_limit = angel_fi_limit
        self.vel = velocity
        self.x = pos_x
        self.y = pos_y
        self.R = R_curve
        self.H = H_base

    def update(self):
        try:
            self.R = self.H / tan(self.fi * pi / 180)
        except ZeroDivisionError:
            self.R = None

        if self.R:
            self.the += (self.vel / self.rate / self.R) * 180 / pi

        self.x += self.vel / self.rate * cos(self.the * pi / 180)
        self.y += self.vel / self.rate * sin(self.the * pi / 180)

    def increase_speed(self):
        self.vel += 1

    def reduce_speed(self):
        self.vel -= 1

    def increase_angle(self):
        self.fi += 1

    def reduce_angle(self):
        self.fi -= 1

    def get(self):
        return {'pos_x': self.x,
                'pos_y': self.y,
                'the': self.the,
                'R': self.R}


def main():
    print('main execute')


if __name__ == '__main__':
    main()
