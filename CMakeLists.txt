cmake_minimum_required(VERSION 3.13)

project(CResourceIntake)

set(CMAKE_VERBOSE_MAKEFILE ON)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

include_directories(cri)
add_subdirectory(cri)

include_directories(example)
add_subdirectory(example)
