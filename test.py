from math import sqrt
import shuffle as s

i = ['123', 'aaa', 'bbb', 'usdhus', '23213', "22", "234", 123, 14342, 21, 677, 564, 56456, 5463]
i = [i*8 for i in range(20)]
bucket_size = int(sqrt(len(i)))
pi = s.fill_pi(len(i), bucket_size)
k1 = "111"
k2 = "222"
i = s.mel_shuffle(i, pi, k1, k2, 2)
print(i)