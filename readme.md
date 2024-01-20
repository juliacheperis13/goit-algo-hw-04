| Algorithm          | Time small data      | Time medium data     | Time small data ps   | Time medium data ps 
:------------------- | :------------------- | :------------------- | :------------------- | :-------------------
| Insertion sort     | 0.17413              | 18.57996             | 0.12900              | 13.54242            
| Merge sort         | 0.01547              | 0.19768              | 0.01285              | 0.18577             
| Tim sort sorted    | 0.00105              | 0.01513              | 0.00053              | 0.00912             
| Tim sort sort      | 0.00101              | 0.01572              | 0.00041              | 0.00768     


As it can be seen from the results, Tim sort sorted and Tim sort sort works much faster with data of small and medium size as well as not sorted and partially sorted data. It proves the efficiency of their usage in Python.

Also, it should be mentioned that insertion sort is executed faster for partially sorted list, but still it takes more time in comparison with other types of sorting algorithms.