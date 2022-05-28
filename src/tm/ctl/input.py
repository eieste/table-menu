from tm.menu.menumanager import Direction


def foo(menu_manager):
    while True:
        text = input("> ")
        if text in ["up", "u", "w"]:
            menu_manager.update(Direction.UP)
        if text in ["down", "s", "d"]:
            menu_manager.update(Direction.DOWN)
        if text in ["select", "", " "]:
            menu_manager.reset_switch()
