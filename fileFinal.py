from random import randint

def create_array(size=10,max=50):
	return [randint(0,max) for _ in range(size)]

def quickSort(a):

	if len(a)<=1: return a
	smaller,equal,larger = [],[],[]
	pivot = a[randint(0,len(a)-1)]

	for x in a:
		if x<pivot:		smaller.append(x)
		elif x==pivot: 	equal.append(x)
		else:			larger.append(x)

	return quickSort(smaller)+equal+quickSort(larger)

def bubbleSort(arr):
    print("lel")

#benchmark quicksort vs bubblesort
def benchmark(samples,array):
    
    times = {'quick':[],'bubble':[]}

    from time import time

    for size in array:
        tot_time=0.0
        for _ in range(samples):
            a=create_array(size,size)
            t0=time()
            s=bubbleSort(a)
            t1=time()
            tot_time+=(t1-t0)
        times['bubble'].append(tot_time/float(samples))

        tot_time=0.0
        for _ in range(samples):
            a=create_array(size,size)
            t0=time()
            s=quickSort(a)
            t1=time()
            tot_time+=(t1-t0)
        times['quick'].append(tot_time/float(samples))

    print ("n\tQuickSort\tBubbleSort")
    print (40*"_")
    for i,size in enumerate(array):
        print ("%d\t%0.5f\t%0.5f"%(
            size,
            times['quick'][i],
            times['bubble'][i]))

samples = 5
array=[10,100,1000,10000,100000]
benchmark(samples,array)

    



 