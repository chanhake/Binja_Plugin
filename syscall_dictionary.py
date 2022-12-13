def ret_dictionary():
	net_dict = {
		41 : ('SOCKET()', 
			{                  
 				0  : "AF_UNSPEC",                  	
 				1  : "AF_UNIX",		                
 				2  : "AF_INET(IPv4)",		                
 				3  : "AF_AX25",		                
 				4  : "AF_IPX",		                    
 				5  : "AF_APPLETALK",                   
 				6  : "AF_NETROM",	                    
 				7  : "AF_BRIDGE",	                    
 				8  : "AF_AAL5",		                 
 				9  : "AF_X25",		                     
 				10 : "AF_INET6(IPv6)", 				
				12 : "AF_MAX"                 
			},
			{ 
				0  : "Undetermined Value",
				1  : "SOCK_STREAM(TCP)",
				2  : "SOCK_DGRAM(UDP)",
				3  : "SOCK_RAW",
				4  : "SOCK_RDM",
				5  : "SOCK_SEQPACKET",
				10 : "SOCK_PACKET"
			}),
		42 : ('CONNECT()','FD', 'SOCKADDR', 'ADDRLEN'),
		43 : ('ACCEPT()', 'FD', 'SOCKADDR', 'ADDRLEN'),
		44 : ('SENDTO()', 'FD', 'BUFF', 'LEN', 'FLAGS', 'DESTADDR', 'ADDRLEN'),
		45 : ('RECVFROM()', 'FD', 'BUFF', 'LEN', 'FLAGS', 'SRCADDR', 'ADDRLEN'),
		46 : ('SENDMSG()','FD', 'MSG', 'FLAGS'),
		47 : ('RECVMSG()', 'FD', 'MSG', 'FLAGS'),
		48 : ('SHUTDOWN()','FD', 
			{
				0 : "No Further Receptions",
				1 : "No Further Transmissions",
				2 : "No Further Communication"
		}),
		49 : ('BIND()', 'FD', 'SOCKADDR', 'ADDRLEN'),
		50 : ('LISTEN()', 'FD', 'Max Backlog'),
		51 : ('GETSOCKNAME()','FD', 'SOCKADDR', 'ADDRLEN'),
		52 : ('GETPEERNAME()','FD', 'SOCKADDR', 'ADDRLEN'),
		53 : ('SOCKETPAIR()',
			{ 
 				0  : "AF_UNSPEC",                  	
 				1  : "AF_UNIX",		                
 				2  : "AF_INET(IPv4)",		                
 				3  : "AF_AX25",		                
 				4  : "AF_IPX",		                    
 				5  : "AF_APPLETALK",                   
 				6  : "AF_NETROM",	                    
 				7  : "AF_BRIDGE",	                    
 				8  : "AF_AAL5",		                 
 				9  : "AF_X25",		                     
 				10 : "AF_INET6(IPv6)", 				
				12 : "AF_MAX"                 
			},
			{ 
				0  : "Undetermined Value",
				1  : "SOCK_STREAM(TCP)",
				2  : "SOCK_DGRAM(UDP)",
				3  : "SOCK_RAW",
				4  : "SOCK_RDM",
				5  : "SOCK_SEQPACKET",
				10 : "SOCK_PACKET"
			}),
		54 : ('SETSOCKOPT()','FD', 'LEVEL', 'OPTNAME', 'OPTVAL', 'OPTLEN'),
		55 : ('GETSOCKOPT()', 'FD', 'LEVEL', 'OPTNAME', 'OPTVAL', 'OPTLEN'),
		170: ('SETHOSTNAME()','NAME', 'LEN'),
		171: ('SETDOMAINNAME()','NAME', 'LEN'),
		288: ('ACCEPT4()', 'FD', 'SOCKADDR', 'ADDRLEN'),
		299: ('RECVMMSG()','FD', 'MSGVEC PTR', 'VLEN'),
		307: ('SENDMMSG()','FD', 'MSGVEC PTR', 'VLEN')
	}

	return net_dict



