Name:           dkms-drbd
Version:        9.1
Release:        4%{?dist}
Summary:        LINBIT DRBD kernel module

License:        GPLv2
URL:            https://github.com/LINBIT/drbd
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  git /usr/bin/pathfix.py make
Requires:       dkms, kernel >= 5.17, kernel-devel >= 5.17, kmod, coccinelle >= 1.0.8

%define NAME_VER %{name}-%{version}

%description
DRBD, developed by LINBIT, provides networked RAID 1 functionality for GNU/Linux. It is designed for high  
availability clusters and software defined storage. DRBD keeps disks on multiple nodes synchronized using TCP/IP or  
RDMA and makes the data available as a block device. This results in RAID 1 but without the use of uncommon  
hardware such as shared SCSI buses or Fibre Channel.

%prep
%setup
git clone --branch drbd-%{version} --depth 500 https://github.com/LINBIT/drbd.git drbd-repo
cd drbd-repo
git submodule update --init --recursive
make drbd/.drbd_git_revision
cd %{_builddir}/%{NAME_VER}

%install
mkdir -p %{buildroot}/%{_usrsrc}
cp -r %{_builddir}/%{NAME_VER}/drbd-repo/drbd %{buildroot}/%{_usrsrc}/drbd-%{version}
cp %{_builddir}/%{NAME_VER}/dkms.conf %{buildroot}/%{_usrsrc}/drbd-%{version}/dkms.conf
pathfix.py -pni "%{__python3} %{py3_shbang_opts}" %{buildroot}/%{_usrsrc}/drbd-%{version}/drbd-kernel-compat/scripts/*.py

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
* Fri Dec 16 2022 SaigyoujiYuyuko233 <HGK-SaigyoujiYuyuko@outlook.com> 9.1-4
- Fix: Missing file '.drbd_git_revision'
- Fix: Your DRBD source tree is broken. Unpack again.

* Fri Dec 16 2022 SaigyoujiYuyuko233 <HGK-SaigyoujiYuyuko@outlook.com> 9.1-3
- Fix: incorrect src path
- Fix Err: cannot open: FileNotFoundError(2, 'No such file or directory')

* Fri Dec 16 2022 SaigyoujiYuyuko233 <HGK-SaigyoujiYuyuko@outlook.com> 9.1-2
- Fix: dkms src path not exist (hgk-saigyoujiyuyuko@outlook.com)
- Fix: Submodule not exist
- Fix: Broken DRDB src tree
* Fri Dec 16 2022 SaigyoujiYuyuko233 <HGK-SaigyoujiYuyuko@outlook.com> 9.1-1
- Standard dkms package
