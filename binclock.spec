Summary:	Display system time in binary format
Summary(pl):	Wy¶wietlanie czasu w formacie binarnym
Name:		binclock
Version:	1.5
Release:	1
License:	GPL v2+
Group:		Applications/Console
Source0:	http://www.ngolde.de/%{name}-%{version}.tar.gz
# Source0-md5:	d26ea67970c782ee56c87595ed3bfef0
URL:		http://www.ngolde.de/binclock/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BinClock is a program which shows the system time in a binary format.
It supports showing the time with eight different colors, and it can
run a loop that prints the time every second.

%description -l pl
BinClock jest programem, który pokazuje czas u¿ywaj±c formatu
binarnego. Czas pokazywany jest za pomoc± 8 ró¿nych kolorów. Program
mo¿e byæ uruchomiony w pêtli i aktualizowaæ czas co sekundê.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_sysconfdir}}

install binclock $RPM_BUILD_ROOT%{_bindir}/binclock
install doc/binclock.1 $RPM_BUILD_ROOT%{_mandir}/man1/binclock.1
install binclockrc $RPM_BUILD_ROOT%{_sysconfdir}/binclockrc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/binclockrc
%{_mandir}/man1/binclock.1*
