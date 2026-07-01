# Documento de Diseno Tecnico: The Forge

## Resumen del Motor
Motor 2D construido sobre Pygame y PyTMX. Implementa hibridacion de patron de estados (State Machine) con Entidades acopladas.

## Sistemas Principales
- **Inventario:** Limitacion por peso dinamico (Encumbrance). Items divididos en Weapons, Apparel, Ingredients.
- **Herreria:** Arbol jerarquico de materiales. 
- **Eventos:** Bus de transmision de mensajes para conectar colisiones del entorno con el audio sin acoplamiento estricto.
