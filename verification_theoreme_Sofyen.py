import itertools

DEG, G = 7, 3

def polymul(A, B, p):
    if not A or not B: return []
    C = [0]*(len(A)+len(B)-1)
    for i, a in enumerate(A):
        if a:
            for j, b in enumerate(B):
                if b: C[i+j] = (C[i+j] + a*b) % p
    return C

def polyadd(A, B, p):
    n = max(len(A), len(B)); C = [0]*n
    for i in range(n):
        C[i] = ((A[i] if i < len(A) else 0) + (B[i] if i < len(B) else 0)) % p
    return C

def xmul(A, B, p):
    C = {}
    for ea, pa in A.items():
        for eb, pb in B.items():
            e = ea + eb
            C[e] = polyadd(C.get(e, []), polymul(pa, pb, p), p)
    return {e: v for e, v in C.items() if any(v)}

def fpow(e, p):
    base = {7: [1], 1: [0, 1], 0: [1]}
    result, b = {0: [1]}, base
    while e > 0:
        if e & 1: result = xmul(result, b, p)
        e >>= 1
        if e: b = xmul(b, b, p)
    return result

def cartier_manin_poly(p):
    P = fpow((p - 1) // 2, p)
    get = lambda n: P.get(n, [0])
    D = []
    for perm in itertools.permutations(range(G)):
        inv = sum(1 for i in range(G) for j in range(i+1, G) if perm[i] > perm[j])
        term = [((-1)**inv) % p]
        for i in range(G):
            term = polymul(term, get((i+1)*p - (perm[i]+1)), p)
        D = polyadd(D, term, p)
    return [c % p for c in D]

def minimal_term(D, p):
    D = [c % p for c in D]
    if not any(D): return None
    md = min(i for i, c in enumerate(D) if c)
    return (md, D[md] % p)

def primes_upto(n):
    s = [True]*n; s[0:2] = [False, False]
    for i in range(2, int(n**0.5)+1):
        if s[i]:
            for j in range(i*i, n, i): s[j] = False
    return [i for i, v in enumerate(s) if v]

if __name__ == "__main__":
    cert = {p: minimal_term(cartier_manin_poly(p), p)
            for p in primes_upto(160) if p >= 3}
    nuls = [p for p, v in cert.items() if v is None]
    for p, v in cert.items():
        print(f"p = {p} : determinant identiquement nul" if v is None
              else f"p = {p} : degre minimal = {v[0]} ; coefficient = {v[1]}")
    print("Liste obtenue :", nuls)
    assert nuls == [3, 7, 11, 23]
    print(">>> CERTIFICAT FINI OK")
