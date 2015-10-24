from pyanaconda.installclasses.fedora import FedoraBaseInstallClass

class FedoraServerInstallClass(FedoraBaseInstallClass):
    name = "Fedora Server"
    stylesheet = "/usr/share/anaconda/fedora-server.css"
    defaultFS = "xfs"
    defaultPackageEnvironment = "rfremix-server-product-environment"
