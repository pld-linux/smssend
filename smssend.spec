%define ver      2.0
%define rel      1
%define prefix   /usr

Summary: interface to internet SMS forwarding services
Name: smssend
Version: %ver
Release: %rel
Copyright: GPL
Group: Utilities
Source: %{name}-%{ver}.tar.gz
URL: http://zekiller.skytech.org/smssend_menu_en.html
Patch0: smssend-1.9-debug+dump.patch
BuildRoot: /tmp/%{name}-%{ver}-root
Packager: Moritz Barsnick <barsnick@gmx.net>
#Docdir: %{prefix}/doc

%description
smssend is a utility providing a command line interface to
the GSM Short Message Service (SMS) via internet gateways.
It requires an active internet connection (HTTP proxy is
suitable) and may require a registration for such gateways.
The program is quite configurable for other gateways than
provided, examples are included.

Please keep in mind that these internet to SMS gateways may
not tolerate and may even forbid their usage via scripts.
 
%prep
%setup -q
#%patch0 -p1
#%patch1 -p1
#%patch2 -p1

%build
%configure --disable-shared --enable-skyutils

if [ "$SMP" != "" ]; then
  (make "MAKE=make -k -j $SMP"; exit 0)
  make
else
  make
fi

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

#%post

#%postun

%files
%defattr(-, root, root)
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/smssend/*

%doc AUTHORS COPYING ChangeLog NEWS README

%changelog
* Sun Oct 29 2000 Moritz Barsnick <barsnick@gmx.net>
  [2.0-1]
- updated to 2.0
- disabled debug+dump patch

* Sun Oct 08 2000 Moritz Barsnick <barsnick@gmx.net>
  [1.9-2]
- added "legal" notice to description
- added patch for making "-d" = "dump" and "-v" = "verbose/debug"
  command line options, at least for skyutils, instead of compile
  time options

* Tue Oct 03 2000 Moritz Barsnick <barsnick@gmx.net>
  [1.9-1]
- updated to 1.9
- removed patches (the problem is partly solved, at least now builds
  fine on RedHat)
- corrected spelling mistake in package description
- removed %post and %postun sections, they gave ugly script sections
- added "--enable-skyutils" to %configure, so included SkyUtils are
  automatically used (we're linking statically)

* Mon Sep 18 2000 Moritz Barsnick <barsnick@gmx.net>
  [1.8-1]
- updated to 1.8
- updated patches to 1.8
- rearranged datadir patch

* Fri Sep 15 2000 Moritz Barsnick <barsnick@gmx.net>
  [1.7-2]
- added patch for spelling and clarification in man page
- added patch to display and use correct datadir from ./configure
  (includes patch for shorter length usage message)

* Fri Sep 15 2000 Moritz Barsnick <barsnick@gmx.net>
  [1.7-1]
- first RPM
