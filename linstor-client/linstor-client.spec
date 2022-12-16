Summary: DRBD distributed resource management utility
Name: linstor-client
Version: 1.16.0
Release: 3%{?dist}
License: GPLv3
Group: System Environment/Daemons
Source0: https://pkg.linbit.com//downloads/linstor/%{name}-%{version}.tar.gz
BuildArch: noarch
Vendor: LINBIT HA-Solutions GmbH
Packager: LINSTOR Team <drbd-user@lists.linbit.com>
Requires:  python-linstor >= 1.16.0
Url: https://www.linbit.com
BuildRequires:  python3-setuptools git

%define NAME_VERS %{name}-%{version}

%description
This client program communicates to controller node which manages the resources

%prep
%setup -n %{NAME_VERS} -n %{NAME_VERS}
git clone --branch v%{version} https://github.com/LINBIT/linstor-client.git

%build
/usr/bin/python3 setup.py build

%install
/usr/bin/python3 setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)

%changelog
* Fri Dec 16 2022 SaigyoujiYuyuko233 <HGK-SaigyoujiYuyuko@outlook.com> 1.16.0-3
- Fix variable

* Fri Dec 16 2022 SaigyoujiYuyuko233 <HGK-SaigyoujiYuyuko@outlook.com> 1.16.0-2
- Pull src from git
