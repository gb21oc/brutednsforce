import dns.resolver   #pip install dnspython

def bruteForceDns():
    domain = input("Digite o dominio: ")  # Aonde eu vou 'atacar'
    list = input("Digite o arquivo com os dominios: ")    # caminho do arquivo txt aonde esta os dominios escrito por vc

    if domain != "" and list != "":
        try:
            with open(list, 'r') as path:
                for line in path:
                    line = line.rstrip('\n')
                    subdomain = f"{line}.{domain}"
                    try:
                        answers = dns.resolver.resolve(subdomain, 'a')
                        for answer in answers:
                            print(subdomain, answer)
                    except:
                        print("An unknown error has occurred")
        except:
            print("An unknown error has occurred")

    else:
        print("Arguments cannot be empty")


bruteForceDns()
