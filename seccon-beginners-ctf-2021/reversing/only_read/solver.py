from pathlib import Path

import angr


def solve():
    path = Path(__file__).parent / 'chall'
    p = angr.Project(f'{path}')
    state = p.factory.entry_state()
    sim = p.factory.simulation_manager(state)
    sim.explore(find=(0x400000 + 0x12b8,))

    for found in sim.found:
        return found.posix.dumps(0).decode()


if __name__ == '__main__':
    print(solve())
