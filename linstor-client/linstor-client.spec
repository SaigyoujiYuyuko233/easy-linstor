%define name linstor-client
%define version 1.16.0
%define unmangled_version 1.16.0
%define release 1

Summary: DRBD distributed resource management utility
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: GPLv3
Group: System Environment/Daemons
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: LINBIT HA-Solutions GmbH
Packager: LINSTOR Team <drbd-user@lists.linbit.com>
Requires:  python-linstor >= 1.16.0
Url: https://www.linbit.com
BuildRequires:  python3-setuptools

%description
This client program communicates to controller node which manages the resources

%prep
%setup -n %{name}-%{unmangled_version} -n %{name}-%{unmangled_version}

%build
/usr/bin/python3 setup.py build

%install
/usr/bin/python3 setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
