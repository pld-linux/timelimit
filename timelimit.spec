Summary:	Limit a process's absolute execution time
Name:		timelimit
Version:	1.5
Release:	2
License:	distributable
Group:		Base
Source0:	http://devel.ringlet.net/sysutils/timelimit/%{name}-%{version}.tar.gz
# Source0-md5:	e9d3da9a81479689a59c58a93914b034
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
timelimit executes a command and terminates the spawned process after
a given time with a given signal. A warning signal is sent first, then,
after a timeout, a kill signal, similar to the way init(8) operates on
shutdown.

%prep
%setup

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags} -pipe -DHAVE_ERR -DHAVE_SYSEXITS_H -DHAVE_ERRNO_H -DHAVE_SIGACTION" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install %{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}*
