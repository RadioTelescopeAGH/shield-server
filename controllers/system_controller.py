from utils.response_format import ResponseFormat


class SystemController:
    def restart(self, data):
        return ResponseFormat.format(True, 200, {"test": 1})

    def shutdown(self, data):
        return ResponseFormat.format(True, 200, {"test": 1})

    def stop_collect(self, data):
        return ResponseFormat.format(True, 200, {"test": 1})

    def start_collect(self, data):
        return ResponseFormat.format(True, 200, {"test": 1})
