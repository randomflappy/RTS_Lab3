#   RTS Lab3
#   IO-71 Fryzyuk
#   var: n, w_max, N = 12, 2700, 64
import math
import random
import matplotlib.pyplot as plt


def signal(the_n, the_upper_n, the_w_max):
    amplitude = [random.random() for i in range(the_n)]
    phi = [random.random() for j in range(the_n)]
    cont = []
    for i in range(the_upper_n):
        tmp_sum = 0
        for p in range(the_n):
            tmp_sum += amplitude[p] * math.sin(the_w_max / the_n * p * i + phi[p])
        cont.append(tmp_sum)
    return cont


def furies(the_signal, the_upper_n, the_wpkn_table):
    result = []
    for p in range(the_upper_n):
        real_part = 0
        imaginary_part = 0
        for k in range(the_upper_n):
            real_part += the_signal[k] * the_wpkn_table[p][k][0]
            imaginary_part += the_signal[k] * the_wpkn_table[p][k][1]
        result.append(math.sqrt(real_part**2 + imaginary_part**2))
    return result


def create_table_wpkn(the_upper_n):
    wpkn_table = []
    for p in range(the_upper_n):
        row = []
        for k in range(the_upper_n):
            re_w = math.cos((2*math.pi*p*k)/the_upper_n)
            im_w = math.cos((2*math.pi*p*k)/the_upper_n)
            row.append((re_w, im_w))
        wpkn_table.append(row)
    return wpkn_table


# Graph 1 -----------------
n, w_max, N = 12, 2700, 64
sig = signal(n, N, w_max)
wpkn_tab = create_table_wpkn(N)
fur = furies(sig, N, wpkn_tab)

plt.bar([i for i in range(N)], fur)
plt.title('Lab3')
plt.show()