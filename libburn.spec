%bcond_without	static_libs	# don't build static library
Summary:	Library for reading and writing optical discs
Summary(pl):	Biblioteka s³u¿±ca do odczytywania i zapisywania dysków optycznych
Name:		libburn
Version:	0.2
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://icculus.org/burn/releases/%{name}-%{version}.tar.gz
# Source0-md5:	fcf42dd1a5ed137b96a60e1cc2141d18
URL:		http://icculus.org/burn/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
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
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static}
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

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif
