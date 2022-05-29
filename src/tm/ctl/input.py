import threading

from tm.contrib.pos import Direction


def setup_input(menu_manager):
    input_loop = InputLoopThread(menu_manager)
    input_loop.start()


class InputLoopThread(threading.Thread):

    def __init__(self, menu_manager):
        self.menu_manager = menu_manager
        super(InputLoopThread, self).__init__()

    def run(self) -> None:
        while True:
            text = input("> ")
            if text in ["up", "u", "w"]:
                self.menu_manager.update(Direction.UP)
            if text in ["down", "s", "d"]:
                self.menu_manager.update(Direction.DOWN)
            if text in ["select", "", " "]:
                self.menu_manager.update(Direction.SELECT)
