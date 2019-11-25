from builtins import int
from typing import Tuple, List
from tqdm import tqdm

import math

import matplotlib.pyplot as plt
import matplotlib.animation as animation
Writer = animation.FFMpegWriter(fps=30, codec='libx264')  # To get the animation working

import time
import datetime

from .body import Body
from .system import BruteForceSystem, BarnesHutSystem

CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'


class RenderableSystem:
    def name(self) -> str:
        raise NotImplementedError

    def get_solar_mass(self) -> float:
        raise NotImplementedError

    def get_x_limits(self) -> Tuple[int, int]:
        raise NotImplementedError

    def get_y_limits(self) -> Tuple[int, int]:
        raise NotImplementedError

    def get_bodies(self) -> List[Body]:
        raise NotImplementedError

    def step(self, elapsed_time):
        raise NotImplementedError


class SystemRenderer:
    min_marker_size = 0.1
    max_marker_size = 10
    progress_bar = None

    _background = None
    _body_dots = []
    _body_trailing_lines = []

    __last_step_time = None

    @property
    def time_warp_factor(self):
        return self.system.time_warp_factor

    @property
    def _last_step_time(self):
        if self.__last_step_time is None:
            self.__last_step_time = time.process_time()
        return self.__last_step_time

    def __init__(self, universe: RenderableSystem, frames: int, trail_size: int = 0,
                 performance_test: bool=False):
        self.system = universe
        self.trail_size = trail_size
        self.frames = frames
        self.performance_test = performance_test

        if self.performance_test:
            return

        self._fig, self._ax = plt.subplots(1, 1, figsize=(16, 12))
        self._ax.set_aspect('equal')
        self._ax.set_xlim(*self.system.get_x_limits())
        self._ax.set_ylim(*self.system.get_y_limits())

        # Comment to show axies
        plt.axis('off')

        # Setup Dots and Lines
        for body in self.system.get_bodies():
            marker_size = (math.floor(body.mass / self.system.get_solar_mass() / 2) + 1) 
            marker_size = min(marker_size, self.max_marker_size)
            marker_size = max(marker_size, self.min_marker_size)
            dot = plt.plot(body.rx, body.ry, 'o', markersize=marker_size)

            if body == self.system.get_bodies()[0]:
                # Special Case for the sun
                dot[0].set_color(self.system.parent_body_color())

            self._body_dots.append(dot)

            trailing_lines = []
            for _ in range(self.trail_size):
                trailing_line = plt.plot([0, 0], [0, 0], dot[0].get_color())
                trailing_lines.append(trailing_line)
            self._body_trailing_lines.append(trailing_lines)

    def run(self):
        self.progress_bar = tqdm(total=self.frames, unit=' frames')
        if self.performance_test:
            for frame in range(self.frames):
                self.progress_bar.update()
                self.system.step(self.time_warp_factor)
            self.progress_bar.update()
        else:
            file_name = f'renders/render-{time.time}-{self.system.name()}-{len(self.system.get_bodies())}b-{self.frames}f.mp4'
            anim = animation.FuncAnimation(self._fig, self.step, self.frames, interval=30, blit=True)
            anim.save(file_name)
        self.progress_bar.close()

    def step(self, frame):
        self.progress_bar.update()
        self.system.step(self.time_warp_factor)

        # Update The Dots
        dots_to_update = []
        for i in range(len(self.system.get_bodies())):
            dot = self._body_dots[i][0]
            body = self.system.get_bodies()[i]
            dots_to_update.append(dot)

            old_xdata = dot.get_xdata()
            old_ydata = dot.get_ydata()
            xdata = [body.rx]
            ydata = [body.ry]

            # Update the Dot
            dot.set_xdata(xdata)
            dot.set_ydata(ydata)

            # Update the trailing line
            if self.trail_size < 1:
                continue
            trailing_line = self._body_trailing_lines[i].pop()
            trailing_line[0].set_xdata([old_xdata, xdata])
            trailing_line[0].set_ydata([old_ydata, ydata])
            self._body_trailing_lines[i].insert(0, trailing_line)
        return dots_to_update


class RenderableBruteForceSystem(BruteForceSystem, RenderableSystem):
    def name(self):
        return 'BruteForce'

    def get_solar_mass(self):
        return self.solar_mass

    def get_x_limits(self):
        return -self.radius/6, self.radius/6

    def get_y_limits(self):
        return -self.radius/8, self.radius/8

    def get_bodies(self):
        return self.bodies

    def step(self, elapsed_time):
        self.calculate(elapsed_time)

class RenderableBarnesHutSystem(BarnesHutSystem, RenderableSystem):
    def name(self):
        return 'BarnesHut'

    def get_solar_mass(self):
        return self.solar_mass

    def get_x_limits(self):
        return -self.radius/6, self.radius/6

    def get_y_limits(self):
        return -self.radius/8, self.radius/8

    def get_bodies(self):
        return self.bodies

    def step(self, elapsed_time):
        self.calculate(elapsed_time)