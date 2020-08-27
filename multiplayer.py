import radio

from core import XY, Ball, Paddle


class HostXY(XY):
    def __init__(self, *args):
        super().__init__(*args)

    def sync(self):
        pass


class HostBall(Ball, HostXY):
    def __init__(self, *args):
        super().__init__(*args)


class HostPaddle(Paddle, HostXY):
    def __init__(self, *args):
        super().__init__(*args)


class ClientXY(XY):
    def __init__(self, *args):
        super().__init__(*args)

    def sync(self):
        pass


class ClientPaddle(Paddle, ClientXY):
    def __init__(self, *args):
        super().__init__(*args)
