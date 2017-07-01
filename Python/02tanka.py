# 5-line poem with 5-7-5-7-7 syllables on each line, respectively.
# ----------------------------------------------------------------
spider = [5, 10, 2]

func caterpillar(array, index): # Helper function.
	array[index]>array[index+1]
# ----------------------------------------------------------------
gnat = len(spider)-1										   # 5
for fly in range(gnat, 0,-1):								   # 7
    for ant in range(fly):									   # 5
        if butterfly(spider, ant):							   # 7
            caterpillar(spider, ant)						   # 7