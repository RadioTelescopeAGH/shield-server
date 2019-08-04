from controllers.movement_controller import MovementController
from controllers.sensors_controller import SensorsController
from controllers.system_controller import SystemController

movement = MovementController()
sensors = SensorsController()
system = SystemController()


class Actions:

    controllers_actions = {
        'movement': {
            'move_to_cords': lambda data: movement.move_to_cords(data),
            'move_engine_x': lambda data: movement.move_engine_x(data),
            'move_engine_y': lambda data: movement.move_engine_y(data),
            'move_top': lambda data: movement.move_top(data),
            'move_bottom': lambda data: movement.move_bottom(data),
            'move_left': lambda data: movement.move_left(data),
            'move_right': lambda data: movement.move_right(data),
        },
        'sensors': {
            'sensor_data': lambda data: sensors.sensor_data(data),
            'motor_state': lambda data: sensors.motor_state(data),
            'all_sensors': lambda data: sensors.all_sensors(data),
        },
        'system': {
            'restart': lambda data: system.restart(data),
            'shutdown': lambda data: system.shutdown(data),
            'stop_collect': lambda data: system.stop_collect(data),
            'start_collect': lambda data: system.start_collect(data),
        },
    }

    def exec(self, controller, action, data):
        if controller not in self.controllers_actions.keys():
            return False, 404, None
        if action not in self.controllers_actions[controller].keys():
            return False, 404, None

        return self.controllers_actions[controller][action](data)
