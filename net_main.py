
from .syscall_dictionary import ret_dictionary
from binaryninja import *

registers = ['rax', 'rdi', 'rsi', 'rdx', 'r10', 'r8']

def main_network(bv):
	sys_dict = ret_dictionary()
	for function in bv.functions:
		for block in function.low_level_il:
			for i in block:
				if (i.operation == binaryninja.LowLevelILOperation.LLIL_SYSCALL and ((i.get_reg_value('rax').value) in sys_dict)):
					call = int(i.get_reg_value('rax'))
					msg = "Network Syscall found at " + str(hex(i.address)) + " with " + str(sys_dict[call][0])
					log_info(msg)
					option_function(call, i, bv)


def option_function(call: int, i, bv):
	#Dictionary of Networking syscalls
	temp_dict = ret_dictionary()
	#Current Syscall
	syscall = temp_dict[call]
	#Begin Comment with Syscall Name
	comment = f"{syscall[0]}\t"
	#Counter being used for correct registers
	counter = 0

	#Each Option within Syscall (key: (tuple, of, options))
	for option in syscall:
		if counter > 0:
			add_str = ''
	
			#---------Option Storing Types/Cases---------###################
			#Nested Dictionary Cases
			if call in (41, 48, 53) and (option != 'FD'):
				try:
					add_str = str(option[int(i.get_reg_value(str(registers[counter])))])
				except:
					log_info("Invalid Option")
			#Case if Stack being used
			elif "<stack" in str(i.get_reg_value(str(registers[counter]))):
			
				#Address Parsing
				if option in ('SOCKADDR', 'DESTADDR', 'SRCADDR'):
					add_str = int(i.get_reg_value(str(registers[counter])))
					add_str = int(i.get_stack_contents(add_str, 8))
					add_str = get_address(add_str)

				#Anything else on stack 
				else:
					#Returns Offset
					add_str = int(i.get_reg_value(str(registers[counter])))
					#Stack Contents
					add_str = int(i.get_stack_contents(add_str, 8))

					#If Listen() backlog too large (max is 32767)
					if call == 50 and add_str > 32767:
						add_str = 32767
					#If Listen() backlog less than 0 set to 0
					elif call == 50 and add_str < 0:
						add_str = 0
			
			#All other Cases
			else:
				add_str = int(i.get_reg_value(str(registers[counter])))
			################################################################
			
	
	
			#---------Comment Building Cases---------#######################
			#<undetermined> returned
			if "<undet" in str(add_str):
				add_str = i.get_reg_value(str(registers[counter]))
				comment += f"{option}: <undetermined/runtime>\t"
			#Nested Dictionary Case (only add result nested dict)
			elif call in (41, 48, 53) and (type(option) is dict):
				comment += f"{add_str} "
			else:
				comment += f"{option}: {add_str}\t"
			################################################################
	
		counter += 1

	#Set Comment
	bv.set_comment_at(i.address, comment)


##----Code from Dr. O'Connors Github for Converting Address----##
def get_address(num):
    response = ''
    tmp = (num & 0xFFFF0000) >> 16
    port = ((tmp << 8) | (tmp >> 8)) & 0xFFFF
    tmp = num >> 32
    ip = f"{tmp&0xFF}.{(tmp>>8)&0xFF}.{(tmp>>16)&0xFF}.{(tmp>>24)&0xFF}"
    return f"IP={ip}/Port={port}"
####https://github.com/tj-oconnor/undergraduate-re/blob/main/labs/networking-lab/student_work/syscall.py#####












					
