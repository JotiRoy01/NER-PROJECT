from pythonjsonlogger import jsonlogger


class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def process_log_record(self, log_record):
        # This keeps the nested "custom" dictionary intact
        if "custom" in log_record and isinstance(log_record["custom"], dict):
            log_record["message"] = log_record.get("message", "")
        return super().process_log_record(log_record)
