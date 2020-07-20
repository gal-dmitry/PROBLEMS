{Ввод: p, q, r, A}

Инициализация: B = [0...0](массив длины n)

1) if p == 0 and q == 0:
    for i from 1 to n:
        B[i] = r

2) else if p == 0:
    if q > 0:
        for i from 1 to n:
            B[i] = q * A[i] + r
    else:
        for i from 1 to n:
            B[i] = q * A[n + 1 - i] + r

3) else:
    x = - q / 2p
    if x <= A[1]:
        if p > 0:
            for i from 1 to n:
                B[i] = p * (A[i]) ^ 2 + q * A[i] + r
        else:
            for i from 1 to n:
                B[i] = p * (A[n + 1 - i]) ^ 2 + q * A[n + 1 - i] + r

    else if x >= A[n]:
        if p > 0:
            for i from 1 to n:
                B[i] = p * (A[n + 1 - i]) ^ 2 + q * A[n + 1 - i] + r
        else:
            for i from 1 to n:
                B[i] = p * (A[i]) ^ 2 + q * A[i] + r

    else:
        left = 0
        right = 0
        for i from 1 to n:
            if x >= A[i] and x <= A[i + 1]:
                left = i
                right = i + 1
                break
        if p > 0:
            for j from 1 to n:
                B[j] = min(p*(A[left])^2 + q*A[left] + r, p*(A[right])^2 + q*A[right] + r)
                if B[j] == p*(A[left])^2 + q*A[left] + r:
                    left = left - 1
                else:
                    right = right - 1
        else:
            for j from n downto 1:
                B[j] = max(p*(A[left])^2 + q*A[left] + r, p*(A[right])^2 + q*A[right] + r)
                if B[j] == p*(A[left])^2 + q*A[left] + r:
                    left = left - 1
                else:
                    right = right - 1

4) return B
