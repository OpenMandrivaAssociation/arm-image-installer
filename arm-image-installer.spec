# Tarfile created using git
# git clone https://pagure.io/arm-image-installer.git
# git archive --format=tar --prefix=%{name}-%{version}/ %{version} | xz > ~/%{name}-%{version}.tar.xz

Name:		arm-image-installer
Version:	2.16
Release:	1%{?dist}
Summary:	Writes binary image files to any specified block device
License:	GPLv2+
Url:		https://pagure.io/arm-image-installer

BuildArch:	noarch
Source0:	%{name}-%{version}.tar.xz

Provides:	fedora-arm-installer < 2.5
Requires:	e2fsprogs
Requires:	parted
Requires:	sudo
Requires:	util-linux


%description
Allows one to first select a source image (local or remote). The image must be
a binary file containing: [MBR + Partitions + File Systems + Data]. A
destination block device should then be selected for final installation.


%prep
%autosetup

%build
echo "skipping..."

%install
install -d %{buildroot}%{_datadir}/arm-image-installer
install -d %{buildroot}%{_datadir}/arm-image-installer/socs.d
install -pm 644 socs.d/* %{buildroot}%{_datadir}/arm-image-installer/socs.d/
install -d %{buildroot}%{_datadir}/arm-image-installer/boards.d
install -pm 644 boards.d/* %{buildroot}%{_datadir}/arm-image-installer/boards.d/

install -d %{buildroot}%{_bindir}
install -pm 0755 update-uboot %{buildroot}%{_bindir}/
install -pm 0755 arm-image-installer %{buildroot}%{_bindir}/

%files
%license COPYING
%doc AUTHORS README TODO SUPPORTED-BOARDS
%{_bindir}/arm-image-installer
%{_bindir}/update-uboot
%{_datadir}/arm-image-installer/
