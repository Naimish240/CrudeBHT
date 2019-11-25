import argparse
from .rendering import *
from os import path, mkdir

if not path.exists("./renders"):
    mkdir("./renders")

def main():
    """
        In Circle form, n bodies are initialized in random positions around the centre mass
        In grid form, n^2 bodies are generated along lattice points

    """
    parser = argparse.ArgumentParser(description='Simulate N-Body Problem')
    parser.add_argument("simulation_type", help="BruteForce or BarnesHut")
    parser.add_argument("bodies", help="The number of bodies to simulate")
    parser.add_argument("frames", help="The number of frames to simulate for")
    parser.add_argument("trail_size", help="Display a trail of diameter x while rendering")
    parser.add_argument("--performance_test", help="don't render anything, just calculate", action="store_true")
    parser.add_argument("initialize", help = "Initializes in 'circle' or 'grid' form")
    args = parser.parse_args()

    system = None
    if args.simulation_type == 'BarnesHut':
        system = RenderableBarnesHutSystem()
    elif args.simulation_type == 'BruteForce':
        system = RenderableBruteForceSystem()
    else:
        exit(1)

    if args.initialize.lower() == 'circle':
        system.start_the_bodies_circle(int(args.bodies))
    elif args.initialize.lower() == 'grid':
        system.start_the_bodies_grid(int(args.bodies))

    renderer = SystemRenderer(system, frames=int(args.frames), trail_size=int(args.trail_size), performance_test=args.performance_test)

    renderer.run()
    