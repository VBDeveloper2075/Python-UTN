import logging

def main():

    logging.basicConfig(filename='app.log', level="DEBUG")

    host="pepe.com"
    port="127.0.0.1"

    logging.debug("El host %s no está disponible"%(host))
    logging.info("El host %s no está disponible"%(host))
    logging.warning("El host %s no está disponible"%(host))
    logging.error("El host %s no está disponible"%(host))
    logging.critical("El host %s no está disponible"%(host))
main()