:-module(sCircle).
%method
method(fD__workspace_antlr_C_SCircle_c_, _, type_void(mmain) , (type_int(ia), type_int(ib), type_int(ic), type_int(id), type_int(ix), type_int(iy)), ep_1).
method(fD__workspace_antlr_C_SCircle_c_, _, type_void(mprintSCircle) , (type_int(iv)), ep_2).
%entry point
entry_point(ep_1, fD__workspace_antlr_C_SCircle_c___mmain_r2c1).
entry_point(ep_2, fD__workspace_antlr_C_SCircle_c___mprintSCircle_r22c7).
%instr
instr(fD__workspace_antlr_C_SCircle_c___mmain_r2c1, assign(type_int(ix), const(10)), fD__workspace_antlr_C_SCircle_c___mmain_r3c1).
%instr(fD__workspace_antlr_C_SCircle_c___mmain_r2c1, assign(type_int(ix), call_mprintSCircle(multiply(type_int(ic), type_int(id)))), fD__workspace_antlr_C_SCircle_c___mmain_r3c1).
instr(fD__workspace_antlr_C_SCircle_c___mmain_r6c8, call_mprintf(const(0)), fD__workspace_antlr_C_SCircle_c___mmain_r7c1).
instr(fD__workspace_antlr_C_SCircle_c___mmain_r3c1, ite(great(plus(type_int(ia), type_int(ib)), const(0)), fD__workspace_antlr_C_SCircle_c___mmain_r4c14, fD__workspace_antlr_C_SCircle_c___mmain_r6c8), fD__workspace_antlr_C_SCircle_c___mmain_r7c1).
instr(fD__workspace_antlr_C_SCircle_c___mmain_r4c14, call_mprintSCircle(plus(type_int(ia), type_int(ib))), fD__workspace_antlr_C_SCircle_c___mmain_r7c1).
instr(fD__workspace_antlr_C_SCircle_c___mmain_r10c8, call_mprintf(const(0)), fD__workspace_antlr_C_SCircle_c___mmain_r11c1).
instr(fD__workspace_antlr_C_SCircle_c___mmain_r7c1, ite(great(multiply(type_int(ic), type_int(id)), const(0)), fD__workspace_antlr_C_SCircle_c___mmain_r8c14, fD__workspace_antlr_C_SCircle_c___mmain_r10c8), fD__workspace_antlr_C_SCircle_c___mmain_r11c1).
instr(fD__workspace_antlr_C_SCircle_c___mmain_r8c14, call_mprintSCircle(multiply(type_int(ic), type_int(id))), fD__workspace_antlr_C_SCircle_c___mmain_r11c1).
%instr(fD__workspace_antlr_C_SCircle_c___mmain_r12c15, assign(type_int(ix), type_int(iy)), fD__workspace_antlr_C_SCircle_c___mmain_r12c14).
%instr(fD__workspace_antlr_C_SCircle_c___mmain_r14c15, assign(type_int(ix), type_int(iy)), fD__workspace_antlr_C_SCircle_c___mmain_r14c14).
instr(fD__workspace_antlr_C_SCircle_c___mmain_r14c14, call_mprintSCircle(assign(type_int(ix), minus(type_int(ix), type_int(iy)))), fD__workspace_antlr_C_SCircle_c___mmain_r15c1).
instr(fD__workspace_antlr_C_SCircle_c___mmain_r11c1, ite(great(type_int(ix), type_int(iy)), fD__workspace_antlr_C_SCircle_c___mmain_r12c14, fD__workspace_antlr_C_SCircle_c___mmain_r14c14), fD__workspace_antlr_C_SCircle_c___mmain_r15c1).
instr(fD__workspace_antlr_C_SCircle_c___mmain_r12c14, call_mprintSCircle(assign(type_int(ix), plus(type_int(ix), type_int(iy)))), fD__workspace_antlr_C_SCircle_c___mmain_r15c1).
instr(fD__workspace_antlr_C_SCircle_c___mmain_r18c8, call_mprintf(const(0)), fD__workspace_antlr_C_SCircle_c___mmain_end).
instr(fD__workspace_antlr_C_SCircle_c___mmain_r15c1, ite(great(minus(type_int(ia), type_int(id)), const(0)), fD__workspace_antlr_C_SCircle_c___mmain_r16c14, fD__workspace_antlr_C_SCircle_c___mmain_r18c8), fD__workspace_antlr_C_SCircle_c___mmain_end).
instr(fD__workspace_antlr_C_SCircle_c___mmain_r16c14, call_mprintSCircle(plus(type_int(ix), const(1))), fD__workspace_antlr_C_SCircle_c___mmain_end).
instr(fD__workspace_antlr_C_SCircle_c___mprintSCircle_r22c7, call_massert(greateq(type_int(iv), const(0))), fD__workspace_antlr_C_SCircle_c___mprintSCircle_r23c1).
instr(fD__workspace_antlr_C_SCircle_c___mprintSCircle_r23c1, assign(type_int(is),multiply(multiply(const(3.14), type_int(iv)), type_int(iv))), fD__workspace_antlr_C_SCircle_c___mprintSCircle_end).
