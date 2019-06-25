:-module(tryEX).
%method
method(fD__workspace_swipl_tryEX_c_, _, type_int(mmain) , (type_int(ia), type_int(ib)), ep_1).
method(fD__workspace_swipl_tryEX_c_, _, type_int(mswap) , (type_int(ia), type_int(ib)), ep_2).
method(fD__workspace_swipl_tryEX_c_, _, type_void(muserCout) , (type_int(iarg)), ep_3).
%entry point
entry_point(ep_1, fD__workspace_swipl_tryEX_c___mmain_r3c3).
entry_point(ep_2, fD__workspace_swipl_tryEX_c___mswap_r46c3).
entry_point(ep_3, fD__workspace_swipl_tryEX_c___muserCout_r53c3).
%instr
instr(fD__workspace_swipl_tryEX_c___mmain_r3c3, assign(type_int(im),const(0)), fD__workspace_swipl_tryEX_c___mmain_r4c3).
instr(fD__workspace_swipl_tryEX_c___mmain_r6c6, assign(type_int(im), call_mswap(type_int(ia), type_int(ib))), fD__workspace_swipl_tryEX_c___mmain_r7c6).
instr(fD__workspace_swipl_tryEX_c___mmain_r10c6, assign(type_int(im), type_int(ia)), fD__workspace_swipl_tryEX_c___mmain_r11c3).
instr(fD__workspace_swipl_tryEX_c___mmain_r4c3, ite(great(type_int(ia), type_int(ib)), fD__workspace_swipl_tryEX_c___mmain_r6c6, fD__workspace_swipl_tryEX_c___mmain_r10c6), fD__workspace_swipl_tryEX_c___mmain_r11c3).
instr(fD__workspace_swipl_tryEX_c___mmain_r7c6, assign(type_int(ib), plus(type_int(ib), const(1))), fD__workspace_swipl_tryEX_c___mmain_r11c3).
instr(fD__workspace_swipl_tryEX_c___mmain_r13c6, assign(type_int(ia), plus(type_int(ia), type_int(ii))), fD__workspace_swipl_tryEX_c___mmain_r14c6).
instr(fD__workspace_swipl_tryEX_c___mmain_r14c6, assign(type_int(ib), call_mswap(type_int(ia), type_int(ib))), fD__workspace_swipl_tryEX_c___mmain_r15c6).
instr(fD__workspace_swipl_tryEX_c___mmain_r15c6, assign(type_int(ib), plus(type_int(ib), const(1))), fD__workspace_swipl_tryEX_c___mmain_r11c3).
instr(fD__workspace_swipl_tryEX_c___mmain_r11c3, for((assign(type_int(ii),const(0));less(type_int(ii), const(4));assign(type_int(ii), plus(type_int(ii), const(1)))), fD__workspace_swipl_tryEX_c___mmain_r13c6), fD__workspace_swipl_tryEX_c___mmain_r17c3).
instr(fD__workspace_swipl_tryEX_c___mmain_r17c3, assign(type_double(dc),const(1.5)), fD__workspace_swipl_tryEX_c___mmain_r18c3).
instr(fD__workspace_swipl_tryEX_c___mmain_r20c6, case_1(call_mprintf("%s\n",type_int(im))), fD__workspace_swipl_tryEX_c___mmain_r22c9).
instr(fD__workspace_swipl_tryEX_c___mmain_r22c9, assign(type_int(im), minus(plus(multiply(type_int(ib), minus(type_int(ia), const(1))), multiply(const(4), type_int(ib))), const(5))), fD__workspace_swipl_tryEX_c___mmain_r23c9).
instr(fD__workspace_swipl_tryEX_c___mmain_r23c9, assign(type_int(ib), call_mswap(type_int(ia), type_int(ib))), fD__workspace_swipl_tryEX_c___mmain_r24c9).
instr(fD__workspace_swipl_tryEX_c___mmain_r26c6, case_2(call_printf("%s\n",type_int(im))), fD__workspace_swipl_tryEX_c___mmain_r28c9).
instr(fD__workspace_swipl_tryEX_c___mmain_r31c14, call_mprintf(const("%s\n"), type_int(im)), fD__workspace_swipl_tryEX_c___mmain_r32c9).
instr(fD__workspace_swipl_tryEX_c___mmain_r32c9, assign(type_int(im), minus(type_int(ia), type_int(ib))), fD__workspace_swipl_tryEX_c___mmain_r35c3).
instr(fD__workspace_swipl_tryEX_c___mmain_r18c3, switch(type_int(ia),(1,fD__workspace_swipl_tryEX_c___mmain_r20c6),(2,fD__workspace_swipl_tryEX_c___mmain_r26c6), fD__workspace_swipl_tryEX_c___mmain_r31c14), fD__workspace_swipl_tryEX_c___mmain_r35c3).
instr(fD__workspace_swipl_tryEX_c___mmain_r28c9, assign(type_int(im), minus(type_int(ia), const(2))), fD__workspace_swipl_tryEX_c___mmain_r35c3).
instr(fD__workspace_swipl_tryEX_c___mmain_r24c9, assign(type_int(ib), plus(type_int(ib), const(1))), fD__workspace_swipl_tryEX_c___mmain_r35c3).
instr(fD__workspace_swipl_tryEX_c___mmain_r37c6, assign(type_int(im), plus(type_int(im), type_int(ib))), fD__workspace_swipl_tryEX_c___mmain_r38c6).
instr(fD__workspace_swipl_tryEX_c___mmain_r38c6, assign(type_int(ib1), plus(type_int(ia1), call_mswap(type_int(ia2), type_int(ib2)))), fD__workspace_swipl_tryEX_c___mmain_r39c6).
instr(fD__workspace_swipl_tryEX_c___mmain_r39c6, assign(type_int(ib), plus(type_int(ib), const(1))), fD__workspace_swipl_tryEX_c___mmain_r35c3).
instr(fD__workspace_swipl_tryEX_c___mmain_r35c3, while(less(type_int(im), const(0)), fD__workspace_swipl_tryEX_c___mmain_r37c6), fD__workspace_swipl_tryEX_c___mmain_r41c3).
instr(fD__workspace_swipl_tryEX_c___mmain_r41c3, call_muserCout(type_int(im)), fD__workspace_swipl_tryEX_c___mmain_r42c3).
instr(fD__workspace_swipl_tryEX_c___mmain_r42c3, mreturn(type_int(im)), fD__workspace_swipl_tryEX_c___mmain_ret).
instr(fD__workspace_swipl_tryEX_c___mswap_r46c3, assign(type_int(ia), plus(type_int(ia), type_int(ib))), fD__workspace_swipl_tryEX_c___mswap_r47c3).
instr(fD__workspace_swipl_tryEX_c___mswap_r47c3, assign(type_int(ib), minus(type_int(ia), type_int(ib))), fD__workspace_swipl_tryEX_c___mswap_r48c3).
instr(fD__workspace_swipl_tryEX_c___mswap_r48c3, assign(type_int(ia), minus(type_int(ia), type_int(ib))), fD__workspace_swipl_tryEX_c___mswap_r49c3).
instr(fD__workspace_swipl_tryEX_c___mswap_r49c3, mreturn(type_int(ia)), fD__workspace_swipl_tryEX_c___mswap_ret).
instr(fD__workspace_swipl_tryEX_c___muserCout_r54c3, assign(type_int(iarg), plus(type_int(iarg), const(1))), fD__workspace_swipl_tryEX_c___muserCout_r55c3).
instr(fD__workspace_swipl_tryEX_c___muserCout_r55c3, assign(type_int(ibrg),call_mswap(type_int(iarg), const(1))), fD__workspace_swipl_tryEX_c___muserCout_end).
