# Autogenerated from /Users/cschen/llvm/test/clang/test/lit.site.cfg.py.in
# Do not edit!

import os

llvm_project_dir = os.environ["LLVM_DIR"]
print('llvm_project_dir: ', llvm_project_dir)
install_dir = os.environ["LLVM_INSTALLED_DIR"]

# Allow generated file to be relocatable.
from pathlib import Path
def path(p):
    if not p: return ''
    return str((Path(__file__).parent / p).resolve())


import sys

config.llvm_src_root = path(llvm_project_dir)+path(r"/llvm")
config.llvm_obj_root = path(install_dir)
config.llvm_tools_dir = path(install_dir)+path(r"/./bin")
config.llvm_libs_dir = path(install_dir)+path(r"/./lib")
config.llvm_shlib_dir = path(install_dir)+path(r"/./lib")
config.llvm_plugin_ext = ".so"
config.lit_tools_dir = path(r"")
config.errc_messages = "No such file or directory;Is a directory;Invalid argument;Permission denied"
config.clang_lit_site_cfg = __file__
config.clang_obj_root = path(install_dir)+path(r"/tools/clang")
config.clang_src_dir = path(llvm_project_dir)+path(r"/clang")
config.clang_tools_dir = path(install_dir)+path(r"/./bin")
config.clang_lib_dir = path(install_dir)+path(r"/lib")
config.host_triple = "x86_64-unknown-linux-gnu"
config.target_triple = "riscv64-unknown-elf"
config.host_cc = "/usr/bin/cc"
config.host_cxx = "/usr/bin/c++"
config.llvm_use_sanitizer = ""
config.have_zlib = 1
config.clang_arcmt = 1
config.clang_default_cxx_stdlib = ""
config.clang_staticanalyzer = 1
config.clang_staticanalyzer_z3 = ""
config.clang_examples = 0
config.enable_shared = 1
config.enable_backtrace = 1
config.enable_experimental_new_pass_manager = 1
config.enable_threads = 1
config.host_arch = "x86_64"
config.python_executable = "/usr/bin/python3.6"
config.use_z3_solver = lit_config.params.get('USE_Z3_SOLVER', "")
config.has_plugins = 1
config.clang_vendor_uti = "org.llvm.clang"
config.llvm_external_lit = path(r"")

# Support substitution of the tools and libs dirs with user parameters. This is
# used when we can't determine the tool dir at configuration time.
try:
    config.clang_tools_dir = config.clang_tools_dir % lit_config.params
    config.llvm_tools_dir = config.llvm_tools_dir % lit_config.params
    config.llvm_shlib_dir = config.llvm_shlib_dir % lit_config.params
    config.llvm_libs_dir = config.llvm_libs_dir % lit_config.params
except KeyError:
    e = sys.exc_info()[1]
    key, = e.args
    lit_config.fatal("unable to find %r parameter, use '--param=%s=VALUE'" % (key,key))

import lit.llvm
lit.llvm.initialize(lit_config, config)

# Let the main config do the real work.
lit_config.load_config(
    config, os.path.join(config.clang_src_dir, "test/lit.cfg.py"))
