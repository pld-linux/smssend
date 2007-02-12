Summary:	Interface to internet SMS forwarding services
Summary(pl.UTF-8):   Interfejs do bramek SMS
Name:		smssend
Version:	3.5
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://zekiller.skytech.org/fichiers/smssend/%{name}-%{version}.tar.gz
# Source0-md5:	3be49bc779259a5ab39731a70f17bebf
URL:		http://zekiller.skytech.org/smssend_menu_en.html
BuildRequires:	autoconf
BuildRequires:	skyutils-devel >= 2.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
smssend is a utility providing a command line interface to the GSM
Short Message Service (SMS) via internet gateways. It requires an
active internet connection (HTTP proxy is suitable) and may require a
registration for such gateways. The program is quite configurable for
other gateways than provided, examples are included.

Please keep in mind that these internet to SMS gateways may not
tolerate and may even forbid their usage via scripts.

%description -l pl.UTF-8
smssend to narzędzie udostępniające interfejs wywoływany z linii
poleceń do GSM Short Message Service (SMS) poprzez internetowe bramki.
Program wymaga aktywnego połączenia z internetem i może wymagać
rejestracji na wspomnianych bramkach. Program jest wysoce
konfigurowalny dla innych bramek niż w dostarczonych przykładach.

Proszę wziąć pod uwagę fakt, że niektóre z bramek SMS nie tolerują, a
nawet uniemożliwiają korzystanie z nich za pomocą skryptów.

%prep
%setup -q -n %{name}

%build
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README todo.txt
%attr(755,root,root) %{_bindir}/*
%{_datadir}/smssend
%{_mandir}/man1/*
%lang(fr) %{_mandir}/fr/man1/*
