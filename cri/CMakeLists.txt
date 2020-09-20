cmake_minimum_required(VERSION 3.10)

project(resources)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

set(CMAKE_INCLUDE_CURRENT_DIR ON)

set(RESOURCES_GENERATE_SCRIPT "${CMAKE_CURRENT_SOURCE_DIR}/intake.py")
message("RESOURCES_GENERATE_SCRIPT=" ${RESOURCES_GENERATE_SCRIPT})
set(RESOURCES_GENERATE_COMMAND python3 ${RESOURCES_GENERATE_SCRIPT}
    --resources-path=${CMAKE_CURRENT_SOURCE_DIR}
    --sources-path=${CMAKE_CURRENT_BINARY_DIR})
message("RESOURCES_GENERATE_COMMAND=" ${RESOURCES_GENERATE_COMMAND})
execute_process(COMMAND ${RESOURCES_GENERATE_COMMAND}
    #WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
    )

#target_compile_features(${PROJECT_NAME} PUBLIC cxx_std_17)
#include_directories (${PROJECT_NAME})

#set(LIBRESOURCES_FILES
#  "${CMAKE_CURRENT_BINARY_DIR}/resources.cpp"
#  "${CMAKE_CURRENT_BINARY_DIR}/resources.h"
#)

#add_custom_command(OUTPUT ${LIBRESOURCES_FILES}
#  COMMAND ${CMAKE_COMMAND} -E intake.py
#  WORKING_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}"
#  COMMENT "Generate resources files"
#  VERBATIM
#)

#add_custom_target(resources_generate DEPENDS ${LIBRESOURCES_FILES})

set(SRCS
    "${CMAKE_CURRENT_BINARY_DIR}/resources.cpp")
set(HDRS
    "${CMAKE_CURRENT_BINARY_DIR}/resources.h")

add_library(${PROJECT_NAME} STATIC ${SRCS} ${HDRS})
#target_include_directories(foo INTERFACE "${CMAKE_CURRENT_BINARY_DIR}/include/foo")
#target_link_libraries(foo INTERFACE ${FOO_LIBRARIES})
