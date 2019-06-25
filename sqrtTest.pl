:-module(sqrtTest).
%method
method(fD__workspace_antlr_C_sqrtTest_c_, _, type_void(mmain) , (type_int(ia), type_int(ib), type_int(ic), type_int(id), type_int(in)), ep_1).
method(fD__workspace_antlr_C_sqrtTest_c_, _, type_void(mprintSqrt) , (type_int(iv)), ep_2).
%entry point
entry_point(ep_1, fD__workspace_antlr_C_sqrtTest_c___mmain_r2c1).
entry_point(ep_2, fD__workspace_antlr_C_sqrtTest_c___mprintSqrt_r23c7).
%instr
instr(fD__workspace_antlr_C_sqrtTest_c___mmain_r2c1, assign(type_int(im),const(10)), fD__workspace_antlr_C_sqrtTest_c___mmain_r3c1).
instr(fD__workspace_antlr_C_sqrtTest_c___mmain_r3c1, assign(type_int(ia), const(1)), fD__workspace_antlr_C_sqrtTest_c___mmain_r4c1).
instr(fD__workspace_antlr_C_sqrtTest_c___mmain_r7c8, call_mprintf(const(0)), fD__workspace_antlr_C_sqrtTest_c___mmain_r8c1).
instr(fD__workspace_antlr_C_sqrtTest_c___mmain_r4c1, ite(greateq(plus(type_int(ia), type_int(ib)), const(0)), fD__workspace_antlr_C_sqrtTest_c___mmain_r5c11, fD__workspace_antlr_C_sqrtTest_c___mmain_r7c8), fD__workspace_antlr_C_sqrtTest_c___mmain_r8c1).
instr(fD__workspace_antlr_C_sqrtTest_c___mmain_r5c11, call_mprintSqrt(plus(type_int(ia), type_int(ib))), fD__workspace_antlr_C_sqrtTest_c___mmain_r8c1).
instr(fD__workspace_antlr_C_sqrtTest_c___mmain_r11c8, call_mprintf(const(0)), fD__workspace_antlr_C_sqrtTest_c___mmain_r12c1).
instr(fD__workspace_antlr_C_sqrtTest_c___mmain_r8c1, ite(greateq(multiply(type_int(ic), type_int(id)), const(0)), fD__workspace_antlr_C_sqrtTest_c___mmain_r9c11, fD__workspace_antlr_C_sqrtTest_c___mmain_r11c8), fD__workspace_antlr_C_sqrtTest_c___mmain_r12c1).
instr(fD__workspace_antlr_C_sqrtTest_c___mmain_r9c11, call_mprintSqrt(multiply(type_int(ic), type_int(id))), fD__workspace_antlr_C_sqrtTest_c___mmain_r12c1).
instr(fD__workspace_antlr_C_sqrtTest_c___mmain_r15c11, call_mprintSqrt(assign(type_int(im), minus(type_int(im), type_int(in)))), fD__workspace_antlr_C_sqrtTest_c___mmain_r16c1).
instr(fD__workspace_antlr_C_sqrtTest_c___mmain_r12c1, ite(greateq(type_int(im), type_int(in)), fD__workspace_antlr_C_sqrtTest_c___mmain_r13c11, fD__workspace_antlr_C_sqrtTest_c___mmain_r15c11), fD__workspace_antlr_C_sqrtTest_c___mmain_r16c1).
instr(fD__workspace_antlr_C_sqrtTest_c___mmain_r13c11, call_mprintSqrt(assign(type_int(im), plus(type_int(im), type_int(in)))), fD__workspace_antlr_C_sqrtTest_c___mmain_r16c1).
instr(fD__workspace_antlr_C_sqrtTest_c___mmain_r19c8, call_mprintf(const(0)), fD__workspace_antlr_C_sqrtTest_c___mmain_end).
instr(fD__workspace_antlr_C_sqrtTest_c___mmain_r16c1, ite(greateq(minus(type_int(ia), type_int(id)), const(0)), fD__workspace_antlr_C_sqrtTest_c___mmain_r17c11, fD__workspace_antlr_C_sqrtTest_c___mmain_r19c8), fD__workspace_antlr_C_sqrtTest_c___mmain_end).
instr(fD__workspace_antlr_C_sqrtTest_c___mmain_r17c11, call_mprintSqrt(plus(type_int(im), const(1))), fD__workspace_antlr_C_sqrtTest_c___mmain_end).
instr(fD__workspace_antlr_C_sqrtTest_c___mprintSqrt_r23c7, call_massert(greateq(type_int(iv), const(0))), fD__workspace_antlr_C_sqrtTest_c___mprintSqrt_r24c1).
instr(fD__workspace_antlr_C_sqrtTest_c___mprintSqrt_r24c1, assign(type_int(iq),call_msqrt(type_int(iv))), fD__workspace_antlr_C_sqrtTest_c___mprintSqrt_end).

