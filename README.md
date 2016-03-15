# SPASS Proof Parser

Very simple script to make a more understandable output for [SPASS](http://www.spass-prover.org/)

Example input:
```
 $ SPASS -DocProof sokrates.dfg
 --------------------------SPASS-START-----------------------------
 Input Problem:
 1[0:Inp] ||  -> Human(sokrates)*.
 2[0:Inp] || Mortal(sokrates)* -> .
 3[0:Inp] || Human(U) -> Mortal(U)*.
  This is a monadic Horn problem without equality.
  This is a problem that has, if any, a finite domain model.
  There are no function symbols.
  This is a problem that contains sort information.
  The conjecture is ground.
  The following monadic predicates have finite extensions: Human.
  Axiom clauses: 2 Conjecture clauses: 1
  Inferences: IEmS=1 ISoR=1 IORe=1
  Reductions: RFMRR=1 RBMRR=1 RObv=1 RUnC=1 RTaut=1 RSST=1 RSSi=1 RFSub=1 RBSub=1 RCon=1
  Extras    : Input Saturation, Always Selection, No Splitting, Full Reduction,  Ratio: 5, FuncWeight: 1, VarWeight: 1
  Precedence: Mortal > Human > p > sokrates
  Ordering  : KBO
 Processed Problem:

 Worked Off Clauses:

 Usable Clauses:
 1[0:Inp] ||  -> Human(sokrates)*.
 2[0:Inp] || Mortal(sokrates)* -> .
 3[0:Inp] Human(U) ||  -> Mortal(U)*.
 SPASS V 3.5
 SPASS beiseite: Proof found.
 Problem: formal-validation/CompCert/test/spass/sokrates.dfg
 SPASS derived 1 clauses, backtracked 0 clauses, performed 0 splits and kept 4 clauses.
 SPASS allocated 52184 KBytes.
 SPASS spent   0:00:00.05 on the problem.
       0:00:00.02 for the input.
       0:00:00.01 for the FLOTTER CNF translation.
       0:00:00.00 for inferences.
       0:00:00.00 for the backtracking.
       0:00:00.00 for the reduction.


 Here is a proof with depth 1, length 5 :
 1[0:Inp] ||  -> Human(sokrates)*.
 2[0:Inp] || Mortal(sokrates)* -> .
 3[0:Inp] Human(U) ||  -> Mortal(U)*.
 4[0:Res:3.1,2.0] Human(sokrates) ||  -> .
 5[0:MRR:4.0,1.0] ||  -> .
 Formulae used in the proof : axiom0 conjecture0 axiom1

 --------------------------SPASS-STOP------------------------------
```

Example output:
```
 Method: Input
 ##
 1  Human(sokrates)*
 ---------------------------------------
 Method: Input
 ##
 2  ~Mortal(sokrates)*
 ---------------------------------------
 Method: Input
 ##
 3  Human(U) -> Mortal(U)
 ---------------------------------------
 Method: General Resolution
 3  Human(U) -> Mortal(U)
 2  ~Mortal(sokrates)*
 ##
 4  ~Human(sokrates)
 ---------------------------------------
 Method: Matching Replacement ResolutioN
 4  ~Human(sokrates)
 1  Human(sokrates)*
 ##
 5  END
 ---------------------------------------
```

