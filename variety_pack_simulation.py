__author__ = 'ritaotao'

# enter the number of inventory and transfer string to int
r = {}
w = {}
#r['r1'],r['r2'],r['r3'] = [int(x) for x in input("Enter number of red wines here (divide by space): ").split()]
#w['w1'],w['w2'],r['w3'] = [int(x) for x in input("Enter number of white wines here (divide by space): ").split()]
r['r1'],r['r2'],r['r3'] = 672, 1344, 1344
w['w1'],w['w2'],w['w3'] = 672, 672, 672

# count inventory subtotal
tot_inventory = sum(r.values())+sum(w.values())

# membership
member = 1400
member_red = int(0.28 * 1400)
member_white = int(0.1 * 1400)
member_sixpack = int(0.1 * 1400)
member_variety = int(0.52 * 1400)

# first fulfill orders including (red, white, sixpack)
r = {key: r[key] - member_red - member_sixpack for key in r.keys()}
w = {key: w[key] - member_red - member_sixpack for key in w.keys()}
print("Inventory for variety packs: ", [r], [w])

# gogogo is the actual program
def gogogo(r,w):
    variety_3 = []
    n = 0
    while any(v > 0 for v in r.values()) and any(v > 0 for v in w.values()) and sum(r.values())+sum(w.values()) >= 3:
        variety_3.append([])
        # pick 1st slot - red wine
        variety_3[n].append(max(r, key=r.get))
        r[max(r, key=r.get)] -= 1
        # pick 1st slot - white wine
        variety_3[n].append(max(w, key=w.get))
        w[max(w, key=w.get)] -= 1
        # pick 3rd slot - either
        z = r.copy()
        z.update(w)
        t = {i: z[i] for i in z if (i != variety_3[n][0] and i != variety_3[n][1])} # exclude 1st & 2nd choices
        m = max(t, key=t.get)
        variety_3[n].append(m)
        if m in r:
            r[m] -= 1
        else:
            w[m] -= 1
        n += 1
    return n, r, w, variety_3 # return the loop number, remaining reds, remaining whites, and all the vairety_packs

n_1, r_1, w_1, variety_31 = gogogo(r,w)
print("The number of fulfilled red, white, sixpack, variety members: ", member_red,member_white,member_sixpack,n_1)
print("The total number: ", member_red+member_white+member_sixpack+n_1)
print("The number of loops completed (the variety pack): ", n_1)
print("The remaining inventory:\n",[r_1],[w_1])
print("The percentage of variety_box out of total inventory:", n_1/tot_inventory)
print("The variety_box:", variety_31)
