from utils.response_format import ResponseFormat


class SensorsController:
    def sensor_data(self, data):
        return ResponseFormat.format(True, 200, {"test": 1})

    def motor_state(self, data):
        return ResponseFormat.format(True, 200, {"test": 1})

    def all_sensors(self, data):
        return ResponseFormat.format(True, 200, {"test": 1})
