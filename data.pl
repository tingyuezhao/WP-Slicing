:-module(data).
%method
method(fD__data_c_, _, type_void(m__VERIFIER_assert) , (type_int(icond)), ep_1).
method(fD__data_c_, _, type_int(minsert) , (type_int(iarraylist(iset[])), type_int(isize), type_int(ivalue)), ep_2).
method(fD__data_c_, _, type_int(melem_exists) , (type_int(iarraylist(iset[])), type_int(isize), type_int(ivalue)), ep_3).
method(fD__data_c_, _, type_int(mmain) , (_), ep_4).
%entry point
entry_point(ep_1, fD__data_c___m__VERIFIER_assert_r2c35).
entry_point(ep_2, fD__data_c___minsert_r9c5).
entry_point(ep_3, fD__data_c___melem_exists_r14c2).
entry_point(ep_4, fD__data_c___mmain_r22c2).
%instr
instr(fD__data_c___m__VERIFIER_assert_r2c35, ite(not(type_int(icond),), fD__data_c___m__VERIFIER_assert_end).
instr(fD__data_c___minsert_r9c2, assign(type_int(iarrayelement(iset[size]), type_int(ivalue)), fD__data_c___minsert_r10c2).
instr(fD__data_c___minsert_r10c2, mreturn(plus(type_int(isize), const(1))), fD__data_c___minsert_ret).
instr(fD__data_c___melem_exists_r16c4, ite(equal(type_int(iarrayelement(iset[i]), type_int(ivalue)), fD__data_c___melem_exists_r16c29, fD__data_c___melem_exists_r16c29), fD__data_c___melem_exists_r16c29).
instr(fD__data_c___melem_exists_r15c2, for((assign(type_int(ii), const(0));less(type_int(ii), type_int(isize));assign(type_int(ii), const(1))), fD__data_c___melem_exists_r16c4), fD__data_c___melem_exists_r16c29).
instr(fD__data_c___melem_exists_r16c29, mreturn(const(0)), fD__data_c___melem_exists_ret).
instr(fD__data_c___melem_exists_r18c2, mreturn(const(0)), fD__data_c___melem_exists_ret).
instr(fD__data_c___mmain_r22c2, assign(type_int(in),const(0)), fD__data_c___mmain_r28c2).
instr(fD__data_c___mmain_r30c23, call_m__VERIFIER_assert(notequal(type_int(iarrayelement(iset[x]), type_int(iarrayelement(iset[y]))), fD__data_c___mmain_r29c4).
instr(fD__data_c___mmain_r29c4, for((assign(type_int(iy), plus(type_int(ix), const(1)));less(type_int(iy), type_int(in));assign(type_int(iy), const(1))), fD__data_c___mmain_r30c23), fD__data_c___mmain_r28c2).
instr(fD__data_c___mmain_r28c2, for((assign(type_int(ix), const(0));less(type_int(ix), type_int(in));assign(type_int(ix), const(1))), fD__data_c___mmain_r29c4), fD__data_c___mmain_r39c2).
instr(fD__data_c___mmain_r39c2, for((assign(type_int(iv), const(0));less(type_int(iv), const(SIZE));assign(type_int(iv), const(1))), fD__data_c___mmain_r41c4), fD__data_c___mmain_r41c21).
instr(fD__data_c___mmain_r41c4, ite(not(call_melem_exists(type_int(in), type_int(iarrayelement(ivalues[v]))), fD__data_c___mmain_r43c6, fD__data_c___mmain_r39c2), fD__data_c___mmain_r39c2).
instr(fD__data_c___mmain_r43c6, assign(type_int(in), call_minsert(type_int(in), type_int(iarrayelement(ivalues[v]))), fD__data_c___mmain_r39c2).
instr(fD__data_c___mmain_r41c21, call_melem_exists(type_int(in), type_int(iarrayelement(ivalues[v])), fD__data_c___mmain_r39c2).
instr(fD__data_c___mmain_r50c23, call_m__VERIFIER_assert(notequal(type_int(iarrayelement(iset[x]), type_int(iarrayelement(iset[y]))), fD__data_c___mmain_r49c4).
instr(fD__data_c___mmain_r49c4, for((assign(type_int(iy), plus(type_int(ix), const(1)));less(type_int(iy), type_int(in));assign(type_int(iy), const(1))), fD__data_c___mmain_r50c23), fD__data_c___mmain_r48c2).
instr(fD__data_c___mmain_r48c2, for((assign(type_int(ix), const(0));less(type_int(ix), type_int(in));assign(type_int(ix), const(1))), fD__data_c___mmain_r49c4), fD__data_c___mmain_r53c2).
instr(fD__data_c___mmain_r53c2, mreturn(const(0)), fD__data_c___mmain_ret).
