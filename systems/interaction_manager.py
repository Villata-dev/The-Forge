import math

class InteractionSystem:
    def get_closest_interactable(self, player_pos, entities):
        closest = None
        min_dist = float('inf')
        for ent in entities:
            if hasattr(ent, 'interaction_radius'):
                dist = math.hypot(ent.rect.centerx - player_pos[0], ent.rect.centery - player_pos[1])
                if dist <= ent.interaction_radius and dist < min_dist:
                    closest = ent
                    min_dist = dist
        return closest
