
from insertion import insertion_sort
from merge_sort import merge_sort
from partially_sorted import get_partially_sorted_numbers
from random_numbers import get_random_numbers
import timeit



def main():
  data_small = get_random_numbers(1000, 1000)
  data_medium = get_random_numbers(10000, 10000)
  data_partially_sorted_small = get_partially_sorted_numbers(1000, 0.5)
  data_partially_sorted_medium = get_partially_sorted_numbers(10000, 0.5)
    
  
  time_small_insertion = timeit.timeit(lambda: insertion_sort(data_small[:]), number=10)
  time_small_merge = timeit.timeit(lambda: merge_sort(data_small[:]), number=10)
  time_small_timsort = timeit.timeit(lambda: sorted(data_small[:]), number=10)
  time_small_timsort_s = timeit.timeit(lambda: data_small[:].sort(), number=10)
  
  time_medium_insertion = timeit.timeit(lambda: insertion_sort(data_medium[:]), number=10)
  time_medium_merge = timeit.timeit(lambda: merge_sort(data_medium[:]), number=10)
  time_medium_timsort = timeit.timeit(lambda: sorted(data_medium[:]), number=10)
  time_medium_timsort_s = timeit.timeit(lambda: data_medium[:].sort(), number=10)
  
  time_small_ps_insertion = timeit.timeit(lambda: insertion_sort(data_partially_sorted_small[:]), number=10)
  time_small_ps_merge = timeit.timeit(lambda: merge_sort(data_partially_sorted_small[:]), number=10)
  time_small_ps_timsort = timeit.timeit(lambda: sorted(data_partially_sorted_small[:]), number=10)
  time_small_ps_timsort_s = timeit.timeit(lambda: data_partially_sorted_small[:].sort(), number=10)
  
  time_medium_ps_insertion = timeit.timeit(lambda: insertion_sort(data_partially_sorted_medium[:]), number=10)
  time_medium_ps_merge = timeit.timeit(lambda: merge_sort(data_partially_sorted_medium[:]), number=10)
  time_medium_ps_timsort = timeit.timeit(lambda: sorted(data_partially_sorted_medium[:]), number=10)
  time_medium_ps_timsort_s = timeit.timeit(lambda: data_partially_sorted_medium[:].sort(), number=10)
  
  print(f"{'| Algorithm': <20} | {'Time small data': <20} | {'Time medium data': <20} | {'Time small data ps': <20} | {'Time medium data ps': <20}")
  print(f":{'-'*19} | :{'-'*19} | :{'-'*19} | :{'-'*19} | :{'-'*19}")
  print(f"{'| Insertion sort': <20} | {time_small_insertion:<20.5f} | {time_medium_insertion:<20.5f} | {time_small_ps_insertion:<20.5f} | {time_medium_ps_insertion:<20.5f}")
  print(f"{'| Merge sort': <20} | {time_small_merge:<20.5f} | {time_medium_merge:<20.5f} | {time_small_ps_merge:<20.5f} | {time_medium_ps_merge:<20.5f}")
  print(f"{'| Tim sort sorted': <20} | {time_small_timsort:<20.5f} | {time_medium_timsort:<20.5f} | {time_small_ps_timsort:<20.5f} | {time_medium_ps_timsort:<20.5f}")
  print(f"{'| Tim sort sort': <20} | {time_small_timsort_s:<20.5f} | {time_medium_timsort_s:<20.5f} | {time_small_ps_timsort_s:<20.5f} | {time_medium_ps_timsort_s:<20.5f}")
  
  
  

if __name__ == "__main__":
    main()