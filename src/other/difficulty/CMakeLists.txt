cmake_minimum_required (VERSION 3.5)

# application project
project (difficulty)

# The sources to be used
file(GLOB SOURCE_FILES "*.cpp")

# Output
set(EXECUTABLE_OUTPUT_PATH "${BIN_CMDS_DIR}")

# Define the executable to be generated
set(TOOL_NAME "difficulty")
add_executable(${TOOL_NAME} ${SOURCE_FILES})

# Add the project static libs at linking
target_link_libraries (${TOOL_NAME} ${BASE_LIBS})
