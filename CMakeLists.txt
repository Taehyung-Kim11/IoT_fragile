cmake_minimum_required(VERSION 3.22)

if (NOT "${LLVM_INSTALL_DIR}" STREQUAL "")
  set (CMAKE_C_COMPILER "${LLVM_INSTALL_DIR}/bin/clang")
  set (CMAKE_CXX_COMPILER "${LLVM_INSTALL_DIR}/bin/clang++")
endif()
SET(CMAKE_CXX_FLAGS "-fno-rtti")

project(llvm-tutorial-skeleton)

list(APPEND CMAKE_PREFIX_PATH "${LLVM_INSTALL_DIR}/lib/cmake/llvm/")
find_package(LLVM REQUIRED CONFIG)
include_directories(${LLVM_INCLUDE_DIRS})

add_library(Skeleton MODULE Skeleton_Combine.cpp)

if (APPLE)
  set_target_properties(Skeleton PROPERTIES LINK_FLAGS "-undefined dynamic_lookup")
endif(APPLE)
