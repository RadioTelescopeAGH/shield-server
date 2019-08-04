from utils.response_format import ResponseFormat


class MovementController:
    def move_to_cords(self, data):
        return ResponseFormat.format(True, 200, {"test": 1})

    def move_engine_x(self, data):
        return ResponseFormat.format(True, 200, {"test": 1})

    def move_engine_y(self, data):
        return ResponseFormat.format(True, 200, {"test": 1})

    def move_top(self, data):
        return ResponseFormat.format(True, 200, {"test": 1})

    def move_bottom(self, data):
        return ResponseFormat.format(True, 200, {"test": 1})

    def move_left(self, data):
        return ResponseFormat.format(True, 200, {"test": 1})

    def move_right(self, data):
        return ResponseFormat.format(True, 200, {"test": 1})
