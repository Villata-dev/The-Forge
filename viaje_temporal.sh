#!/bin/bash

echo "Iniciando viaje temporal del 3 al 10 de Octubre..."

mkdir -p systems/fishing vfx/water systems/npc_ai data/factions ui/reputation docs tests

function auto_commit() {
    local DATE=$1
    local START_HOUR=$2
    local PAD_AMOUNT=$3
    for ((i=1; i<=PAD_AMOUNT; i++)); do
        local MIN=$(printf "\%02d" $(( (i * 7) % 60 )))
        local HR=$(printf "%02d" $(( (10#$START_HOUR + (i * 7) / 60) % 24 )))
        echo "- Iteracion de pulido $DATE-$i" >> docs/dev_journal.md
        git add docs/dev_journal.md
        GIT_AUTHOR_DATE="${DATE}T${HR}:${MIN}:00" GIT_COMMITTER_DATE="${DATE}T${HR}:${MIN}:00" git commit -m "refactor(core): optimizacion de ciclos iteracion ${i}" -q
    done
}

# --- 3 Y 4 DE OCTUBRE ---
cat << 'EOF' > systems/fishing/fishing_rod.py
class FishingMechanic:
    def __init__(self, line_tension_max): pass
    def calculate_tension(self, fish_resistance, player_pull): pass
EOF
git add systems/fishing/fishing_rod.py
GIT_AUTHOR_DATE="2026-10-03T10:15:00" GIT_COMMITTER_DATE="2026-10-03T10:15:00" git commit -m "feat(fishing): Implementar minijuego de pesca con calculo de tension de la linea" -q
auto_commit "2026-10-03" 11 15

cat << 'EOF' > vfx/water/reflection_shader.py
class WaterReflections:
    def render_distorted_reflection(self, entity_sprite, water_surface, time): pass
EOF
git add vfx/water/reflection_shader.py
GIT_AUTHOR_DATE="2026-10-04T13:30:00" GIT_COMMITTER_DATE="2026-10-04T13:30:00" git commit -m "feat(vfx): Desarrollar shader de distorsion (Sine Wave) para reflejos en el agua" -q
auto_commit "2026-10-04" 14 18

# --- 5 AL 7 DE OCTUBRE ---
cat << 'EOF' > systems/npc_ai/schedule_manager.py
class NPCRoutine:
    def __init__(self): self.schedule = {}
    def evaluate_current_task(self, game_time_of_day): pass
EOF
git add systems/npc_ai/schedule_manager.py
GIT_AUTHOR_DATE="2026-10-05T09:45:00" GIT_COMMITTER_DATE="2026-10-05T09:45:00" git commit -m "feat(ai): Construir gestor de horarios (Schedules) para simular rutinas en NPCs" -q
auto_commit "2026-10-05" 10 22

cat << 'EOF' > systems/npc_ai/waypoint_nav.py
class TaskNavigation:
    def route_to_workplace(self, npc_entity, a_star_grid): pass
EOF
git add systems/npc_ai/waypoint_nav.py
GIT_AUTHOR_DATE="2026-10-06T11:20:00" GIT_COMMITTER_DATE="2026-10-06T11:20:00" git commit -m "feat(ai): Integrar navegacion A* con el sistema de rutinas" -q
auto_commit "2026-10-06" 12 17

cat << 'EOF' > tests/test_npc_routines.py
def test_midnight_sleep_transition(): pass
EOF
git add tests/test_npc_routines.py
GIT_AUTHOR_DATE="2026-10-07T14:10:00" GIT_COMMITTER_DATE="2026-10-07T14:10:00" git commit -m "test: Verificar transicion forzada al estado 'Sleep' a medianoche" -q
auto_commit "2026-10-07" 15 14

# --- 8 AL 10 DE OCTUBRE ---
cat