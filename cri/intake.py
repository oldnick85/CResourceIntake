#!/usr/bin/env python3

import sys
import json

def main(args):
	rsrcs = CResources(sys.argv)
	rsrcs.proc()
	return 0
	
	
class CResources:
	resources_path = ""
	sources_path = ""
	namespace = None
	
	def __init__(self, argv):
		for arg in sys.argv:
			if (arg.find("--resources-path=") == 0):
				self.resources_path = arg.replace("--resources-path=", "") + "/"
			if (arg.find("--sources-path=") == 0):
				self.sources_path = arg.replace("--sources-path=", "") + "/"
		return
		
	def proc(self):
		with open(self.resources_path+"resources.json", "r") as resources_file:
			resources_all = json.load(resources_file)
		print("resources_all=%s\n" % str(resources_all))
		self.namespace = resources_all["namespace"]
		resources = resources_all["resources"]
		[code_h, code_cpp] = self.proc_resources(resources)
		if (self.namespace):
			code_h = ("namespace %s {\n" % self.namespace) + code_h + "\n}"
			code_cpp = "#include \"resources.h\"\n\n" + ("using namespace %s;\n\n" % self.namespace) +  code_cpp
		code_h = "#include <array>\n" + code_h
		file_h = open(self.sources_path+"resources.h", 'w')
		file_h.write(code_h)
		file_h.close()
		file_cpp = open(self.sources_path+"resources.cpp", 'w')
		file_cpp.write(code_cpp)
		file_cpp.close()
		return
		
	def proc_resources(self, resources):
		code_h = ""
		code_cpp = ""
		for resource in resources:
			[h, cpp] = self.proc_resource(resource)
			code_h += h
			code_cpp += cpp
		return [code_h, code_cpp]
	
	def proc_resource(self, resource):
		code_h = ""
		code_cpp = ""
		fname = resource["file"]
		varname = resource["var"]
		f = open(self.resources_path+fname, 'rb')
		data = f.read()
		code_h += "\nextern std::array<uint8_t, %d> %s;\n" % (len(data), varname)
		code_cpp += "std::array<uint8_t, %d> %s::%s = {\n" % (len(data), self.namespace, varname)
		for d in data:
			code_cpp += (" 0x%02X," % d)
		code_cpp += "\n};\n\n"
		f.close()
		return [code_h, code_cpp]

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
