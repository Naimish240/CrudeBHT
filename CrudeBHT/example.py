from .simulation import *

if __name__ == '__main__':
    print('*' * 50)
    
    system = None
    if simulation_type == 'BarnesHut':
        system = RenderableBarnesHutSystem()
    elif simulation_type == 'BruteForce':
        system = RenderableBruteForceSystem()

    system.start_the_bodies(int(bodies))
    renderer = SystemRenderer(system, frames=int(frames), trail_size=int(trail_size), performance_test=performance_test)

    renderer.run()

