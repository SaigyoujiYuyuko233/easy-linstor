Name: python-linstor
Version: 1.16.0
Release: 2%{?dist}
Summary: Virtual Package that use pip to install python-linstor
BuildArch: noarch

Group: System Environment/Daemons
License: GPLv2+
URL: https://github.com/LINBIT/linstor-api-py

Requires: python3 python3-pip

%description
# LINSTOR Python API

This repository contains a Python library to communicate with a linstor controller.

LINSTOR, developed by [LINBIT](https://www.linbit.com), is a software that manages DRBD replicated
LVM/ZFS volumes across a group of machines. It maintains DRBD configuration on the participating machines.  It
creates/deletes the backing LVM/ZFS volumes. It automatically places the backing LVM/ZFS volumes among the
participating machines.

# Online API documentation
A rendered html documentation for the LINSTOR Python API can be found [here](https://linbit.github.io/linstor-api-py/).

# Using Linstor
Please read the user-guide provided at [docs.linbit.com](https://docs.linbit.com).

# Support
For further products and professional support, please
[contact](http://links.linbit.com/support) us.

# Releases
Releases generated by git tags on github are snapshots of the git repository at the given time. You most
likely do not want to use these. They might lack things such as generated man pages, the `configure` script,
and other generated files. If you want to build from a tarball, use the ones [provided by us](https://www.linbit.com/en/drbd-community/drbd-download/).

%pre
pip install python-linstor

%clean
rm -rf $RPM_BUILD_ROOT

%postun
pip uninstall python-linstor -y

%changelog
* Fri Dec 16 2022 SaigyoujiYuyuko233 <HGK-SaigyoujiYuyuko@outlook.com> 1.16.0-2
- Fix: command not found python-linstor

* Fri Dec 16 2022 SaigyoujiYuyuko233 <HGK-SaigyoujiYuyuko@outlook.com> 1.16.0-1
- Virtual Package that use pip to install python-linstor

