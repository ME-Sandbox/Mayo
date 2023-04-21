# Generated from mayo.pro.

cmake_minimum_required(VERSION 3.16)
project(mayo VERSION 0.7.0 LANGUAGES CXX)
include(${CMAKE_CURRENT_SOURCE_DIR}/cmake/auto-setup.cmake)

set(CMAKE_INCLUDE_CURRENT_DIR ON)

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTOUIC ON)

if(NOT DEFINED INSTALL_EXAMPLESDIR)
    set(INSTALL_EXAMPLESDIR "examples")
endif()

set(INSTALL_EXAMPLEDIR "${INSTALL_EXAMPLESDIR}")

find_package(QT NAMES Qt5 Qt6 REQUIRED COMPONENTS Core)
find_package(Qt${QT_VERSION_MAJOR} REQUIRED COMPONENTS Gui Widgets)
#find_package(WrapZLIB 1.0.8)
find_package(Qt${QT_VERSION_MAJOR} OPTIONAL_COMPONENTS OpenGLWidgets Test)
find_package(WrapIconv)
find_package(BZip2 REQUIRED)
find_package(OpenCASCADE REQUIRED COMPONENTS
    TKBO
    TKBRep
    TKBin
    TKBinL
    TKBinXCAF
    TKBool
    TKCAF
    TKCDF
    TKG2d
    TKG3d
    TKGeomAlgo
    TKGeomBase
    TKHLR
    TKIGES
    TKLCAF
    TKMath
    TKMesh
    TKMeshVS
    TKOpenGl
    TKPrim
    TKSTEP
    TKSTEP209
    TKSTEPAttr
    TKSTEPBase
    TKSTL
    TKService
    TKShHealing
    TKTopAlgo
    TKV3d
    TKVCAF
    TKVRML
    TKXCAF
    TKXDEIGES
    TKXDESTEP
    TKXSBase
    TKXSDRAW
    TKXml
    TKXmlL
    TKXmlXCAF
    TKernel
)

file(GLOB APP_SOURCES src/app/*.cpp src/app/*.h src/app/*.ui)
file(GLOB BASE_SOURCES src/base/*.cpp src/base/*.h)
file(GLOB GRAPHICS_SOURCES src/graphics/*.cpp src/graphics/*.h)
file(GLOB GUI_SOURCES src/gui/*.cpp src/gui/*.h)
file(GLOB IODXF_SOURCES src/io_dxf/*.cpp src/io_dxf/*.h)
file(GLOB IOIMAGE_SOURCES src/io_image/*.cpp src/io_image/*.h)
file(GLOB IOOCC_SOURCES src/io_occ/*.cpp src/io_occ/*.h)
file(GLOB IOPLY_SOURCES src/io_ply/*.cpp src/io_ply/*.h)
file(GLOB MEASURE_SOURCES src/measure/*.cpp src/measure/*.h)

qt_add_executable(mayo WIN32 MACOSX_BUNDLE
    src/3rdparty/fmt/src/format.cc
    ${APP_SOURCES}
    ${BASE_SOURCES}
    ${GRAPHICS_SOURCES}
    ${GUI_SOURCES}
    ${IODXF_SOURCES}
    ${IOIMAGE_SOURCES}
    ${IOOCC_SOURCES}
    ${IOPLY_SOURCES}
    ${MEASURE_SOURCES}
)
target_include_directories(mayo PUBLIC
    ${CMAKE_CURRENT_BINARY_DIR}/src/app
    3rdParty/release/include
    src/3rdparty
    src/app
)

target_compile_definitions(mayo PUBLIC
    (CASCADE_DEFINES, ;)
    OCCT_HANDLE_NOCAST
    QT_DISABLE_DEPRECATED_BEFORE=0x050F00
    QT_IMPLICIT_QFILEINFO_CONSTRUCTION
)

target_link_libraries(mayo PUBLIC
    Advapi32.lib
    Qt::Core
    Qt::Gui
    Qt::Widgets
    OpenCASCADE::TKBO
    OpenCASCADE::TKBRep
    OpenCASCADE::TKBin
    OpenCASCADE::TKBinL
    OpenCASCADE::TKBinXCAF
    OpenCASCADE::TKBool
    OpenCASCADE::TKCAF
    OpenCASCADE::TKCDF
    OpenCASCADE::TKG2d
    OpenCASCADE::TKG3d
    OpenCASCADE::TKGeomAlgo
    OpenCASCADE::TKGeomBase
    OpenCASCADE::TKHLR
    OpenCASCADE::TKIGES
    OpenCASCADE::TKLCAF
    OpenCASCADE::TKMath
    OpenCASCADE::TKMesh
    OpenCASCADE::TKMeshVS
    OpenCASCADE::TKOpenGl
    OpenCASCADE::TKPrim
    OpenCASCADE::TKSTEP
    OpenCASCADE::TKSTEP209
    OpenCASCADE::TKSTEPAttr
    OpenCASCADE::TKSTEPBase
    OpenCASCADE::TKSTL
    OpenCASCADE::TKService
    OpenCASCADE::TKShHealing
    OpenCASCADE::TKTopAlgo
    OpenCASCADE::TKV3d
    OpenCASCADE::TKVCAF
    OpenCASCADE::TKVRML
    OpenCASCADE::TKXCAF
    OpenCASCADE::TKXDEIGES
    OpenCASCADE::TKXDESTEP
    OpenCASCADE::TKXSBase
    OpenCASCADE::TKXSDRAW
    OpenCASCADE::TKXml
    OpenCASCADE::TKXmlL
    OpenCASCADE::TKXmlXCAF
    OpenCASCADE::TKernel
    BZip2::BZip2
)


# Resources:
set(mayo_resource_files
    "i18n/mayo_en.qm"
    "i18n/mayo_fr.qm"
    "images/appicon_128.png"
    "images/appicon_16.png"
    "images/appicon_24.png"
    "images/appicon_32.png"
    "images/appicon_64.png"
    "images/graphics/opencascade_hatch_1.png"
    "images/themes/classic/add-file.svg"
    "images/themes/classic/back-square.svg"
    "images/themes/classic/back.svg"
    "images/themes/classic/camera.svg"
    "images/themes/classic/clip-plane.svg"
    "images/themes/classic/cross.svg"
    "images/themes/classic/edit.svg"
    "images/themes/classic/expand.svg"
    "images/themes/classic/export.svg"
    "images/themes/classic/file.svg"
    "images/themes/classic/gear.svg"
    "images/themes/classic/import.svg"
    "images/themes/classic/indicator-down-disabled_8.png"
    "images/themes/classic/indicator-down_8.png"
    "images/themes/classic/item-mesh.svg"
    "images/themes/classic/item-xde.svg"
    "images/themes/classic/left-sidebar.svg"
    "images/themes/classic/link.svg"
    "images/themes/classic/measure.svg"
    "images/themes/classic/multiple.svg"
    "images/themes/classic/next.svg"
    "images/themes/classic/open-files.svg"
    "images/themes/classic/reload.svg"
    "images/themes/classic/stop.svg"
    "images/themes/classic/view-back.svg"
    "images/themes/classic/view-bottom.svg"
    "images/themes/classic/view-front.svg"
    "images/themes/classic/view-iso.svg"
    "images/themes/classic/view-left.svg"
    "images/themes/classic/view-right.svg"
    "images/themes/classic/view-top.svg"
    "images/themes/classic/xde-assembly.svg"
    "images/themes/classic/xde-simple-shape.svg"
    "images/themes/classic/zoom-in.svg"
    "images/themes/classic/zoom-out.svg"
    "images/themes/dark/back-square.svg"
    "images/themes/dark/back.svg"
    "images/themes/dark/camera.svg"
    "images/themes/dark/clip-plane.svg"
    "images/themes/dark/cross.svg"
    "images/themes/dark/edit.svg"
    "images/themes/dark/expand.svg"
    "images/themes/dark/export.svg"
    "images/themes/dark/file.svg"
    "images/themes/dark/gear.svg"
    "images/themes/dark/import.svg"
    "images/themes/dark/indicator-down-disabled_8.png"
    "images/themes/dark/indicator-down_8.png"
    "images/themes/dark/item-mesh.svg"
    "images/themes/dark/item-xde.svg"
    "images/themes/dark/left-sidebar.svg"
    "images/themes/dark/link.svg"
    "images/themes/dark/measure.svg"
    "images/themes/dark/multiple.svg"
    "images/themes/dark/next.svg"
    "images/themes/dark/reload.svg"
    "images/themes/dark/stop.svg"
    "images/themes/dark/view-back.svg"
    "images/themes/dark/view-bottom.svg"
    "images/themes/dark/view-front.svg"
    "images/themes/dark/view-iso.svg"
    "images/themes/dark/view-left.svg"
    "images/themes/dark/view-right.svg"
    "images/themes/dark/view-top.svg"
    "images/themes/dark/xde-assembly.svg"
    "images/themes/dark/xde-simple-shape.svg"
    "images/themes/dark/zoom-in.svg"
    "images/themes/dark/zoom-out.svg"
    "images/widget_pseudo_fold.png"
    "images/xde_reference_16.png"
)

qt6_add_resources(mayo "mayo"
    PREFIX
        "/"
    FILES
        ${mayo_resource_files}
)

if(CMAKE_BUILD_TYPE STREQUAL Debug)
    set_target_properties(mayo PROPERTIES
        WIN32_EXECUTABLE FALSE
    )
endif()

if((QT_VERSION_MAJOR GREATER 5))
    target_link_libraries(mayo PUBLIC
        Qt::OpenGLWidgets
    )
endif()

if(MSVC)
    target_compile_definitions(mayo PUBLIC
        NOMINMAX
    )

    target_compile_options(mayo PUBLIC
        /std:c++17
        /we4150
    )
endif()

if((MSVC) AND ((QT_VERSION_MAJOR GREATER 5)))
    target_compile_definitions(mayo PUBLIC
        _USE_MATH_DEFINES
    )
endif()

if(CLANG OR GCC)
    target_compile_options(mayo
        -std=c++17
    )
endif()

if(CLANG)
    target_compile_options(mayo
        -Wno-undefined-var-template
    )
endif()

if(MACOS)
    target_compile_definitions(mayo PUBLIC
        GL_SILENCE_DEPRECATION
    )

    target_link_libraries(mayo PUBLIC
        WrapIconv::WrapIconv
    )
endif()

if(WIN32)
    target_link_libraries(mayo PUBLIC
        Opengl32
        User32
    )
endif()

if(WIN32 AND (QT_VERSION_MAJOR LESS 6))
    file(GLOB APP_WINDOWS_SOURCES src/app/windows/*.cpp src/app/windows/*.h)
    target_sources(mayo PUBLIC
        ${APP_WINDOWS_SOURCES}
    )
endif()

if(Debug)
    target_link_libraries(mayo PUBLIC
        freetyped.lib
        libpng16d.lib
        tk86tsgx.lib
    )
endif()

if(Release)
    target_link_libraries(mayo PUBLIC
        freetype.lib
        libpng16.lib
        tk86tsx.lib
    )
endif()

#if(minOpenCascadeVersion(7, 4, 0))
    target_link_libraries(mayo PUBLIC
        TKRWMesh
    )
#endif()

#if(NOT GMIO_ROOT_ISEMPTY)
#    file(GLOB IOGMIO_WINDOWS_SOURCES src/io_gmio/*.cpp src/io_gmio/*.h)
#    target_sources(mayo PUBLIC
#        ${IOGMIO_WINDOWS_SOURCES}
#    )

#    target_include_directories(mayo PUBLIC
#        /include
#    )

#    target_compile_definitions(mayo PUBLIC
#        HAVE_GMIO
#    )

#    target_link_libraries(mayo PUBLIC
#        # Remove: L/lib
#        gmio_static
#        zlibstatic
#    )
#endif()

#if(CONFIG(withtests))
#    target_sources(mayo PUBLIC
#        tests/runtests.cpp
#        tests/test_app.cpp tests/test_app.h
#        tests/test_base.cpp tests/test_base.h
#        tests/test_measure.cpp tests/test_measure.h
#    )

#    target_compile_definitions(mayo PUBLIC
#        MAYO_WITH_TESTS
#    )

#    target_link_libraries(mayo PUBLIC
#        Qt::Test
#    )
#endif()

if((TEST_architecture_arch STREQUAL "x86_64") AND NOT (TEST_architecture_arch STREQUAL "i386"))
    target_compile_definitions(mayo PUBLIC
        _OCC64
    )
endif()

if(LINUX)
    target_compile_definitions(mayo PUBLIC
        HAVE_CONFIG_H
        HAVE_FSTREAM
        HAVE_IOMANIP
        HAVE_IOSTREAM
        HAVE_LIMITS_H
        LIN
        LININTEL
        OCC_CONVERT_SIGNALS
    )
endif()

#if(NOT ((NOT (minOpenCascadeVersion(7, 4, 0)))))
    target_sources(mayo PUBLIC
        src/io_occ/io_occ_base_mesh.cpp
        src/io_occ/io_occ_gltf_reader.cpp
        src/io_occ/io_occ_obj_reader.cpp
    )
#endif()

#if(NOT ((NOT minOpenCascadeVersion(7, 5, 0))))
    target_sources(mayo PUBLIC
        src/io_occ/io_occ_gltf_writer.cpp
    )
#endif()

#if(NOT ((NOT minOpenCascadeVersion(7, 6, 0))))
    target_sources(mayo PUBLIC
        src/io_occ/io_occ_obj_writer.cpp
    )
#endif()

install(TARGETS mayo
    RUNTIME DESTINATION "${INSTALL_EXAMPLEDIR}"
    BUNDLE DESTINATION "${INSTALL_EXAMPLEDIR}"
    LIBRARY DESTINATION "${INSTALL_EXAMPLEDIR}"
)
