Summary:	interface to internet SMS forwarding services
Name:		smssend
Version:	2.1
Release:	1
License:	GPL
Group:		Utilities
Source0:	http://zekiller.skytech.org/fichiers/smssend/%{name}-%{version}.tar.gz
URL:		http://zekiller.skytech.org/smssend_menu_en.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
smssend is a utility providing a command line interface to the GSM
Short Message Service (SMS) via internet gateways. It requires an
active internet connection (HTTP proxy is suitable) and may require a
registration for such gateways. The program is quite configurable for
other gateways than provided, examples are included.

Please keep in mind that these internet to SMS gateways may not
tolerate and may even forbid their usage via scripts.

%prep
%setup -q

%build
%configure \
	--enable-skyutils
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog NEWS README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/smssend
%{_mandir}/man1/*
%lang(fr) %{_mandir}/fr/man1
