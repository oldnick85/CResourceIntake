cmake_minimum_required(VERSION 3.10)

project(example)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

set(CMAKE_INCLUDE_CURRENT_DIR ON)

set(SRCS
    "main.cpp")

set(RESOURCES_LIB_PATH ${CMAKE_CURRENT_BINARY_DIR}/../cri)
#set(RESOURCES_LIB_PATH "/home/oldnick/projects/build-CResourceIntake-Desktop-Debug/cri")
message("RESOURCES_LIB_PATH=" ${RESOURCES_LIB_PATH})

add_executable(${PROJECT_NAME} ${SRCS})
target_link_libraries(${PROJECT_NAME} resources)
target_include_directories(${PROJECT_NAME} PRIVATE ${RESOURCES_LIB_PATH})
target_compile_features(${PROJECT_NAME} PUBLIC cxx_std_17)
include_directories (${PROJECT_NAME})
