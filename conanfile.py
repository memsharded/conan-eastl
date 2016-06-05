from conans import ConanFile, CMake, tools
import os

class EastlConan(ConanFile):
    name = "EASTL"
    version = "3.01.01"
    license = "Modified BSD (3-clause) https://github.com/electronicarts/EASTL/blob/master/LICENSE"
    url = "https://github.com/memsharded/conan-eastl.git"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def source(self):
        tools.download("https://github.com/electronicarts/EASTL/archive/%s.zip" % self.version, "eastl.zip")
        tools.unzip("eastl.zip")
        

    def build(self):
        cmake = CMake(self.settings)
        self.run('cmake EASTL-%s %s' % (self.version, cmake.command_line))
        self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", "include", "EASTL-%s/include" % self.version)
        self.copy("*docopt.lib", "lib", keep_path=False)   
        if self.options.shared:
            self.copy("*.dll", "bin", keep_path=False)
            self.copy("*.so", "lib", keep_path=False)
        else:
            self.copy("*.a", "lib", keep_path=False)
        
    def package_info(self):
        if self.options.shared:
            self.cpp_info.libs = ["docopt"]
        else:
            self.cpp_info.libs = ["docopt_s"]
        

