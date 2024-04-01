# TO DO add text lookup system

# Algorithm "xor" from p. 4 of Marsaglia, "Xorshift RNGs"
# source: https://en.wikipedia.org/w/index.php?title=Xorshift&oldid=1214507567 (accessed: 30/03/24)
def xorshift32(state):
    """
    Calculates the next state of the RNG state.
    Used when ProgressiveExcessItems is set to random.
    This algorithm matches the one implemented in the rom exactly (chosen for ease of implementation in rom).
    This keeps the random items generated consistent between client and rom.

    :param state: Current 32-bit RNG state
    :return: Next 32-bit RNG state
    """
    state = (state ^ (state << 13)) & 0xFFFFFFFF
    state = (state ^ (state >> 17)) & 0xFFFFFFFF
    state = (state ^ (state << 5)) & 0xFFFFFFFF
    return state
