cmake_minimum_required(VERSION 3.8)
project(googlito)

set(CMAKE_C_STANDARD 99)

set(SOURCE_FILES functions.c)
add_executable(googlito ${SOURCE_FILES})