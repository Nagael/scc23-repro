from copy import deepcopy

# Base of both SBC patterns
# Returns a pattern where all tiles except the diagonals are correct
# a pattern is a (r x r) array
def sbc_base(r):
    result = [ [None for _ in range(r)] for _ in range(r) ]
    count = 0
    for i in range(r):
        for j in range(i):
            result[i][j] = count
            result[j][i] = count
            count += 1
    return result

# requires even r
# result: uses P=r/2 processors
#         (r x r) array, containing the processor number (from 0 to P-1) which owns this tile
def sbc_basic(r):
    if r%2 != 0:
        raise ValueError("Basic SBC requires an even value of r, not %d" % r)
    result = sbc_base(r)
    count = r*(r-1)//2
    for i in range(r//2):
        result[i][i] = count
        result[i+r//2][i+r//2] = count
        count += 1
    return result

# result: uses P=r(r-1)/2 processors
#         list of patterns, each pattern is a (r x r) array, containing the processor number (from 0 to P-1) which owns this tile
#         number of patterns: (r-1)/2 if r is odd, r-1 if r is even.
def sbc_extended(r):
    base = sbc_base(r)
    diags = []

    # Base case, valid both for even and odd r
    for l in range(1, 1 + (r-1)//2):
        diag = [None] * r
        for k in range(r-l):
            diag[k] = base[k][l + k]
        for k in range(l):
            diag[r+k-l] = base[k][r + k - l]
        diags.append(diag)

    # Special case for even r
    if r % 2 == 0:
        l = r//2
        bonus_pack = [None] * l
        for k in range(l):
            bonus_pack[k] = base[k][l + k]

        left_packs =  [bonus_pack] + [ diag[:l] for diag in diags ]
        right_packs = [ diag[l:] for diag in diags ] + [bonus_pack]

        diags.extend( a + b for (a, b) in zip(left_packs, right_packs) )

    # Making the patterns
    def make_pattern(diag):
        result = deepcopy(base)
        for k in range(r):
            result[k][k] = diag[k]
        return result
    
    return [ make_pattern(d) for d in diags ]

# Print functions
def print_pattern(p, **args):
    print(len(p), len(p[0]), **args)
    for x in p:
        print(*x, **args)

def print_patterns(l, **args):
    for p in l:
        print_pattern(p, **args)
        print()

# Replicate over the whole matrix
# r = size of the patterns
# n = matrix size
# output: (n x n) array
def replicate(patterns, r, n):
    result = [ [None] * n for _ in range(n) ]

    def apply_pattern(pattern, start_x, start_y):
        for u in range(r):
            for v in range(r):
                result[start_x+u][start_y+v] = pattern[u][v]
    
    if n % r != 0:
        raise ValueError("Replication: n should be a multiple of r, here n=%d and r=%d" % (n, r))
    repetitions = n // r
    idx = 0
    for i in range(0, n, r):
        for j in range(i, n, r):
            apply_pattern(patterns[idx], i, j)
            if i != j:
                apply_pattern(patterns[idx], j, i)
            idx = (idx + 1) % len(patterns)
    return result

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser("SBC pattern")

    parser.add_argument("-r", type=int, default=3, help="Value of r. Number of processors is r/2 for basic SBC, r(r-1)/2 for extended version.")
    parser.add_argument("-n", type=int, default=None, help="Matrix size (in number of tiles). Must be a multiple of r. Defaults to r")
    parser.add_argument("-o", type=argparse.FileType("w"), default = None, help="File for output")
    parser.add_argument("--extended", action="store_true", help = "Use extended version of SBC")

    args = parser.parse_args()

    patterns = sbc_extended(args.r) if args.extended else [sbc_basic(args.r)]
    n = args.n or args.r
    matrix = replicate(patterns, args.r, n)

    if args.o is not None:
        print_pattern(matrix, file=args.o)
    else:
        print_pattern(matrix)
