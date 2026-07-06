import pygame

class RenderCulling:
    @staticmethod
    def get_visible_entities(camera_rect: pygame.Rect, all_entities: list) -> list:
        # Solo devuelve las entidades que colisionan con la camara (Viewport)
        # Evita renderizar objetos que estan fuera de la pantalla para salvar FPS
        visible = []
        for entity in all_entities:
            # Asumiendo que la entidad tiene un atributo 'rect'
            if hasattr(entity, 'rect') and camera_rect.colliderect(entity.rect):
                visible.append(entity)
        return visible
