#include <llvm/Pass.h> 
#include <llvm/IR/Function.h>
#include <llvm/IR/Instructions.h>
#include <llvm/Analysis/CallGraphSCCPass.h>
#include <llvm/Analysis/CallGraph.h>
#include <llvm/Support/raw_ostream.h>
#include "llvm/IR/LegacyPassManager.h"
#include "llvm/IR/InstIterator.h"
#include <vector>

using namespace llvm;

namespace {
struct SkeletonPass : public FunctionPass {
  static char ID;
  SkeletonPass() : FunctionPass(ID) {
  }

  bool runOnFunction(Function &F) override {
    for (auto& B: F) {
      for (auto& I: B) {
        for (Use &U : I.operands()) {
          Value* v = U.get();
          auto def = dyn_cast<Instruction>(v);
          if (def) {
            errs() << def <<"," << &I <<"\n";
          }
        }
          auto CI = dyn_cast<CallInst>(&I);
          if (CI) {
          Function *calledFunc=CI->getCalledFunction();
          errs()<<&I<<","<<calledFunc<<"\n";
          if (calledFunc && calledFunc->getName() == "function_1881bc") {
                    errs() <<"<" <<&I << "," << I <<">"<< "\n";
                }
      }
     }
    }
    return false;
  }
};

struct SkeletonPass2 : public CallGraphSCCPass {
  static char ID;
  SkeletonPass2() : CallGraphSCCPass(ID) {
  }

  bool runOnSCC(CallGraphSCC &SCC) override {
    for (auto &N : SCC)
    {
      for (auto &C: *N) {
        errs()<<&N<<","<<&C<<"\n";
      }
    }
    return false;
  }
}; // end of struct Hello
}

char SkeletonPass::ID = 0;
static llvm::RegisterPass<SkeletonPass> X(
              "skeleton",           // command line to activate the pass
              "SkeletonPass pass",  // description text of the pass
              false,                // flag to indicate if the pass only looks at CFG
              true                  // ` flag to indicate if the pass is a analysis pass
);
char SkeletonPass2::ID = 1;
static llvm::RegisterPass<SkeletonPass2> Y(
              "skeleton2",           // command line to activate the pass
              "SkeletonPass2 pass2",  // description text of the pass
              false,                // flag to indicate if the pass only looks at CFG
              true                  // flag to indicate if the pass is a analysis pass
);
