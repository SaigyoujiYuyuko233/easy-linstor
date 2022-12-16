Name:           jre-headless
Version:        1.8.0
Release:        1%{?dist}
Summary:        Virtual package for linstor-server

License:        MIT
URL:            https://github.com/SaigyoujiYuyuko233/easy-linstor  

Requires:       java-1.8.0-openjdk-headless

%description
This is a virtual package for linstor-common/controller/satellite which require 15 > java-jre >= 1.8

%prep

%build

%install

%files

%changelog
* Fri Dec 16 2022 SaigyoujiYuyuko233 <HGK-SaigyoujiYuyuko@outlook.com> 1.8.0-1
- Create this package with java 1.8.0 support.

