from conans import ConanFile, CMake

class Mayo(ConanFile):
   settings = "os", "compiler", "build_type", "arch"
   requires = "opencascade/7.6.2", "zlib/1.2.13", "bzip2/1.0.8", "tk/8.6.10", "tcl/8.6.11" # comma-separated list of requirements
   generators = "cmake", "cmake_paths"
   default_options = {"opencascade:shared": False}

   def imports(self):
      self.copy("*.dll", dst="bin", src="bin") # From bin to bin
      self.copy("*.dylib*", dst="bin", src="lib") # From lib to bin
      
   def build(self):
      cmake = CMake(self)
      cmake.configure()
      cmake.build()
