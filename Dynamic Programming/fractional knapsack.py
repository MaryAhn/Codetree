m_n = input().split()
m, n = int(m_n[0]), int(m_n[1])
weight_price = [[0, 0, 0] for _ in range(m)]

for i in range(m):
    tmp = input()
    w_p = tmp.split()
    weight_price[i][0], weight_price[i][1] = int(w_p[0]), int(w_p[1])
    weight_price[i][2] = weight_price[i][1] / weight_price[i][0]

weight_price.sort(key=lambda x:x[2], reverse=True)

present_weight, present_price, idx, rest = 0, 0, 0, 0

for i in range(m):
    if present_weight + weight_price[i][0] <= n:
        present_weight += weight_price[i][0]
        present_price += weight_price[i][1]
        idx += 1
    else:
        break

rest = n - present_weight

if rest == 0 or idx == m:
    print(f'{present_price:.3f}')

elif idx < m:
    present_price += rest * weight_price[idx][2]
    print(f'{present_price:.3f}')