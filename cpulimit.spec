Name:		cpulimit
Version:	1.1
Release:	1%{?dist}
Summary:	CPU Usage Limiter for Linux

Group:		Applications/Text
License:	GPLv2+
URL:		http://cpulimit.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/cpulimit/cpulimit/cpulimit/cpulimit-1.1.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%description
cpulimit is a simple program which attempts to limit the CPU usage of a process
(expressed in percentage, not in CPU time). This is useful to control batch
jobs, when you don't want them to eat too much CPU. It does not act on the nice
value or other scheduling priority stuff, but on the real CPU usage. Also, it
is able to adapt itself to the overall system load, dynamically and quickly.

%prep
%setup -q


%build
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
install -Dp -m 755 cpulimit $RPM_BUILD_ROOT/usr/bin/cpulimit

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/usr/bin/cpulimit
%doc

%changelog
* Sat Jan 07 2011 Christos Triantafyllidis <christos.triantafyllidis@gmail.com> 1.1-1
- initial package creation
