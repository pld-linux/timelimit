%bcond_without	tests
Summary:	Limit a process's absolute execution time
Name:		timelimit
Version:	1.9.2
Release:	1
License:	distributable
Group:		Base
Source0:	http://devel.ringlet.net/files/sys/timelimit/%{name}-%{version}.tar.xz
# Source0-md5:	2390f78a965e4d37b06406a9985d80eb
# for prove binary
%{?with_tests:BuildRequires:	perl-tools-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
timelimit executes a command and terminates the spawned process after
a given time with a given signal. A warning signal is sent first,
then, after a timeout, a kill signal, similar to the way init(8)
operates on shutdown.

%prep
%setup -q

sed -i -e 's#fgrep#grep -F#g' t/02-subsecond.t

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags}" \
	LDFLAGS="%{rpmldflags}"

%{?with_tests:%{__make} check}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_bindir} \
	MANDIR=%{_mandir}/man \
	BINOWN=$(id -u) \
	BINGRP=$(id -g) \
	SHAREOWN=$(id -u) \
	SHAREGRP=$(id -g) \
 	STRIP=""

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}*
