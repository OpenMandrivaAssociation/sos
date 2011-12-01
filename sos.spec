Summary: A set of tools to gather troubleshooting information from a system
Name: sos
Version: 2.2
Release: %mkrel 2
Group: System/Base
Source0: https://fedorahosted.org/releases/s/o/sos/%{name}-%{version}.tar.gz
License: GPLv2+
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Url: http://fedorahosted.org/sos
BuildRequires: python-devel
BuildRequires: gettext
Requires: libxml2-python
Requires: tar
Requires: bzip2
Requires: xz

%description
Sos is a set of tools that gathers information about system
hardware and configuration. The information can then be used for
diagnostic purposes and debugging. Sos is commonly used to help
support technicians and developers.

%prep
%setup -q

%build
make

%install
rm -rf %{buildroot}
%makeinstall_std
%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc README TODO LICENSE ChangeLog doc/*
%{_sbindir}/sosreport
%{_datadir}/%{name}
%{python_sitelib}/*
%{_mandir}/man1/*
%{_mandir}/man5/*
%config(noreplace) %{_sysconfdir}/sos.conf
