from binaryninja import *
from .net_main import main_network

def network_report(bv, function):
	log_info("Starting Network Plugin")
	main_network(bv)

PluginCommand.register_for_address(
"Network-Plugin", "Display Network Syscall Info", network_report)
