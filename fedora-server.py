from pyanaconda.installclasses.fedora import FedoraBaseInstallClass
from pyanaconda.constants import *
from pyanaconda.product import *
from pyanaconda import network
from pyanaconda import nm
from pyanaconda import iutil
import types
from pyanaconda.kickstart import getAvailableDiskSpace
from blivet.partspec import PartSpec
from blivet.autopart import swapSuggestion
from blivet.platform import platform
from blivet.size import Size

class FedoraServerInstallClass(FedoraBaseInstallClass):
    name = "Fedora Server"
    stylesheet = "/usr/share/anaconda/fedora-server.css"
    defaultFS = "xfs"
    defaultPackageEnvironment = "rfremix-server-product-environment"

    def setDefaultPartitioning(self, storage):
        autorequests = [PartSpec(mountpoint="/", fstype=storage.defaultFSType,
                                 size=Size("2GiB"),
                                 maxSize=Size("15GiB"),
                                 grow=True,
                                 btr=True, lv=True, thin=True, encrypted=True)]

        bootreqs = platform.setDefaultPartitioning()
        if bootreqs:
            autorequests.extend(bootreqs)


        disk_space = getAvailableDiskSpace(storage)
        swp = swapSuggestion(disk_space=disk_space)
        autorequests.append(PartSpec(fstype="swap", size=swp, grow=False,
                                     lv=True, encrypted=True))

        for autoreq in autorequests:
            if autoreq.fstype is None:
                if autoreq.mountpoint == "/boot":
                    autoreq.fstype = storage.defaultBootFSType
                else:
                    autoreq.fstype = storage.defaultFSType

        storage.autoPartitionRequests = autorequests
