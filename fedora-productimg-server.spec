%global pixmaptarget %{_datadir}/lorax/product/usr/share/anaconda/pixmaps
%global pixmapsource %{_datadir}/anaconda/pixmaps/server
%global adverttarget %{pixmaptarget}/rnotes/en

Name:           fedora-productimg-server
Version:        23
Release:        5%{?dist}
Summary:        Installer branding and configuration for Fedora Server

# Copyright and related rights waived via CC0
# http://creativecommons.org/publicdomain/zero/1.0/
License:        CC0

Source0:        fedora-server.css
Source1:        fedora-server.py
Source2:        Cockpit.svg

BuildRequires:  cpio
BuildRequires:  findutils
BuildRequires:  xz
BuildRequires:  python3-devel

Provides:       lorax-product-server
Conflicts:      fedora-productimg-workstation
Conflicts:      fedora-productimg-cloud

%description
This package contains differentiated branding and configuration for Fedora
Server for use in a product.img file for Anaconda, the Fedora installer. It
is not useful on an installed system.

%prep

%build

%install

install -m 755 -d %{buildroot}%{pixmaptarget}

install -m 644 %{SOURCE0} %{buildroot}%{pixmaptarget}/../

mkdir -p %{buildroot}%{_datadir}/lorax/product/%{python3_sitearch}/pyanaconda/installclasses
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/lorax/product/%{python3_sitearch}/pyanaconda/installclasses

ln -sf %{pixmapsource}/sidebar-bg.png %{buildroot}%{pixmaptarget}
ln -sf %{pixmapsource}/topbar-bg.png %{buildroot}%{pixmaptarget}

# Add banner advertisement for Cockpit
install -m 755 -d %{buildroot}%{adverttarget}
install -m 644 %{SOURCE2} %{buildroot}%{adverttarget}

# note filename change with this one
ln -sf %{pixmapsource}/sidebar-logo.png %{buildroot}%{pixmaptarget}/sidebar-logo_flavor.png

install -m 755 -d %{buildroot}%{_datadir}/fedora-productimg

pushd %{buildroot}%{_datadir}/lorax/product/
find %{buildroot}%{_datadir}/lorax/product/ -depth -printf '%%P\0' | \
   cpio --null --quiet -H newc -o | \
   xz -9 > \
   %{buildroot}%{_datadir}/fedora-productimg/product.img
popd


%files
%dir %{_datadir}/lorax/product/usr/share/anaconda
%{_datadir}/lorax/product/usr/share/anaconda/fedora-server.css
%{_datadir}/lorax/product/%{python3_sitearch}/pyanaconda/installclasses/fedora-server.py*
%{_datadir}/lorax/product/%{python3_sitearch}/pyanaconda/installclasses/__pycache__/*
%dir %{adverttarget}
%{adverttarget}/Cockpit.svg
%dir %{_datadir}/lorax/product/usr/share
%dir %{_datadir}/lorax/product/usr
%dir %{pixmaptarget}
%{pixmaptarget}/*.png
%dir %{_datadir}/fedora-productimg
%{_datadir}/fedora-productimg/product.img

%changelog
* Wed Mar 16 2016 Arkady L. Shane <ashejn@russianfedora.pro> 23-5.R
- bump release to rebuild

* Thu Jan 14 2016 Arkady L. Shane <ashejn@russianfedora.pro> 23-4.R
- rebuilt

* Sun Oct 25 2015 Arkady L. Shane <ashejn@russianfedora.pro> 23-3.R
- set rfremix env by default

* Fri Jul 10 2015 Stephen Gallagher <sgallagh@redhat.com> 23-2
- Switch to Python 3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 12 2015 Stephen Gallagher <sgallagh@redhat.com> 23-1
- Bump version to 23 for Rawhide

* Tue May 12 2015 Stephen Gallagher <sgallagh@redhat.com> 22-8
- Add Cockpit advertising banner for anaconda

* Wed Feb 25 2015 Adam Williamson <awilliam@redhat.com> - 22-7
- BuildRequire python2-devel so the install class goes to the right place

* Tue Jan 27 2015 Stephen Gallagher <sgallagh@redhat.com> 22-6
- Create a Fedora Server InstallClass object to modify the installer defaults.
- Install the CSS in the proper location so that it can be merged in rather
  than replacing the existing copy.
- Change the default environment group to be Fedora Server.
- Change the default filesystem to XFS.

* Wed Nov 26 2014 Matthew Miller <mattdm@fedoraproject.org> 22-5
- correctly pregenerate product.img cpio archive

* Thu Nov 20 2014 Matthew Miller <mattdm@fedoraproject.org> 22-4
- provide lorax-product-server

* Thu Nov 20 2014 Matthew Miller <mattdm@fedoraproject.org> 22-3
- merge changes in from f21

* Fri Nov  7 2014 Matthew Miller <mattdm@fedoraproject.org> 22-1 
- bump to 22 for rawhide

* Thu Nov  6 2014 Matthew Miller <mattdm@fedoraproject.org> 21-2
- conflict with the other fedora-productimg packages

* Thu Nov  6 2014 Matthew Miller <mattdm@fedoraproject.org> 21-1
- Change license to CC0

* Thu Nov  6 2014 Matthew Miller <mattdm@fedoraproject.org> 21-0
- Initial creation for Fedora 21
