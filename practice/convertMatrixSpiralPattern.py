#!/usr/bin/env python

m1 = [ [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0] ]
m2 = [ [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0] ]
m3 = [ [0], [0] ]
m4 = [ [0, 0], [0, 0] ]

def print_matrix(m):
    for row in m:
        for e in row:
            print e,
        print ''
    print ''

def convert_spiral(m):
    # d = direction, 1=right, 2=down, 3=left, 4=up
    r = 0
    c = 0
    d = 1
    r_spiral_end = r + 1
    r_i_max = len(m[0]) - 1
    d_i_max = len(m) - 1
    l_i_min = 0
    while True:
        #print '%s, %s' % (r,c)
        if m[r][c] == 1:
            print 'finishing, r=%s, c=%s' % (r,c)
            break
        m[r][c] = 1
        if d == 1:
            if c == r_i_max:
                #print 'switch down\n'
                d = 2
                r += 1
                r_i_max -= 1
                continue
            else:
                #print 'moving right'
                c += 1
        if d == 2:
            if r == d_i_max:
                #print 'switch left\n'
                d = 3
                c -= 1
                d_i_max -= 1
                continue
            else:
                #print 'moving down'
                r += 1
        if d == 3:
            if c == l_i_min:
                #print 'switch up\n'
                d = 4
                r -= 1
                l_i_min += 1
                continue
            else:
                #print 'moving left'
                c -= 1
        if d == 4:
            if r == r_spiral_end:
                d = 1
                c += 1
                r_spiral_end = r + 1
                print 'reset direction to right, r=%s, c=%s, r_spiral_end=%s\n' % (r,c,r_spiral_end)
                continue
            else:
                #print 'moving up'
                r -= 1

for m in [m1, m2, m3, m4]:
    print '-----------------------------------------------------------'
    print_matrix(m)
    convert_spiral(m)
    print_matrix(m)

