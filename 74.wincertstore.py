import wincertstore


def main():

    for storename in ("CA", "ROOT", "MY"):
        with wincertstore.CertSystemStore(storename) as store:
            for cert in store.itercerts(usage=wincertstore.SERVER_AUTH):
                print("--------")
                print(cert.get_pem()[28:40])
                print(cert.get_name())
                print(cert.enhanced_keyusage_names())







    return

if __name__ == "__main__":
    main()
