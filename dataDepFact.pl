:-module(dataDepFact).
%method
method(fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c_, _, type_int(mbinarySearch) , (type_int(iarraylist(ia)), type_int(iitem), type_int(ilow), type_int(ihigh)), ep_1).
method(fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c_, _, type_void(minsertionSort) , (type_int(iarraylist(ia)), type_int(in)), ep_2).
method(fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c_, _, type_int(mmain) , (_), ep_3).
%entry point
entry_point(ep_1, fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___mbinarySearch_r9c4).
entry_point(ep_2, fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___minsertionSort_r25c4).
entry_point(ep_3, fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___mmain_r47c4).
%instr
instr(fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___mbinarySearch_r9c4, ite(lesseq(type_int(ihigh), type_int(ilow)), fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___mbinarySearch_r10c8, fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___mbinarySearch_r10c8), fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___mbinarySearch_r10c8).
instr(fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___mbinarySearch_r10c8, mreturn(type_int(ilow)), fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___mbinarySearch_ret).
instr(fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___mbinarySearch_r12c4, assign(type_int(imid),divide(plus(type_int(ilow), type_int(ihigh)), const(2))), fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___mbinarySearch_r14c4).
instr(fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___mbinarySearch_r14c4, ite(equal(type_int(iitem), type_int(iarrayelement(ia(mid)))), fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___mbinarySearch_r15c8, fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___mbinarySearch_r15c8), fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___mbinarySearch_r15c8).
instr(fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___mbinarySearch_r15c8, mreturn(plus(type_int(imid), const(1))), fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___mbinarySearch_ret).
instr(fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___mbinarySearch_r17c4, ite(great(type_int(iitem), type_int(iarrayelement(ia(mid)))), fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___mbinarySearch_r18c8, fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___mbinarySearch_r18c8), fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___mbinarySearch_r18c8).
instr(fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___mbinarySearch_r18c8, mreturn(call_mbinarySearch(plus(type_int(imid), const(1)), type_int(ihigh))), fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___mbinarySearch_ret).
instr(fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___mbinarySearch_r18c27, call_mbinarySearch(plus(type_int(imid), const(1)), type_int(ihigh)), fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___mbinarySearch_r19c4).
instr(fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___mbinarySearch_r19c4, mreturn(call_mbinarySearch(type_int(ilow), minus(type_int(imid), const(1)))), fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___mbinarySearch_ret).
instr(fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___mbinarySearch_r19c23, call_mbinarySearch(type_int(ilow), minus(type_int(imid), const(1))), fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___mbinarySearch_end).
instr(fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___minsertionSort_r29c8, assign(type_int(ij), minus(type_int(ii), const(1))), fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___minsertionSort_r30c8).
instr(fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___minsertionSort_r30c8, assign(type_int(iselected), type_int(iarrayelement(ia(i)))), fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___minsertionSort_r33c8).
instr(fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___minsertionSort_r33c8, assign(type_int(iloc), call_mbinarySearch(const(0), type_int(ij))), fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___minsertionSort_r36c8).
instr(fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___minsertionSort_r38c12, assign(type_int(iarrayelement(ia(j+1))), type_int(iarrayelement(ia(j)))), fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___minsertionSort_r39c12).
instr(fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___minsertionSort_r39c12, assign(type_int(ij), minus_l(type_int(ij), const(1))), fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___minsertionSort_r36c8).
instr(fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___minsertionSort_r36c8, while(greateq(type_int(ij), type_int(iloc)), fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___minsertionSort_r38c12), fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___minsertionSort_r41c8).
instr(fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___minsertionSort_r41c8, assign(type_int(iarrayelement(ia(j+1))), type_int(iselected)), fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___minsertionSort_r27c4).
instr(fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___minsertionSort_r27c4, for((assign(type_int(ii), const(1));less(type_int(ii), type_int(in));++(type_int(ii))), fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___minsertionSort_r29c8), fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___minsertionSort_end).
instr(fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___mmain_r48c9, call_mscanf(const("%d"), reference(n)), fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___mmain_r50c4).
instr(fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___mmain_r52c6, call_mscanf(const("%d"), reference(type_int(iarray(ia)))), fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___mmain_r50c4).
instr(fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___mmain_r50c4, for((assign(type_int(ii), const(0));less(type_int(ii), type_int(in));assign(type_int(ii), plus_l(type_int(ii), const(1)))), fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___mmain_r52c6), fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___mmain_r55c17).
instr(fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___mmain_r55c17, call_minsertionSort(const(a), type_int(in)), fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___mmain_r57c10).
instr(fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___mmain_r57c10, call_mprintf(const("Sorted array: \n")), fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___mmain_r58c4).
instr(fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___mmain_r59c14, call_mprintf(const("%d "), type_int(iarrayelement(ia(i)))), fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___mmain_r58c4).
instr(fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___mmain_r58c4, for((assign(type_int(ii), const(0));less(type_int(ii), type_int(in));assign(type_int(ii), plus_l(type_int(ii), const(1)))), fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___mmain_r59c14), fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___mmain_r61c4).
instr(fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___mmain_r61c4, mreturn(const(0)), fD__workspace_360Broswer_sliceProject_Algorithm_C_sorting_binary_insertion_sort_c___mmain_ret).