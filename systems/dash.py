class DashMechanic:
    def __init__(self):
        self.is_dashing = False
        self.i_frames = 0
    def trigger_dash(self):
        self.is_dashing = True
        self.i_frames = 15 # 15 frames de invulnerabilidad a 60FPS
