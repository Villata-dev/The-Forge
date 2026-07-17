import math
class AreaOfEffect:
    def calculate_targets(self, epicenter, radius, entities):
        targets = []
        for ent in entities:
            dist = math.hypot(ent.x - epicenter[0], ent.y - epicenter[1])
            if dist <= radius: targets.append(ent)
        return targets
