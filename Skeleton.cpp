#include <llvm/Pass.h>
#include <llvm/IR/Function.h>
#include <llvm/Analysis/CallGraphSCCPass.h>
#include <llvm/Analysis/CallGraph.h>
#include <llvm/Support/raw_ostream.h>
#include "llvm/IR/LegacyPassManager.h"
#include "llvm/IR/InstIterator.h"
#include <vector>
#include <llvm/IR/Instructions.h>

using namespace llvm;

namespace {
struct SkeletonPass : public FunctionPass {
  static char ID;
  SkeletonPass() : FunctionPass(ID) {}

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
      }
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
              true                  // flag to indicate if the pass is a analysis pass
);
