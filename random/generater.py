class XORshift:
    def __init__(self, seed):
        self.state = seed & 0xffffffffffffffff
        if self.state == 0:
            self.state = 88172645463325252

    def next(self):
        x = self.state
        x ^= (x << 13) & 0xffffffffffffffff
        x ^= (x >> 7)
        x ^= (x << 17) & 0xffffffffffffffff
        self.state = x & 0xffffffffffffffff
        return self.state

    def randint(self, min_n, max_n):
        range_size = max_n - min_n + 1
        max_val = 0xffffffffffffffff
        threshold = (max_val+1) - ((max_val+1) % range_size)
        while True:
            r = self.next()
            if r < threshold:
                return min_n + (r % range_size)
    
    def sequence(self, N, min_n, max_n):
        #長さNの各要素がmin_n以上max_n以下の数列を生成する
        return [self.randint(min_n, max_n) for _ in range(N)]

    def gen_grid(self,H,W):
        #H*Wのgridを生成する
        return [[".#"[b] for b in self.sequence(W,0,1)] for _ in range(H)]



def generate(seed):
  xs = XORshift(seed)
  
  if seed < 100:
    N = xs.randint(1,10)
    min_n = 1
    max_n = 10
  
  elif seed < 1000:
    N = xs.randint(1,50)
    min_n = 1
    max_n = 100
  
  #これより下はジャッジ想定
  elif seed < 10000:
    N = xs.randint(1,1000)
    min_n = 1
    max_n = 10**9
  
  elif seed < 100000:
    N = xs.randint(1,3000)
    min_n = 1
    max_n = 10**9
  
  elif seed < 1000000:
    N = xs.randint(1,50000)
    min_n = 1
    max_n = 10**9
  
  elif seed < 10**10:
    N = xs.randint(1,2*10**5)
    min_n = 1
    max_n = 10**9
  
  else:
    N = xs.randint(1,10**6)
    min_n = 1
    max_n = 10**9
  

  A = xs.sequence(N, min_n, max_n)
  G = xs.gen_grid(10,3)
  
  return N,A,G

# 使用例
seed = 97
N,A,G = generate(seed)
print(N)
print(A)
for g in G:
    print(g)
