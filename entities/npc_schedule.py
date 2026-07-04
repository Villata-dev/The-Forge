class NPCSchedule:
    def __init__(self):
        self.schedule = {
            "00:00": "SLEEP",
            "07:00": "EAT",
            "09:00": "WORK",
            "18:00": "RELAX",
            "22:00": "SLEEP"
        }

    def get_current_action(self, time_of_day: float) -> str:
        # time_of_day = horas en formato decimal (ej. 14.5 = 14:30)
        current_action = "IDLE"
        latest_hour = -1.0
        
        for time_str, action in self.schedule.items():
            h, m = map(int, time_str.split(':'))
            hour_decimal = h + (m / 60.0)
            
            if latest_hour <= hour_decimal <= time_of_day:
                latest_hour = hour_decimal
                current_action = action
                
        return current_action
