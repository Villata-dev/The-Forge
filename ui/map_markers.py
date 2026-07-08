class MapMarkers:
    def __init__(self):
        self.markers = {} # id: (x, y, icon_type)

    def add_custom_marker(self, marker_id: str, pos: tuple, m_type: str):
        self.markers[marker_id] = (pos[0], pos[1], m_type)

    def remove_marker(self, marker_id: str):
        if marker_id in self.markers:
            del self.markers[marker_id]
