Summary:	Displays system time in binary format
Summary(pl):	Wy¶wietla czas w formacie binarnym
Name:		binclock
Version:	1.5
Release:	1
License:	GPL
Group:		Applications/Console
Source0:	%{name}-%{version}.tar.gz
URL:		http://www.ngolde.de/binclock/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BinClock is a program which shows the system time in a binary format.
It supports showing the time with eight different colors, and it can
run a loop that prints the time every second.

%description -l pl
BinClock jest programem, który pokazuje czas u¿ywaj±c formatu
binarnego. Czas pokazywany jest za pomoc± 8 ró¿nych kolorów. Program
mo¿e byæ uruchomiony w pêtli i aktualizowaæ czas co sekunde.

%prep
%setup -q -n %{name}-%{version}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install binclock $RPM_BUILD_ROOT%{_bindir}/binclock
install doc/binclock.1 $RPM_BUILD_ROOT%{_mandir}/man1/binclock.1

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%doc CHANGELOG COPYING README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/binclock.1*
