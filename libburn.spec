Summary:	Library for reading and writing optical discs
Summary(pl):	Biblioteka s³u¿±ca do odczytywania i zapisywania dysków optycznych
Name:		libburn
Version:	0.1
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://icculus.org/burn/releases/%{name}-%{version}.tar.gz
# Source0-md5:	8c968ca4d8f9c071de6660ffe405b72b
URL:		http://icculus.org/burn/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libburn is an open-source library for reading, mastering and writing
optical discs.

%description -l pl
Libburn jest wolnodostêpn± bibliotek± s³u¿±c± do odczytywania,
zarz±dzania i zapisywania dysków optycznych.

%package devel
Summary:	Header files for libburn library
Summary(pl):	Pliki nag³ówkowe biblioteki libburn
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for libburn library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libburn.

%package static
Summary:	Static libburn library
Summary(pl):	Statyczna biblioteka libburn
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libburn library.

%description static -l pl
Statyczna biblioteka libburn.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/%{name}
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
