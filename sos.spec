Summary: A set of tools to gather troubleshooting information from a system
Name: sos
Version: 2.2
Release: 5
Group: System/Base
Source0: https://fedorahosted.org/releases/s/o/sos/%{name}-%{version}.tar.gz
Source100:	sos.rpmlintrc
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
%makeinstall_std
%find_lang %{name}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc README TODO LICENSE ChangeLog doc/*
%{_sbindir}/sosreport
%{_datadir}/%{name}
%{py_puresitedir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*
%config(noreplace) %{_sysconfdir}/sos.conf


%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 2.2-2mdv2011.0
+ Revision: 669997
- mass rebuild

* Thu Dec 02 2010 Funda Wang <fwang@mandriva.org> 2.2-1mdv2011.0
+ Revision: 604670
- import sos

