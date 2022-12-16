Name:           dkms-drbd
Version:        9.1
Release:        1%{?dist}
Summary:        LINBIT DRBD kernel module

License:        GPLv2
URL:            https://github.com/LINBIT/drbd
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  git /usr/bin/pathfix.py
Requires:       dkms, kernel >= 5.17, kernel-devel >= 5.17, kmod

%define NAME_VER %{name}-%{version}

%description
DRBD, developed by LINBIT, provides networked RAID 1 functionality for GNU/Linux. It is designed for high  
availability clusters and software defined storage. DRBD keeps disks on multiple nodes synchronized using TCP/IP or  
RDMA and makes the data available as a block device. This results in RAID 1 but without the use of uncommon  
hardware such as shared SCSI buses or Fibre Channel.

%prep
%setup
git clone --branch drbd-%{version} --depth 1 https://github.com/LINBIT/drbd.git drbd-repo

%install
mkdir -p %{buildroot}/%{_usrsrc}/drbd-%{version}
cp -r %{_builddir}/%{NAME_VER}/drbd-repo/drbd/* %{buildroot}/%{_usrsrc}/drbd-%{version}
cp %{_builddir}/%{NAME_VER}/dkms.conf %{buildroot}/%{_usrsrc}/drbd-%{version}/dkms.conf

pathfix.py -pni "%{__python3} %{py3_shbang_opts}" %{buildroot}/%{_usrsrc}/drbd-%{version}/drbd-kernel-compat/scripts/*

%files
%{_usrsrc}/drbd-%{version}

%post
dkms add drbd/%{version}
dkms build drbd/%{version}
dkms install drbd/%{version} --modprobe-on-install

%postun
rmmod drbd
dkms uninstall drbd/%{version}
dkms remove drbd/%{version}

%changelog
* Fri Dec 16 2022 SaigyoujiYuyuko233 <HGK-SaigyoujiYuyuko@outlook.com> 9.1-1
- Standard dkms package

