#
# Conditional build:
%bcond_without	static_libs	# static library
#
Summary:	Library for reading and writing optical discs
Summary(pl.UTF-8):	Biblioteka służąca do odczytywania i zapisywania dysków optycznych
Name:		libburn
Version:	1.5.8
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	https://files.libburnia-project.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	4c8c786e88eb3e9f7c1d0ddc4d4a39e7
URL:		https://dev.lovelyhq.com/libburnia/web/wiki
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libburn is an open-source library for reading, mastering and writing
optical discs.

%description -l pl.UTF-8
Libburn jest wolnodostępną biblioteką służącą do odczytywania,
zarządzania i zapisywania dysków optycznych.

%package devel
Summary:	Header files for libburn library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libburn
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libburn library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libburn.

%package static
Summary:	Static libburn library
Summary(pl.UTF-8):	Statyczna biblioteka libburn
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libburn library.

%description static -l pl.UTF-8
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

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libburn.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CONTRIBUTORS COPYRIGHT ChangeLog README
%attr(755,root,root) %{_bindir}/cdrskin
%{_libdir}/libburn.so.*.*.*
%ghost %{_libdir}/libburn.so.4
%{_mandir}/man1/cdrskin.1*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libburn.so
%{_includedir}/libburn
%{_pkgconfigdir}/libburn-1.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libburn.a
%endif
