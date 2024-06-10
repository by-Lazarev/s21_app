def fix_wiring(cables, sockets, plugs):
    return (f"plug {cable} into {socket} using {plug}" if plug else f"weld {cable} to {socket} without plug"
            for cable, socket, plug in zip((c for c in cables if isinstance(c, str)),
                                           (s for s in sockets if isinstance(s, str)),
                                           list(plug for plug in plugs if isinstance(plug, str)) + [None] * max(len(cables), len(sockets))))

