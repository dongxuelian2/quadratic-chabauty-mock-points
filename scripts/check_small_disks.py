#!/usr/bin/env python3
"""Exhaustive finite-field check for <=8 disks at eligible p=3 mod4.
The Hasse reduction to this finite list is in the companion note.
"""

def points(a, p):
    return [(x,y) for x in range(p) for y in range(p)
            if (y*y-x**6-a*x**4-a*x*x-1) % p == 0]


def main():
    rows = []
    for p in (3,7,11,19,23):
        for a in range(p):
            if (a+1)*(a-3) % p == 0:
                continue
            pts = points(a,p)
            ec = 1+sum(1 for x in range(p) for y in range(p)
                       if (y*y-x**3-(a-3)*x*x+(a-3)*x) % p == 0)
            assert len(pts)+2 == 2*ec-p-1
            if len(pts)+2 <= 8:
                extra = [(x,y) for x,y in pts if x != 0]
                if not extra:
                    layout = 'four endpoints only'
                elif all(x in (1,p-1) for x,y in extra):
                    layout = 'endpoints plus four x=+-1 centers'
                elif all(y == 0 for x,y in extra):
                    layout = 'endpoints plus four quartic Weierstrass centers'
                else:
                    raise AssertionError((p,a,extra))
                rows.append((p,a,len(pts)+2,layout))
                print(p,a,len(pts)+2,layout,'extra=',extra)
    assert [(p,a,n) for p,a,n,_ in rows] == [
        (3,1,8),(7,2,8),(7,4,4),(11,1,8),(11,2,4),(11,7,8),
        (19,0,4),(23,20,8)]
    print('Complete <=8-disk classification: PASS')


if __name__ == '__main__':
    main()
