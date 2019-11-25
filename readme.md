The N-Body Problem

    what is it
        Newton tried to use analytical geometry to predict the planets' motions from its orbital properties (position, orbital diameter, period and orbital velocity) and failed
        realised that there is a gravitational interaction between the planets that is affecting their orbits
        In the solar system, every planet is gravitationally affected by all the other planets to some degree.
        This is also true for other bodies inside and outside the solar system
        it is easy to calculate the gravitationally interactive forces between two bodies using newtonian physics
        as soon as there are more than two bodies involved, things get harder to predict
        This technique is pretty close to reality -- the moon landings used newtonian mechanics to calculate their orbits -- but it has to be said that einstein showed that there are small micro-interactions between bodies that newtonian physics cannot predict
    
    why is it hard
        This is because every body's gravity influences all the other bodies orbital parameters, which in turn influence all OTHER bodies
        for n bodies, there are n^2 interactions to calculate
        you have to take all bodies into account, or your result will be very imprecise
        You can use this to find bodies you don't know about: Plug all bodies you know about into the equations, calculate, and if the result differs from reality, Boom, you know where to look for your new dark moon
    
    approximation using Barnes-Hut
        organise all bodies into an octo-tree (or quad-tree for 2d), ordered by their distance from each other
        each Body is a leaf on the end of the tree, and saves its mass, plus its orbital parameters
        save the combined mass of the attached bodies for each node
        for far away bodies, do not calculate every body's mass and gravitational interaction individually -- instead, with increasing distance, retreat further and further up the tree and use the mass information in the upper nodes
        it can be proven that due to the inverse square root relation of gravity to mass over distance, this only gives us very small errors as opposed to calculating every individual body
        However, the complexity sinks from O(n^2) to O(n log n)

Reference Code (java)

http://physics.princeton.edu/~fpretori/Nbody/code.htm

Sources

https://en.m.wikipedia.org/wiki/Barnes–Hut_simulation
https://en.m.wikipedia.org/wiki/N-body_simulation
https://en.wikipedia.org/wiki/Celestial_mechanics

J. Barnes & P. Hut (December 1986). "A hierarchical O(N log N) force-calculation algorithm". Nature. 324 (4): 446–449. Bibcode:1986Natur.324..446B. doi:10.1038/324446a0.


Troubleshooting:

https://stackoverflow.com/questions/13316397/matplotlib-animation-no-moviewriters-available
https://stackoverflow.com/questions/47736457/runtimeerror-no-moviewriters-available-in-matplotlib-animation?rq=1